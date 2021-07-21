import logging

try:
    from django.conf import settings as django_settings
except ImportError:
    logging.warning("Django not installed")
    django_settings = None


def default_callback(**kwargs):
    raise NotImplemented("MasterPay callback not implemented")


MASTER_PAY_SETTINGS = {
    'token': '',
    'callback': default_callback,
    'default_partner_id': None,
    'base_url': "https://master-pay.ru/",
    'timeout': 30,
    'logger_name': 'django_master_pay'
}

if hasattr(django_settings, 'MASTER_PAY_SETTINGS'):
    MASTER_PAY_SETTINGS.update(django_settings.MASTER_PAY_SETTINGS)
