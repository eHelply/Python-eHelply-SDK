# ehelply-python-sdk.ProjectsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_member_to_project_projects_projects_project_uuid_members_entity_uuid_post**](ProjectsApi.md#add_member_to_project_projects_projects_project_uuid_members_entity_uuid_post) | **POST** /sam/projects/projects/{project_uuid}/members/{entity_uuid} | Add Member To Project
[**add_permission_to_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_permissions_node_uuid_post**](ProjectsApi.md#add_permission_to_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_permissions_node_uuid_post) | **POST** /sam/projects/projects/{project_uuid}/members/{entity_uuid}/keys/{key_uuid}/permissions/{node_uuid} | Add Permission To Key
[**archive_project_projects_projects_project_uuid_delete**](ProjectsApi.md#archive_project_projects_projects_project_uuid_delete) | **DELETE** /sam/projects/projects/{project_uuid} | Archive Project
[**cloud_participant_projects_cloud_participant_post**](ProjectsApi.md#cloud_participant_projects_cloud_participant_post) | **POST** /sam/projects/cloud_participant | Cloud Participant
[**create_project_key_projects_projects_project_uuid_members_entity_uuid_keys_post**](ProjectsApi.md#create_project_key_projects_projects_project_uuid_members_entity_uuid_keys_post) | **POST** /sam/projects/projects/{project_uuid}/members/{entity_uuid}/keys | Create Project Key
[**create_project_projects_projects_post**](ProjectsApi.md#create_project_projects_projects_post) | **POST** /sam/projects/projects | Create Project
[**create_usage_type_projects_usage_types_post**](ProjectsApi.md#create_usage_type_projects_usage_types_post) | **POST** /sam/projects/usage/types | Create Usage Type
[**delete_usage_type_projects_usage_types_usage_type_key_delete**](ProjectsApi.md#delete_usage_type_projects_usage_types_usage_type_key_delete) | **DELETE** /sam/projects/usage/types/{usage_type_key} | Delete Usage Type
[**get_all_project_usage_projects_projects_project_uuid_usage_get**](ProjectsApi.md#get_all_project_usage_projects_projects_project_uuid_usage_get) | **GET** /sam/projects/projects/{project_uuid}/usage | Get All Project Usage
[**get_member_projects_projects_members_entity_uuid_projects_get**](ProjectsApi.md#get_member_projects_projects_members_entity_uuid_projects_get) | **GET** /sam/projects/members/{entity_uuid}/projects | Get Member Projects
[**get_permissions_for_entity_projects_projects_project_uuid_members_entity_uuid_permissions_get**](ProjectsApi.md#get_permissions_for_entity_projects_projects_project_uuid_members_entity_uuid_permissions_get) | **GET** /sam/projects/projects/{project_uuid}/members/{entity_uuid}/permissions | Get Permissions For Entity
[**get_permissions_for_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_permissions_get**](ProjectsApi.md#get_permissions_for_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_permissions_get) | **GET** /sam/projects/projects/{project_uuid}/members/{entity_uuid}/keys/{key_uuid}/permissions | Get Permissions For Key
[**get_permissions_type_projects_projects_project_uuid_members_entity_uuid_permissions_types_type_uuid_get**](ProjectsApi.md#get_permissions_type_projects_projects_project_uuid_members_entity_uuid_permissions_types_type_uuid_get) | **GET** /sam/projects/projects/{project_uuid}/members/{entity_uuid}/permissions/types/{type_uuid} | Get Permissions Type
[**get_project_keys_projects_projects_project_uuid_members_entity_uuid_keys_get**](ProjectsApi.md#get_project_keys_projects_projects_project_uuid_members_entity_uuid_keys_get) | **GET** /sam/projects/projects/{project_uuid}/members/{entity_uuid}/keys | Get Project Keys
[**get_project_members_projects_projects_project_uuid_members_get**](ProjectsApi.md#get_project_members_projects_projects_project_uuid_members_get) | **GET** /sam/projects/projects/{project_uuid}/members | Get Project Members
[**get_project_projects_projects_project_uuid_get**](ProjectsApi.md#get_project_projects_projects_project_uuid_get) | **GET** /sam/projects/projects/{project_uuid} | Get Project
[**get_specific_project_usage_projects_projects_project_uuid_usage_usage_type_key_get**](ProjectsApi.md#get_specific_project_usage_projects_projects_project_uuid_usage_usage_type_key_get) | **GET** /sam/projects/projects/{project_uuid}/usage/{usage_type_key} | Get Specific Project Usage
[**get_usage_type_projects_usage_types_usage_type_key_get**](ProjectsApi.md#get_usage_type_projects_usage_types_usage_type_key_get) | **GET** /sam/projects/usage/types/{usage_type_key} | Get Usage Type
[**remove_member_from_project_projects_projects_project_uuid_members_entity_uuid_delete**](ProjectsApi.md#remove_member_from_project_projects_projects_project_uuid_members_entity_uuid_delete) | **DELETE** /sam/projects/projects/{project_uuid}/members/{entity_uuid} | Remove Member From Project
[**remove_permission_from_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_permissions_node_uuid_delete**](ProjectsApi.md#remove_permission_from_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_permissions_node_uuid_delete) | **DELETE** /sam/projects/projects/{project_uuid}/members/{entity_uuid}/keys/{key_uuid}/permissions/{node_uuid} | Remove Permission From Key
[**remove_project_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_delete**](ProjectsApi.md#remove_project_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_delete) | **DELETE** /sam/projects/projects/{project_uuid}/members/{entity_uuid}/keys/{key_uuid} | Remove Project Key
[**search_projects_projects_projects_get**](ProjectsApi.md#search_projects_projects_projects_get) | **GET** /sam/projects/projects | Search Projects
[**search_usage_type_projects_usage_types_get**](ProjectsApi.md#search_usage_type_projects_usage_types_get) | **GET** /sam/projects/usage/types | Search Usage Type
[**update_project_projects_projects_project_uuid_put**](ProjectsApi.md#update_project_projects_projects_project_uuid_put) | **PUT** /sam/projects/projects/{project_uuid} | Update Project
[**update_usage_type_projects_usage_types_usage_type_key_put**](ProjectsApi.md#update_usage_type_projects_usage_types_usage_type_key_put) | **PUT** /sam/projects/usage/types/{usage_type_key} | Update Usage Type


# **add_member_to_project_projects_projects_project_uuid_members_entity_uuid_post**
> bool, date, datetime, dict, float, int, list, str, none_type add_member_to_project_projects_projects_project_uuid_members_entity_uuid_post(project_uuid, entity_uuid)

Add Member To Project

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import projects_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    project_uuid = "project_uuid_example" # str | 
    entity_uuid = "entity_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add Member To Project
        api_response = api_instance.add_member_to_project_projects_projects_project_uuid_members_entity_uuid_post(project_uuid, entity_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->add_member_to_project_projects_projects_project_uuid_members_entity_uuid_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add Member To Project
        api_response = api_instance.add_member_to_project_projects_projects_project_uuid_members_entity_uuid_post(project_uuid, entity_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->add_member_to_project_projects_projects_project_uuid_members_entity_uuid_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**|  |
 **entity_uuid** | **str**|  |
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
**404** | Project does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_permission_to_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_permissions_node_uuid_post**
> bool, date, datetime, dict, float, int, list, str, none_type add_permission_to_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_permissions_node_uuid_post(project_uuid, entity_uuid, key_uuid, node_uuid)

Add Permission To Key

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import projects_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    project_uuid = "project_uuid_example" # str | 
    entity_uuid = "entity_uuid_example" # str | 
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
        # Add Permission To Key
        api_response = api_instance.add_permission_to_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_permissions_node_uuid_post(project_uuid, entity_uuid, key_uuid, node_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->add_permission_to_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_permissions_node_uuid_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add Permission To Key
        api_response = api_instance.add_permission_to_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_permissions_node_uuid_post(project_uuid, entity_uuid, key_uuid, node_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->add_permission_to_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_permissions_node_uuid_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**|  |
 **entity_uuid** | **str**|  |
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
**404** | Project, Entity, or Key does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archive_project_projects_projects_project_uuid_delete**
> bool, date, datetime, dict, float, int, list, str, none_type archive_project_projects_projects_project_uuid_delete(project_uuid)

Archive Project

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import projects_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    project_uuid = "project_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Archive Project
        api_response = api_instance.archive_project_projects_projects_project_uuid_delete(project_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->archive_project_projects_projects_project_uuid_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Archive Project
        api_response = api_instance.archive_project_projects_projects_project_uuid_delete(project_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->archive_project_projects_projects_project_uuid_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**|  |
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

# **cloud_participant_projects_cloud_participant_post**
> CloudParticipantResponse cloud_participant_projects_cloud_participant_post(body_cloud_participant_projects_cloud_participant_post)

Cloud Participant

:param auth: :param cloud_participant_auth: :return:

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import projects_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.cloud_participant_response import CloudParticipantResponse
from ehelply-python-sdk.model.body_cloud_participant_projects_cloud_participant_post import BodyCloudParticipantProjectsCloudParticipantPost
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    body_cloud_participant_projects_cloud_participant_post = BodyCloudParticipantProjectsCloudParticipantPost(
        cloud_participant_auth=CloudParticipantRequest(
            auth=CloudParticipantAuthRequest(
                x_access_token="x_access_token_example",
                x_secret_token="x_secret_token_example",
                authorization="authorization_example",
                ehelply_active_participant="ehelply_active_participant_example",
                ehelply_project="ehelply_project_example",
                ehelply_data="ehelply_data_example",
            ),
            node="node_example",
            service_target="service_target_example",
            ignore_project_enabled=False,
            ignore_spend_limits=False,
            exception_if_unauthorized=True,
            exception_if_spend_maxed=True,
            exception_if_project_not_enabled=True,
            skip_project_check=False,
        ),
    ) # BodyCloudParticipantProjectsCloudParticipantPost | 

    # example passing only required values which don't have defaults set
    try:
        # Cloud Participant
        api_response = api_instance.cloud_participant_projects_cloud_participant_post(body_cloud_participant_projects_cloud_participant_post)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->cloud_participant_projects_cloud_participant_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_cloud_participant_projects_cloud_participant_post** | [**BodyCloudParticipantProjectsCloudParticipantPost**](BodyCloudParticipantProjectsCloudParticipantPost.md)|  |

### Return type

[**CloudParticipantResponse**](CloudParticipantResponse.md)

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

# **create_project_key_projects_projects_project_uuid_members_entity_uuid_keys_post**
> CreateKeyResponse create_project_key_projects_projects_project_uuid_members_entity_uuid_keys_post(project_uuid, entity_uuid, body_create_project_key_projects_projects_project_uuid_members_entity_uuid_keys_post)

Create Project Key

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import projects_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.create_key_response import CreateKeyResponse
from ehelply-python-sdk.model.body_create_project_key_projects_projects_project_uuid_members_entity_uuid_keys_post import BodyCreateProjectKeyProjectsProjectsProjectUuidMembersEntityUuidKeysPost
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    project_uuid = "project_uuid_example" # str | 
    entity_uuid = "entity_uuid_example" # str | 
    body_create_project_key_projects_projects_project_uuid_members_entity_uuid_keys_post = BodyCreateProjectKeyProjectsProjectsProjectUuidMembersEntityUuidKeysPost(
        key=SecurityKeyCreate(
            name="name_example",
            summary="summary_example",
        ),
    ) # BodyCreateProjectKeyProjectsProjectsProjectUuidMembersEntityUuidKeysPost | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Project Key
        api_response = api_instance.create_project_key_projects_projects_project_uuid_members_entity_uuid_keys_post(project_uuid, entity_uuid, body_create_project_key_projects_projects_project_uuid_members_entity_uuid_keys_post)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->create_project_key_projects_projects_project_uuid_members_entity_uuid_keys_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Project Key
        api_response = api_instance.create_project_key_projects_projects_project_uuid_members_entity_uuid_keys_post(project_uuid, entity_uuid, body_create_project_key_projects_projects_project_uuid_members_entity_uuid_keys_post, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->create_project_key_projects_projects_project_uuid_members_entity_uuid_keys_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**|  |
 **entity_uuid** | **str**|  |
 **body_create_project_key_projects_projects_project_uuid_members_entity_uuid_keys_post** | [**BodyCreateProjectKeyProjectsProjectsProjectUuidMembersEntityUuidKeysPost**](BodyCreateProjectKeyProjectsProjectsProjectUuidMembersEntityUuidKeysPost.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**CreateKeyResponse**](CreateKeyResponse.md)

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
**404** | Project or Entity does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_projects_projects_post**
> ProjectsProjectDB create_project_projects_projects_post(body_create_project_projects_projects_post)

Create Project

Create a new Project

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import projects_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.body_create_project_projects_projects_post import BodyCreateProjectProjectsProjectsPost
from ehelply-python-sdk.model.projects_project_db import ProjectsProjectDB
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    body_create_project_projects_projects_post = BodyCreateProjectProjectsProjectsPost(
        project=ProjectsProjectCreate(
            name="name_example",
        ),
    ) # BodyCreateProjectProjectsProjectsPost | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Project
        api_response = api_instance.create_project_projects_projects_post(body_create_project_projects_projects_post)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->create_project_projects_projects_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Project
        api_response = api_instance.create_project_projects_projects_post(body_create_project_projects_projects_post, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->create_project_projects_projects_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_create_project_projects_projects_post** | [**BodyCreateProjectProjectsProjectsPost**](BodyCreateProjectProjectsProjectsPost.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**ProjectsProjectDB**](ProjectsProjectDB.md)

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

# **create_usage_type_projects_usage_types_post**
> ProjectsUsageTypeDB create_usage_type_projects_usage_types_post(body_create_usage_type_projects_usage_types_post)

Create Usage Type

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import projects_api
from ehelply-python-sdk.model.body_create_usage_type_projects_usage_types_post import BodyCreateUsageTypeProjectsUsageTypesPost
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.projects_usage_type_db import ProjectsUsageTypeDB
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    body_create_usage_type_projects_usage_types_post = BodyCreateUsageTypeProjectsUsageTypesPost(
        usage_type=ProjectsUsageTypeCreate(
            key="key_example",
            name="name_example",
            summary="summary_example",
            category="category_example",
            service="service_example",
            unit_prices=[
                ProjectsUsageTypeUnitPrice(
                    min_quantity=1,
                    max_quantity=1,
                    unit_price=1,
                ),
            ],
        ),
    ) # BodyCreateUsageTypeProjectsUsageTypesPost | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Usage Type
        api_response = api_instance.create_usage_type_projects_usage_types_post(body_create_usage_type_projects_usage_types_post)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->create_usage_type_projects_usage_types_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Usage Type
        api_response = api_instance.create_usage_type_projects_usage_types_post(body_create_usage_type_projects_usage_types_post, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->create_usage_type_projects_usage_types_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_create_usage_type_projects_usage_types_post** | [**BodyCreateUsageTypeProjectsUsageTypesPost**](BodyCreateUsageTypeProjectsUsageTypesPost.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**ProjectsUsageTypeDB**](ProjectsUsageTypeDB.md)

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

# **delete_usage_type_projects_usage_types_usage_type_key_delete**
> bool, date, datetime, dict, float, int, list, str, none_type delete_usage_type_projects_usage_types_usage_type_key_delete(usage_type_key)

Delete Usage Type

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import projects_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    usage_type_key = "usage_type_key_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete Usage Type
        api_response = api_instance.delete_usage_type_projects_usage_types_usage_type_key_delete(usage_type_key)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->delete_usage_type_projects_usage_types_usage_type_key_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Usage Type
        api_response = api_instance.delete_usage_type_projects_usage_types_usage_type_key_delete(usage_type_key, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->delete_usage_type_projects_usage_types_usage_type_key_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usage_type_key** | **str**|  |
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

# **get_all_project_usage_projects_projects_project_uuid_usage_get**
> [ProjectsProjectUsageDB] get_all_project_usage_projects_projects_project_uuid_usage_get(project_uuid)

Get All Project Usage

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import projects_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.projects_project_usage_db import ProjectsProjectUsageDB
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    project_uuid = "project_uuid_example" # str | 
    year = 1 # int |  (optional)
    month = 1 # int |  (optional)
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get All Project Usage
        api_response = api_instance.get_all_project_usage_projects_projects_project_uuid_usage_get(project_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->get_all_project_usage_projects_projects_project_uuid_usage_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get All Project Usage
        api_response = api_instance.get_all_project_usage_projects_projects_project_uuid_usage_get(project_uuid, year=year, month=month, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->get_all_project_usage_projects_projects_project_uuid_usage_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**|  |
 **year** | **int**|  | [optional]
 **month** | **int**|  | [optional]
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**[ProjectsProjectUsageDB]**](ProjectsProjectUsageDB.md)

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
**404** | Project does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_member_projects_projects_members_entity_uuid_projects_get**
> [ProjectsProjectGet] get_member_projects_projects_members_entity_uuid_projects_get(entity_uuid)

Get Member Projects

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import projects_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.projects_project_get import ProjectsProjectGet
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    entity_uuid = "entity_uuid_example" # str | 
    role = "role_example" # str |  (optional)
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Member Projects
        api_response = api_instance.get_member_projects_projects_members_entity_uuid_projects_get(entity_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->get_member_projects_projects_members_entity_uuid_projects_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Member Projects
        api_response = api_instance.get_member_projects_projects_members_entity_uuid_projects_get(entity_uuid, role=role, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->get_member_projects_projects_members_entity_uuid_projects_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_uuid** | **str**|  |
 **role** | **str**|  | [optional]
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**[ProjectsProjectGet]**](ProjectsProjectGet.md)

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
**404** | Member does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permissions_for_entity_projects_projects_project_uuid_members_entity_uuid_permissions_get**
> [AccessNodeGet] get_permissions_for_entity_projects_projects_project_uuid_members_entity_uuid_permissions_get(project_uuid, entity_uuid)

Get Permissions For Entity

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import projects_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.access_node_get import AccessNodeGet
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    project_uuid = "project_uuid_example" # str | 
    entity_uuid = "entity_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Permissions For Entity
        api_response = api_instance.get_permissions_for_entity_projects_projects_project_uuid_members_entity_uuid_permissions_get(project_uuid, entity_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->get_permissions_for_entity_projects_projects_project_uuid_members_entity_uuid_permissions_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Permissions For Entity
        api_response = api_instance.get_permissions_for_entity_projects_projects_project_uuid_members_entity_uuid_permissions_get(project_uuid, entity_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->get_permissions_for_entity_projects_projects_project_uuid_members_entity_uuid_permissions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**|  |
 **entity_uuid** | **str**|  |
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
**404** | Project or Entity does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permissions_for_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_permissions_get**
> [AccessNodeGet] get_permissions_for_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_permissions_get(project_uuid, entity_uuid, key_uuid)

Get Permissions For Key

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import projects_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.access_node_get import AccessNodeGet
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    project_uuid = "project_uuid_example" # str | 
    entity_uuid = "entity_uuid_example" # str | 
    key_uuid = "key_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Permissions For Key
        api_response = api_instance.get_permissions_for_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_permissions_get(project_uuid, entity_uuid, key_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->get_permissions_for_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_permissions_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Permissions For Key
        api_response = api_instance.get_permissions_for_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_permissions_get(project_uuid, entity_uuid, key_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->get_permissions_for_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_permissions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**|  |
 **entity_uuid** | **str**|  |
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
**404** | Project, Entity, or Key does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permissions_type_projects_projects_project_uuid_members_entity_uuid_permissions_types_type_uuid_get**
> AccessTypeGet get_permissions_type_projects_projects_project_uuid_members_entity_uuid_permissions_types_type_uuid_get(project_uuid, entity_uuid, type_uuid)

Get Permissions Type

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import projects_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.access_type_get import AccessTypeGet
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    project_uuid = "project_uuid_example" # str | 
    entity_uuid = "entity_uuid_example" # str | 
    type_uuid = "type_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Permissions Type
        api_response = api_instance.get_permissions_type_projects_projects_project_uuid_members_entity_uuid_permissions_types_type_uuid_get(project_uuid, entity_uuid, type_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->get_permissions_type_projects_projects_project_uuid_members_entity_uuid_permissions_types_type_uuid_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Permissions Type
        api_response = api_instance.get_permissions_type_projects_projects_project_uuid_members_entity_uuid_permissions_types_type_uuid_get(project_uuid, entity_uuid, type_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->get_permissions_type_projects_projects_project_uuid_members_entity_uuid_permissions_types_type_uuid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**|  |
 **entity_uuid** | **str**|  |
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
**404** | Project, Entity or Type does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_keys_projects_projects_project_uuid_members_entity_uuid_keys_get**
> bool, date, datetime, dict, float, int, list, str, none_type get_project_keys_projects_projects_project_uuid_members_entity_uuid_keys_get(project_uuid, entity_uuid)

Get Project Keys

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import projects_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    project_uuid = "project_uuid_example" # str | 
    entity_uuid = "entity_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Project Keys
        api_response = api_instance.get_project_keys_projects_projects_project_uuid_members_entity_uuid_keys_get(project_uuid, entity_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->get_project_keys_projects_projects_project_uuid_members_entity_uuid_keys_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Project Keys
        api_response = api_instance.get_project_keys_projects_projects_project_uuid_members_entity_uuid_keys_get(project_uuid, entity_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->get_project_keys_projects_projects_project_uuid_members_entity_uuid_keys_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**|  |
 **entity_uuid** | **str**|  |
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
**404** | Project or Entity does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_members_projects_projects_project_uuid_members_get**
> [ProjectsProjectMemberDB] get_project_members_projects_projects_project_uuid_members_get(project_uuid)

Get Project Members

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import projects_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.projects_project_member_db import ProjectsProjectMemberDB
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    project_uuid = "project_uuid_example" # str | 
    role = "role_example" # str |  (optional)
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Project Members
        api_response = api_instance.get_project_members_projects_projects_project_uuid_members_get(project_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->get_project_members_projects_projects_project_uuid_members_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Project Members
        api_response = api_instance.get_project_members_projects_projects_project_uuid_members_get(project_uuid, role=role, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->get_project_members_projects_projects_project_uuid_members_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**|  |
 **role** | **str**|  | [optional]
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**[ProjectsProjectMemberDB]**](ProjectsProjectMemberDB.md)

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
**404** | Project does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_projects_projects_project_uuid_get**
> ProjectsProjectGet get_project_projects_projects_project_uuid_get(project_uuid)

Get Project

Get a Project

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import projects_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.projects_project_get import ProjectsProjectGet
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    project_uuid = "project_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Project
        api_response = api_instance.get_project_projects_projects_project_uuid_get(project_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->get_project_projects_projects_project_uuid_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Project
        api_response = api_instance.get_project_projects_projects_project_uuid_get(project_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->get_project_projects_projects_project_uuid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**ProjectsProjectGet**](ProjectsProjectGet.md)

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
**404** | Project does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_specific_project_usage_projects_projects_project_uuid_usage_usage_type_key_get**
> ProjectsProjectUsageDB get_specific_project_usage_projects_projects_project_uuid_usage_usage_type_key_get(usage_type_key, project_uuid)

Get Specific Project Usage

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import projects_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.projects_project_usage_db import ProjectsProjectUsageDB
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    usage_type_key = "usage_type_key_example" # str | 
    project_uuid = "project_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Specific Project Usage
        api_response = api_instance.get_specific_project_usage_projects_projects_project_uuid_usage_usage_type_key_get(usage_type_key, project_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->get_specific_project_usage_projects_projects_project_uuid_usage_usage_type_key_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Specific Project Usage
        api_response = api_instance.get_specific_project_usage_projects_projects_project_uuid_usage_usage_type_key_get(usage_type_key, project_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->get_specific_project_usage_projects_projects_project_uuid_usage_usage_type_key_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usage_type_key** | **str**|  |
 **project_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**ProjectsProjectUsageDB**](ProjectsProjectUsageDB.md)

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
**404** | Project, Usage does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_type_projects_usage_types_usage_type_key_get**
> ProjectsUsageTypeGet get_usage_type_projects_usage_types_usage_type_key_get(usage_type_key)

Get Usage Type

Get a UsageType  No auth because we may want to use this on pricing/docs pages

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import projects_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.projects_usage_type_get import ProjectsUsageTypeGet
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    usage_type_key = "usage_type_key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Usage Type
        api_response = api_instance.get_usage_type_projects_usage_types_usage_type_key_get(usage_type_key)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->get_usage_type_projects_usage_types_usage_type_key_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usage_type_key** | **str**|  |

### Return type

[**ProjectsUsageTypeGet**](ProjectsUsageTypeGet.md)

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
**404** | UsageType does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_member_from_project_projects_projects_project_uuid_members_entity_uuid_delete**
> bool, date, datetime, dict, float, int, list, str, none_type remove_member_from_project_projects_projects_project_uuid_members_entity_uuid_delete(project_uuid, entity_uuid)

Remove Member From Project

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import projects_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    project_uuid = "project_uuid_example" # str | 
    entity_uuid = "entity_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove Member From Project
        api_response = api_instance.remove_member_from_project_projects_projects_project_uuid_members_entity_uuid_delete(project_uuid, entity_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->remove_member_from_project_projects_projects_project_uuid_members_entity_uuid_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove Member From Project
        api_response = api_instance.remove_member_from_project_projects_projects_project_uuid_members_entity_uuid_delete(project_uuid, entity_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->remove_member_from_project_projects_projects_project_uuid_members_entity_uuid_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**|  |
 **entity_uuid** | **str**|  |
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
**404** | Project does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_permission_from_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_permissions_node_uuid_delete**
> bool, date, datetime, dict, float, int, list, str, none_type remove_permission_from_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_permissions_node_uuid_delete(project_uuid, entity_uuid, key_uuid, node_uuid)

Remove Permission From Key

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import projects_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    project_uuid = "project_uuid_example" # str | 
    entity_uuid = "entity_uuid_example" # str | 
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
        # Remove Permission From Key
        api_response = api_instance.remove_permission_from_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_permissions_node_uuid_delete(project_uuid, entity_uuid, key_uuid, node_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->remove_permission_from_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_permissions_node_uuid_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove Permission From Key
        api_response = api_instance.remove_permission_from_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_permissions_node_uuid_delete(project_uuid, entity_uuid, key_uuid, node_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->remove_permission_from_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_permissions_node_uuid_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**|  |
 **entity_uuid** | **str**|  |
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
**404** | Project, Entity, or Key does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_project_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_delete**
> bool, date, datetime, dict, float, int, list, str, none_type remove_project_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_delete(project_uuid, entity_uuid, key_uuid)

Remove Project Key

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import projects_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    project_uuid = "project_uuid_example" # str | 
    entity_uuid = "entity_uuid_example" # str | 
    key_uuid = "key_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove Project Key
        api_response = api_instance.remove_project_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_delete(project_uuid, entity_uuid, key_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->remove_project_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove Project Key
        api_response = api_instance.remove_project_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_delete(project_uuid, entity_uuid, key_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->remove_project_key_projects_projects_project_uuid_members_entity_uuid_keys_key_uuid_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**|  |
 **entity_uuid** | **str**|  |
 **key_uuid** | **str**|  |
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
**404** | Project, Entity, or Key does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_projects_projects_projects_get**
> Page search_projects_projects_projects_get()

Search Projects

Search projects

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import projects_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.page import Page
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
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
    # and optional values
    try:
        # Search Projects
        api_response = api_instance.search_projects_projects_projects_get(page=page, page_size=page_size, search=search, search_on=search_on, sort_on=sort_on, sort_desc=sort_desc, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->search_projects_projects_projects_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **search_usage_type_projects_usage_types_get**
> Page search_usage_type_projects_usage_types_get()

Search Usage Type

Get a UsageType  No auth because we may want to use this on pricing/docs pages

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import projects_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.page import Page
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    page = 1 # int |  (optional) if omitted the server will use the default value of 1
    page_size = 25 # int |  (optional) if omitted the server will use the default value of 25
    search = "search_example" # str |  (optional)
    search_on = "search_on_example" # str |  (optional)
    sort_on = "sort_on_example" # str |  (optional)
    sort_desc = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Usage Type
        api_response = api_instance.search_usage_type_projects_usage_types_get(page=page, page_size=page_size, search=search, search_on=search_on, sort_on=sort_on, sort_desc=sort_desc)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->search_usage_type_projects_usage_types_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 25
 **search** | **str**|  | [optional]
 **search_on** | **str**|  | [optional]
 **sort_on** | **str**|  | [optional]
 **sort_desc** | **bool**|  | [optional] if omitted the server will use the default value of False

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

# **update_project_projects_projects_project_uuid_put**
> ProjectsProjectDB update_project_projects_projects_project_uuid_put(project_uuid, body_update_project_projects_projects_project_uuid_put)

Update Project

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import projects_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.body_update_project_projects_projects_project_uuid_put import BodyUpdateProjectProjectsProjectsProjectUuidPut
from ehelply-python-sdk.model.projects_project_db import ProjectsProjectDB
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    project_uuid = "project_uuid_example" # str | 
    body_update_project_projects_projects_project_uuid_put = BodyUpdateProjectProjectsProjectsProjectUuidPut(
        project=ProjectsProjectUpdate(
            max_spend=1,
            status="status_example",
        ),
    ) # BodyUpdateProjectProjectsProjectsProjectUuidPut | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Project
        api_response = api_instance.update_project_projects_projects_project_uuid_put(project_uuid, body_update_project_projects_projects_project_uuid_put)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->update_project_projects_projects_project_uuid_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Project
        api_response = api_instance.update_project_projects_projects_project_uuid_put(project_uuid, body_update_project_projects_projects_project_uuid_put, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->update_project_projects_projects_project_uuid_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**|  |
 **body_update_project_projects_projects_project_uuid_put** | [**BodyUpdateProjectProjectsProjectsProjectUuidPut**](BodyUpdateProjectProjectsProjectsProjectUuidPut.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**ProjectsProjectDB**](ProjectsProjectDB.md)

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
**404** | Project does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_usage_type_projects_usage_types_usage_type_key_put**
> ProjectsUsageTypeDB update_usage_type_projects_usage_types_usage_type_key_put(usage_type_key, body_update_usage_type_projects_usage_types_usage_type_key_put)

Update Usage Type

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import projects_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.body_update_usage_type_projects_usage_types_usage_type_key_put import BodyUpdateUsageTypeProjectsUsageTypesUsageTypeKeyPut
from ehelply-python-sdk.model.projects_usage_type_db import ProjectsUsageTypeDB
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    usage_type_key = "usage_type_key_example" # str | 
    body_update_usage_type_projects_usage_types_usage_type_key_put = BodyUpdateUsageTypeProjectsUsageTypesUsageTypeKeyPut(
        usage_type=ProjectsUsageTypeUpdate(
            name="name_example",
            summary="summary_example",
            category="category_example",
            service="service_example",
            unit_prices=[
                ProjectsUsageTypeUnitPrice(
                    min_quantity=1,
                    max_quantity=1,
                    unit_price=1,
                ),
            ],
        ),
    ) # BodyUpdateUsageTypeProjectsUsageTypesUsageTypeKeyPut | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Usage Type
        api_response = api_instance.update_usage_type_projects_usage_types_usage_type_key_put(usage_type_key, body_update_usage_type_projects_usage_types_usage_type_key_put)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->update_usage_type_projects_usage_types_usage_type_key_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Usage Type
        api_response = api_instance.update_usage_type_projects_usage_types_usage_type_key_put(usage_type_key, body_update_usage_type_projects_usage_types_usage_type_key_put, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling ProjectsApi->update_usage_type_projects_usage_types_usage_type_key_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usage_type_key** | **str**|  |
 **body_update_usage_type_projects_usage_types_usage_type_key_put** | [**BodyUpdateUsageTypeProjectsUsageTypesUsageTypeKeyPut**](BodyUpdateUsageTypeProjectsUsageTypesUsageTypeKeyPut.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**ProjectsUsageTypeDB**](ProjectsUsageTypeDB.md)

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
**404** | UsageType does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

