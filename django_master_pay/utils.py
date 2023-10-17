from django.db import transaction

from django_master_pay.api import MasterPayApi
from django_master_pay.settings import MASTER_PAY_SETTINGS


def create_payment(
        amount,
        currency,
        purse_type,
        purse_number,
        external_id,
        partner_id=MASTER_PAY_SETTINGS['default_partner_id'],
        **extra_params
):
    from django_master_pay.models import Payment
    api = MasterPayApi()

    with transaction.atomic():
        payment_data = api.create_payment(
            amount,
            purse_type,
            currency,
            purse_number,
            external_id,
            partner_id=partner_id,
            **extra_params
        )
        payment = Payment(
            external_id=external_id,
            master_pay_id=payment_data['id'],
            record_data=payment_data,
            partner_id=partner_id
        )
        payment.save()
        return payment
