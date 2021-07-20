from django.db import transaction

from django_master_pay.api import MasterPayApi
from django_master_pay.models import Payment


def create_payment(amount, currency, purse_type, purse_number, external_id):
    api = MasterPayApi()
    with transaction.atomic():
        payment_data = api.create_payment(amount, purse_type, currency, purse_number, external_id)
        payment = Payment(
            external_id=external_id,
            master_pay_id=payment_data['id'],
            record_data=payment_data
        )
        return payment
