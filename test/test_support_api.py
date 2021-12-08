"""
    eHelply SDK

    eHelply SDK  # noqa: E501

    The version of the OpenAPI document: 1.1.30
    Generated by: https://openapi-generator.tech
"""


import unittest

import ehelply-python-sdk
from ehelply-python-sdk.api.support_api import SupportApi  # noqa: E501


class TestSupportApi(unittest.TestCase):
    """SupportApi unit test stubs"""

    def setUp(self):
        self.api = SupportApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_contact_support_contact_post(self):
        """Test case for create_contact_support_contact_post

        Create Contact  # noqa: E501
        """
        pass

    def test_create_ticket_support_projects_project_uuid_members_member_uuid_tickets_post(self):
        """Test case for create_ticket_support_projects_project_uuid_members_member_uuid_tickets_post

        Create Ticket  # noqa: E501
        """
        pass

    def test_delete_contact_support_contact_delete(self):
        """Test case for delete_contact_support_contact_delete

        Delete Contact  # noqa: E501
        """
        pass

    def test_list_tickets_support_projects_project_uuid_members_member_uuid_tickets_get(self):
        """Test case for list_tickets_support_projects_project_uuid_members_member_uuid_tickets_get

        List Tickets  # noqa: E501
        """
        pass

    def test_update_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_put(self):
        """Test case for update_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_put

        Update Ticket  # noqa: E501
        """
        pass

    def test_view_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_get(self):
        """Test case for view_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_get

        View Ticket  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
