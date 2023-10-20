from django.conf import settings
from django.core.mail import send_mail

from main.models import Mailing


def send_mailing():
    mailings = Mailing.objects.filter(status='started')

    for mailing in mailings:
        mailing.status = 'started'
        mailing.save()
        user_emails = list(mailing.user.values_list('email', flat=True))

        send_mail(
            subject='Text',
            message='text',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=user_emails,
            fail_silently=False
        )

        # print(mailing.status)
        # users = mailing.user.all()
        # print(users)


