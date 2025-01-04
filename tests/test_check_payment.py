from tests.base_forumpay_test import BaseForumPayTest


class TestCheckPayment(BaseForumPayTest):

    def test_check_payment(self):
        payment_id = '8efd2074-4f55-4c65-914f-fdf4d4a2816b'
        address = 'btc-e743879a2c5e460abf507887666b81bc'
        pos_id = 'widget'
        currency = 'BTC'

        headers = self.forumpay.endpoints.check_payment.create_request_header_list()
        query = self.forumpay.endpoints.check_payment.create_request_query_list(pos_id=pos_id, currency=currency, payment_id=payment_id, address=address)
        res = self.forumpay.endpoints.check_payment.send_request(headers, query_params=query)
        self.assertTrue('err' not in res.json().keys())


