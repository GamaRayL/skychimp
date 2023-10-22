import logging
from datetime import datetime, timedelta
from logging.handlers import RotatingFileHandler
from pprint import pprint, pformat

from django.core.mail import send_mail

from config import settings
from constants import MAILING_CREATED, MAILING_STARTED, LOG_SUCCESS, LOG_FAILURE, DAILY, WEEKLY, MONTHLY
from main.models import Mailing, Log

logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)

file_handler = RotatingFileHandler(settings.LOGS_PATH)
file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


def check_mailing():
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().date()

    logger.info(f'Текущее время: {current_time}')
    logger.info(f'Текущая дата: {current_date}')

    mailings = Mailing.objects \
        .filter(status=MAILING_CREATED) \
        .filter(time__lte=datetime.now().time()) \
        .filter(date_run__lte=datetime.now().date())

    logger.info(f'Количество рассылок для запуска: {len(mailings)}\n')

    return mailings


def send_mailing():
    for mailing in check_mailing():
        pprint_str = pformat(mailing.__dict__)
        logger.info('Рассылка:')
        logger.info(pprint_str)

        user_emails = list(mailing.user.values_list('email', flat=True))
        logger.info('Клиенты рассылки:')
        for user_email in user_emails:
            logger.info(f'{user_email}\n')

        mailing.status = MAILING_STARTED
        mailing.save()

        log = Log.objects.create(mailing_id=mailing.pk)
        try:
            response = send_mail(
                subject=mailing.message.title,
                message=mailing.message.description,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=user_emails,
                fail_silently=False
            )

            log.status = LOG_SUCCESS

            message_response = f'Письма успешно отправлены'

            if response:
                log.server_response = message_response

        except Exception as e:
            log.status = LOG_FAILURE
            print(e)

        log.save()

        if mailing.frequency == DAILY:
            mailing.date_run = mailing.date_run + timedelta(days=1)
        elif mailing.frequency == WEEKLY:
            mailing.date_run = mailing.date_run + timedelta(weeks=1)
        elif mailing.frequency == MONTHLY:
            mailing.date_run = mailing.date_run + timedelta(days=30)

        mailing.status = MAILING_CREATED

        mailing.save()




