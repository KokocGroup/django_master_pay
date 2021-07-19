import logging

from django.core.management import BaseCommand

from django_master_pay import settings


class Command(BaseCommand):

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger(settings.MASTER_PAY_SETTINGS['logger_name'])

    def handle(self, *args, **options):
        pass
