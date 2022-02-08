# ehelply-python-sdk.AccessApi

All URIs are relative to *https://api.prod.ehelply.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_entity_to_group_access_partitions_partition_identifier_who_groups_group_uuid_entities_entity_identifier_post**](AccessApi.md#add_entity_to_group_access_partitions_partition_identifier_who_groups_group_uuid_entities_entity_identifier_post) | **POST** /sam/access/partitions/{partition_identifier}/who/groups/{group_uuid}/entities/{entity_identifier} | Add Entity To Group
[**add_node_to_key_access_partitions_partition_identifier_keys_key_uuid_nodes_node_uuid_post**](AccessApi.md#add_node_to_key_access_partitions_partition_identifier_keys_key_uuid_nodes_node_uuid_post) | **POST** /sam/access/partitions/{partition_identifier}/keys/{key_uuid}/nodes/{node_uuid} | Add Node To Key
[**add_node_to_role_access_partitions_partition_identifier_roles_role_uuid_nodes_node_uuid_post**](AccessApi.md#add_node_to_role_access_partitions_partition_identifier_roles_role_uuid_nodes_node_uuid_post) | **POST** /sam/access/partitions/{partition_identifier}/roles/{role_uuid}/nodes/{node_uuid} | Add Node To Role
[**attach_key_to_entity_access_partitions_partition_identifier_who_entities_entity_identifier_keys_key_uuid_post**](AccessApi.md#attach_key_to_entity_access_partitions_partition_identifier_who_entities_entity_identifier_keys_key_uuid_post) | **POST** /sam/access/partitions/{partition_identifier}/who/entities/{entity_identifier}/keys/{key_uuid} | Attach Key To Entity
[**create_group_access_partitions_partition_identifier_who_groups_post**](AccessApi.md#create_group_access_partitions_partition_identifier_who_groups_post) | **POST** /sam/access/partitions/{partition_identifier}/who/groups | Create Group
[**create_node**](AccessApi.md#create_node) | **POST** /sam/access/partitions/{partition_identifier}/permissions/types/{type_uuid}/nodes | Createnode
[**create_role_access_partitions_partition_identifier_roles_post**](AccessApi.md#create_role_access_partitions_partition_identifier_roles_post) | **POST** /sam/access/partitions/{partition_identifier}/roles | Create Role
[**create_type_access_partitions_partition_identifier_permissions_types_post**](AccessApi.md#create_type_access_partitions_partition_identifier_permissions_types_post) | **POST** /sam/access/partitions/{partition_identifier}/permissions/types | Create Type
[**delete_group_access_partitions_partition_identifier_who_groups_group_uuid_delete**](AccessApi.md#delete_group_access_partitions_partition_identifier_who_groups_group_uuid_delete) | **DELETE** /sam/access/partitions/{partition_identifier}/who/groups/{group_uuid} | Delete Group
[**delete_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_delete**](AccessApi.md#delete_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_delete) | **DELETE** /sam/access/partitions/{partition_identifier}/permissions/nodes/{node_uuid} | Delete Node
[**delete_role_access_partitions_partition_identifier_roles_role_uuid_delete**](AccessApi.md#delete_role_access_partitions_partition_identifier_roles_role_uuid_delete) | **DELETE** /sam/access/partitions/{partition_identifier}/roles/{role_uuid} | Delete Role
[**delete_type_access_partitions_partition_identifier_permissions_types_type_uuid_delete**](AccessApi.md#delete_type_access_partitions_partition_identifier_permissions_types_type_uuid_delete) | **DELETE** /sam/access/partitions/{partition_identifier}/permissions/types/{type_uuid} | Delete Type
[**destroy_rgt_access_partitions_partition_identifier_rgts_roles_role_uuid_groups_group_uuid_targets_target_identifier_delete**](AccessApi.md#destroy_rgt_access_partitions_partition_identifier_rgts_roles_role_uuid_groups_group_uuid_targets_target_identifier_delete) | **DELETE** /sam/access/partitions/{partition_identifier}/rgts/roles/{role_uuid}/groups/{group_uuid}/targets/{target_identifier} | Destroy Rgt
[**dettach_key_from_entity_access_partitions_partition_identifier_who_entities_entity_identifier_keys_key_uuid_delete**](AccessApi.md#dettach_key_from_entity_access_partitions_partition_identifier_who_entities_entity_identifier_keys_key_uuid_delete) | **DELETE** /sam/access/partitions/{partition_identifier}/who/entities/{entity_identifier}/keys/{key_uuid} | Dettach Key From Entity
[**get_entity_access_partitions_partition_identifier_who_entities_entity_identifier_get**](AccessApi.md#get_entity_access_partitions_partition_identifier_who_entities_entity_identifier_get) | **GET** /sam/access/partitions/{partition_identifier}/who/entities/{entity_identifier} | Get Entity
[**get_entity_for_key_access_partitions_partition_identifier_who_entities_keys_key_uuid_get**](AccessApi.md#get_entity_for_key_access_partitions_partition_identifier_who_entities_keys_key_uuid_get) | **GET** /sam/access/partitions/{partition_identifier}/who/entities/keys/{key_uuid} | Get Entity For Key
[**get_entity_keys_access_partitions_partition_identifier_who_entities_entity_identifier_keys_get**](AccessApi.md#get_entity_keys_access_partitions_partition_identifier_who_entities_entity_identifier_keys_get) | **GET** /sam/access/partitions/{partition_identifier}/who/entities/{entity_identifier}/keys | Get Entity Keys
[**get_group_access_partitions_partition_identifier_who_groups_group_uuid_get**](AccessApi.md#get_group_access_partitions_partition_identifier_who_groups_group_uuid_get) | **GET** /sam/access/partitions/{partition_identifier}/who/groups/{group_uuid} | Get Group
[**get_groups_for_entity_access_partitions_partition_identifier_who_groups_entities_entity_identifier_get**](AccessApi.md#get_groups_for_entity_access_partitions_partition_identifier_who_groups_entities_entity_identifier_get) | **GET** /sam/access/partitions/{partition_identifier}/who/groups/entities/{entity_identifier} | Get Groups For Entity
[**get_limits_for_entity_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_entities_entity_identifier_get**](AccessApi.md#get_limits_for_entity_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_entities_entity_identifier_get) | **GET** /sam/access/partitions/{partition_identifier}/limits/targets/{target_identifier}/entities/{entity_identifier} | Get Limits For Entity On Target
[**get_limits_for_key_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_keys_get**](AccessApi.md#get_limits_for_key_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_keys_get) | **GET** /sam/access/partitions/{partition_identifier}/limits/targets/{target_identifier}/keys | Get Limits For Key On Target
[**get_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_get**](AccessApi.md#get_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_get) | **GET** /sam/access/partitions/{partition_identifier}/permissions/nodes/{node_uuid} | Get Node
[**get_nodes_for_entity_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_get**](AccessApi.md#get_nodes_for_entity_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_get) | **GET** /sam/access/partitions/{partition_identifier}/permissions/nodes/entities/{entity_identifier} | Get Nodes For Entity
[**get_nodes_for_entity_key_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_keys_key_uuid_get**](AccessApi.md#get_nodes_for_entity_key_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_keys_key_uuid_get) | **GET** /sam/access/partitions/{partition_identifier}/permissions/nodes/entities/{entity_identifier}/keys/{key_uuid} | Get Nodes For Entity Key
[**get_nodes_for_entity_target_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_targets_target_identifier_get**](AccessApi.md#get_nodes_for_entity_target_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_targets_target_identifier_get) | **GET** /sam/access/partitions/{partition_identifier}/permissions/nodes/entities/{entity_identifier}/targets/{target_identifier} | Get Nodes For Entity Target
[**get_rgt_access_partitions_partition_identifier_rgts_rgt_uuid_get**](AccessApi.md#get_rgt_access_partitions_partition_identifier_rgts_rgt_uuid_get) | **GET** /sam/access/partitions/{partition_identifier}/rgts/{rgt_uuid} | Get Rgt
[**get_role_access_partitions_partition_identifier_roles_role_uuid_get**](AccessApi.md#get_role_access_partitions_partition_identifier_roles_role_uuid_get) | **GET** /sam/access/partitions/{partition_identifier}/roles/{role_uuid} | Get Role
[**get_type_access_partitions_partition_identifier_permissions_types_type_uuid_get**](AccessApi.md#get_type_access_partitions_partition_identifier_permissions_types_type_uuid_get) | **GET** /sam/access/partitions/{partition_identifier}/permissions/types/{type_uuid} | Get Type
[**is_allowed_for_entity_on_target_with_node_access_partitions_partition_identifier_auth_targets_target_identifier_nodes_node_entities_entity_identifier_get**](AccessApi.md#is_allowed_for_entity_on_target_with_node_access_partitions_partition_identifier_auth_targets_target_identifier_nodes_node_entities_entity_identifier_get) | **GET** /sam/access/partitions/{partition_identifier}/auth/targets/{target_identifier}/nodes/{node}/entities/{entity_identifier} | Is Allowed For Entity On Target With Node
[**make_rgt_access_partitions_partition_identifier_rgts_roles_role_uuid_groups_group_uuid_targets_target_identifier_post**](AccessApi.md#make_rgt_access_partitions_partition_identifier_rgts_roles_role_uuid_groups_group_uuid_targets_target_identifier_post) | **POST** /sam/access/partitions/{partition_identifier}/rgts/roles/{role_uuid}/groups/{group_uuid}/targets/{target_identifier} | Make Rgt
[**remove_entity_from_group_access_partitions_partition_identifier_who_groups_group_uuid_entities_entity_identifier_delete**](AccessApi.md#remove_entity_from_group_access_partitions_partition_identifier_who_groups_group_uuid_entities_entity_identifier_delete) | **DELETE** /sam/access/partitions/{partition_identifier}/who/groups/{group_uuid}/entities/{entity_identifier} | Remove Entity From Group
[**remove_node_from_key_access_partitions_partition_identifier_keys_key_uuid_nodes_node_uuid_delete**](AccessApi.md#remove_node_from_key_access_partitions_partition_identifier_keys_key_uuid_nodes_node_uuid_delete) | **DELETE** /sam/access/partitions/{partition_identifier}/keys/{key_uuid}/nodes/{node_uuid} | Remove Node From Key
[**remove_node_from_role_access_partitions_partition_identifier_roles_role_uuid_nodes_node_uuid_delete**](AccessApi.md#remove_node_from_role_access_partitions_partition_identifier_roles_role_uuid_nodes_node_uuid_delete) | **DELETE** /sam/access/partitions/{partition_identifier}/roles/{role_uuid}/nodes/{node_uuid} | Remove Node From Role
[**search_groups_access_partitions_partition_identifier_who_groups_get**](AccessApi.md#search_groups_access_partitions_partition_identifier_who_groups_get) | **GET** /sam/access/partitions/{partition_identifier}/who/groups | Search Groups
[**search_nodes_access_partitions_partition_identifier_permissions_types_type_uuid_nodes_get**](AccessApi.md#search_nodes_access_partitions_partition_identifier_permissions_types_type_uuid_nodes_get) | **GET** /sam/access/partitions/{partition_identifier}/permissions/types/{type_uuid}/nodes | Search Nodes
[**search_roles_access_partitions_partition_identifier_roles_get**](AccessApi.md#search_roles_access_partitions_partition_identifier_roles_get) | **GET** /sam/access/partitions/{partition_identifier}/roles | Search Roles
[**search_types_access_partitions_partition_identifier_permissions_types_get**](AccessApi.md#search_types_access_partitions_partition_identifier_permissions_types_get) | **GET** /sam/access/partitions/{partition_identifier}/permissions/types | Search Types
[**update_group_access_partitions_partition_identifier_who_groups_group_uuid_put**](AccessApi.md#update_group_access_partitions_partition_identifier_who_groups_group_uuid_put) | **PUT** /sam/access/partitions/{partition_identifier}/who/groups/{group_uuid} | Update Group
[**update_limits_for_entity_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_entities_entity_identifier_post**](AccessApi.md#update_limits_for_entity_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_entities_entity_identifier_post) | **POST** /sam/access/partitions/{partition_identifier}/limits/targets/{target_identifier}/entities/{entity_identifier} | Update Limits For Entity On Target
[**update_limits_for_key_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_keys_post**](AccessApi.md#update_limits_for_key_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_keys_post) | **POST** /sam/access/partitions/{partition_identifier}/limits/targets/{target_identifier}/keys | Update Limits For Key On Target
[**update_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_put**](AccessApi.md#update_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_put) | **PUT** /sam/access/partitions/{partition_identifier}/permissions/nodes/{node_uuid} | Update Node
[**update_role_access_partitions_partition_identifier_roles_role_uuid_put**](AccessApi.md#update_role_access_partitions_partition_identifier_roles_role_uuid_put) | **PUT** /sam/access/partitions/{partition_identifier}/roles/{role_uuid} | Update Role
[**update_type_access_partitions_partition_identifier_permissions_types_type_uuid_put**](AccessApi.md#update_type_access_partitions_partition_identifier_permissions_types_type_uuid_put) | **PUT** /sam/access/partitions/{partition_identifier}/permissions/types/{type_uuid} | Update Type


# **add_entity_to_group_access_partitions_partition_identifier_who_groups_group_uuid_entities_entity_identifier_post**
> bool, date, datetime, dict, float, int, list, str, none_type add_entity_to_group_access_partitions_partition_identifier_who_groups_group_uuid_entities_entity_identifier_post(partition_identifier, group_uuid, entity_identifier)

Add Entity To Group

Put a new Entity into a Group

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    group_uuid = "group_uuid_example" # str | 
    entity_identifier = "entity_identifier_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add Entity To Group
        api_response = api_instance.add_entity_to_group_access_partitions_partition_identifier_who_groups_group_uuid_entities_entity_identifier_post(partition_identifier, group_uuid, entity_identifier)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->add_entity_to_group_access_partitions_partition_identifier_who_groups_group_uuid_entities_entity_identifier_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add Entity To Group
        api_response = api_instance.add_entity_to_group_access_partitions_partition_identifier_who_groups_group_uuid_entities_entity_identifier_post(partition_identifier, group_uuid, entity_identifier, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->add_entity_to_group_access_partitions_partition_identifier_who_groups_group_uuid_entities_entity_identifier_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **group_uuid** | **str**|  |
 **entity_identifier** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Group does not exist |  -  |
**409** | Entity already exists |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_node_to_key_access_partitions_partition_identifier_keys_key_uuid_nodes_node_uuid_post**
> bool, date, datetime, dict, float, int, list, str, none_type add_node_to_key_access_partitions_partition_identifier_keys_key_uuid_nodes_node_uuid_post(partition_identifier, key_uuid, node_uuid)

Add Node To Key

Whitelist a Node on a Key.  Note: In order to whitelist a Node, the Entity which the Key belongs to MUST have access to the same Node

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    key_uuid = "key_uuid_example" # str | 
    node_uuid = "node_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add Node To Key
        api_response = api_instance.add_node_to_key_access_partitions_partition_identifier_keys_key_uuid_nodes_node_uuid_post(partition_identifier, key_uuid, node_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->add_node_to_key_access_partitions_partition_identifier_keys_key_uuid_nodes_node_uuid_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add Node To Key
        api_response = api_instance.add_node_to_key_access_partitions_partition_identifier_keys_key_uuid_nodes_node_uuid_post(partition_identifier, key_uuid, node_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->add_node_to_key_access_partitions_partition_identifier_keys_key_uuid_nodes_node_uuid_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **key_uuid** | **str**|  |
 **node_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Key or Node does not exist |  -  |
**409** | Node already exists |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_node_to_role_access_partitions_partition_identifier_roles_role_uuid_nodes_node_uuid_post**
> bool, date, datetime, dict, float, int, list, str, none_type add_node_to_role_access_partitions_partition_identifier_roles_role_uuid_nodes_node_uuid_post(partition_identifier, role_uuid, node_uuid)

Add Node To Role

Add a Node to a Role

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    role_uuid = "role_uuid_example" # str | 
    node_uuid = "node_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add Node To Role
        api_response = api_instance.add_node_to_role_access_partitions_partition_identifier_roles_role_uuid_nodes_node_uuid_post(partition_identifier, role_uuid, node_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->add_node_to_role_access_partitions_partition_identifier_roles_role_uuid_nodes_node_uuid_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add Node To Role
        api_response = api_instance.add_node_to_role_access_partitions_partition_identifier_roles_role_uuid_nodes_node_uuid_post(partition_identifier, role_uuid, node_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->add_node_to_role_access_partitions_partition_identifier_roles_role_uuid_nodes_node_uuid_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **role_uuid** | **str**|  |
 **node_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Role or Node does not exist |  -  |
**409** | Node already exists |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_key_to_entity_access_partitions_partition_identifier_who_entities_entity_identifier_keys_key_uuid_post**
> bool, date, datetime, dict, float, int, list, str, none_type attach_key_to_entity_access_partitions_partition_identifier_who_entities_entity_identifier_keys_key_uuid_post(partition_identifier, key_uuid, entity_identifier)

Attach Key To Entity

Attach a Key to an Entity (This makes an Entity Key)

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    key_uuid = "key_uuid_example" # str | 
    entity_identifier = "entity_identifier_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Attach Key To Entity
        api_response = api_instance.attach_key_to_entity_access_partitions_partition_identifier_who_entities_entity_identifier_keys_key_uuid_post(partition_identifier, key_uuid, entity_identifier)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->attach_key_to_entity_access_partitions_partition_identifier_who_entities_entity_identifier_keys_key_uuid_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Attach Key To Entity
        api_response = api_instance.attach_key_to_entity_access_partitions_partition_identifier_who_entities_entity_identifier_keys_key_uuid_post(partition_identifier, key_uuid, entity_identifier, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->attach_key_to_entity_access_partitions_partition_identifier_who_entities_entity_identifier_keys_key_uuid_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **key_uuid** | **str**|  |
 **entity_identifier** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group_access_partitions_partition_identifier_who_groups_post**
> AccessGroupDB create_group_access_partitions_partition_identifier_who_groups_post(partition_identifier, body_create_group_access_partitions_partition_identifier_who_groups_post)

Create Group

Create a new group

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.body_create_group_access_partitions_partition_identifier_who_groups_post import BodyCreateGroupAccessPartitionsPartitionIdentifierWhoGroupsPost
from ehelply-python-sdk.model.access_group_db import AccessGroupDB
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    body_create_group_access_partitions_partition_identifier_who_groups_post = BodyCreateGroupAccessPartitionsPartitionIdentifierWhoGroupsPost(
        group=AccessGroupCreate(
            name="name_example",
            summary="summary_example",
            entity_identifiers=[],
            default=False,
        ),
    ) # BodyCreateGroupAccessPartitionsPartitionIdentifierWhoGroupsPost | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Group
        api_response = api_instance.create_group_access_partitions_partition_identifier_who_groups_post(partition_identifier, body_create_group_access_partitions_partition_identifier_who_groups_post)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->create_group_access_partitions_partition_identifier_who_groups_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Group
        api_response = api_instance.create_group_access_partitions_partition_identifier_who_groups_post(partition_identifier, body_create_group_access_partitions_partition_identifier_who_groups_post, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->create_group_access_partitions_partition_identifier_who_groups_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **body_create_group_access_partitions_partition_identifier_who_groups_post** | [**BodyCreateGroupAccessPartitionsPartitionIdentifierWhoGroupsPost**](BodyCreateGroupAccessPartitionsPartitionIdentifierWhoGroupsPost.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**AccessGroupDB**](AccessGroupDB.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_node**
> AccessNodeDB create_node(partition_identifier, type_uuid, body_create_node_access_partitions_partition_identifier_permissions_types_type_uuid_nodes_post)

Createnode

Create a new Node

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.access_node_db import AccessNodeDB
from ehelply-python-sdk.model.body_create_node_access_partitions_partition_identifier_permissions_types_type_uuid_nodes_post import BodyCreateNodeAccessPartitionsPartitionIdentifierPermissionsTypesTypeUuidNodesPost
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    type_uuid = "type_uuid_example" # str | 
    body_create_node_access_partitions_partition_identifier_permissions_types_type_uuid_nodes_post = BodyCreateNodeAccessPartitionsPartitionIdentifierPermissionsTypesTypeUuidNodesPost(
        node=AccessNodeCreate(
            name="name_example",
            node="node_example",
            summary="summary_example",
        ),
    ) # BodyCreateNodeAccessPartitionsPartitionIdentifierPermissionsTypesTypeUuidNodesPost | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Createnode
        api_response = api_instance.create_node(partition_identifier, type_uuid, body_create_node_access_partitions_partition_identifier_permissions_types_type_uuid_nodes_post)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->create_node: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Createnode
        api_response = api_instance.create_node(partition_identifier, type_uuid, body_create_node_access_partitions_partition_identifier_permissions_types_type_uuid_nodes_post, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->create_node: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **type_uuid** | **str**|  |
 **body_create_node_access_partitions_partition_identifier_permissions_types_type_uuid_nodes_post** | [**BodyCreateNodeAccessPartitionsPartitionIdentifierPermissionsTypesTypeUuidNodesPost**](BodyCreateNodeAccessPartitionsPartitionIdentifierPermissionsTypesTypeUuidNodesPost.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**AccessNodeDB**](AccessNodeDB.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Type does not exist |  -  |
**409** | Node already exists |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role_access_partitions_partition_identifier_roles_post**
> AccessRoleDB create_role_access_partitions_partition_identifier_roles_post(partition_identifier, body_create_role_access_partitions_partition_identifier_roles_post)

Create Role

Create a new Role

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.body_create_role_access_partitions_partition_identifier_roles_post import BodyCreateRoleAccessPartitionsPartitionIdentifierRolesPost
from ehelply-python-sdk.model.access_role_db import AccessRoleDB
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    body_create_role_access_partitions_partition_identifier_roles_post = BodyCreateRoleAccessPartitionsPartitionIdentifierRolesPost(
        role=AccessRoleCreate(
            name="name_example",
            summary="summary_example",
        ),
    ) # BodyCreateRoleAccessPartitionsPartitionIdentifierRolesPost | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Role
        api_response = api_instance.create_role_access_partitions_partition_identifier_roles_post(partition_identifier, body_create_role_access_partitions_partition_identifier_roles_post)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->create_role_access_partitions_partition_identifier_roles_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Role
        api_response = api_instance.create_role_access_partitions_partition_identifier_roles_post(partition_identifier, body_create_role_access_partitions_partition_identifier_roles_post, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->create_role_access_partitions_partition_identifier_roles_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **body_create_role_access_partitions_partition_identifier_roles_post** | [**BodyCreateRoleAccessPartitionsPartitionIdentifierRolesPost**](BodyCreateRoleAccessPartitionsPartitionIdentifierRolesPost.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**AccessRoleDB**](AccessRoleDB.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_type_access_partitions_partition_identifier_permissions_types_post**
> AccessTypeDB create_type_access_partitions_partition_identifier_permissions_types_post(partition_identifier, body_create_type_access_partitions_partition_identifier_permissions_types_post)

Create Type

Create a new Type

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.body_create_type_access_partitions_partition_identifier_permissions_types_post import BodyCreateTypeAccessPartitionsPartitionIdentifierPermissionsTypesPost
from ehelply-python-sdk.model.access_type_db import AccessTypeDB
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    body_create_type_access_partitions_partition_identifier_permissions_types_post = BodyCreateTypeAccessPartitionsPartitionIdentifierPermissionsTypesPost(
        partition_type=AccessTypeCreate(
            name="name_example",
            summary="summary_example",
        ),
    ) # BodyCreateTypeAccessPartitionsPartitionIdentifierPermissionsTypesPost | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Type
        api_response = api_instance.create_type_access_partitions_partition_identifier_permissions_types_post(partition_identifier, body_create_type_access_partitions_partition_identifier_permissions_types_post)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->create_type_access_partitions_partition_identifier_permissions_types_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Type
        api_response = api_instance.create_type_access_partitions_partition_identifier_permissions_types_post(partition_identifier, body_create_type_access_partitions_partition_identifier_permissions_types_post, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->create_type_access_partitions_partition_identifier_permissions_types_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **body_create_type_access_partitions_partition_identifier_permissions_types_post** | [**BodyCreateTypeAccessPartitionsPartitionIdentifierPermissionsTypesPost**](BodyCreateTypeAccessPartitionsPartitionIdentifierPermissionsTypesPost.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**AccessTypeDB**](AccessTypeDB.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**409** | Type already exists |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_access_partitions_partition_identifier_who_groups_group_uuid_delete**
> bool, date, datetime, dict, float, int, list, str, none_type delete_group_access_partitions_partition_identifier_who_groups_group_uuid_delete(partition_identifier, group_uuid)

Delete Group

Delete a Group

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    group_uuid = "group_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete Group
        api_response = api_instance.delete_group_access_partitions_partition_identifier_who_groups_group_uuid_delete(partition_identifier, group_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->delete_group_access_partitions_partition_identifier_who_groups_group_uuid_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Group
        api_response = api_instance.delete_group_access_partitions_partition_identifier_who_groups_group_uuid_delete(partition_identifier, group_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->delete_group_access_partitions_partition_identifier_who_groups_group_uuid_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **group_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Group does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_delete**
> bool, date, datetime, dict, float, int, list, str, none_type delete_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_delete(partition_identifier, node_uuid)

Delete Node

Delete an existing Node

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    node_uuid = "node_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete Node
        api_response = api_instance.delete_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_delete(partition_identifier, node_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->delete_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Node
        api_response = api_instance.delete_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_delete(partition_identifier, node_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->delete_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **node_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Node does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_access_partitions_partition_identifier_roles_role_uuid_delete**
> bool, date, datetime, dict, float, int, list, str, none_type delete_role_access_partitions_partition_identifier_roles_role_uuid_delete(partition_identifier, role_uuid)

Delete Role

Delete an existing Role

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    role_uuid = "role_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete Role
        api_response = api_instance.delete_role_access_partitions_partition_identifier_roles_role_uuid_delete(partition_identifier, role_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->delete_role_access_partitions_partition_identifier_roles_role_uuid_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Role
        api_response = api_instance.delete_role_access_partitions_partition_identifier_roles_role_uuid_delete(partition_identifier, role_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->delete_role_access_partitions_partition_identifier_roles_role_uuid_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **role_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_type_access_partitions_partition_identifier_permissions_types_type_uuid_delete**
> bool, date, datetime, dict, float, int, list, str, none_type delete_type_access_partitions_partition_identifier_permissions_types_type_uuid_delete(partition_identifier, type_uuid)

Delete Type

Delete an existing Type

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    type_uuid = "type_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete Type
        api_response = api_instance.delete_type_access_partitions_partition_identifier_permissions_types_type_uuid_delete(partition_identifier, type_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->delete_type_access_partitions_partition_identifier_permissions_types_type_uuid_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Type
        api_response = api_instance.delete_type_access_partitions_partition_identifier_permissions_types_type_uuid_delete(partition_identifier, type_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->delete_type_access_partitions_partition_identifier_permissions_types_type_uuid_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **type_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Type does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_rgt_access_partitions_partition_identifier_rgts_roles_role_uuid_groups_group_uuid_targets_target_identifier_delete**
> bool, date, datetime, dict, float, int, list, str, none_type destroy_rgt_access_partitions_partition_identifier_rgts_roles_role_uuid_groups_group_uuid_targets_target_identifier_delete(partition_identifier, role_uuid, group_uuid, target_identifier)

Destroy Rgt

Remove an existing RGT

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    role_uuid = "role_uuid_example" # str | 
    group_uuid = "group_uuid_example" # str | 
    target_identifier = "target_identifier_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Destroy Rgt
        api_response = api_instance.destroy_rgt_access_partitions_partition_identifier_rgts_roles_role_uuid_groups_group_uuid_targets_target_identifier_delete(partition_identifier, role_uuid, group_uuid, target_identifier)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->destroy_rgt_access_partitions_partition_identifier_rgts_roles_role_uuid_groups_group_uuid_targets_target_identifier_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Destroy Rgt
        api_response = api_instance.destroy_rgt_access_partitions_partition_identifier_rgts_roles_role_uuid_groups_group_uuid_targets_target_identifier_delete(partition_identifier, role_uuid, group_uuid, target_identifier, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->destroy_rgt_access_partitions_partition_identifier_rgts_roles_role_uuid_groups_group_uuid_targets_target_identifier_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **role_uuid** | **str**|  |
 **group_uuid** | **str**|  |
 **target_identifier** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Role, Group, or Target does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dettach_key_from_entity_access_partitions_partition_identifier_who_entities_entity_identifier_keys_key_uuid_delete**
> bool, date, datetime, dict, float, int, list, str, none_type dettach_key_from_entity_access_partitions_partition_identifier_who_entities_entity_identifier_keys_key_uuid_delete(partition_identifier, key_uuid, entity_identifier)

Dettach Key From Entity

Dettach a Key from an Entity

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    key_uuid = "key_uuid_example" # str | 
    entity_identifier = "entity_identifier_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Dettach Key From Entity
        api_response = api_instance.dettach_key_from_entity_access_partitions_partition_identifier_who_entities_entity_identifier_keys_key_uuid_delete(partition_identifier, key_uuid, entity_identifier)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->dettach_key_from_entity_access_partitions_partition_identifier_who_entities_entity_identifier_keys_key_uuid_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Dettach Key From Entity
        api_response = api_instance.dettach_key_from_entity_access_partitions_partition_identifier_who_entities_entity_identifier_keys_key_uuid_delete(partition_identifier, key_uuid, entity_identifier, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->dettach_key_from_entity_access_partitions_partition_identifier_who_entities_entity_identifier_keys_key_uuid_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **key_uuid** | **str**|  |
 **entity_identifier** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Key does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_access_partitions_partition_identifier_who_entities_entity_identifier_get**
> bool, date, datetime, dict, float, int, list, str, none_type get_entity_access_partitions_partition_identifier_who_entities_entity_identifier_get(partition_identifier, entity_identifier)

Get Entity

Returns the Groups and/or Keys for an Entity

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    entity_identifier = "entity_identifier_example" # str | 
    include_keys = True # bool |  (optional) if omitted the server will use the default value of True
    include_groups = True # bool |  (optional) if omitted the server will use the default value of True
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Entity
        api_response = api_instance.get_entity_access_partitions_partition_identifier_who_entities_entity_identifier_get(partition_identifier, entity_identifier)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->get_entity_access_partitions_partition_identifier_who_entities_entity_identifier_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Entity
        api_response = api_instance.get_entity_access_partitions_partition_identifier_who_entities_entity_identifier_get(partition_identifier, entity_identifier, include_keys=include_keys, include_groups=include_groups, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->get_entity_access_partitions_partition_identifier_who_entities_entity_identifier_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **entity_identifier** | **str**|  |
 **include_keys** | **bool**|  | [optional] if omitted the server will use the default value of True
 **include_groups** | **bool**|  | [optional] if omitted the server will use the default value of True
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Invalid query parameters |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_for_key_access_partitions_partition_identifier_who_entities_keys_key_uuid_get**
> bool, date, datetime, dict, float, int, list, str, none_type get_entity_for_key_access_partitions_partition_identifier_who_entities_keys_key_uuid_get(partition_identifier, key_uuid)

Get Entity For Key

Get the Entity UUID and Entity Type for a Key

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    key_uuid = "key_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Entity For Key
        api_response = api_instance.get_entity_for_key_access_partitions_partition_identifier_who_entities_keys_key_uuid_get(partition_identifier, key_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->get_entity_for_key_access_partitions_partition_identifier_who_entities_keys_key_uuid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **key_uuid** | **str**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Key does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_keys_access_partitions_partition_identifier_who_entities_entity_identifier_keys_get**
> Page get_entity_keys_access_partitions_partition_identifier_who_entities_entity_identifier_keys_get(partition_identifier, entity_identifier)

Get Entity Keys

Get a list of Keys attached to an Entity

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.page import Page
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    entity_identifier = "entity_identifier_example" # str | 
    page = 1 # int |  (optional) if omitted the server will use the default value of 1
    page_size = 25 # int |  (optional) if omitted the server will use the default value of 25
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Entity Keys
        api_response = api_instance.get_entity_keys_access_partitions_partition_identifier_who_entities_entity_identifier_keys_get(partition_identifier, entity_identifier)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->get_entity_keys_access_partitions_partition_identifier_who_entities_entity_identifier_keys_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Entity Keys
        api_response = api_instance.get_entity_keys_access_partitions_partition_identifier_who_entities_entity_identifier_keys_get(partition_identifier, entity_identifier, page=page, page_size=page_size, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->get_entity_keys_access_partitions_partition_identifier_who_entities_entity_identifier_keys_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **entity_identifier** | **str**|  |
 **page** | **int**|  | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 25
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**Page**](Page.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_access_partitions_partition_identifier_who_groups_group_uuid_get**
> AccessGroupGet get_group_access_partitions_partition_identifier_who_groups_group_uuid_get(partition_identifier, group_uuid)

Get Group

Get a Group

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.access_group_get import AccessGroupGet
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    group_uuid = "group_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Group
        api_response = api_instance.get_group_access_partitions_partition_identifier_who_groups_group_uuid_get(partition_identifier, group_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->get_group_access_partitions_partition_identifier_who_groups_group_uuid_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Group
        api_response = api_instance.get_group_access_partitions_partition_identifier_who_groups_group_uuid_get(partition_identifier, group_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->get_group_access_partitions_partition_identifier_who_groups_group_uuid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **group_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**AccessGroupGet**](AccessGroupGet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Group does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups_for_entity_access_partitions_partition_identifier_who_groups_entities_entity_identifier_get**
> Page get_groups_for_entity_access_partitions_partition_identifier_who_groups_entities_entity_identifier_get(partition_identifier, entity_identifier)

Get Groups For Entity

Get a list of Groups which an Entity belongs to

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.page import Page
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    entity_identifier = "entity_identifier_example" # str | 
    page = 1 # int |  (optional) if omitted the server will use the default value of 1
    page_size = 25 # int |  (optional) if omitted the server will use the default value of 25
    search = "search_example" # str |  (optional)
    search_on = "search_on_example" # str |  (optional)
    sort_on = "sort_on_example" # str |  (optional)
    sort_desc = False # bool |  (optional) if omitted the server will use the default value of False
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Groups For Entity
        api_response = api_instance.get_groups_for_entity_access_partitions_partition_identifier_who_groups_entities_entity_identifier_get(partition_identifier, entity_identifier)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->get_groups_for_entity_access_partitions_partition_identifier_who_groups_entities_entity_identifier_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Groups For Entity
        api_response = api_instance.get_groups_for_entity_access_partitions_partition_identifier_who_groups_entities_entity_identifier_get(partition_identifier, entity_identifier, page=page, page_size=page_size, search=search, search_on=search_on, sort_on=sort_on, sort_desc=sort_desc, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->get_groups_for_entity_access_partitions_partition_identifier_who_groups_entities_entity_identifier_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **entity_identifier** | **str**|  |
 **page** | **int**|  | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 25
 **search** | **str**|  | [optional]
 **search_on** | **str**|  | [optional]
 **sort_on** | **str**|  | [optional]
 **sort_desc** | **bool**|  | [optional] if omitted the server will use the default value of False
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**Page**](Page.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_limits_for_entity_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_entities_entity_identifier_get**
> [AccessLimitCreate] get_limits_for_entity_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_entities_entity_identifier_get(partition_identifier, entity_identifier, target_identifier)

Get Limits For Entity On Target

Returns the limits for an entity on a target

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.access_limit_create import AccessLimitCreate
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    entity_identifier = "entity_identifier_example" # str | 
    target_identifier = "target_identifier_example" # str | 
    limit = "limit_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Limits For Entity On Target
        api_response = api_instance.get_limits_for_entity_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_entities_entity_identifier_get(partition_identifier, entity_identifier, target_identifier)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->get_limits_for_entity_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_entities_entity_identifier_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Limits For Entity On Target
        api_response = api_instance.get_limits_for_entity_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_entities_entity_identifier_get(partition_identifier, entity_identifier, target_identifier, limit=limit)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->get_limits_for_entity_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_entities_entity_identifier_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **entity_identifier** | **str**|  |
 **target_identifier** | **str**|  |
 **limit** | **str**|  | [optional]

### Return type

[**[AccessLimitCreate]**](AccessLimitCreate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Limit or RGT does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_limits_for_key_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_keys_get**
> [AccessLimitCreate] get_limits_for_key_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_keys_get(partition_identifier, target_identifier)

Get Limits For Key On Target

Returns the limits for a key on a target

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.access_limit_create import AccessLimitCreate
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    target_identifier = "target_identifier_example" # str | 
    limit = "limit_example" # str |  (optional)
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Limits For Key On Target
        api_response = api_instance.get_limits_for_key_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_keys_get(partition_identifier, target_identifier)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->get_limits_for_key_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_keys_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Limits For Key On Target
        api_response = api_instance.get_limits_for_key_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_keys_get(partition_identifier, target_identifier, limit=limit, x_access_token=x_access_token, x_secret_token=x_secret_token)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->get_limits_for_key_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_keys_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **target_identifier** | **str**|  |
 **limit** | **str**|  | [optional]
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]

### Return type

[**[AccessLimitCreate]**](AccessLimitCreate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Limit or RGT does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_get**
> AccessNodeGet get_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_get(partition_identifier, node_uuid)

Get Node

Get a Node

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.access_node_get import AccessNodeGet
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    node_uuid = "node_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Node
        api_response = api_instance.get_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_get(partition_identifier, node_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->get_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Node
        api_response = api_instance.get_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_get(partition_identifier, node_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->get_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **node_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**AccessNodeGet**](AccessNodeGet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Node or Role does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nodes_for_entity_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_get**
> [AccessNodeGet] get_nodes_for_entity_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_get(partition_identifier, entity_identifier)

Get Nodes For Entity

Get a list of Nodes which an Entity has

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.access_node_get import AccessNodeGet
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    entity_identifier = "entity_identifier_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Nodes For Entity
        api_response = api_instance.get_nodes_for_entity_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_get(partition_identifier, entity_identifier)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->get_nodes_for_entity_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Nodes For Entity
        api_response = api_instance.get_nodes_for_entity_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_get(partition_identifier, entity_identifier, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->get_nodes_for_entity_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **entity_identifier** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**[AccessNodeGet]**](AccessNodeGet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nodes_for_entity_key_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_keys_key_uuid_get**
> [AccessNodeGet] get_nodes_for_entity_key_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_keys_key_uuid_get(partition_identifier, entity_identifier, key_uuid)

Get Nodes For Entity Key

Get a list of Nodes which an Entity Key has

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.access_node_get import AccessNodeGet
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    entity_identifier = "entity_identifier_example" # str | 
    key_uuid = "key_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Nodes For Entity Key
        api_response = api_instance.get_nodes_for_entity_key_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_keys_key_uuid_get(partition_identifier, entity_identifier, key_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->get_nodes_for_entity_key_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_keys_key_uuid_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Nodes For Entity Key
        api_response = api_instance.get_nodes_for_entity_key_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_keys_key_uuid_get(partition_identifier, entity_identifier, key_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->get_nodes_for_entity_key_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_keys_key_uuid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **entity_identifier** | **str**|  |
 **key_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**[AccessNodeGet]**](AccessNodeGet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nodes_for_entity_target_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_targets_target_identifier_get**
> [AccessNodeGet] get_nodes_for_entity_target_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_targets_target_identifier_get(partition_identifier, entity_identifier, target_identifier)

Get Nodes For Entity Target

Get a list of Nodes which an Entity has on a Target

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.access_node_get import AccessNodeGet
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    entity_identifier = "entity_identifier_example" # str | 
    target_identifier = "target_identifier_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Nodes For Entity Target
        api_response = api_instance.get_nodes_for_entity_target_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_targets_target_identifier_get(partition_identifier, entity_identifier, target_identifier)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->get_nodes_for_entity_target_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_targets_target_identifier_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Nodes For Entity Target
        api_response = api_instance.get_nodes_for_entity_target_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_targets_target_identifier_get(partition_identifier, entity_identifier, target_identifier, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->get_nodes_for_entity_target_access_partitions_partition_identifier_permissions_nodes_entities_entity_identifier_targets_target_identifier_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **entity_identifier** | **str**|  |
 **target_identifier** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**[AccessNodeGet]**](AccessNodeGet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Target does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rgt_access_partitions_partition_identifier_rgts_rgt_uuid_get**
> bool, date, datetime, dict, float, int, list, str, none_type get_rgt_access_partitions_partition_identifier_rgts_rgt_uuid_get(partition_identifier, rgt_uuid)

Get Rgt

Retrieve the Role, Group, and/or Target which belong to an RGT

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    rgt_uuid = "rgt_uuid_example" # str | 
    include_role = False # bool |  (optional) if omitted the server will use the default value of False
    include_group = False # bool |  (optional) if omitted the server will use the default value of False
    include_target = False # bool |  (optional) if omitted the server will use the default value of False
    include_keys = False # bool |  (optional) if omitted the server will use the default value of False
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Rgt
        api_response = api_instance.get_rgt_access_partitions_partition_identifier_rgts_rgt_uuid_get(partition_identifier, rgt_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->get_rgt_access_partitions_partition_identifier_rgts_rgt_uuid_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Rgt
        api_response = api_instance.get_rgt_access_partitions_partition_identifier_rgts_rgt_uuid_get(partition_identifier, rgt_uuid, include_role=include_role, include_group=include_group, include_target=include_target, include_keys=include_keys, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->get_rgt_access_partitions_partition_identifier_rgts_rgt_uuid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **rgt_uuid** | **str**|  |
 **include_role** | **bool**|  | [optional] if omitted the server will use the default value of False
 **include_group** | **bool**|  | [optional] if omitted the server will use the default value of False
 **include_target** | **bool**|  | [optional] if omitted the server will use the default value of False
 **include_keys** | **bool**|  | [optional] if omitted the server will use the default value of False
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | RGT does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_access_partitions_partition_identifier_roles_role_uuid_get**
> AccessRoleGet get_role_access_partitions_partition_identifier_roles_role_uuid_get(partition_identifier, role_uuid)

Get Role

Get a Role

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.access_role_get import AccessRoleGet
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    role_uuid = "role_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Role
        api_response = api_instance.get_role_access_partitions_partition_identifier_roles_role_uuid_get(partition_identifier, role_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->get_role_access_partitions_partition_identifier_roles_role_uuid_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Role
        api_response = api_instance.get_role_access_partitions_partition_identifier_roles_role_uuid_get(partition_identifier, role_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->get_role_access_partitions_partition_identifier_roles_role_uuid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **role_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**AccessRoleGet**](AccessRoleGet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Role or Node does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_type_access_partitions_partition_identifier_permissions_types_type_uuid_get**
> AccessTypeGet get_type_access_partitions_partition_identifier_permissions_types_type_uuid_get(partition_identifier, type_uuid)

Get Type

Get a Type

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.access_type_get import AccessTypeGet
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    type_uuid = "type_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Type
        api_response = api_instance.get_type_access_partitions_partition_identifier_permissions_types_type_uuid_get(partition_identifier, type_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->get_type_access_partitions_partition_identifier_permissions_types_type_uuid_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Type
        api_response = api_instance.get_type_access_partitions_partition_identifier_permissions_types_type_uuid_get(partition_identifier, type_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->get_type_access_partitions_partition_identifier_permissions_types_type_uuid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **type_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**AccessTypeGet**](AccessTypeGet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Type does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_allowed_for_entity_on_target_with_node_access_partitions_partition_identifier_auth_targets_target_identifier_nodes_node_entities_entity_identifier_get**
> bool, date, datetime, dict, float, int, list, str, none_type is_allowed_for_entity_on_target_with_node_access_partitions_partition_identifier_auth_targets_target_identifier_nodes_node_entities_entity_identifier_get(partition_identifier, entity_identifier, target_identifier, node)

Is Allowed For Entity On Target With Node

Returns whether an entity has a node on a target  If yes, returns True  If no, returns HTTP 403

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    entity_identifier = "entity_identifier_example" # str | 
    target_identifier = "target_identifier_example" # str | 
    node = "node_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Is Allowed For Entity On Target With Node
        api_response = api_instance.is_allowed_for_entity_on_target_with_node_access_partitions_partition_identifier_auth_targets_target_identifier_nodes_node_entities_entity_identifier_get(partition_identifier, entity_identifier, target_identifier, node)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->is_allowed_for_entity_on_target_with_node_access_partitions_partition_identifier_auth_targets_target_identifier_nodes_node_entities_entity_identifier_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **entity_identifier** | **str**|  |
 **target_identifier** | **str**|  |
 **node** | **str**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **make_rgt_access_partitions_partition_identifier_rgts_roles_role_uuid_groups_group_uuid_targets_target_identifier_post**
> bool, date, datetime, dict, float, int, list, str, none_type make_rgt_access_partitions_partition_identifier_rgts_roles_role_uuid_groups_group_uuid_targets_target_identifier_post(partition_identifier, role_uuid, group_uuid, target_identifier, body_make_rgt_access_partitions_partition_identifier_rgts_roles_role_uuid_groups_group_uuid_targets_target_identifier_post)

Make Rgt

Make a new RGT  An RGT is the combination of a Role, Group, and Target. In English terms, this means that \"Entities within the Group have access defined by the Nodes within the Role to the Target\"

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.body_make_rgt_access_partitions_partition_identifier_rgts_roles_role_uuid_groups_group_uuid_targets_target_identifier_post import BodyMakeRgtAccessPartitionsPartitionIdentifierRgtsRolesRoleUuidGroupsGroupUuidTargetsTargetIdentifierPost
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    role_uuid = "role_uuid_example" # str | 
    group_uuid = "group_uuid_example" # str | 
    target_identifier = "target_identifier_example" # str | 
    body_make_rgt_access_partitions_partition_identifier_rgts_roles_role_uuid_groups_group_uuid_targets_target_identifier_post = BodyMakeRgtAccessPartitionsPartitionIdentifierRgtsRolesRoleUuidGroupsGroupUuidTargetsTargetIdentifierPost(
        limits=[
            AccessLimitCreate(
                name="name_example",
                value=None,
            ),
        ],
    ) # BodyMakeRgtAccessPartitionsPartitionIdentifierRgtsRolesRoleUuidGroupsGroupUuidTargetsTargetIdentifierPost | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Make Rgt
        api_response = api_instance.make_rgt_access_partitions_partition_identifier_rgts_roles_role_uuid_groups_group_uuid_targets_target_identifier_post(partition_identifier, role_uuid, group_uuid, target_identifier, body_make_rgt_access_partitions_partition_identifier_rgts_roles_role_uuid_groups_group_uuid_targets_target_identifier_post)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->make_rgt_access_partitions_partition_identifier_rgts_roles_role_uuid_groups_group_uuid_targets_target_identifier_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Make Rgt
        api_response = api_instance.make_rgt_access_partitions_partition_identifier_rgts_roles_role_uuid_groups_group_uuid_targets_target_identifier_post(partition_identifier, role_uuid, group_uuid, target_identifier, body_make_rgt_access_partitions_partition_identifier_rgts_roles_role_uuid_groups_group_uuid_targets_target_identifier_post, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->make_rgt_access_partitions_partition_identifier_rgts_roles_role_uuid_groups_group_uuid_targets_target_identifier_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **role_uuid** | **str**|  |
 **group_uuid** | **str**|  |
 **target_identifier** | **str**|  |
 **body_make_rgt_access_partitions_partition_identifier_rgts_roles_role_uuid_groups_group_uuid_targets_target_identifier_post** | [**BodyMakeRgtAccessPartitionsPartitionIdentifierRgtsRolesRoleUuidGroupsGroupUuidTargetsTargetIdentifierPost**](BodyMakeRgtAccessPartitionsPartitionIdentifierRgtsRolesRoleUuidGroupsGroupUuidTargetsTargetIdentifierPost.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Role, Group, or Target does not exist |  -  |
**409** | RGT already exists |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_entity_from_group_access_partitions_partition_identifier_who_groups_group_uuid_entities_entity_identifier_delete**
> bool, date, datetime, dict, float, int, list, str, none_type remove_entity_from_group_access_partitions_partition_identifier_who_groups_group_uuid_entities_entity_identifier_delete(partition_identifier, group_uuid, entity_identifier)

Remove Entity From Group

Remove an Entity from a Group

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    group_uuid = "group_uuid_example" # str | 
    entity_identifier = "entity_identifier_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove Entity From Group
        api_response = api_instance.remove_entity_from_group_access_partitions_partition_identifier_who_groups_group_uuid_entities_entity_identifier_delete(partition_identifier, group_uuid, entity_identifier)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->remove_entity_from_group_access_partitions_partition_identifier_who_groups_group_uuid_entities_entity_identifier_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove Entity From Group
        api_response = api_instance.remove_entity_from_group_access_partitions_partition_identifier_who_groups_group_uuid_entities_entity_identifier_delete(partition_identifier, group_uuid, entity_identifier, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->remove_entity_from_group_access_partitions_partition_identifier_who_groups_group_uuid_entities_entity_identifier_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **group_uuid** | **str**|  |
 **entity_identifier** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Group or Entity does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_node_from_key_access_partitions_partition_identifier_keys_key_uuid_nodes_node_uuid_delete**
> bool, date, datetime, dict, float, int, list, str, none_type remove_node_from_key_access_partitions_partition_identifier_keys_key_uuid_nodes_node_uuid_delete(partition_identifier, key_uuid, node_uuid)

Remove Node From Key

Remove a Node from a Key's Node whitelist

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    key_uuid = "key_uuid_example" # str | 
    node_uuid = "node_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove Node From Key
        api_response = api_instance.remove_node_from_key_access_partitions_partition_identifier_keys_key_uuid_nodes_node_uuid_delete(partition_identifier, key_uuid, node_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->remove_node_from_key_access_partitions_partition_identifier_keys_key_uuid_nodes_node_uuid_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove Node From Key
        api_response = api_instance.remove_node_from_key_access_partitions_partition_identifier_keys_key_uuid_nodes_node_uuid_delete(partition_identifier, key_uuid, node_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->remove_node_from_key_access_partitions_partition_identifier_keys_key_uuid_nodes_node_uuid_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **key_uuid** | **str**|  |
 **node_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Key or Node does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_node_from_role_access_partitions_partition_identifier_roles_role_uuid_nodes_node_uuid_delete**
> bool, date, datetime, dict, float, int, list, str, none_type remove_node_from_role_access_partitions_partition_identifier_roles_role_uuid_nodes_node_uuid_delete(partition_identifier, role_uuid, node_uuid)

Remove Node From Role

Remove a Node from a Role

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    role_uuid = "role_uuid_example" # str | 
    node_uuid = "node_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove Node From Role
        api_response = api_instance.remove_node_from_role_access_partitions_partition_identifier_roles_role_uuid_nodes_node_uuid_delete(partition_identifier, role_uuid, node_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->remove_node_from_role_access_partitions_partition_identifier_roles_role_uuid_nodes_node_uuid_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove Node From Role
        api_response = api_instance.remove_node_from_role_access_partitions_partition_identifier_roles_role_uuid_nodes_node_uuid_delete(partition_identifier, role_uuid, node_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->remove_node_from_role_access_partitions_partition_identifier_roles_role_uuid_nodes_node_uuid_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **role_uuid** | **str**|  |
 **node_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Role or Node does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_groups_access_partitions_partition_identifier_who_groups_get**
> Page search_groups_access_partitions_partition_identifier_who_groups_get(partition_identifier)

Search Groups

Search for Groups

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.page import Page
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    page = 1 # int |  (optional) if omitted the server will use the default value of 1
    page_size = 25 # int |  (optional) if omitted the server will use the default value of 25
    search = "search_example" # str |  (optional)
    search_on = "search_on_example" # str |  (optional)
    sort_on = "sort_on_example" # str |  (optional)
    sort_desc = False # bool |  (optional) if omitted the server will use the default value of False
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search Groups
        api_response = api_instance.search_groups_access_partitions_partition_identifier_who_groups_get(partition_identifier)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->search_groups_access_partitions_partition_identifier_who_groups_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Groups
        api_response = api_instance.search_groups_access_partitions_partition_identifier_who_groups_get(partition_identifier, page=page, page_size=page_size, search=search, search_on=search_on, sort_on=sort_on, sort_desc=sort_desc, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->search_groups_access_partitions_partition_identifier_who_groups_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **page** | **int**|  | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 25
 **search** | **str**|  | [optional]
 **search_on** | **str**|  | [optional]
 **sort_on** | **str**|  | [optional]
 **sort_desc** | **bool**|  | [optional] if omitted the server will use the default value of False
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**Page**](Page.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_nodes_access_partitions_partition_identifier_permissions_types_type_uuid_nodes_get**
> Page search_nodes_access_partitions_partition_identifier_permissions_types_type_uuid_nodes_get(partition_identifier, type_uuid)

Search Nodes

Search for Nodes

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.page import Page
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    type_uuid = "type_uuid_example" # str | 
    node = "node_example" # str |  (optional)
    page = 1 # int |  (optional) if omitted the server will use the default value of 1
    page_size = 25 # int |  (optional) if omitted the server will use the default value of 25
    search = "search_example" # str |  (optional)
    search_on = "search_on_example" # str |  (optional)
    sort_on = "sort_on_example" # str |  (optional)
    sort_desc = False # bool |  (optional) if omitted the server will use the default value of False
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search Nodes
        api_response = api_instance.search_nodes_access_partitions_partition_identifier_permissions_types_type_uuid_nodes_get(partition_identifier, type_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->search_nodes_access_partitions_partition_identifier_permissions_types_type_uuid_nodes_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Nodes
        api_response = api_instance.search_nodes_access_partitions_partition_identifier_permissions_types_type_uuid_nodes_get(partition_identifier, type_uuid, node=node, page=page, page_size=page_size, search=search, search_on=search_on, sort_on=sort_on, sort_desc=sort_desc, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->search_nodes_access_partitions_partition_identifier_permissions_types_type_uuid_nodes_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **type_uuid** | **str**|  |
 **node** | **str**|  | [optional]
 **page** | **int**|  | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 25
 **search** | **str**|  | [optional]
 **search_on** | **str**|  | [optional]
 **sort_on** | **str**|  | [optional]
 **sort_desc** | **bool**|  | [optional] if omitted the server will use the default value of False
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**Page**](Page.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Type does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_roles_access_partitions_partition_identifier_roles_get**
> Page search_roles_access_partitions_partition_identifier_roles_get(partition_identifier)

Search Roles

Search for Roles

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.page import Page
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    page = 1 # int |  (optional) if omitted the server will use the default value of 1
    page_size = 25 # int |  (optional) if omitted the server will use the default value of 25
    search = "search_example" # str |  (optional)
    search_on = "search_on_example" # str |  (optional)
    sort_on = "sort_on_example" # str |  (optional)
    sort_desc = False # bool |  (optional) if omitted the server will use the default value of False
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search Roles
        api_response = api_instance.search_roles_access_partitions_partition_identifier_roles_get(partition_identifier)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->search_roles_access_partitions_partition_identifier_roles_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Roles
        api_response = api_instance.search_roles_access_partitions_partition_identifier_roles_get(partition_identifier, page=page, page_size=page_size, search=search, search_on=search_on, sort_on=sort_on, sort_desc=sort_desc, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->search_roles_access_partitions_partition_identifier_roles_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **page** | **int**|  | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 25
 **search** | **str**|  | [optional]
 **search_on** | **str**|  | [optional]
 **sort_on** | **str**|  | [optional]
 **sort_desc** | **bool**|  | [optional] if omitted the server will use the default value of False
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**Page**](Page.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_types_access_partitions_partition_identifier_permissions_types_get**
> Page search_types_access_partitions_partition_identifier_permissions_types_get(partition_identifier)

Search Types

Search for Types

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.page import Page
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    name = "name_example" # str |  (optional)
    page = 1 # int |  (optional) if omitted the server will use the default value of 1
    page_size = 25 # int |  (optional) if omitted the server will use the default value of 25
    search = "search_example" # str |  (optional)
    search_on = "search_on_example" # str |  (optional)
    sort_on = "sort_on_example" # str |  (optional)
    sort_desc = False # bool |  (optional) if omitted the server will use the default value of False
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search Types
        api_response = api_instance.search_types_access_partitions_partition_identifier_permissions_types_get(partition_identifier)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->search_types_access_partitions_partition_identifier_permissions_types_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Types
        api_response = api_instance.search_types_access_partitions_partition_identifier_permissions_types_get(partition_identifier, name=name, page=page, page_size=page_size, search=search, search_on=search_on, sort_on=sort_on, sort_desc=sort_desc, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->search_types_access_partitions_partition_identifier_permissions_types_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **name** | **str**|  | [optional]
 **page** | **int**|  | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 25
 **search** | **str**|  | [optional]
 **search_on** | **str**|  | [optional]
 **sort_on** | **str**|  | [optional]
 **sort_desc** | **bool**|  | [optional] if omitted the server will use the default value of False
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**Page**](Page.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_access_partitions_partition_identifier_who_groups_group_uuid_put**
> AccessGroupDB update_group_access_partitions_partition_identifier_who_groups_group_uuid_put(partition_identifier, group_uuid, body_update_group_access_partitions_partition_identifier_who_groups_group_uuid_put)

Update Group

Update a Group

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.body_update_group_access_partitions_partition_identifier_who_groups_group_uuid_put import BodyUpdateGroupAccessPartitionsPartitionIdentifierWhoGroupsGroupUuidPut
from ehelply-python-sdk.model.access_group_db import AccessGroupDB
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    group_uuid = "group_uuid_example" # str | 
    body_update_group_access_partitions_partition_identifier_who_groups_group_uuid_put = BodyUpdateGroupAccessPartitionsPartitionIdentifierWhoGroupsGroupUuidPut(
        group=AccessGroupUpdate(
            name="name_example",
            summary="summary_example",
            default=True,
        ),
    ) # BodyUpdateGroupAccessPartitionsPartitionIdentifierWhoGroupsGroupUuidPut | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Group
        api_response = api_instance.update_group_access_partitions_partition_identifier_who_groups_group_uuid_put(partition_identifier, group_uuid, body_update_group_access_partitions_partition_identifier_who_groups_group_uuid_put)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->update_group_access_partitions_partition_identifier_who_groups_group_uuid_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Group
        api_response = api_instance.update_group_access_partitions_partition_identifier_who_groups_group_uuid_put(partition_identifier, group_uuid, body_update_group_access_partitions_partition_identifier_who_groups_group_uuid_put, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->update_group_access_partitions_partition_identifier_who_groups_group_uuid_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **group_uuid** | **str**|  |
 **body_update_group_access_partitions_partition_identifier_who_groups_group_uuid_put** | [**BodyUpdateGroupAccessPartitionsPartitionIdentifierWhoGroupsGroupUuidPut**](BodyUpdateGroupAccessPartitionsPartitionIdentifierWhoGroupsGroupUuidPut.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**AccessGroupDB**](AccessGroupDB.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Group does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_limits_for_entity_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_entities_entity_identifier_post**
> bool, date, datetime, dict, float, int, list, str, none_type update_limits_for_entity_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_entities_entity_identifier_post(partition_identifier, entity_identifier, target_identifier, body_update_limits_for_entity_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_entities_entity_identifier_post)

Update Limits For Entity On Target

Updates the limits for an entity on a target

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.body_update_limits_for_entity_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_entities_entity_identifier_post import BodyUpdateLimitsForEntityOnTargetAccessPartitionsPartitionIdentifierLimitsTargetsTargetIdentifierEntitiesEntityIdentifierPost
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    entity_identifier = "entity_identifier_example" # str | 
    target_identifier = "target_identifier_example" # str | 
    body_update_limits_for_entity_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_entities_entity_identifier_post = BodyUpdateLimitsForEntityOnTargetAccessPartitionsPartitionIdentifierLimitsTargetsTargetIdentifierEntitiesEntityIdentifierPost(
        limits=[
            AccessLimitCreate(
                name="name_example",
                value=None,
            ),
        ],
    ) # BodyUpdateLimitsForEntityOnTargetAccessPartitionsPartitionIdentifierLimitsTargetsTargetIdentifierEntitiesEntityIdentifierPost | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Limits For Entity On Target
        api_response = api_instance.update_limits_for_entity_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_entities_entity_identifier_post(partition_identifier, entity_identifier, target_identifier, body_update_limits_for_entity_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_entities_entity_identifier_post)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->update_limits_for_entity_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_entities_entity_identifier_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Limits For Entity On Target
        api_response = api_instance.update_limits_for_entity_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_entities_entity_identifier_post(partition_identifier, entity_identifier, target_identifier, body_update_limits_for_entity_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_entities_entity_identifier_post, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->update_limits_for_entity_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_entities_entity_identifier_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **entity_identifier** | **str**|  |
 **target_identifier** | **str**|  |
 **body_update_limits_for_entity_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_entities_entity_identifier_post** | [**BodyUpdateLimitsForEntityOnTargetAccessPartitionsPartitionIdentifierLimitsTargetsTargetIdentifierEntitiesEntityIdentifierPost**](BodyUpdateLimitsForEntityOnTargetAccessPartitionsPartitionIdentifierLimitsTargetsTargetIdentifierEntitiesEntityIdentifierPost.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | RGT does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_limits_for_key_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_keys_post**
> bool, date, datetime, dict, float, int, list, str, none_type update_limits_for_key_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_keys_post(partition_identifier, target_identifier, body_update_limits_for_key_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_keys_post)

Update Limits For Key On Target

Updates the limits for a key on a target

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.body_update_limits_for_key_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_keys_post import BodyUpdateLimitsForKeyOnTargetAccessPartitionsPartitionIdentifierLimitsTargetsTargetIdentifierKeysPost
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    target_identifier = "target_identifier_example" # str | 
    body_update_limits_for_key_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_keys_post = BodyUpdateLimitsForKeyOnTargetAccessPartitionsPartitionIdentifierLimitsTargetsTargetIdentifierKeysPost(
        limits=[
            AccessLimitCreate(
                name="name_example",
                value=None,
            ),
        ],
    ) # BodyUpdateLimitsForKeyOnTargetAccessPartitionsPartitionIdentifierLimitsTargetsTargetIdentifierKeysPost | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Limits For Key On Target
        api_response = api_instance.update_limits_for_key_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_keys_post(partition_identifier, target_identifier, body_update_limits_for_key_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_keys_post)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->update_limits_for_key_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_keys_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Limits For Key On Target
        api_response = api_instance.update_limits_for_key_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_keys_post(partition_identifier, target_identifier, body_update_limits_for_key_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_keys_post, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->update_limits_for_key_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_keys_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **target_identifier** | **str**|  |
 **body_update_limits_for_key_on_target_access_partitions_partition_identifier_limits_targets_target_identifier_keys_post** | [**BodyUpdateLimitsForKeyOnTargetAccessPartitionsPartitionIdentifierLimitsTargetsTargetIdentifierKeysPost**](BodyUpdateLimitsForKeyOnTargetAccessPartitionsPartitionIdentifierLimitsTargetsTargetIdentifierKeysPost.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | RGT does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_put**
> AccessNodeDB update_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_put(partition_identifier, node_uuid, body_update_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_put)

Update Node

Update an existing Node

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.body_update_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_put import BodyUpdateNodeAccessPartitionsPartitionIdentifierPermissionsNodesNodeUuidPut
from ehelply-python-sdk.model.access_node_db import AccessNodeDB
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    node_uuid = "node_uuid_example" # str | 
    body_update_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_put = BodyUpdateNodeAccessPartitionsPartitionIdentifierPermissionsNodesNodeUuidPut(
        node=AccessNodeUpdate(
            name="name_example",
            node="node_example",
            summary="summary_example",
        ),
    ) # BodyUpdateNodeAccessPartitionsPartitionIdentifierPermissionsNodesNodeUuidPut | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Node
        api_response = api_instance.update_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_put(partition_identifier, node_uuid, body_update_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_put)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->update_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Node
        api_response = api_instance.update_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_put(partition_identifier, node_uuid, body_update_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_put, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->update_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **node_uuid** | **str**|  |
 **body_update_node_access_partitions_partition_identifier_permissions_nodes_node_uuid_put** | [**BodyUpdateNodeAccessPartitionsPartitionIdentifierPermissionsNodesNodeUuidPut**](BodyUpdateNodeAccessPartitionsPartitionIdentifierPermissionsNodesNodeUuidPut.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**AccessNodeDB**](AccessNodeDB.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Node does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role_access_partitions_partition_identifier_roles_role_uuid_put**
> AccessRoleDB update_role_access_partitions_partition_identifier_roles_role_uuid_put(partition_identifier, role_uuid, body_update_role_access_partitions_partition_identifier_roles_role_uuid_put)

Update Role

Update an existing Role

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.access_role_db import AccessRoleDB
from ehelply-python-sdk.model.body_update_role_access_partitions_partition_identifier_roles_role_uuid_put import BodyUpdateRoleAccessPartitionsPartitionIdentifierRolesRoleUuidPut
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    role_uuid = "role_uuid_example" # str | 
    body_update_role_access_partitions_partition_identifier_roles_role_uuid_put = BodyUpdateRoleAccessPartitionsPartitionIdentifierRolesRoleUuidPut(
        role=AccessRoleUpdate(
            name="name_example",
            summary="summary_example",
        ),
    ) # BodyUpdateRoleAccessPartitionsPartitionIdentifierRolesRoleUuidPut | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Role
        api_response = api_instance.update_role_access_partitions_partition_identifier_roles_role_uuid_put(partition_identifier, role_uuid, body_update_role_access_partitions_partition_identifier_roles_role_uuid_put)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->update_role_access_partitions_partition_identifier_roles_role_uuid_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Role
        api_response = api_instance.update_role_access_partitions_partition_identifier_roles_role_uuid_put(partition_identifier, role_uuid, body_update_role_access_partitions_partition_identifier_roles_role_uuid_put, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->update_role_access_partitions_partition_identifier_roles_role_uuid_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **role_uuid** | **str**|  |
 **body_update_role_access_partitions_partition_identifier_roles_role_uuid_put** | [**BodyUpdateRoleAccessPartitionsPartitionIdentifierRolesRoleUuidPut**](BodyUpdateRoleAccessPartitionsPartitionIdentifierRolesRoleUuidPut.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**AccessRoleDB**](AccessRoleDB.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Role does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_type_access_partitions_partition_identifier_permissions_types_type_uuid_put**
> AccessTypeDB update_type_access_partitions_partition_identifier_permissions_types_type_uuid_put(partition_identifier, type_uuid, body_update_type_access_partitions_partition_identifier_permissions_types_type_uuid_put)

Update Type

Update an existing Type

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import access_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.access_type_db import AccessTypeDB
from ehelply-python-sdk.model.body_update_type_access_partitions_partition_identifier_permissions_types_type_uuid_put import BodyUpdateTypeAccessPartitionsPartitionIdentifierPermissionsTypesTypeUuidPut
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = access_api.AccessApi(api_client)
    partition_identifier = "partition_identifier_example" # str | 
    type_uuid = "type_uuid_example" # str | 
    body_update_type_access_partitions_partition_identifier_permissions_types_type_uuid_put = BodyUpdateTypeAccessPartitionsPartitionIdentifierPermissionsTypesTypeUuidPut(
        partition_type=AccessTypeUpdate(
            name="name_example",
            summary="summary_example",
        ),
    ) # BodyUpdateTypeAccessPartitionsPartitionIdentifierPermissionsTypesTypeUuidPut | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Type
        api_response = api_instance.update_type_access_partitions_partition_identifier_permissions_types_type_uuid_put(partition_identifier, type_uuid, body_update_type_access_partitions_partition_identifier_permissions_types_type_uuid_put)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->update_type_access_partitions_partition_identifier_permissions_types_type_uuid_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Type
        api_response = api_instance.update_type_access_partitions_partition_identifier_permissions_types_type_uuid_put(partition_identifier, type_uuid, body_update_type_access_partitions_partition_identifier_permissions_types_type_uuid_put, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling AccessApi->update_type_access_partitions_partition_identifier_permissions_types_type_uuid_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_identifier** | **str**|  |
 **type_uuid** | **str**|  |
 **body_update_type_access_partitions_partition_identifier_permissions_types_type_uuid_put** | [**BodyUpdateTypeAccessPartitionsPartitionIdentifierPermissionsTypesTypeUuidPut**](BodyUpdateTypeAccessPartitionsPartitionIdentifierPermissionsTypesTypeUuidPut.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**AccessTypeDB**](AccessTypeDB.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Type does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

