import base64

from forumpaypy.endpoints.endpoints import Endpoints
from forumpaypy.enums.forumpay_base_url import ForumPayBaseUrl


class ForumPay:

    def __init__(self, api_user: str, api_secret: str, is_production_mode: bool = False):
        self._is_production_mode = is_production_mode
        self._base_url = ForumPayBaseUrl.PRODUCTION.value if self._is_production_mode else ForumPayBaseUrl.SANDBOX.value
        b64_auth_key = base64.standard_b64encode(f'{api_user}:{api_secret}'.encode('utf-8')).decode('utf-8')
        self._api_key = f'Basic {b64_auth_key}'
        self.endpoints = Endpoints(self.base_url, self.api_key)

    @property
    def is_production_mode(self):
        return self._is_production_mode

    @property
    def base_url(self):
        return self._base_url

    @property
    def api_key(self):
        return self._api_key
