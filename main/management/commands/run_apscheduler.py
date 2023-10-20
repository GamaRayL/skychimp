from django.conf import settings
from django.core.management import BaseCommand
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore
from apscheduler.schedulers.background import BackgroundScheduler


def my_task():
    print('Confirm')


class Command(BaseCommand):
    def handle(self, *args, **options):
        scheduler = BackgroundScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), 'default')

        scheduler.add_job(
            my_task,
            trigger=CronTrigger(second="*/2"),
            id='my_task',
            max_instances=1,
            replace_existing=True,
        )

        try:
            print('Запуск print')
            scheduler.start()

        except KeyboardInterrupt:
            print('Остановка print')
            scheduler.shutdown()

