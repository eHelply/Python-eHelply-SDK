# coding: utf-8

"""
    eHelply SDK - 1.1.88

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.88
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""

import unittest

import ehelply_python_sdk
from ehelply_python_sdk.api.projects_api import ProjectsApi  # noqa: E501


class TestProjectsApi(unittest.TestCase):
    """ProjectsApi unit test stubs"""

    def setUp(self):
        self.api = ProjectsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_member_to_project_projects_projects_project_uuid_members_entity_uuid_post(self):
        """Test case for add_member_to_project_projects_projects_project_uuid_members_entity_uuid_post

        Add Member To Project  # noqa: E501
        """
        pass

    def test_archive_project_projects_projects_project_uuid_delete(self):
        """Test case for archive_project_projects_projects_project_uuid_delete

        Archive Project  # noqa: E501
        """
        pass

    def test_create_project_key_projects_projects_project_uuid_keys_post(self):
        """Test case for create_project_key_projects_projects_project_uuid_keys_post

        Create Project Key  # noqa: E501
        """
        pass

    def test_create_project_projects_projects_post(self):
        """Test case for create_project_projects_projects_post

        Create Project  # noqa: E501
        """
        pass

    def test_create_usage_type_projects_usage_types_post(self):
        """Test case for create_usage_type_projects_usage_types_post

        Create Usage Type  # noqa: E501
        """
        pass

    def test_delete_usage_type_projects_usage_types_usage_type_key_delete(self):
        """Test case for delete_usage_type_projects_usage_types_usage_type_key_delete

        Delete Usage Type  # noqa: E501
        """
        pass

    def test_get_all_project_usage_projects_projects_project_uuid_usage_get(self):
        """Test case for get_all_project_usage_projects_projects_project_uuid_usage_get

        Get All Project Usage  # noqa: E501
        """
        pass

    def test_get_member_projects_projects_members_entity_uuid_projects_get(self):
        """Test case for get_member_projects_projects_members_entity_uuid_projects_get

        Get Member Projects  # noqa: E501
        """
        pass

    def test_get_project_keys_projects_projects_project_uuid_keys_get(self):
        """Test case for get_project_keys_projects_projects_project_uuid_keys_get

        Get Project Keys  # noqa: E501
        """
        pass

    def test_get_project_members_projects_projects_project_uuid_members_get(self):
        """Test case for get_project_members_projects_projects_project_uuid_members_get

        Get Project Members  # noqa: E501
        """
        pass

    def test_get_project_projects_projects_project_uuid_get(self):
        """Test case for get_project_projects_projects_project_uuid_get

        Get Project  # noqa: E501
        """
        pass

    def test_get_specific_project_usage_projects_projects_project_uuid_usage_usage_type_key_get(self):
        """Test case for get_specific_project_usage_projects_projects_project_uuid_usage_usage_type_key_get

        Get Specific Project Usage  # noqa: E501
        """
        pass

    def test_get_usage_type_projects_usage_types_usage_type_key_get(self):
        """Test case for get_usage_type_projects_usage_types_usage_type_key_get

        Get Usage Type  # noqa: E501
        """
        pass

    def test_remove_member_from_project_projects_projects_project_uuid_members_entity_uuid_delete(self):
        """Test case for remove_member_from_project_projects_projects_project_uuid_members_entity_uuid_delete

        Remove Member From Project  # noqa: E501
        """
        pass

    def test_remove_project_key_projects_projects_project_uuid_keys_delete(self):
        """Test case for remove_project_key_projects_projects_project_uuid_keys_delete

        Remove Project Key  # noqa: E501
        """
        pass

    def test_sandbox_projects_sandbox_get(self):
        """Test case for sandbox_projects_sandbox_get

        Sandbox  # noqa: E501
        """
        pass

    def test_search_projects_projects_projects_get(self):
        """Test case for search_projects_projects_projects_get

        Search Projects  # noqa: E501
        """
        pass

    def test_search_usage_type_projects_usage_types_get(self):
        """Test case for search_usage_type_projects_usage_types_get

        Search Usage Type  # noqa: E501
        """
        pass

    def test_update_project_projects_projects_project_uuid_put(self):
        """Test case for update_project_projects_projects_project_uuid_put

        Update Project  # noqa: E501
        """
        pass

    def test_update_usage_type_projects_usage_types_usage_type_key_put(self):
        """Test case for update_usage_type_projects_usage_types_usage_type_key_put

        Update Usage Type  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
