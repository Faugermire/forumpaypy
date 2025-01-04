from tests.base_forumpay_test import BaseForumPayTest


class TestPing(BaseForumPayTest):

    def test_ping(self):
        headers = self.forumpay.endpoints.ping.create_request_header_list()
        body = self.forumpay.endpoints.ping.create_request_body_list()

        res = self.forumpay.endpoints.ping.send_request(headers, body)
        self.assertEqual(res.json()['result'], 'pong')
