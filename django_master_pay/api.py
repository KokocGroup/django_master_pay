import json
import os
from decimal import Decimal
from urllib.parse import urlencode

import requests

from .settings import MASTER_PAY_SETTINGS


class MasterPayApiException(Exception):

    def __init__(self, code, error, status_code):
        self.code = code
        self.error = error
        self.status_code = status_code
        super(MasterPayApiException, self).__init__("code: {}, error: {}".format(self.code, self.error))


class MasterPayApi(object):

    def __init__(self, token=MASTER_PAY_SETTINGS['token']):
        self.token = token
        self.session = requests.Session()

    def _make_request(self, method, url, *args, **kwargs):
        if 'timeout' not in kwargs:
            kwargs['timeout'] = MASTER_PAY_SETTINGS['timeout']

        try:
            response = getattr(self.session, method.lower())(url, *args, **kwargs)
            response.raise_for_status()
        except requests.HTTPError as e:
            try:
                error_data = json.loads(e.response.content)
                raise MasterPayApiException(error_data['code'], error_data['error'], e.response.status_code)
            except json.JSONDecodeError:
                raise e
        json_data = response.json()
        if not json_data['success']:
            raise MasterPayApiException(json_data['code'], json_data['error'], response.status_code)

        return json_data['result']

    def create_payment(
            self,
            amount,
            purse_type,
            currency,
            purse_number,
            external_id,
            partner_id=MASTER_PAY_SETTINGS['default_partner_id'],
            **extra_params
    ):
        url = os.path.join(MASTER_PAY_SETTINGS['base_url'], 'api', 'partner', str(partner_id), 'payment', 'create/')
        extra = extra_params or {}
        params = {
            'amount': Decimal(amount),
            'purse_type': purse_type,
            'currency': currency,
            'number': purse_number,
            'external_id': external_id,
            **extra
        }

        url = url + "?{}".format(urlencode({'token': self.token}))
        data = self._make_request('post', url, data=params)
        return data

    def get_payment(self, payment_id, partner_id=MASTER_PAY_SETTINGS['default_partner_id']):
        url = os.path.join(MASTER_PAY_SETTINGS['base_url'], 'api', 'partner', str(partner_id), 'payment', str(payment_id), 'detail')
        data = self._make_request('get', "{}?{}".format(url, urlencode({'token': self.token})))
        return data
