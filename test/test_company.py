"""
    eHelply SDK - 1.1.110

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.110
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ehelply_python_sdk
from ehelply_python_sdk.model.company_base import CompanyBase
from ehelply_python_sdk.model.contact_base import ContactBase
globals()['CompanyBase'] = CompanyBase
globals()['ContactBase'] = ContactBase
from ehelply_python_sdk.model.company import Company


class TestCompany(unittest.TestCase):
    """Company unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCompany(self):
        """Test Company"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Company()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
