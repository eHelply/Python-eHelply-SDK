"""
    eHelply SDK - 1.1.104

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.104
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import ehelply_python_sdk
from ehelply_python_sdk.api.billing_api import BillingApi  # noqa: E501


class TestBillingApi(unittest.TestCase):
    """BillingApi unit test stubs"""

    def setUp(self):
        self.api = BillingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_billing_account(self):
        """Test case for create_billing_account

        Createbillingaccount  # noqa: E501
        """
        pass

    def test_get_client_secret(self):
        """Test case for get_client_secret

        Getclientsecret  # noqa: E501
        """
        pass

    def test_has_payment(self):
        """Test case for has_payment

        Haspayment  # noqa: E501
        """
        pass

    def test_list_payment_methods(self):
        """Test case for list_payment_methods

        Listpaymentmethods  # noqa: E501
        """
        pass

    def test_process_payment(self):
        """Test case for process_payment

        Processpayment  # noqa: E501
        """
        pass

    def test_reconcile_payment_method(self):
        """Test case for reconcile_payment_method

        Reconcilepaymentmethod  # noqa: E501
        """
        pass

    def test_remove_payment_method(self):
        """Test case for remove_payment_method

        Removepaymentmethod  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
