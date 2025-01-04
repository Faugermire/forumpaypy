from forumpaypy.endpoints.check_payment import CheckPayment
from forumpaypy.endpoints.ping import Ping


class Endpoints:

    def __init__(self, base_url: str, api_key: str):
        self.check_payment = CheckPayment(base_url, api_key)
        self.ping = Ping(base_url, api_key)