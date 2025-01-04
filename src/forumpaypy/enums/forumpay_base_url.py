from enum import Enum


class ForumPayBaseUrl(Enum):

    PRODUCTION = 'https://api.forumpay.com/pay/v2/'
    SANDBOX = 'https://sandbox.api.forumpay.com/pay/v2/'