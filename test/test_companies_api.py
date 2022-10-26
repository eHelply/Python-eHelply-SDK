"""
    eHelply SDK - 1.1.116

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.116
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import ehelply_python_sdk
from ehelply_python_sdk.api.companies_api import CompaniesApi  # noqa: E501


class TestCompaniesApi(unittest.TestCase):
    """CompaniesApi unit test stubs"""

    def setUp(self):
        self.api = CompaniesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_company_places_companies_post(self):
        """Test case for create_company_places_companies_post

        Create Company  # noqa: E501
        """
        pass

    def test_delete_company_places_companies_company_uuid_delete(self):
        """Test case for delete_company_places_companies_company_uuid_delete

        Delete Company  # noqa: E501
        """
        pass

    def test_get_company_places_companies_company_uuid_get(self):
        """Test case for get_company_places_companies_company_uuid_get

        Get Company  # noqa: E501
        """
        pass

    def test_search_companies_places_companies_get(self):
        """Test case for search_companies_places_companies_get

        Search Companies  # noqa: E501
        """
        pass

    def test_update_company_places_companies_company_uuid_put(self):
        """Test case for update_company_places_companies_company_uuid_put

        Update Company  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
