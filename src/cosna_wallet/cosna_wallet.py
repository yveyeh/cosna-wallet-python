"""cosna_wallet"""

import requests

base_url = 'https://api.staging.payment.cosna-afrique.com/v1/wallet'

class CosnaWallet:
    """A controller to access endpoints in the cosna wallet integration API."""

    def __init__(self, master_key: str, private_key: str):
        """
        Class constructor

        Args:
        - master_key: `string`
        - private_key: `string`

        Returns:
            Void.
        """
        self.master_key = master_key
        self.private_key = private_key
        if not master_key:
            raise Exception('master_key is required')
        if not isinstance(master_key, str):
            raise Exception('master_key is required to be a string')
        if not private_key:
            raise Exception('private_key is required')
        if not isinstance(private_key, str):
            raise Exception('private_key is required to be a string')

    def init_payment(self, payload, request_type = 'POST', endpoint='/payment/'):
        """
        Exposes an API endpoint to perform payments through cosna wallet.

        Args:
        - payload: `dict`
            - amount: The amount to be paid by user. min= 200 and max = 500 000 XAF | XOF
            - currency: The currency in which the transaction is performed. enum (XAF, XOF, USD, EUR ).
            - hash: The hash param is a combination of currency and amount.
                - example: If amount = 200 , currency = XAF, `hash = md5(amount + currency)`.
            - cancel_url: Url to which user will be redirected if paiement is canceled.
            - return_url: Url to which user will be redirected if paiement is completed.
            - callback_url: Url to which paiement response will be posted to notify marchant on the state of the tramsaction.
        - request_type: `string`
            - 'POST' by default.
        - endpoint: `string`
            - payment endpoint. Defaults to '/payment/'.

        Returns:
            A Response object from the API.
        """

        headers = {
            'master-key': self.master_key,
            'private-key': self.private_key
        }
        body = {
            'amount': payload['amount'],
            'currency': payload['currency'],
            'hash': payload['hash'],
            'return_url': payload['return_url'],
            'cancel_url': payload['cancel_url'],
            'callback_url': payload['callback_url']
        }
        return requests.request(request_type, base_url + endpoint, headers = headers, data = body)
