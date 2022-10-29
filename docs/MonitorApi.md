# ehelply_python_sdk.MonitorApi

All URIs are relative to *https://api.prod.ehelply.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acknowledge_alarm**](MonitorApi.md#acknowledge_alarm) | **POST** /sam/monitor/services/{service}/stages/{stage}/alarms/{alarm_uuid}/acknowledge | Acknowledgealarm
[**assign_alarm**](MonitorApi.md#assign_alarm) | **POST** /sam/monitor/services/{service}/stages/{stage}/alarms/{alarm_uuid}/assign | Assignalarm
[**attach_alarm_note**](MonitorApi.md#attach_alarm_note) | **POST** /sam/monitor/services/{service}/stages/{stage}/alarms/{alarm_uuid}/note | Attachalarmnote
[**attach_alarm_ticket**](MonitorApi.md#attach_alarm_ticket) | **POST** /sam/monitor/services/{service}/stages/{stage}/alarms/{alarm_uuid}/ticket | Attachalarmticket
[**clear_alarm**](MonitorApi.md#clear_alarm) | **POST** /sam/monitor/services/{service}/stages/{stage}/alarms/{alarm_uuid}/clear | Clearalarm
[**delete_service_super_stack_meta**](MonitorApi.md#delete_service_super_stack_meta) | **DELETE** /sam/monitor/services/{service}/superstack | Deleteservicesuperstackmeta
[**get_service**](MonitorApi.md#get_service) | **GET** /sam/monitor/services/{service} | Getservice
[**get_service_alarm**](MonitorApi.md#get_service_alarm) | **GET** /sam/monitor/services/{service}/stages/{stage}/alarms/{alarm_uuid} | Getservicealarm
[**get_service_alarms**](MonitorApi.md#get_service_alarms) | **GET** /sam/monitor/services/{service}/stages/{stage}/alarms | Getservicealarms
[**get_service_heartbeat**](MonitorApi.md#get_service_heartbeat) | **GET** /sam/monitor/services/{service}/stages/{stage}/heartbeats | Getserviceheartbeat
[**get_service_kpis**](MonitorApi.md#get_service_kpis) | **GET** /sam/monitor/services/{service}/kpis | Getservicekpis
[**get_service_spec**](MonitorApi.md#get_service_spec) | **GET** /sam/monitor/services/{service}/specs/{spec} | Getservicespec
[**get_service_specs**](MonitorApi.md#get_service_specs) | **GET** /sam/monitor/services/{service}/specs | Getservicespecs
[**get_service_vitals**](MonitorApi.md#get_service_vitals) | **GET** /sam/monitor/services/{service}/stages/{stage}/vitals | Getservicevitals
[**get_services**](MonitorApi.md#get_services) | **GET** /sam/monitor/services | Getservices
[**get_services_with_specs**](MonitorApi.md#get_services_with_specs) | **GET** /sam/monitor/specs/services | Getserviceswithspecs
[**get_supertack_services**](MonitorApi.md#get_supertack_services) | **GET** /sam/monitor/superstack-services | Getsupertackservices
[**hide_service**](MonitorApi.md#hide_service) | **POST** /sam/monitor/services/{service}/stages/{stage}/hide | Hideservice
[**ignore_alarm**](MonitorApi.md#ignore_alarm) | **POST** /sam/monitor/services/{service}/stages/{stage}/alarms/{alarm_uuid}/ignore | Ignorealarm
[**register_service**](MonitorApi.md#register_service) | **POST** /sam/monitor/services | Registerservice
[**save_service_super_stack_meta**](MonitorApi.md#save_service_super_stack_meta) | **POST** /sam/monitor/services/{service}/superstack | Saveservicesuperstackmeta
[**search_alarms**](MonitorApi.md#search_alarms) | **GET** /sam/monitor/services/{service}/alarms | Searchalarms
[**show_service**](MonitorApi.md#show_service) | **POST** /sam/monitor/services/{service}/stages/{stage}/show | Showservice
[**terminate_alarm**](MonitorApi.md#terminate_alarm) | **POST** /sam/monitor/services/{service}/stages/{stage}/alarms/{alarm_uuid}/terminate | Terminatealarm
[**trigger_alarm**](MonitorApi.md#trigger_alarm) | **POST** /sam/monitor/services/{service}/stages/{stage}/alarms | Triggeralarm


# **acknowledge_alarm**
> AlarmResponse acknowledge_alarm(service, stage, alarm_uuid, alarm_acknowledge)

Acknowledgealarm

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.alarm_response import AlarmResponse
from ehelply_python_sdk.model.alarm_acknowledge import AlarmAcknowledge
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
    api_instance = monitor_api.MonitorApi(api_client)
    service = "service_example" # str | 
    stage = "stage_example" # str | 
    alarm_uuid = "alarm_uuid_example" # str | 
    alarm_acknowledge = AlarmAcknowledge(
        acknowledger_uuid="acknowledger_uuid_example",
    ) # AlarmAcknowledge | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Acknowledgealarm
        api_response = api_instance.acknowledge_alarm(service, stage, alarm_uuid, alarm_acknowledge)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->acknowledge_alarm: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Acknowledgealarm
        api_response = api_instance.acknowledge_alarm(service, stage, alarm_uuid, alarm_acknowledge, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->acknowledge_alarm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **stage** | **str**|  |
 **alarm_uuid** | **str**|  |
 **alarm_acknowledge** | [**AlarmAcknowledge**](AlarmAcknowledge.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**AlarmResponse**](AlarmResponse.md)

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

# **assign_alarm**
> AlarmResponse assign_alarm(service, stage, alarm_uuid, alarm_assign)

Assignalarm

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.alarm_assign import AlarmAssign
from ehelply_python_sdk.model.alarm_response import AlarmResponse
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
    api_instance = monitor_api.MonitorApi(api_client)
    service = "service_example" # str | 
    stage = "stage_example" # str | 
    alarm_uuid = "alarm_uuid_example" # str | 
    alarm_assign = AlarmAssign(
        assignee_uuid="assignee_uuid_example",
    ) # AlarmAssign | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Assignalarm
        api_response = api_instance.assign_alarm(service, stage, alarm_uuid, alarm_assign)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->assign_alarm: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Assignalarm
        api_response = api_instance.assign_alarm(service, stage, alarm_uuid, alarm_assign, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->assign_alarm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **stage** | **str**|  |
 **alarm_uuid** | **str**|  |
 **alarm_assign** | [**AlarmAssign**](AlarmAssign.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**AlarmResponse**](AlarmResponse.md)

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

# **attach_alarm_note**
> AlarmResponse attach_alarm_note(service, stage, alarm_uuid, alarm_note)

Attachalarmnote

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.alarm_note import AlarmNote
from ehelply_python_sdk.model.alarm_response import AlarmResponse
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
    api_instance = monitor_api.MonitorApi(api_client)
    service = "service_example" # str | 
    stage = "stage_example" # str | 
    alarm_uuid = "alarm_uuid_example" # str | 
    alarm_note = AlarmNote(
        author_uuid="author_uuid_example",
        message="message_example",
    ) # AlarmNote | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Attachalarmnote
        api_response = api_instance.attach_alarm_note(service, stage, alarm_uuid, alarm_note)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->attach_alarm_note: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Attachalarmnote
        api_response = api_instance.attach_alarm_note(service, stage, alarm_uuid, alarm_note, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->attach_alarm_note: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **stage** | **str**|  |
 **alarm_uuid** | **str**|  |
 **alarm_note** | [**AlarmNote**](AlarmNote.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**AlarmResponse**](AlarmResponse.md)

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

# **attach_alarm_ticket**
> AlarmResponse attach_alarm_ticket(service, stage, alarm_uuid, alarm_ticket)

Attachalarmticket

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.alarm_response import AlarmResponse
from ehelply_python_sdk.model.alarm_ticket import AlarmTicket
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
    api_instance = monitor_api.MonitorApi(api_client)
    service = "service_example" # str | 
    stage = "stage_example" # str | 
    alarm_uuid = "alarm_uuid_example" # str | 
    alarm_ticket = AlarmTicket(
        ticket_uuid="ticket_uuid_example",
    ) # AlarmTicket | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Attachalarmticket
        api_response = api_instance.attach_alarm_ticket(service, stage, alarm_uuid, alarm_ticket)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->attach_alarm_ticket: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Attachalarmticket
        api_response = api_instance.attach_alarm_ticket(service, stage, alarm_uuid, alarm_ticket, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->attach_alarm_ticket: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **stage** | **str**|  |
 **alarm_uuid** | **str**|  |
 **alarm_ticket** | [**AlarmTicket**](AlarmTicket.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**AlarmResponse**](AlarmResponse.md)

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

# **clear_alarm**
> AlarmResponse clear_alarm(service, stage, alarm_uuid)

Clearalarm

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.alarm_response import AlarmResponse
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
    api_instance = monitor_api.MonitorApi(api_client)
    service = "service_example" # str | 
    stage = "stage_example" # str | 
    alarm_uuid = "alarm_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Clearalarm
        api_response = api_instance.clear_alarm(service, stage, alarm_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->clear_alarm: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Clearalarm
        api_response = api_instance.clear_alarm(service, stage, alarm_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->clear_alarm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **stage** | **str**|  |
 **alarm_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**AlarmResponse**](AlarmResponse.md)

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

# **delete_service_super_stack_meta**
> bool, date, datetime, dict, float, int, list, str, none_type delete_service_super_stack_meta(service)

Deleteservicesuperstackmeta

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
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
    api_instance = monitor_api.MonitorApi(api_client)
    service = "service_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deleteservicesuperstackmeta
        api_response = api_instance.delete_service_super_stack_meta(service)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->delete_service_super_stack_meta: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deleteservicesuperstackmeta
        api_response = api_instance.delete_service_super_stack_meta(service, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->delete_service_super_stack_meta: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
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

# **get_service**
> ServiceResponse get_service(service)

Getservice

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.service_response import ServiceResponse
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
    api_instance = monitor_api.MonitorApi(api_client)
    service = "service_example" # str | 
    heartbeats = False # bool |  (optional) if omitted the server will use the default value of False
    heartbeat_limit = 5 # int |  (optional) if omitted the server will use the default value of 5
    alarms = False # bool |  (optional) if omitted the server will use the default value of False
    alarm_limit = 5 # int |  (optional) if omitted the server will use the default value of 5
    stage = "stage_example" # str |  (optional)
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Getservice
        api_response = api_instance.get_service(service)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Getservice
        api_response = api_instance.get_service(service, heartbeats=heartbeats, heartbeat_limit=heartbeat_limit, alarms=alarms, alarm_limit=alarm_limit, stage=stage, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **heartbeats** | **bool**|  | [optional] if omitted the server will use the default value of False
 **heartbeat_limit** | **int**|  | [optional] if omitted the server will use the default value of 5
 **alarms** | **bool**|  | [optional] if omitted the server will use the default value of False
 **alarm_limit** | **int**|  | [optional] if omitted the server will use the default value of 5
 **stage** | **str**|  | [optional]
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**ServiceResponse**](ServiceResponse.md)

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

# **get_service_alarm**
> AlarmResponse get_service_alarm(service, stage, alarm_uuid)

Getservicealarm

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.alarm_response import AlarmResponse
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
    api_instance = monitor_api.MonitorApi(api_client)
    service = "service_example" # str | 
    stage = "stage_example" # str | 
    alarm_uuid = "alarm_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Getservicealarm
        api_response = api_instance.get_service_alarm(service, stage, alarm_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_alarm: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Getservicealarm
        api_response = api_instance.get_service_alarm(service, stage, alarm_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_alarm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **stage** | **str**|  |
 **alarm_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**AlarmResponse**](AlarmResponse.md)

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

# **get_service_alarms**
> [AlarmResponse] get_service_alarms(service, stage)

Getservicealarms

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.alarm_response import AlarmResponse
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
    api_instance = monitor_api.MonitorApi(api_client)
    service = "service_example" # str | 
    stage = "stage_example" # str | 
    history = 5 # int |  (optional) if omitted the server will use the default value of 5
    include_terminated = False # bool |  (optional) if omitted the server will use the default value of False
    include_cleared = False # bool |  (optional) if omitted the server will use the default value of False
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Getservicealarms
        api_response = api_instance.get_service_alarms(service, stage)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_alarms: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Getservicealarms
        api_response = api_instance.get_service_alarms(service, stage, history=history, include_terminated=include_terminated, include_cleared=include_cleared, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_alarms: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **stage** | **str**|  |
 **history** | **int**|  | [optional] if omitted the server will use the default value of 5
 **include_terminated** | **bool**|  | [optional] if omitted the server will use the default value of False
 **include_cleared** | **bool**|  | [optional] if omitted the server will use the default value of False
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**[AlarmResponse]**](AlarmResponse.md)

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

# **get_service_heartbeat**
> [HeartbeatResponse] get_service_heartbeat(service, stage)

Getserviceheartbeat

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.heartbeat_response import HeartbeatResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)
    service = "service_example" # str | 
    stage = "stage_example" # str | 
    history = 5 # int |  (optional) if omitted the server will use the default value of 5
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Getserviceheartbeat
        api_response = api_instance.get_service_heartbeat(service, stage)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_heartbeat: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Getserviceheartbeat
        api_response = api_instance.get_service_heartbeat(service, stage, history=history, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_heartbeat: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **stage** | **str**|  |
 **history** | **int**|  | [optional] if omitted the server will use the default value of 5
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**[HeartbeatResponse]**](HeartbeatResponse.md)

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

# **get_service_kpis**
> [KpiResponse] get_service_kpis(service)

Getservicekpis

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.kpi_response import KpiResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)
    service = "service_example" # str | 
    history = 5 # int |  (optional) if omitted the server will use the default value of 5
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Getservicekpis
        api_response = api_instance.get_service_kpis(service)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_kpis: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Getservicekpis
        api_response = api_instance.get_service_kpis(service, history=history, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_kpis: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **history** | **int**|  | [optional] if omitted the server will use the default value of 5
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**[KpiResponse]**](KpiResponse.md)

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

# **get_service_spec**
> GetServiceSpecResponse get_service_spec(service, spec)

Getservicespec

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.get_appointment403_response import GetAppointment403Response
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.get_service_spec_response import GetServiceSpecResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)
    service = "service_example" # str | 
    spec = "spec_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Getservicespec
        api_response = api_instance.get_service_spec(service, spec)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_spec: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **spec** | **str**|  |

### Return type

[**GetServiceSpecResponse**](GetServiceSpecResponse.md)

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

# **get_service_specs**
> GetServiceSpecsResponse get_service_specs(service)

Getservicespecs

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.get_service_specs_response import GetServiceSpecsResponse
from ehelply_python_sdk.model.get_appointment403_response import GetAppointment403Response
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
    api_instance = monitor_api.MonitorApi(api_client)
    service = "service_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Getservicespecs
        api_response = api_instance.get_service_specs(service)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_specs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |

### Return type

[**GetServiceSpecsResponse**](GetServiceSpecsResponse.md)

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

# **get_service_vitals**
> [StatsVitalsResponse] get_service_vitals(service, stage)

Getservicevitals

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.stats_vitals_response import StatsVitalsResponse
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
    api_instance = monitor_api.MonitorApi(api_client)
    service = "service_example" # str | 
    stage = "stage_example" # str | 
    history = 5 # int |  (optional) if omitted the server will use the default value of 5
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Getservicevitals
        api_response = api_instance.get_service_vitals(service, stage)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_vitals: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Getservicevitals
        api_response = api_instance.get_service_vitals(service, stage, history=history, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_vitals: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **stage** | **str**|  |
 **history** | **int**|  | [optional] if omitted the server will use the default value of 5
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**[StatsVitalsResponse]**](StatsVitalsResponse.md)

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

# **get_services**
> [ServiceResponse] get_services()

Getservices

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.service_response import ServiceResponse
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
    api_instance = monitor_api.MonitorApi(api_client)
    heartbeats = False # bool |  (optional) if omitted the server will use the default value of False
    heartbeat_limit = 5 # int |  (optional) if omitted the server will use the default value of 5
    alarms = False # bool |  (optional) if omitted the server will use the default value of False
    alarm_limit = 5 # int |  (optional) if omitted the server will use the default value of 5
    include_hidden = False # bool |  (optional) if omitted the server will use the default value of False
    stage = "stage_example" # str |  (optional)
    key = "key_example" # str |  (optional)
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Getservices
        api_response = api_instance.get_services(heartbeats=heartbeats, heartbeat_limit=heartbeat_limit, alarms=alarms, alarm_limit=alarm_limit, include_hidden=include_hidden, stage=stage, key=key, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_services: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **heartbeats** | **bool**|  | [optional] if omitted the server will use the default value of False
 **heartbeat_limit** | **int**|  | [optional] if omitted the server will use the default value of 5
 **alarms** | **bool**|  | [optional] if omitted the server will use the default value of False
 **alarm_limit** | **int**|  | [optional] if omitted the server will use the default value of 5
 **include_hidden** | **bool**|  | [optional] if omitted the server will use the default value of False
 **stage** | **str**|  | [optional]
 **key** | **str**|  | [optional]
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**[ServiceResponse]**](ServiceResponse.md)

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

# **get_services_with_specs**
> GetServiceServiceWithSpecsResponse get_services_with_specs()

Getserviceswithspecs

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.get_appointment403_response import GetAppointment403Response
from ehelply_python_sdk.model.get_service_service_with_specs_response import GetServiceServiceWithSpecsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Getserviceswithspecs
        api_response = api_instance.get_services_with_specs()
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_services_with_specs: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetServiceServiceWithSpecsResponse**](GetServiceServiceWithSpecsResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supertack_services**
> [ServiceSuperStackMeta] get_supertack_services()

Getsupertackservices

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.service_super_stack_meta import ServiceSuperStackMeta
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Getsupertackservices
        api_response = api_instance.get_supertack_services()
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_supertack_services: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[ServiceSuperStackMeta]**](ServiceSuperStackMeta.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hide_service**
> ServiceMessageResponse hide_service(service, stage)

Hideservice

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.service_message_response import ServiceMessageResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)
    service = "service_example" # str | 
    stage = "stage_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Hideservice
        api_response = api_instance.hide_service(service, stage)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->hide_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Hideservice
        api_response = api_instance.hide_service(service, stage, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->hide_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **stage** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**ServiceMessageResponse**](ServiceMessageResponse.md)

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

# **ignore_alarm**
> AlarmResponse ignore_alarm(service, stage, alarm_uuid, alarm_ignore)

Ignorealarm

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.alarm_response import AlarmResponse
from ehelply_python_sdk.model.alarm_ignore import AlarmIgnore
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
    api_instance = monitor_api.MonitorApi(api_client)
    service = "service_example" # str | 
    stage = "stage_example" # str | 
    alarm_uuid = "alarm_uuid_example" # str | 
    alarm_ignore = AlarmIgnore(
        ignorer_uuid="ignorer_uuid_example",
    ) # AlarmIgnore | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Ignorealarm
        api_response = api_instance.ignore_alarm(service, stage, alarm_uuid, alarm_ignore)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->ignore_alarm: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Ignorealarm
        api_response = api_instance.ignore_alarm(service, stage, alarm_uuid, alarm_ignore, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->ignore_alarm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **stage** | **str**|  |
 **alarm_uuid** | **str**|  |
 **alarm_ignore** | [**AlarmIgnore**](AlarmIgnore.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**AlarmResponse**](AlarmResponse.md)

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

# **register_service**
> ServiceResponse register_service(service_create)

Registerservice

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.service_response import ServiceResponse
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.service_create import ServiceCreate
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)
    service_create = ServiceCreate(
        name="name_example",
        key="key_example",
        version="version_example",
        summary="summary_example",
        authors=[
            "authors_example",
        ],
        author_emails=[
            "author_emails_example",
        ],
    ) # ServiceCreate | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Registerservice
        api_response = api_instance.register_service(service_create)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->register_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Registerservice
        api_response = api_instance.register_service(service_create, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->register_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_create** | [**ServiceCreate**](ServiceCreate.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**ServiceResponse**](ServiceResponse.md)

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

# **save_service_super_stack_meta**
> bool, date, datetime, dict, float, int, list, str, none_type save_service_super_stack_meta(service, service_super_stack_meta)

Saveservicesuperstackmeta

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.service_super_stack_meta import ServiceSuperStackMeta
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)
    service = "service_example" # str | 
    service_super_stack_meta = ServiceSuperStackMeta(
        human_name="human_name_example",
        route_name="route_name_example",
        service_name="service_name_example",
        advertise=True,
        featured=True,
        picture="picture_example",
        background_picture="background_picture_example",
        tag_line="tag_line_example",
        summary="summary_example",
        description="description_example",
        features=[
            ServiceSuperStackMetaFeature(
                name="name_example",
                summary="summary_example",
            ),
        ],
        use_cases=[
            ServiceSuperStackMetaUseCase(
                name="name_example",
                summary="summary_example",
            ),
        ],
        getting_started=ServiceSuperStackMetaGettingStarted(
            blurb="blurb_example",
            endpoint_teasers=[
                ServiceSuperStackMetaGettingStartedEndpointTeaser(
                    path="path_example",
                    method="method_example",
                    description="description_example",
                ),
            ],
        ),
        faqs=[
            ServiceSuperStackMetaFaq(
                question="question_example",
                answer="answer_example",
            ),
        ],
    ) # ServiceSuperStackMeta | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Saveservicesuperstackmeta
        api_response = api_instance.save_service_super_stack_meta(service, service_super_stack_meta)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->save_service_super_stack_meta: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Saveservicesuperstackmeta
        api_response = api_instance.save_service_super_stack_meta(service, service_super_stack_meta, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->save_service_super_stack_meta: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **service_super_stack_meta** | [**ServiceSuperStackMeta**](ServiceSuperStackMeta.md)|  |
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
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_alarms**
> Page search_alarms(service)

Searchalarms

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
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
    api_instance = monitor_api.MonitorApi(api_client)
    service = "service_example" # str | 
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
        # Searchalarms
        api_response = api_instance.search_alarms(service)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->search_alarms: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Searchalarms
        api_response = api_instance.search_alarms(service, page=page, page_size=page_size, search=search, search_on=search_on, sort_on=sort_on, sort_desc=sort_desc, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->search_alarms: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
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
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_service**
> ServiceMessageResponse show_service(service, stage)

Showservice

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.service_message_response import ServiceMessageResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)
    service = "service_example" # str | 
    stage = "stage_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Showservice
        api_response = api_instance.show_service(service, stage)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->show_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Showservice
        api_response = api_instance.show_service(service, stage, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->show_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **stage** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**ServiceMessageResponse**](ServiceMessageResponse.md)

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

# **terminate_alarm**
> AlarmResponse terminate_alarm(service, stage, alarm_uuid, alarm_terminate)

Terminatealarm

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.alarm_response import AlarmResponse
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.alarm_terminate import AlarmTerminate
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)
    service = "service_example" # str | 
    stage = "stage_example" # str | 
    alarm_uuid = "alarm_uuid_example" # str | 
    alarm_terminate = AlarmTerminate(
        terminater_uuid="terminater_uuid_example",
    ) # AlarmTerminate | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Terminatealarm
        api_response = api_instance.terminate_alarm(service, stage, alarm_uuid, alarm_terminate)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->terminate_alarm: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Terminatealarm
        api_response = api_instance.terminate_alarm(service, stage, alarm_uuid, alarm_terminate, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->terminate_alarm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **stage** | **str**|  |
 **alarm_uuid** | **str**|  |
 **alarm_terminate** | [**AlarmTerminate**](AlarmTerminate.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**AlarmResponse**](AlarmResponse.md)

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

# **trigger_alarm**
> AlarmResponse trigger_alarm(service, stage, alarm_create)

Triggeralarm

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.alarm_response import AlarmResponse
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.alarm_create import AlarmCreate
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)
    service = "service_example" # str | 
    stage = "stage_example" # str | 
    alarm_create = AlarmCreate(
        process="process_example",
        severity="severity_example",
        name="name_example",
        summary="summary_example",
        description="description_example",
    ) # AlarmCreate | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Triggeralarm
        api_response = api_instance.trigger_alarm(service, stage, alarm_create)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->trigger_alarm: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Triggeralarm
        api_response = api_instance.trigger_alarm(service, stage, alarm_create, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->trigger_alarm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **stage** | **str**|  |
 **alarm_create** | [**AlarmCreate**](AlarmCreate.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**AlarmResponse**](AlarmResponse.md)

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

