"""
    eHelply SDK

    eHelply SDK  # noqa: E501

    The version of the OpenAPI document: 1.1.30
    Generated by: https://openapi-generator.tech
"""


import unittest

import ehelply-python-sdk
from ehelply-python-sdk.api.access_api import AccessApi  # noqa: E501


class TestAccessApi(unittest.TestCase):
    """AccessApi unit test stubs"""

    def setUp(self):
        self.api = AccessApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_entity_to_group_access_partitions_partition_identifier_who_groups_group_uuid_entities_entity_identifier_post(self):
        """Test case for add_entity_to_group_access_partitions_partition_identifier_who_groups_group_uuid_entities_entity_identifier_post

        Add Entity To Group  # noqa: E501
        """
        pass

    def test_add_node_to_key_access_partitions_partition_identifier_keys_key_uuid_nodes_node_uuid_post(self):
        """Test case for add_node_to_key_access_partitions_partition_identifier_keys_key_uuid_nodes_node_uuid_post

        Add Node To Key  # noqa: E501
        """
        pass

    def test_add_node_to_role_access_partitions_partition_identifier_roles_role_uuid_nodes_node_uuid_post(self):
        """Test case for add_node_to_role_access_partitions_partition_identifier_roles_role_uuid_nodes_node_uuid_post

        Add Node To Role  # noqa: E501
        """
        pass

    def test_attach_key_to_entity_access_partitions_partition_identifier_who_entities_entity_identifier_keys_key_uuid_post(self):
        """Test case for attach_key_to_entity_access_partitions_partition_identifier_who_entities_entity_identifier_keys_key_uuid_post

        Attach Key To Entity  # noqa: E501
        """
        pass

    def test_create_group_access_partitions_partition_identifier_who_groups_post(self):
        """Test case for create_group_access_partitions_partition_identifier_who_groups_post

        Create Group  # noqa: E501
        """
        pass

    def test_create_node(self):
        """Test case for create_node

        Createnode  # noqa: E501
        """
        pass

    def test_create_role_access_partitions_partition_identifier_roles_post(self):
        """Test case for create_role_access_partitions_partition_identifier_roles_post

        Create Role  # noqa: E501
        """
        pass

    def test_create_type_access_partitions_partition_identifier_permissions_types_post(self):
        """Test case for create_type_access_partitions_partition_identifier_permissions_types_post

        Create Type  # noqa: E501
        """
        pass

    def test_delete_group_access_partitions_partition_identifier_who_groups_group_uuid_delete(self):
        """Test case for delete_group_access_partitions_partition_identifier_who_groups_group_uuid_delete

        Delete Group  # noqa: E501
        """
        pass

    def test_delete_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_delete(self):
        """Test case for delete_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_delete

        Delete Node  # noqa: E501
        """
        pass

    def test_delete_role_access_partitions_partition_identifier_roles_role_uuid_delete(self):
        """Test case for delete_role_access_partitions_partition_identifier_roles_role_uuid_delete

        Delete Role  # noqa: E501
        """
        pass

    def test_delete_type_access_partitions_partition_identifier_permissions_types_type_uuid_delete(self):
        """Test case for delete_type_access_partitions_partition_identifier_permissions_types_type_uuid_delete

        Delete Type  # noqa: E501
        """
        pass

    def test_destroy_rgt_access_partitions_partition_identifier_rgts_roles_role_uuid_groups_group_uuid_targets_target_identifier_delete(self):
        """Test case for destroy_rgt_access_partitions_partition_identifier_rgts_roles_role_uuid_groups_group_uuid_targets_target_identifier_delete

        Destroy Rgt  # noqa: E501
        """
        pass

    def test_dettach_key_from_entity_access_partitions_partition_identifier_who_entities_entity_identifier_keys_key_uuid_delete(self):
        """Test case for dettach_key_from_entity_access_partitions_partition_identifier_who_entities_entity_identifier_keys_key_uuid_delete

        Dettach Key From Entity  # noqa: E501
        """
        pass

    def test_get_entity_access_partitions_partition_identifier_who_entities_entity_identifier_get(self):
        """Test case for get_entity_access_partitions_partition_identifier_who_entities_entity_identifier_get

        Get Entity  # noqa: E501
        """
        pass

    def test_get_entity_for_key_access_partitions_partition_identifier_who_entities_keys_key_uuid_get(self):
        """Test case for get_entity_for_key_access_partitions_partition_identifier_who_entities_keys_key_uuid_get

        Get Entity For Key  # noqa: E501
        """
        pass

    def test_get_entity_keys_access_partitions_partition_identifier_who_entities_entity_identifier_keys_get(self):
        """Test case for get_entity_keys_access_partitions_partition_identifier_who_entities_entity_identifier_keys_get

        Get Entity Keys  # noqa: E501
        """
        pass

    def test_get_group_access_partitions_partition_identifier_who_groups_group_uuid_get(self):
        """Test case for get_group_access_partitions_partition_identifier_who_groups_group_uuid_get

        Get Group  # noqa: E501
        """
        pass

    def test_get_groups_for_entity_access_partitions_partition_identifier_who_groups_entities_entity_identifier_get(self):
        """Test case for get_groups_for_entity_access_partitions_partition_identifier_who_groups_entities_entity_identifier_get

        Get Groups For Entity  # noqa: E501
        """
        pass

    def test_get_limits_for_entity_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_entities_entity_identifier_get(self):
        """Test case for get_limits_for_entity_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_entities_entity_identifier_get

        Get Limits For Entity On Target  # noqa: E501
        """
        pass

    def test_get_limits_for_key_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_keys_get(self):
        """Test case for get_limits_for_key_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_keys_get

        Get Limits For Key On Target  # noqa: E501
        """
        pass

    def test_get_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_get(self):
        """Test case for get_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_get

        Get Node  # noqa: E501
        """
        pass

    def test_get_nodes_for_entity_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_get(self):
        """Test case for get_nodes_for_entity_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_get

        Get Nodes For Entity  # noqa: E501
        """
        pass

    def test_get_nodes_for_entity_key_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_keys_key_uuid_get(self):
        """Test case for get_nodes_for_entity_key_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_keys_key_uuid_get

        Get Nodes For Entity Key  # noqa: E501
        """
        pass

    def test_get_nodes_for_entity_target_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_targets_target_identifier_get(self):
        """Test case for get_nodes_for_entity_target_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_targets_target_identifier_get

        Get Nodes For Entity Target  # noqa: E501
        """
        pass

    def test_get_rgt_access_partitions_partition_identifier_rgts_rgt_uuid_get(self):
        """Test case for get_rgt_access_partitions_partition_identifier_rgts_rgt_uuid_get

        Get Rgt  # noqa: E501
        """
        pass

    def test_get_role_access_partitions_partition_identifier_roles_role_uuid_get(self):
        """Test case for get_role_access_partitions_partition_identifier_roles_role_uuid_get

        Get Role  # noqa: E501
        """
        pass

    def test_get_type_access_partitions_partition_identifier_permissions_types_type_uuid_get(self):
        """Test case for get_type_access_partitions_partition_identifier_permissions_types_type_uuid_get

        Get Type  # noqa: E501
        """
        pass

    def test_is_allowed_for_entity_on_target_with_node_access_partitions_partition_identifier_auth_targets_target_identifier_nodes_node_entities_entity_identifier_get(self):
        """Test case for is_allowed_for_entity_on_target_with_node_access_partitions_partition_identifier_auth_targets_target_identifier_nodes_node_entities_entity_identifier_get

        Is Allowed For Entity On Target With Node  # noqa: E501
        """
        pass

    def test_make_rgt_access_partitions_partition_identifier_rgts_roles_role_uuid_groups_group_uuid_targets_target_identifier_post(self):
        """Test case for make_rgt_access_partitions_partition_identifier_rgts_roles_role_uuid_groups_group_uuid_targets_target_identifier_post

        Make Rgt  # noqa: E501
        """
        pass

    def test_remove_entity_from_group_access_partitions_partition_identifier_who_groups_group_uuid_entities_entity_identifier_delete(self):
        """Test case for remove_entity_from_group_access_partitions_partition_identifier_who_groups_group_uuid_entities_entity_identifier_delete

        Remove Entity From Group  # noqa: E501
        """
        pass

    def test_remove_node_from_key_access_partitions_partition_identifier_keys_key_uuid_nodes_node_uuid_delete(self):
        """Test case for remove_node_from_key_access_partitions_partition_identifier_keys_key_uuid_nodes_node_uuid_delete

        Remove Node From Key  # noqa: E501
        """
        pass

    def test_remove_node_from_role_access_partitions_partition_identifier_roles_role_uuid_nodes_node_uuid_delete(self):
        """Test case for remove_node_from_role_access_partitions_partition_identifier_roles_role_uuid_nodes_node_uuid_delete

        Remove Node From Role  # noqa: E501
        """
        pass

    def test_search_groups_access_partitions_partition_identifier_who_groups_get(self):
        """Test case for search_groups_access_partitions_partition_identifier_who_groups_get

        Search Groups  # noqa: E501
        """
        pass

    def test_search_nodes_access_partitions_partition_identifier_permissions_types_type_uuid_nodes_get(self):
        """Test case for search_nodes_access_partitions_partition_identifier_permissions_types_type_uuid_nodes_get

        Search Nodes  # noqa: E501
        """
        pass

    def test_search_roles_access_partitions_partition_identifier_roles_get(self):
        """Test case for search_roles_access_partitions_partition_identifier_roles_get

        Search Roles  # noqa: E501
        """
        pass

    def test_search_types_access_partitions_partition_identifier_permissions_types_get(self):
        """Test case for search_types_access_partitions_partition_identifier_permissions_types_get

        Search Types  # noqa: E501
        """
        pass

    def test_update_group_access_partitions_partition_identifier_who_groups_group_uuid_put(self):
        """Test case for update_group_access_partitions_partition_identifier_who_groups_group_uuid_put

        Update Group  # noqa: E501
        """
        pass

    def test_update_limits_for_entity_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_entities_entity_identifier_post(self):
        """Test case for update_limits_for_entity_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_entities_entity_identifier_post

        Update Limits For Entity On Target  # noqa: E501
        """
        pass

    def test_update_limits_for_key_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_keys_post(self):
        """Test case for update_limits_for_key_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_keys_post

        Update Limits For Key On Target  # noqa: E501
        """
        pass

    def test_update_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_put(self):
        """Test case for update_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_put

        Update Node  # noqa: E501
        """
        pass

    def test_update_role_access_partitions_partition_identifier_roles_role_uuid_put(self):
        """Test case for update_role_access_partitions_partition_identifier_roles_role_uuid_put

        Update Role  # noqa: E501
        """
        pass

    def test_update_type_access_partitions_partition_identifier_permissions_types_type_uuid_put(self):
        """Test case for update_type_access_partitions_partition_identifier_permissions_types_type_uuid_put

        Update Type  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
