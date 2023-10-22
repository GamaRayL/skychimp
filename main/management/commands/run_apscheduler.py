from django.conf import settings
from main.services import send_mailing
from django.core.management import BaseCommand
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore
from apscheduler.schedulers.blocking import BlockingScheduler


class Command(BaseCommand):
    """Запуск рассылок по расписанию"""
    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), 'default')

        scheduler.add_job(
            send_mailing,
            trigger=CronTrigger(second="*/5"),
            id='my_task',
            max_instances=1,
            replace_existing=True,
        )

        try:
            print('Запуск рассылок по расписанию')
            scheduler.start()

        except KeyboardInterrupt:
            print('Остановка рассылок по расписанию')
            scheduler.shutdown()
