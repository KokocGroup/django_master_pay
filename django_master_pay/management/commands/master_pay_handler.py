import logging

from django.core.management import BaseCommand
from django.db import transaction

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
            status__in=Payment.WORK_STATUSES
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
            self.logger.warning("\t{}".format(str(e)))
        else:
            if payment_data['status'] != payment.status:
                self.logger.info('\tNew status: OLD={} NEW={}'.format(Payment.status_display(payment.status), Payment.status_display(payment_data['status'])))
                with transaction.atomic():
                    payment.status = payment_data['status']
                    payment.record_data = payment_data
                    payment.error = payment_data['auto_payment_error']
                    payment.save(update_fields=['status', 'record_data', 'error'])
                    self.callback(**payment_data)
