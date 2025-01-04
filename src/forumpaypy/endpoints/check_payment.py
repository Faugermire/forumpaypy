from forumpaypy.endpoints.base_endpoint import BaseEndpoint
from forumpaypy.endpoints.request_parameters.parameter_restriction import ParameterRestriction
from forumpaypy.endpoints.request_parameters.request_parameter import RequestParameter
from forumpaypy.endpoints.request_parameters.request_parameter_list import RequestParameterList
from forumpaypy.enums.content_type_enum import ContentType
from forumpaypy.enums.http_method_enum import HTTPMethod


class CheckPayment(BaseEndpoint):

    def __init__(self, base_url: str, api_key):
        url_tail = 'CheckPayment/'
        method = HTTPMethod.GET
        content_type = ContentType.APPLICATION_JSON
        super().__init__(base_url, url_tail, api_key, method, content_type)

    def create_request_header_list(self):
        header_parameters = RequestParameterList(
            RequestParameter(
                param_name='Authorization',
                param_types=str,
                param_value=self.api_key,
                restrictions=[],
                description='Authorization header containing your API key.',
                required=True
            ),
            RequestParameter(
                param_name='Content-Type',
                param_types=str,
                param_value=self.content_type.value,
                restrictions=[],
                description='It tells the server what type of data is actually sent.',
                required=False
            )
        )
        return header_parameters

    def create_request_body_list(self) -> RequestParameterList:
        return RequestParameterList()

    def create_request_query_list(self, *, pos_id: str, currency: str, payment_id: str, address: str) -> RequestParameterList:
        query_parameters = RequestParameterList(
            RequestParameter(
                param_name='pos_id',
                param_types=str,
                param_value=pos_id,
                restrictions=[
                    ParameterRestriction(lambda x: len(x) > 0),
                ],
                description='''The point-of-sale identifier, represented as a string.''',
                required=True
            ),
            RequestParameter(
                param_name='currency',
                param_types=str,
                param_value=currency,
                restrictions=[
                    ParameterRestriction(lambda x: len(x) > 0),
                ],
                description='''The currency in which the payment is to be checked, represented as a string.''',
                required=True
            ),
            RequestParameter(
                param_name='payment_id',
                param_types=str,
                param_value=payment_id,
                restrictions=[
                    ParameterRestriction(lambda x: len(x) > 0),
                ],
                description='''The unique identifier for the payment to be checked, represented as a string.''',
                required=True
            ),
            RequestParameter(
                param_name='address',
                param_types=str,
                param_value=address,
                restrictions=[
                    ParameterRestriction(lambda x: len(x) > 0),
                ],
                description='''The address associated with the payment, represented as a string.''',
                required=True
            ),
        )
        return query_parameters
