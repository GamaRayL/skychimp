NULLABLE = {'blank': True, 'null': True}

DAILY = 'daily'
WEEKLY = 'weekly'
MONTHLY = 'monthly'
FREQUENCY_CHOOSE = [
        (DAILY, 'Раз в день'),
        (WEEKLY, 'Раз в неделю'),
        (MONTHLY, 'Раз в месяц')
]

MAILING_CREATED = 'created'
MAILING_STARTED = 'started'
MAILING_CLOSED = 'closed'
MAILING_STATUS = [
        (MAILING_CREATED, 'Создана'),
        (MAILING_STARTED, 'Запущена'),
        (MAILING_CLOSED, 'Завершена')
]

LOG_SUCCESS = 'success'
LOG_FAILURE = 'failure'
LOG_STATUS = (
        (LOG_SUCCESS, 'Успешно'),
        (LOG_FAILURE, 'Неуспешно'),
)