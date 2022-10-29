"""
    eHelply SDK - 1.1.119

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.119
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import ehelply_python_sdk
from ehelply_python_sdk.api.support_api import SupportApi  # noqa: E501


class TestSupportApi(unittest.TestCase):
    """SupportApi unit test stubs"""

    def setUp(self):
        self.api = SupportApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_contact(self):
        """Test case for create_contact

        Createcontact  # noqa: E501
        """
        pass

    def test_create_ticket(self):
        """Test case for create_ticket

        Createticket  # noqa: E501
        """
        pass

    def test_list_tickets(self):
        """Test case for list_tickets

        Listtickets  # noqa: E501
        """
        pass

    def test_update_ticket(self):
        """Test case for update_ticket

        Updateticket  # noqa: E501
        """
        pass

    def test_view_ticket(self):
        """Test case for view_ticket

        Viewticket  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
