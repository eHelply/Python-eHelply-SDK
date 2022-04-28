# ehelply_python_sdk.ProjectsApi

All URIs are relative to *https://api.prod.ehelply.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_member_to_project_projects_projects_project_uuid_members_entity_uuid_post**](ProjectsApi.md#add_member_to_project_projects_projects_project_uuid_members_entity_uuid_post) | **POST** /sam/projects/projects/{project_uuid}/members/{entity_uuid} | Add Member To Project
[**archive_project_projects_projects_project_uuid_delete**](ProjectsApi.md#archive_project_projects_projects_project_uuid_delete) | **DELETE** /sam/projects/projects/{project_uuid} | Archive Project
[**create_project_key_projects_projects_project_uuid_keys_post**](ProjectsApi.md#create_project_key_projects_projects_project_uuid_keys_post) | **POST** /sam/projects/projects/{project_uuid}/keys | Create Project Key
[**create_project_projects_projects_post**](ProjectsApi.md#create_project_projects_projects_post) | **POST** /sam/projects/projects | Create Project
[**create_usage_type_projects_usage_types_post**](ProjectsApi.md#create_usage_type_projects_usage_types_post) | **POST** /sam/projects/usage/types | Create Usage Type
[**delete_usage_type_projects_usage_types_usage_type_key_delete**](ProjectsApi.md#delete_usage_type_projects_usage_types_usage_type_key_delete) | **DELETE** /sam/projects/usage/types/{usage_type_key} | Delete Usage Type
[**get_all_project_usage_projects_projects_project_uuid_usage_get**](ProjectsApi.md#get_all_project_usage_projects_projects_project_uuid_usage_get) | **GET** /sam/projects/projects/{project_uuid}/usage | Get All Project Usage
[**get_member_projects_projects_members_entity_uuid_projects_get**](ProjectsApi.md#get_member_projects_projects_members_entity_uuid_projects_get) | **GET** /sam/projects/members/{entity_uuid}/projects | Get Member Projects
[**get_project_keys_projects_projects_project_uuid_keys_get**](ProjectsApi.md#get_project_keys_projects_projects_project_uuid_keys_get) | **GET** /sam/projects/projects/{project_uuid}/keys | Get Project Keys
[**get_project_members_projects_projects_project_uuid_members_get**](ProjectsApi.md#get_project_members_projects_projects_project_uuid_members_get) | **GET** /sam/projects/projects/{project_uuid}/members | Get Project Members
[**get_project_projects_projects_project_uuid_get**](ProjectsApi.md#get_project_projects_projects_project_uuid_get) | **GET** /sam/projects/projects/{project_uuid} | Get Project
[**get_specific_project_usage_projects_projects_project_uuid_usage_usage_type_key_get**](ProjectsApi.md#get_specific_project_usage_projects_projects_project_uuid_usage_usage_type_key_get) | **GET** /sam/projects/projects/{project_uuid}/usage/{usage_type_key} | Get Specific Project Usage
[**get_usage_type_projects_usage_types_usage_type_key_get**](ProjectsApi.md#get_usage_type_projects_usage_types_usage_type_key_get) | **GET** /sam/projects/usage/types/{usage_type_key} | Get Usage Type
[**remove_member_from_project_projects_projects_project_uuid_members_entity_uuid_delete**](ProjectsApi.md#remove_member_from_project_projects_projects_project_uuid_members_entity_uuid_delete) | **DELETE** /sam/projects/projects/{project_uuid}/members/{entity_uuid} | Remove Member From Project
[**remove_project_key_projects_projects_project_uuid_keys_delete**](ProjectsApi.md#remove_project_key_projects_projects_project_uuid_keys_delete) | **DELETE** /sam/projects/projects/{project_uuid}/keys | Remove Project Key
[**sandbox_projects_sandbox_get**](ProjectsApi.md#sandbox_projects_sandbox_get) | **GET** /sam/projects/sandbox | Sandbox
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
import ehelply_python_sdk
from ehelply_python_sdk.api import projects_api
from ehelply_python_sdk.model.sam_http_validation_error import SamHTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
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
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ProjectsApi->add_member_to_project_projects_projects_project_uuid_members_entity_uuid_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add Member To Project
        api_response = api_instance.add_member_to_project_projects_projects_project_uuid_members_entity_uuid_post(project_uuid, entity_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
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

# **archive_project_projects_projects_project_uuid_delete**
> bool, date, datetime, dict, float, int, list, str, none_type archive_project_projects_projects_project_uuid_delete(project_uuid)

Archive Project

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import projects_api
from ehelply_python_sdk.model.sam_http_validation_error import SamHTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
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
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ProjectsApi->archive_project_projects_projects_project_uuid_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Archive Project
        api_response = api_instance.archive_project_projects_projects_project_uuid_delete(project_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
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

# **create_project_key_projects_projects_project_uuid_keys_post**
> CreateKeyResponse create_project_key_projects_projects_project_uuid_keys_post(project_uuid, security_key_create)

Create Project Key

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import projects_api
from ehelply_python_sdk.model.sam_http_validation_error import SamHTTPValidationError
from ehelply_python_sdk.model.create_key_response import CreateKeyResponse
from ehelply_python_sdk.model.security_key_create import SecurityKeyCreate
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    project_uuid = "project_uuid_example" # str | 
    security_key_create = SecurityKeyCreate(
        name="name_example",
        summary="summary_example",
    ) # SecurityKeyCreate | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Project Key
        api_response = api_instance.create_project_key_projects_projects_project_uuid_keys_post(project_uuid, security_key_create)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ProjectsApi->create_project_key_projects_projects_project_uuid_keys_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Project Key
        api_response = api_instance.create_project_key_projects_projects_project_uuid_keys_post(project_uuid, security_key_create, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ProjectsApi->create_project_key_projects_projects_project_uuid_keys_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**|  |
 **security_key_create** | [**SecurityKeyCreate**](SecurityKeyCreate.md)|  |
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
> bool, date, datetime, dict, float, int, list, str, none_type create_project_projects_projects_post(projects_project_create)

Create Project

Create a new Project

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import projects_api
from ehelply_python_sdk.model.sam_http_validation_error import SamHTTPValidationError
from ehelply_python_sdk.model.projects_project_create import ProjectsProjectCreate
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    projects_project_create = ProjectsProjectCreate(
        name="name_example",
    ) # ProjectsProjectCreate | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Project
        api_response = api_instance.create_project_projects_projects_post(projects_project_create)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ProjectsApi->create_project_projects_projects_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Project
        api_response = api_instance.create_project_projects_projects_post(projects_project_create, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ProjectsApi->create_project_projects_projects_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_project_create** | [**ProjectsProjectCreate**](ProjectsProjectCreate.md)|  |
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
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_usage_type_projects_usage_types_post**
> ProjectsUsageTypeDB create_usage_type_projects_usage_types_post(projects_usage_type_create)

Create Usage Type

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import projects_api
from ehelply_python_sdk.model.sam_http_validation_error import SamHTTPValidationError
from ehelply_python_sdk.model.projects_usage_type_db import ProjectsUsageTypeDB
from ehelply_python_sdk.model.projects_usage_type_create import ProjectsUsageTypeCreate
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    projects_usage_type_create = ProjectsUsageTypeCreate(
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
    ) # ProjectsUsageTypeCreate | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Usage Type
        api_response = api_instance.create_usage_type_projects_usage_types_post(projects_usage_type_create)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ProjectsApi->create_usage_type_projects_usage_types_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Usage Type
        api_response = api_instance.create_usage_type_projects_usage_types_post(projects_usage_type_create, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ProjectsApi->create_usage_type_projects_usage_types_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_usage_type_create** | [**ProjectsUsageTypeCreate**](ProjectsUsageTypeCreate.md)|  |
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
import ehelply_python_sdk
from ehelply_python_sdk.api import projects_api
from ehelply_python_sdk.model.sam_http_validation_error import SamHTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
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
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ProjectsApi->delete_usage_type_projects_usage_types_usage_type_key_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Usage Type
        api_response = api_instance.delete_usage_type_projects_usage_types_usage_type_key_delete(usage_type_key, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
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
import ehelply_python_sdk
from ehelply_python_sdk.api import projects_api
from ehelply_python_sdk.model.sam_http_validation_error import SamHTTPValidationError
from ehelply_python_sdk.model.projects_project_usage_db import ProjectsProjectUsageDB
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
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
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ProjectsApi->get_all_project_usage_projects_projects_project_uuid_usage_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get All Project Usage
        api_response = api_instance.get_all_project_usage_projects_projects_project_uuid_usage_get(project_uuid, year=year, month=month, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
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
import ehelply_python_sdk
from ehelply_python_sdk.api import projects_api
from ehelply_python_sdk.model.sam_http_validation_error import SamHTTPValidationError
from ehelply_python_sdk.model.projects_project_get import ProjectsProjectGet
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
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
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ProjectsApi->get_member_projects_projects_members_entity_uuid_projects_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Member Projects
        api_response = api_instance.get_member_projects_projects_members_entity_uuid_projects_get(entity_uuid, role=role, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
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

# **get_project_keys_projects_projects_project_uuid_keys_get**
> [ProjectsProjectMemberDB] get_project_keys_projects_projects_project_uuid_keys_get(project_uuid)

Get Project Keys

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import projects_api
from ehelply_python_sdk.model.sam_http_validation_error import SamHTTPValidationError
from ehelply_python_sdk.model.projects_project_member_db import ProjectsProjectMemberDB
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
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
        # Get Project Keys
        api_response = api_instance.get_project_keys_projects_projects_project_uuid_keys_get(project_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ProjectsApi->get_project_keys_projects_projects_project_uuid_keys_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Project Keys
        api_response = api_instance.get_project_keys_projects_projects_project_uuid_keys_get(project_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ProjectsApi->get_project_keys_projects_projects_project_uuid_keys_get: %s\n" % e)
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
**404** | Project or Entity does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_members_projects_projects_project_uuid_members_get**
> [ProjectsProjectMemberDB] get_project_members_projects_projects_project_uuid_members_get(project_uuid)

Get Project Members

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import projects_api
from ehelply_python_sdk.model.sam_http_validation_error import SamHTTPValidationError
from ehelply_python_sdk.model.projects_project_member_db import ProjectsProjectMemberDB
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
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
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ProjectsApi->get_project_members_projects_projects_project_uuid_members_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Project Members
        api_response = api_instance.get_project_members_projects_projects_project_uuid_members_get(project_uuid, role=role, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
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
> bool, date, datetime, dict, float, int, list, str, none_type get_project_projects_projects_project_uuid_get(project_uuid)

Get Project

Get a Project

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import projects_api
from ehelply_python_sdk.model.sam_http_validation_error import SamHTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
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
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ProjectsApi->get_project_projects_projects_project_uuid_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Project
        api_response = api_instance.get_project_projects_projects_project_uuid_get(project_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
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

# **get_specific_project_usage_projects_projects_project_uuid_usage_usage_type_key_get**
> ProjectsProjectUsageDB get_specific_project_usage_projects_projects_project_uuid_usage_usage_type_key_get(usage_type_key, project_uuid)

Get Specific Project Usage

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import projects_api
from ehelply_python_sdk.model.sam_http_validation_error import SamHTTPValidationError
from ehelply_python_sdk.model.projects_project_usage_db import ProjectsProjectUsageDB
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
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
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ProjectsApi->get_specific_project_usage_projects_projects_project_uuid_usage_usage_type_key_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Specific Project Usage
        api_response = api_instance.get_specific_project_usage_projects_projects_project_uuid_usage_usage_type_key_get(usage_type_key, project_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
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
import ehelply_python_sdk
from ehelply_python_sdk.api import projects_api
from ehelply_python_sdk.model.projects_usage_type_get import ProjectsUsageTypeGet
from ehelply_python_sdk.model.sam_http_validation_error import SamHTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    usage_type_key = "usage_type_key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Usage Type
        api_response = api_instance.get_usage_type_projects_usage_types_usage_type_key_get(usage_type_key)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
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
import ehelply_python_sdk
from ehelply_python_sdk.api import projects_api
from ehelply_python_sdk.model.sam_http_validation_error import SamHTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
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
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ProjectsApi->remove_member_from_project_projects_projects_project_uuid_members_entity_uuid_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove Member From Project
        api_response = api_instance.remove_member_from_project_projects_projects_project_uuid_members_entity_uuid_delete(project_uuid, entity_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
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

# **remove_project_key_projects_projects_project_uuid_keys_delete**
> bool, date, datetime, dict, float, int, list, str, none_type remove_project_key_projects_projects_project_uuid_keys_delete(project_uuid)

Remove Project Key

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import projects_api
from ehelply_python_sdk.model.sam_http_validation_error import SamHTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    project_uuid = "project_uuid_example" # str | 
    access_token = "access_token_example" # str |  (optional)
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove Project Key
        api_response = api_instance.remove_project_key_projects_projects_project_uuid_keys_delete(project_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ProjectsApi->remove_project_key_projects_projects_project_uuid_keys_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove Project Key
        api_response = api_instance.remove_project_key_projects_projects_project_uuid_keys_delete(project_uuid, access_token=access_token, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ProjectsApi->remove_project_key_projects_projects_project_uuid_keys_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**|  |
 **access_token** | **str**|  | [optional]
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

# **sandbox_projects_sandbox_get**
> bool, date, datetime, dict, float, int, list, str, none_type sandbox_projects_sandbox_get()

Sandbox

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import projects_api
from ehelply_python_sdk.model.sam_http_validation_error import SamHTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Sandbox
        api_response = api_instance.sandbox_projects_sandbox_get(x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ProjectsApi->sandbox_projects_sandbox_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_projects_projects_projects_get**
> Page search_projects_projects_projects_get()

Search Projects

Search projects

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import projects_api
from ehelply_python_sdk.model.sam_http_validation_error import SamHTTPValidationError
from ehelply_python_sdk.model.page import Page
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
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
    except ehelply_python_sdk.ApiException as e:
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
import ehelply_python_sdk
from ehelply_python_sdk.api import projects_api
from ehelply_python_sdk.model.sam_http_validation_error import SamHTTPValidationError
from ehelply_python_sdk.model.page import Page
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
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
    except ehelply_python_sdk.ApiException as e:
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
> bool, date, datetime, dict, float, int, list, str, none_type update_project_projects_projects_project_uuid_put(project_uuid, projects_project_update)

Update Project

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import projects_api
from ehelply_python_sdk.model.sam_http_validation_error import SamHTTPValidationError
from ehelply_python_sdk.model.projects_project_update import ProjectsProjectUpdate
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    project_uuid = "project_uuid_example" # str | 
    projects_project_update = ProjectsProjectUpdate(
        max_spend=1,
        status="status_example",
    ) # ProjectsProjectUpdate | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Project
        api_response = api_instance.update_project_projects_projects_project_uuid_put(project_uuid, projects_project_update)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ProjectsApi->update_project_projects_projects_project_uuid_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Project
        api_response = api_instance.update_project_projects_projects_project_uuid_put(project_uuid, projects_project_update, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ProjectsApi->update_project_projects_projects_project_uuid_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**|  |
 **projects_project_update** | [**ProjectsProjectUpdate**](ProjectsProjectUpdate.md)|  |
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
**404** | Project does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_usage_type_projects_usage_types_usage_type_key_put**
> ProjectsUsageTypeDB update_usage_type_projects_usage_types_usage_type_key_put(usage_type_key, projects_usage_type_update)

Update Usage Type

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import projects_api
from ehelply_python_sdk.model.sam_http_validation_error import SamHTTPValidationError
from ehelply_python_sdk.model.projects_usage_type_db import ProjectsUsageTypeDB
from ehelply_python_sdk.model.projects_usage_type_update import ProjectsUsageTypeUpdate
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = projects_api.ProjectsApi(api_client)
    usage_type_key = "usage_type_key_example" # str | 
    projects_usage_type_update = ProjectsUsageTypeUpdate(
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
    ) # ProjectsUsageTypeUpdate | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Usage Type
        api_response = api_instance.update_usage_type_projects_usage_types_usage_type_key_put(usage_type_key, projects_usage_type_update)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ProjectsApi->update_usage_type_projects_usage_types_usage_type_key_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Usage Type
        api_response = api_instance.update_usage_type_projects_usage_types_usage_type_key_put(usage_type_key, projects_usage_type_update, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ProjectsApi->update_usage_type_projects_usage_types_usage_type_key_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **usage_type_key** | **str**|  |
 **projects_usage_type_update** | [**ProjectsUsageTypeUpdate**](ProjectsUsageTypeUpdate.md)|  |
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

