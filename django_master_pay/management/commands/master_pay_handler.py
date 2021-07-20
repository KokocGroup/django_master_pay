import logging

from django.core.management import BaseCommand

from django_master_pay import settings
from django_master_pay.api import MasterPayApi, MasterPayApiException
from django_master_pay.models import Payment


class Command(BaseCommand):

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger(settings.MASTER_PAY_SETTINGS['logger_name'])
        self.callback = settings.MASTER_PAY_SETTINGS['callback']
        self.api = MasterPayApi()

    def handle(self, *args, **options):
        self.logger.info('START')

        payments = Payment.objects.filter(
            status__in=(Payment.STATUS_NEW, Payment.STATUS_IN_WORK)
        )

        for payment in payments:
            self.process_payment(payment)

        self.logger.info('END')

    def process_payment(self, payment):
        self.logger.info('Process payment #{}'.format(payment.id))

        try:
            payment_data = self.api.get_payment(
                payment_id=payment.master_pay_id,
                partner_id=payment.partner_id
            )
        except MasterPayApiException as e:
            self.logger.warning(str(e))
        else:
            if payment_data['status'] != payment.status:
                pass