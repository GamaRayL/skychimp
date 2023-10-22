from django.core.management import BaseCommand

from main.services import send_mailing


class Command(BaseCommand):
    """Принудительная проверка рассылок"""

    def handle(self, *args, **options):
        print(f'{self.__doc__}:\n')
        send_mailing()
