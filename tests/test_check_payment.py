from tests.base_forumpay_test import BaseForumPayTest


class TestCheckPayment(BaseForumPayTest):

    def test_check_payment(self):
        payment_id = 'e83b7dc1-33e3-4357-bfe5-9e00fc62cfdb'
        address = 'btc-511e5d644a8849e29e1ad4c46d6e727f	'
        pos_id = 'widget'
        currency = 'BTC'

        headers = self.forumpay.endpoints.check_payment.create_request_header_list()
        query = self.forumpay.endpoints.check_payment.create_request_query_list(pos_id=pos_id, currency=currency, payment_id=payment_id, address=address)
        res = self.forumpay.endpoints.check_payment.send_request(headers, query_params=query)
        self.assertTrue('err' not in res.json().keys())


