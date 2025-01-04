from forumpaypy.endpoints.base_endpoint import BaseEndpoint
from forumpaypy.endpoints.request_parameters.request_parameter import RequestParameter
from forumpaypy.endpoints.request_parameters.request_parameter_list import RequestParameterList
from forumpaypy.enums.content_type_enum import ContentType
from forumpaypy.enums.http_method_enum import HTTPMethod


class Ping(BaseEndpoint):

    def __init__(self, base_url: str, api_key):
        url_tail = 'Ping/'
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

    def create_request_query_list(self) -> RequestParameterList:
        return RequestParameterList()
