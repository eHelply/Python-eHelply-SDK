# ehelply_python_sdk.DefaultApi

All URIs are relative to *https://api.prod.ehelply.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_entity_to_appointment**](DefaultApi.md#attach_entity_to_appointment) | **POST** /appointments/appointments/{appointment_uuid}/entities/{entity_uuid} | Attach Entity To Appointment
[**create_appointment**](DefaultApi.md#create_appointment) | **POST** /appointments/appointments | Create Appointment
[**delete_appointment**](DefaultApi.md#delete_appointment) | **DELETE** /appointments/appointments/{appointment_uuid} | Delete Appointment
[**detach_entity_from_appointment**](DefaultApi.md#detach_entity_from_appointment) | **DELETE** /appointments/appointments/{appointment_uuid}/entities/{entity_uuid} | Detach Entity From Appointment
[**get_appointment**](DefaultApi.md#get_appointment) | **GET** /appointments/appointments/{appointment_uuid} | Get Appointment
[**search_appointment**](DefaultApi.md#search_appointment) | **GET** /appointments/appointments | Search Appointment
[**search_appointment_entities**](DefaultApi.md#search_appointment_entities) | **GET** /appointments/appointments/{appointment_uuid}/entities | Search Appointment Entities
[**search_entity_appointments**](DefaultApi.md#search_entity_appointments) | **GET** /appointments/appointments/entities/{entity_uuid}/appointments | Get Entities Appointments
[**update_appointment**](DefaultApi.md#update_appointment) | **PUT** /appointments/appointments/{appointment_uuid} | Update Appointment


# **attach_entity_to_appointment**
> bool attach_entity_to_appointment(appointment_uuid, entity_uuid)

Attach Entity To Appointment

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    appointment_uuid = "appointment_uuid_example" # str | 
    entity_uuid = "entity_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Attach Entity To Appointment
        api_response = api_instance.attach_entity_to_appointment(appointment_uuid, entity_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling DefaultApi->attach_entity_to_appointment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Attach Entity To Appointment
        api_response = api_instance.attach_entity_to_appointment(appointment_uuid, entity_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling DefaultApi->attach_entity_to_appointment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appointment_uuid** | **str**|  |
 **entity_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

**bool**

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

# **create_appointment**
> AppointmentResponse create_appointment(appointment_base)

Create Appointment

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import default_api
from ehelply_python_sdk.model.appointment_response import AppointmentResponse
from ehelply_python_sdk.model.appointment_base import AppointmentBase
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
    api_instance = default_api.DefaultApi(api_client)
    appointment_base = AppointmentBase(
        project_uuid="project_uuid",
        place_uuid="place_uuid",
        review_group_uuid="review_group_uuid",
        expected_finish_at="2020-06-27T12:00:00.000000",
        expected_start_at="2020-06-27T12:00:00.000000",
        actual_start_at="2020-06-27T12:00:00.000000",
        actual_finish_at="2020-06-27T12:00:00.000000",
        products={},
        meta_uuid="meta_uuid",
        status="Awaiting Approval",
        cancellation_at="2020-06-27T12:00:00.000000",
        cancellation_reason="Sick",
        cancellation_entity_uuid="user_uuid",
    ) # AppointmentBase | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Appointment
        api_response = api_instance.create_appointment(appointment_base)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling DefaultApi->create_appointment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Appointment
        api_response = api_instance.create_appointment(appointment_base, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling DefaultApi->create_appointment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appointment_base** | [**AppointmentBase**](AppointmentBase.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**AppointmentResponse**](AppointmentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_appointment**
> bool delete_appointment(appointment_uuid)

Delete Appointment

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    appointment_uuid = "appointment_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete Appointment
        api_response = api_instance.delete_appointment(appointment_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling DefaultApi->delete_appointment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Appointment
        api_response = api_instance.delete_appointment(appointment_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling DefaultApi->delete_appointment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appointment_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

**bool**

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

# **detach_entity_from_appointment**
> bool detach_entity_from_appointment(appointment_uuid, entity_uuid)

Detach Entity From Appointment

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    appointment_uuid = "appointment_uuid_example" # str | 
    entity_uuid = "entity_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Detach Entity From Appointment
        api_response = api_instance.detach_entity_from_appointment(appointment_uuid, entity_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling DefaultApi->detach_entity_from_appointment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Detach Entity From Appointment
        api_response = api_instance.detach_entity_from_appointment(appointment_uuid, entity_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling DefaultApi->detach_entity_from_appointment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appointment_uuid** | **str**|  |
 **entity_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

**bool**

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

# **get_appointment**
> AppointmentResponse get_appointment(appointment_uuid)

Get Appointment

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import default_api
from ehelply_python_sdk.model.appointment_response import AppointmentResponse
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
    api_instance = default_api.DefaultApi(api_client)
    appointment_uuid = "appointment_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Appointment
        api_response = api_instance.get_appointment(appointment_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_appointment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Appointment
        api_response = api_instance.get_appointment(appointment_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_appointment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appointment_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**AppointmentResponse**](AppointmentResponse.md)

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
**404** | Appointment does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_appointment**
> bool, date, datetime, dict, float, int, list, str, none_type search_appointment()

Search Appointment

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    place_uuid = "place_uuid_example" # str |  (optional)
    exclude_cancelled = False # bool |  (optional) if omitted the server will use the default value of False
    is_deleted = False # bool |  (optional) if omitted the server will use the default value of False
    start_range = "start_range_example" # str |  (optional)
    end_range = "end_range_example" # str |  (optional)
    page = 1 # int |  (optional) if omitted the server will use the default value of 1
    page_size = 25 # int |  (optional) if omitted the server will use the default value of 25
    sort_on = "sort_on_example" # str |  (optional)
    sort_desc = False # bool |  (optional) if omitted the server will use the default value of False
    search = "search_example" # str |  (optional)
    search_on = "search_on_example" # str |  (optional)
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Appointment
        api_response = api_instance.search_appointment(place_uuid=place_uuid, exclude_cancelled=exclude_cancelled, is_deleted=is_deleted, start_range=start_range, end_range=end_range, page=page, page_size=page_size, sort_on=sort_on, sort_desc=sort_desc, search=search, search_on=search_on, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling DefaultApi->search_appointment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **place_uuid** | **str**|  | [optional]
 **exclude_cancelled** | **bool**|  | [optional] if omitted the server will use the default value of False
 **is_deleted** | **bool**|  | [optional] if omitted the server will use the default value of False
 **start_range** | **str**|  | [optional]
 **end_range** | **str**|  | [optional]
 **page** | **int**|  | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 25
 **sort_on** | **str**|  | [optional]
 **sort_desc** | **bool**|  | [optional] if omitted the server will use the default value of False
 **search** | **str**|  | [optional]
 **search_on** | **str**|  | [optional]
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

# **search_appointment_entities**
> bool, date, datetime, dict, float, int, list, str, none_type search_appointment_entities(appointment_uuid)

Search Appointment Entities

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    appointment_uuid = "appointment_uuid_example" # str | 
    page = 1 # int |  (optional) if omitted the server will use the default value of 1
    page_size = 25 # int |  (optional) if omitted the server will use the default value of 25
    sort_on = "sort_on_example" # str |  (optional)
    sort_desc = False # bool |  (optional) if omitted the server will use the default value of False
    search = "search_example" # str |  (optional)
    search_on = "search_on_example" # str |  (optional)
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search Appointment Entities
        api_response = api_instance.search_appointment_entities(appointment_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling DefaultApi->search_appointment_entities: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Appointment Entities
        api_response = api_instance.search_appointment_entities(appointment_uuid, page=page, page_size=page_size, sort_on=sort_on, sort_desc=sort_desc, search=search, search_on=search_on, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling DefaultApi->search_appointment_entities: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appointment_uuid** | **str**|  |
 **page** | **int**|  | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 25
 **sort_on** | **str**|  | [optional]
 **sort_desc** | **bool**|  | [optional] if omitted the server will use the default value of False
 **search** | **str**|  | [optional]
 **search_on** | **str**|  | [optional]
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

# **search_entity_appointments**
> bool, date, datetime, dict, float, int, list, str, none_type search_entity_appointments(entity_uuid)

Get Entities Appointments

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    entity_uuid = "entity_uuid_example" # str | 
    start_date = "start_date_example" # str |  (optional)
    end_date = "end_date_example" # str |  (optional)
    include_cancelled = False # bool |  (optional) if omitted the server will use the default value of False
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Entities Appointments
        api_response = api_instance.search_entity_appointments(entity_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling DefaultApi->search_entity_appointments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Entities Appointments
        api_response = api_instance.search_entity_appointments(entity_uuid, start_date=start_date, end_date=end_date, include_cancelled=include_cancelled, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling DefaultApi->search_entity_appointments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_uuid** | **str**|  |
 **start_date** | **str**|  | [optional]
 **end_date** | **str**|  | [optional]
 **include_cancelled** | **bool**|  | [optional] if omitted the server will use the default value of False
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

# **update_appointment**
> AppointmentResponse update_appointment(appointment_uuid, appointment_base)

Update Appointment

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import default_api
from ehelply_python_sdk.model.appointment_response import AppointmentResponse
from ehelply_python_sdk.model.appointment_base import AppointmentBase
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
    api_instance = default_api.DefaultApi(api_client)
    appointment_uuid = "appointment_uuid_example" # str | 
    appointment_base = AppointmentBase(
        project_uuid="project_uuid",
        place_uuid="place_uuid",
        review_group_uuid="review_group_uuid",
        expected_finish_at="2020-06-27T12:00:00.000000",
        expected_start_at="2020-06-27T12:00:00.000000",
        actual_start_at="2020-06-27T12:00:00.000000",
        actual_finish_at="2020-06-27T12:00:00.000000",
        products={},
        meta_uuid="meta_uuid",
        status="Awaiting Approval",
        cancellation_at="2020-06-27T12:00:00.000000",
        cancellation_reason="Sick",
        cancellation_entity_uuid="user_uuid",
    ) # AppointmentBase | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Appointment
        api_response = api_instance.update_appointment(appointment_uuid, appointment_base)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling DefaultApi->update_appointment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Appointment
        api_response = api_instance.update_appointment(appointment_uuid, appointment_base, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling DefaultApi->update_appointment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appointment_uuid** | **str**|  |
 **appointment_base** | [**AppointmentBase**](AppointmentBase.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**AppointmentResponse**](AppointmentResponse.md)

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
**404** | Appointment does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

