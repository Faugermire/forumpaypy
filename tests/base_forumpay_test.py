import unittest
import dotenv
import os

from forumpaypy.forumpay import ForumPay


class BaseForumPayTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        dotenv.load_dotenv()
        cls.api_user = os.environ['FORUMPAY_API_USER']
        cls.api_secret = os.environ['FORUMPAY_API_SECRET']

    def setUp(self):
        self.forumpay = ForumPay(self.api_user, self.api_secret)
