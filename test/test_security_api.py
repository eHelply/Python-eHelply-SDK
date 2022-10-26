"""
    eHelply SDK - 1.1.117

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.117
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import ehelply_python_sdk
from ehelply_python_sdk.api.security_api import SecurityApi  # noqa: E501


class TestSecurityApi(unittest.TestCase):
    """SecurityApi unit test stubs"""

    def setUp(self):
        self.api = SecurityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_encryption_key(self):
        """Test case for create_encryption_key

        Createencryptionkey  # noqa: E501
        """
        pass

    def test_create_key(self):
        """Test case for create_key

        Createkey  # noqa: E501
        """
        pass

    def test_delete_key(self):
        """Test case for delete_key

        Deletekey  # noqa: E501
        """
        pass

    def test_generate_token(self):
        """Test case for generate_token

        Generatetoken  # noqa: E501
        """
        pass

    def test_get_encryption_key(self):
        """Test case for get_encryption_key

        Getencryptionkey  # noqa: E501
        """
        pass

    def test_get_key(self):
        """Test case for get_key

        Getkey  # noqa: E501
        """
        pass

    def test_search_keys(self):
        """Test case for search_keys

        Searchkeys  # noqa: E501
        """
        pass

    def test_verify_key(self):
        """Test case for verify_key

        Verifykey  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
