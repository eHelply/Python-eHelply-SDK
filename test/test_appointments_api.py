"""
    eHelply SDK - 1.1.114

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.114
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import ehelply_python_sdk
from ehelply_python_sdk.api.appointments_api import AppointmentsApi  # noqa: E501


class TestAppointmentsApi(unittest.TestCase):
    """AppointmentsApi unit test stubs"""

    def setUp(self):
        self.api = AppointmentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_entity_to_appointment(self):
        """Test case for add_entity_to_appointment

        Addentitytoappointment  # noqa: E501
        """
        pass

    def test_create_appointment(self):
        """Test case for create_appointment

        Createappointment  # noqa: E501
        """
        pass

    def test_delete_appointment(self):
        """Test case for delete_appointment

        Deleteappointment  # noqa: E501
        """
        pass

    def test_detach_entity_from_appointment(self):
        """Test case for detach_entity_from_appointment

        Removeentityfromappointment  # noqa: E501
        """
        pass

    def test_get_appointment(self):
        """Test case for get_appointment

        Getappointment  # noqa: E501
        """
        pass

    def test_search_appointment(self):
        """Test case for search_appointment

        Searchappointments  # noqa: E501
        """
        pass

    def test_search_appointment_entities(self):
        """Test case for search_appointment_entities

        Searchappointmententities  # noqa: E501
        """
        pass

    def test_search_entity_appointments(self):
        """Test case for search_entity_appointments

        Getentityappointments  # noqa: E501
        """
        pass

    def test_update_appointment(self):
        """Test case for update_appointment

        Updateappointment  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
