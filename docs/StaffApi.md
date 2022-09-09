# ehelply_python_sdk.StaffApi

All URIs are relative to *https://api.prod.ehelply.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_staff**](StaffApi.md#create_staff) | **POST** /places/staff | Createstaff
[**delete_staff**](StaffApi.md#delete_staff) | **DELETE** /places/staff/{staff_uuid} | Deletestaff
[**get_staff**](StaffApi.md#get_staff) | **GET** /places/staff/{staff_uuid} | Getstaff
[**search_staff**](StaffApi.md#search_staff) | **GET** /places/staff | Searchstaff
[**update_staff**](StaffApi.md#update_staff) | **PUT** /places/staff/{staff_uuid} | Updatestaff


# **create_staff**
> StaffResponse create_staff(staff_base)

Createstaff

Creates a staff member

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import staff_api
from ehelply_python_sdk.model.staff_response import StaffResponse
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.staff_base import StaffBase
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = staff_api.StaffApi(api_client)
    staff_base = StaffBase(
        entity_uuid="entity_uuid_1234",
        project_uuid="project_uuid_1234",
        schedule_uuid="schedule_uuid_1234",
        catalog_uuid="catalog_uuid_1234",
        review_group_uuid="review_uuid_1234",
    ) # StaffBase | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Createstaff
        api_response = api_instance.create_staff(staff_base)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling StaffApi->create_staff: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Createstaff
        api_response = api_instance.create_staff(staff_base, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling StaffApi->create_staff: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **staff_base** | [**StaffBase**](StaffBase.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**StaffResponse**](StaffResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Route not found - Denied by eHelply |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_staff**
> bool, date, datetime, dict, float, int, list, str, none_type delete_staff(staff_uuid)

Deletestaff

Deletes the staff member with the given ID and returns True if successful

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import staff_api
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = staff_api.StaffApi(api_client)
    staff_uuid = "staff_uuid_example" # str | 
    soft_delete = True # bool |  (optional) if omitted the server will use the default value of True
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deletestaff
        api_response = api_instance.delete_staff(staff_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling StaffApi->delete_staff: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deletestaff
        api_response = api_instance.delete_staff(staff_uuid, soft_delete=soft_delete, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling StaffApi->delete_staff: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **staff_uuid** | **str**|  |
 **soft_delete** | **bool**|  | [optional] if omitted the server will use the default value of True
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
**404** | Route not found - Denied by eHelply |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_staff**
> StaffResponse get_staff(staff_uuid)

Getstaff

Gets the staff member information given the staff ID

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import staff_api
from ehelply_python_sdk.model.staff_response import StaffResponse
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = staff_api.StaffApi(api_client)
    staff_uuid = "staff_uuid_example" # str | 
    with_places = False # bool |  (optional) if omitted the server will use the default value of False
    with_companies = False # bool |  (optional) if omitted the server will use the default value of False
    with_catalog = False # bool |  (optional) if omitted the server will use the default value of False
    with_schedule = False # bool |  (optional) if omitted the server will use the default value of False
    with_roles = False # bool |  (optional) if omitted the server will use the default value of False
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Getstaff
        api_response = api_instance.get_staff(staff_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling StaffApi->get_staff: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Getstaff
        api_response = api_instance.get_staff(staff_uuid, with_places=with_places, with_companies=with_companies, with_catalog=with_catalog, with_schedule=with_schedule, with_roles=with_roles, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling StaffApi->get_staff: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **staff_uuid** | **str**|  |
 **with_places** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_companies** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_catalog** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_schedule** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_roles** | **bool**|  | [optional] if omitted the server will use the default value of False
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**StaffResponse**](StaffResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Route not found - Denied by eHelply |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_staff**
> Page search_staff()

Searchstaff

TODO Item return format: ``` {     uuid                                **type:** string     project_uuid                        **type:** string or None      entity                              **type:** string or None      place                               **type:** dict or None      company                             **type:** dict or None      schedule                            **type:** dict or None      catalog                             **type:** dict or None      reviews                             **type:** dict or None      created_at                          **type:** string or None      updated_at                          **type:** string or None      deleted_at                          **type:** string or None  } ```

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import staff_api
from ehelply_python_sdk.model.page import Page
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = staff_api.StaffApi(api_client)
    project_uuid = "project_uuid_example" # str |  (optional)
    first_name = "first_name_example" # str |  (optional)
    last_name = "last_name_example" # str |  (optional)
    is_deleted = False # bool |  (optional) if omitted the server will use the default value of False
    with_companies = False # bool |  (optional) if omitted the server will use the default value of False
    with_places = False # bool |  (optional) if omitted the server will use the default value of False
    with_schedule = False # bool |  (optional) if omitted the server will use the default value of False
    with_catalog = False # bool |  (optional) if omitted the server will use the default value of False
    with_reviews = False # bool |  (optional) if omitted the server will use the default value of False
    with_roles = False # bool |  (optional) if omitted the server will use the default value of False
    page = 1 # int |  (optional) if omitted the server will use the default value of 1
    page_size = 25 # int |  (optional) if omitted the server will use the default value of 25
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
        # Searchstaff
        api_response = api_instance.search_staff(project_uuid=project_uuid, first_name=first_name, last_name=last_name, is_deleted=is_deleted, with_companies=with_companies, with_places=with_places, with_schedule=with_schedule, with_catalog=with_catalog, with_reviews=with_reviews, with_roles=with_roles, page=page, page_size=page_size, sort_on=sort_on, sort_desc=sort_desc, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling StaffApi->search_staff: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**|  | [optional]
 **first_name** | **str**|  | [optional]
 **last_name** | **str**|  | [optional]
 **is_deleted** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_companies** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_places** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_schedule** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_catalog** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_reviews** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_roles** | **bool**|  | [optional] if omitted the server will use the default value of False
 **page** | **int**|  | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 25
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
**404** | Route not found - Denied by eHelply |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_staff**
> StaffResponse update_staff(staff_uuid, staff_base)

Updatestaff

Update staff with given info, only updating the fields supplied. Staff Uuid must be sent however.

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import staff_api
from ehelply_python_sdk.model.staff_response import StaffResponse
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.staff_base import StaffBase
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = staff_api.StaffApi(api_client)
    staff_uuid = "staff_uuid_example" # str | 
    staff_base = StaffBase(
        entity_uuid="entity_uuid_1234",
        project_uuid="project_uuid_1234",
        schedule_uuid="schedule_uuid_1234",
        catalog_uuid="catalog_uuid_1234",
        review_group_uuid="review_uuid_1234",
    ) # StaffBase | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updatestaff
        api_response = api_instance.update_staff(staff_uuid, staff_base)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling StaffApi->update_staff: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updatestaff
        api_response = api_instance.update_staff(staff_uuid, staff_base, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling StaffApi->update_staff: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **staff_uuid** | **str**|  |
 **staff_base** | [**StaffBase**](StaffBase.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**StaffResponse**](StaffResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Route not found - Denied by eHelply |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

