# ehelply-python-sdk.MonitorApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ack_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_acknowledge_post**](MonitorApi.md#ack_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_acknowledge_post) | **POST** /sam/monitor/services/{service_uuid}/stages/{stage}/alarms/{alarm_uuid}/acknowledge | Ack Alarm
[**assign_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_assign_post**](MonitorApi.md#assign_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_assign_post) | **POST** /sam/monitor/services/{service_uuid}/stages/{stage}/alarms/{alarm_uuid}/assign | Assign Alarm
[**attach_alarm_note_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_note_post**](MonitorApi.md#attach_alarm_note_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_note_post) | **POST** /sam/monitor/services/{service_uuid}/stages/{stage}/alarms/{alarm_uuid}/note | Attach Alarm Note
[**attach_alarm_ticket_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_ticket_post**](MonitorApi.md#attach_alarm_ticket_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_ticket_post) | **POST** /sam/monitor/services/{service_uuid}/stages/{stage}/alarms/{alarm_uuid}/ticket | Attach Alarm Ticket
[**clear_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_clear_post**](MonitorApi.md#clear_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_clear_post) | **POST** /sam/monitor/services/{service_uuid}/stages/{stage}/alarms/{alarm_uuid}/clear | Clear Alarm
[**get_service_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_get**](MonitorApi.md#get_service_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_get) | **GET** /sam/monitor/services/{service_uuid}/stages/{stage}/alarms/{alarm_uuid} | Get Service Alarm
[**get_service_alarms_monitor_services_service_uuid_stages_stage_alarms_get**](MonitorApi.md#get_service_alarms_monitor_services_service_uuid_stages_stage_alarms_get) | **GET** /sam/monitor/services/{service_uuid}/stages/{stage}/alarms | Get Service Alarms
[**get_service_heartbeats_monitor_services_service_uuid_stages_stage_heartbeats_get**](MonitorApi.md#get_service_heartbeats_monitor_services_service_uuid_stages_stage_heartbeats_get) | **GET** /sam/monitor/services/{service_uuid}/stages/{stage}/heartbeats | Get Service Heartbeats
[**get_service_kpis_monitor_services_service_uuid_kpis_get**](MonitorApi.md#get_service_kpis_monitor_services_service_uuid_kpis_get) | **GET** /sam/monitor/services/{service_uuid}/kpis | Get Service Kpis
[**get_service_monitor_services_service_uuid_get**](MonitorApi.md#get_service_monitor_services_service_uuid_get) | **GET** /sam/monitor/services/{service_uuid} | Get Service
[**get_service_vitals_monitor_services_service_uuid_stages_stage_vitals_get**](MonitorApi.md#get_service_vitals_monitor_services_service_uuid_stages_stage_vitals_get) | **GET** /sam/monitor/services/{service_uuid}/stages/{stage}/vitals | Get Service Vitals
[**get_services_monitor_services_get**](MonitorApi.md#get_services_monitor_services_get) | **GET** /sam/monitor/services | Get Services
[**hide_service_monitor_services_service_uuid_stages_stage_hide_post**](MonitorApi.md#hide_service_monitor_services_service_uuid_stages_stage_hide_post) | **POST** /sam/monitor/services/{service_uuid}/stages/{stage}/hide | Hide Service
[**ignore_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_ignore_post**](MonitorApi.md#ignore_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_ignore_post) | **POST** /sam/monitor/services/{service_uuid}/stages/{stage}/alarms/{alarm_uuid}/ignore | Ignore Alarm
[**register_service_monitor_services_post**](MonitorApi.md#register_service_monitor_services_post) | **POST** /sam/monitor/services | Register Service
[**search_alarms_monitor_services_service_uuid_alarms_get**](MonitorApi.md#search_alarms_monitor_services_service_uuid_alarms_get) | **GET** /sam/monitor/services/{service_uuid}/alarms | Search Alarms
[**show_service_monitor_services_service_uuid_stages_stage_show_post**](MonitorApi.md#show_service_monitor_services_service_uuid_stages_stage_show_post) | **POST** /sam/monitor/services/{service_uuid}/stages/{stage}/show | Show Service
[**terminate_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_terminate_post**](MonitorApi.md#terminate_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_terminate_post) | **POST** /sam/monitor/services/{service_uuid}/stages/{stage}/alarms/{alarm_uuid}/terminate | Terminate Alarm
[**trigger_alarm_monitor_services_service_uuid_stages_stage_alarms_post**](MonitorApi.md#trigger_alarm_monitor_services_service_uuid_stages_stage_alarms_post) | **POST** /sam/monitor/services/{service_uuid}/stages/{stage}/alarms | Trigger Alarm


# **ack_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_acknowledge_post**
> bool, date, datetime, dict, float, int, list, str, none_type ack_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_acknowledge_post(service_uuid, stage, alarm_uuid, body_ack_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_acknowledge_post)

Ack Alarm

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import monitor_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.body_ack_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_acknowledge_post import BodyAckAlarmMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidAcknowledgePost
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)
    service_uuid = "service_uuid_example" # str | 
    stage = "stage_example" # str | 
    alarm_uuid = "alarm_uuid_example" # str | 
    body_ack_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_acknowledge_post = BodyAckAlarmMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidAcknowledgePost(
        acknowledge=AlarmAcknowledge(
            acknowledger_uuid="acknowledger_uuid_example",
        ),
    ) # BodyAckAlarmMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidAcknowledgePost | 

    # example passing only required values which don't have defaults set
    try:
        # Ack Alarm
        api_response = api_instance.ack_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_acknowledge_post(service_uuid, stage, alarm_uuid, body_ack_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_acknowledge_post)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling MonitorApi->ack_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_acknowledge_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_uuid** | **str**|  |
 **stage** | **str**|  |
 **alarm_uuid** | **str**|  |
 **body_ack_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_acknowledge_post** | [**BodyAckAlarmMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidAcknowledgePost**](BodyAckAlarmMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidAcknowledgePost.md)|  |

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

# **assign_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_assign_post**
> bool, date, datetime, dict, float, int, list, str, none_type assign_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_assign_post(service_uuid, stage, alarm_uuid, body_assign_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_assign_post)

Assign Alarm

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import monitor_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.body_assign_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_assign_post import BodyAssignAlarmMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidAssignPost
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)
    service_uuid = "service_uuid_example" # str | 
    stage = "stage_example" # str | 
    alarm_uuid = "alarm_uuid_example" # str | 
    body_assign_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_assign_post = BodyAssignAlarmMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidAssignPost(
        assignee=AlarmAssign(
            assignee_uuid="assignee_uuid_example",
        ),
    ) # BodyAssignAlarmMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidAssignPost | 

    # example passing only required values which don't have defaults set
    try:
        # Assign Alarm
        api_response = api_instance.assign_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_assign_post(service_uuid, stage, alarm_uuid, body_assign_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_assign_post)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling MonitorApi->assign_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_assign_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_uuid** | **str**|  |
 **stage** | **str**|  |
 **alarm_uuid** | **str**|  |
 **body_assign_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_assign_post** | [**BodyAssignAlarmMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidAssignPost**](BodyAssignAlarmMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidAssignPost.md)|  |

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

# **attach_alarm_note_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_note_post**
> bool, date, datetime, dict, float, int, list, str, none_type attach_alarm_note_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_note_post(service_uuid, stage, alarm_uuid, body_attach_alarm_note_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_note_post)

Attach Alarm Note

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import monitor_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.body_attach_alarm_note_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_note_post import BodyAttachAlarmNoteMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidNotePost
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)
    service_uuid = "service_uuid_example" # str | 
    stage = "stage_example" # str | 
    alarm_uuid = "alarm_uuid_example" # str | 
    body_attach_alarm_note_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_note_post = BodyAttachAlarmNoteMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidNotePost(
        note=AlarmNote(
            author_uuid="author_uuid_example",
            message="message_example",
        ),
    ) # BodyAttachAlarmNoteMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidNotePost | 

    # example passing only required values which don't have defaults set
    try:
        # Attach Alarm Note
        api_response = api_instance.attach_alarm_note_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_note_post(service_uuid, stage, alarm_uuid, body_attach_alarm_note_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_note_post)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling MonitorApi->attach_alarm_note_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_note_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_uuid** | **str**|  |
 **stage** | **str**|  |
 **alarm_uuid** | **str**|  |
 **body_attach_alarm_note_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_note_post** | [**BodyAttachAlarmNoteMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidNotePost**](BodyAttachAlarmNoteMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidNotePost.md)|  |

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

# **attach_alarm_ticket_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_ticket_post**
> bool, date, datetime, dict, float, int, list, str, none_type attach_alarm_ticket_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_ticket_post(service_uuid, stage, alarm_uuid, body_attach_alarm_ticket_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_ticket_post)

Attach Alarm Ticket

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import monitor_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.body_attach_alarm_ticket_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_ticket_post import BodyAttachAlarmTicketMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidTicketPost
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)
    service_uuid = "service_uuid_example" # str | 
    stage = "stage_example" # str | 
    alarm_uuid = "alarm_uuid_example" # str | 
    body_attach_alarm_ticket_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_ticket_post = BodyAttachAlarmTicketMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidTicketPost(
        ticket=AlarmTicket(
            ticket_uuid="ticket_uuid_example",
        ),
    ) # BodyAttachAlarmTicketMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidTicketPost | 

    # example passing only required values which don't have defaults set
    try:
        # Attach Alarm Ticket
        api_response = api_instance.attach_alarm_ticket_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_ticket_post(service_uuid, stage, alarm_uuid, body_attach_alarm_ticket_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_ticket_post)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling MonitorApi->attach_alarm_ticket_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_ticket_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_uuid** | **str**|  |
 **stage** | **str**|  |
 **alarm_uuid** | **str**|  |
 **body_attach_alarm_ticket_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_ticket_post** | [**BodyAttachAlarmTicketMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidTicketPost**](BodyAttachAlarmTicketMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidTicketPost.md)|  |

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

# **clear_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_clear_post**
> bool, date, datetime, dict, float, int, list, str, none_type clear_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_clear_post(service_uuid, stage, alarm_uuid)

Clear Alarm

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import monitor_api
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
    api_instance = monitor_api.MonitorApi(api_client)
    service_uuid = "service_uuid_example" # str | 
    stage = "stage_example" # str | 
    alarm_uuid = "alarm_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Clear Alarm
        api_response = api_instance.clear_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_clear_post(service_uuid, stage, alarm_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling MonitorApi->clear_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_clear_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_uuid** | **str**|  |
 **stage** | **str**|  |
 **alarm_uuid** | **str**|  |

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

# **get_service_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_get**
> bool, date, datetime, dict, float, int, list, str, none_type get_service_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_get(service_uuid, stage, alarm_uuid)

Get Service Alarm

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import monitor_api
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
    api_instance = monitor_api.MonitorApi(api_client)
    service_uuid = "service_uuid_example" # str | 
    stage = "stage_example" # str | 
    alarm_uuid = "alarm_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Service Alarm
        api_response = api_instance.get_service_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_get(service_uuid, stage, alarm_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_uuid** | **str**|  |
 **stage** | **str**|  |
 **alarm_uuid** | **str**|  |

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

# **get_service_alarms_monitor_services_service_uuid_stages_stage_alarms_get**
> bool, date, datetime, dict, float, int, list, str, none_type get_service_alarms_monitor_services_service_uuid_stages_stage_alarms_get(service_uuid, stage)

Get Service Alarms

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import monitor_api
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
    api_instance = monitor_api.MonitorApi(api_client)
    service_uuid = "service_uuid_example" # str | 
    stage = "stage_example" # str | 
    history = 5 # int |  (optional) if omitted the server will use the default value of 5
    include_terminated = False # bool |  (optional) if omitted the server will use the default value of False
    include_cleared = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get Service Alarms
        api_response = api_instance.get_service_alarms_monitor_services_service_uuid_stages_stage_alarms_get(service_uuid, stage)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_alarms_monitor_services_service_uuid_stages_stage_alarms_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Service Alarms
        api_response = api_instance.get_service_alarms_monitor_services_service_uuid_stages_stage_alarms_get(service_uuid, stage, history=history, include_terminated=include_terminated, include_cleared=include_cleared)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_alarms_monitor_services_service_uuid_stages_stage_alarms_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_uuid** | **str**|  |
 **stage** | **str**|  |
 **history** | **int**|  | [optional] if omitted the server will use the default value of 5
 **include_terminated** | **bool**|  | [optional] if omitted the server will use the default value of False
 **include_cleared** | **bool**|  | [optional] if omitted the server will use the default value of False

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

# **get_service_heartbeats_monitor_services_service_uuid_stages_stage_heartbeats_get**
> bool, date, datetime, dict, float, int, list, str, none_type get_service_heartbeats_monitor_services_service_uuid_stages_stage_heartbeats_get(service_uuid, stage)

Get Service Heartbeats

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import monitor_api
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
    api_instance = monitor_api.MonitorApi(api_client)
    service_uuid = "service_uuid_example" # str | 
    stage = "stage_example" # str | 
    history = 5 # int |  (optional) if omitted the server will use the default value of 5

    # example passing only required values which don't have defaults set
    try:
        # Get Service Heartbeats
        api_response = api_instance.get_service_heartbeats_monitor_services_service_uuid_stages_stage_heartbeats_get(service_uuid, stage)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_heartbeats_monitor_services_service_uuid_stages_stage_heartbeats_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Service Heartbeats
        api_response = api_instance.get_service_heartbeats_monitor_services_service_uuid_stages_stage_heartbeats_get(service_uuid, stage, history=history)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_heartbeats_monitor_services_service_uuid_stages_stage_heartbeats_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_uuid** | **str**|  |
 **stage** | **str**|  |
 **history** | **int**|  | [optional] if omitted the server will use the default value of 5

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

# **get_service_kpis_monitor_services_service_uuid_kpis_get**
> bool, date, datetime, dict, float, int, list, str, none_type get_service_kpis_monitor_services_service_uuid_kpis_get(service_uuid)

Get Service Kpis

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import monitor_api
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
    api_instance = monitor_api.MonitorApi(api_client)
    service_uuid = "service_uuid_example" # str | 
    history = 5 # int |  (optional) if omitted the server will use the default value of 5

    # example passing only required values which don't have defaults set
    try:
        # Get Service Kpis
        api_response = api_instance.get_service_kpis_monitor_services_service_uuid_kpis_get(service_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_kpis_monitor_services_service_uuid_kpis_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Service Kpis
        api_response = api_instance.get_service_kpis_monitor_services_service_uuid_kpis_get(service_uuid, history=history)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_kpis_monitor_services_service_uuid_kpis_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_uuid** | **str**|  |
 **history** | **int**|  | [optional] if omitted the server will use the default value of 5

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

# **get_service_monitor_services_service_uuid_get**
> bool, date, datetime, dict, float, int, list, str, none_type get_service_monitor_services_service_uuid_get(service_uuid)

Get Service

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import monitor_api
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
    api_instance = monitor_api.MonitorApi(api_client)
    service_uuid = "service_uuid_example" # str | 
    heartbeats = False # bool |  (optional) if omitted the server will use the default value of False
    heartbeat_limit = 5 # int |  (optional) if omitted the server will use the default value of 5
    alarms = False # bool |  (optional) if omitted the server will use the default value of False
    alarm_limit = 5 # int |  (optional) if omitted the server will use the default value of 5
    stage = "stage_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Service
        api_response = api_instance.get_service_monitor_services_service_uuid_get(service_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_monitor_services_service_uuid_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Service
        api_response = api_instance.get_service_monitor_services_service_uuid_get(service_uuid, heartbeats=heartbeats, heartbeat_limit=heartbeat_limit, alarms=alarms, alarm_limit=alarm_limit, stage=stage)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_monitor_services_service_uuid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_uuid** | **str**|  |
 **heartbeats** | **bool**|  | [optional] if omitted the server will use the default value of False
 **heartbeat_limit** | **int**|  | [optional] if omitted the server will use the default value of 5
 **alarms** | **bool**|  | [optional] if omitted the server will use the default value of False
 **alarm_limit** | **int**|  | [optional] if omitted the server will use the default value of 5
 **stage** | **str**|  | [optional]

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

# **get_service_vitals_monitor_services_service_uuid_stages_stage_vitals_get**
> bool, date, datetime, dict, float, int, list, str, none_type get_service_vitals_monitor_services_service_uuid_stages_stage_vitals_get(service_uuid, stage)

Get Service Vitals

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import monitor_api
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
    api_instance = monitor_api.MonitorApi(api_client)
    service_uuid = "service_uuid_example" # str | 
    stage = "stage_example" # str | 
    history = 5 # int |  (optional) if omitted the server will use the default value of 5

    # example passing only required values which don't have defaults set
    try:
        # Get Service Vitals
        api_response = api_instance.get_service_vitals_monitor_services_service_uuid_stages_stage_vitals_get(service_uuid, stage)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_vitals_monitor_services_service_uuid_stages_stage_vitals_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Service Vitals
        api_response = api_instance.get_service_vitals_monitor_services_service_uuid_stages_stage_vitals_get(service_uuid, stage, history=history)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_vitals_monitor_services_service_uuid_stages_stage_vitals_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_uuid** | **str**|  |
 **stage** | **str**|  |
 **history** | **int**|  | [optional] if omitted the server will use the default value of 5

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

# **get_services_monitor_services_get**
> bool, date, datetime, dict, float, int, list, str, none_type get_services_monitor_services_get()

Get Services

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import monitor_api
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
    api_instance = monitor_api.MonitorApi(api_client)
    heartbeats = False # bool |  (optional) if omitted the server will use the default value of False
    heartbeat_limit = 5 # int |  (optional) if omitted the server will use the default value of 5
    alarms = False # bool |  (optional) if omitted the server will use the default value of False
    alarm_limit = 5 # int |  (optional) if omitted the server will use the default value of 5
    include_hidden = False # bool |  (optional) if omitted the server will use the default value of False
    stage = "stage_example" # str |  (optional)
    key = "key_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Services
        api_response = api_instance.get_services_monitor_services_get(heartbeats=heartbeats, heartbeat_limit=heartbeat_limit, alarms=alarms, alarm_limit=alarm_limit, include_hidden=include_hidden, stage=stage, key=key)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_services_monitor_services_get: %s\n" % e)
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

# **hide_service_monitor_services_service_uuid_stages_stage_hide_post**
> bool, date, datetime, dict, float, int, list, str, none_type hide_service_monitor_services_service_uuid_stages_stage_hide_post(service_uuid, stage)

Hide Service

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import monitor_api
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
    api_instance = monitor_api.MonitorApi(api_client)
    service_uuid = "service_uuid_example" # str | 
    stage = "stage_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Hide Service
        api_response = api_instance.hide_service_monitor_services_service_uuid_stages_stage_hide_post(service_uuid, stage)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling MonitorApi->hide_service_monitor_services_service_uuid_stages_stage_hide_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_uuid** | **str**|  |
 **stage** | **str**|  |

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

# **ignore_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_ignore_post**
> bool, date, datetime, dict, float, int, list, str, none_type ignore_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_ignore_post(service_uuid, stage, alarm_uuid, body_ignore_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_ignore_post)

Ignore Alarm

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import monitor_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.body_ignore_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_ignore_post import BodyIgnoreAlarmMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidIgnorePost
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)
    service_uuid = "service_uuid_example" # str | 
    stage = "stage_example" # str | 
    alarm_uuid = "alarm_uuid_example" # str | 
    body_ignore_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_ignore_post = BodyIgnoreAlarmMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidIgnorePost(
        ignore=AlarmIgnore(
            ignorer_uuid="ignorer_uuid_example",
        ),
    ) # BodyIgnoreAlarmMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidIgnorePost | 

    # example passing only required values which don't have defaults set
    try:
        # Ignore Alarm
        api_response = api_instance.ignore_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_ignore_post(service_uuid, stage, alarm_uuid, body_ignore_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_ignore_post)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling MonitorApi->ignore_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_ignore_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_uuid** | **str**|  |
 **stage** | **str**|  |
 **alarm_uuid** | **str**|  |
 **body_ignore_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_ignore_post** | [**BodyIgnoreAlarmMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidIgnorePost**](BodyIgnoreAlarmMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidIgnorePost.md)|  |

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

# **register_service_monitor_services_post**
> bool, date, datetime, dict, float, int, list, str, none_type register_service_monitor_services_post(body_register_service_monitor_services_post)

Register Service

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import monitor_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.body_register_service_monitor_services_post import BodyRegisterServiceMonitorServicesPost
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)
    body_register_service_monitor_services_post = BodyRegisterServiceMonitorServicesPost(
        service=ServiceCreate(
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
        ),
    ) # BodyRegisterServiceMonitorServicesPost | 

    # example passing only required values which don't have defaults set
    try:
        # Register Service
        api_response = api_instance.register_service_monitor_services_post(body_register_service_monitor_services_post)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling MonitorApi->register_service_monitor_services_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_register_service_monitor_services_post** | [**BodyRegisterServiceMonitorServicesPost**](BodyRegisterServiceMonitorServicesPost.md)|  |

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

# **search_alarms_monitor_services_service_uuid_alarms_get**
> bool, date, datetime, dict, float, int, list, str, none_type search_alarms_monitor_services_service_uuid_alarms_get(service_uuid)

Search Alarms

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import monitor_api
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
    api_instance = monitor_api.MonitorApi(api_client)
    service_uuid = "service_uuid_example" # str | 
    page = 1 # int |  (optional) if omitted the server will use the default value of 1
    page_size = 25 # int |  (optional) if omitted the server will use the default value of 25
    search = "search_example" # str |  (optional)
    search_on = "search_on_example" # str |  (optional)
    sort_on = "sort_on_example" # str |  (optional)
    sort_desc = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Search Alarms
        api_response = api_instance.search_alarms_monitor_services_service_uuid_alarms_get(service_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling MonitorApi->search_alarms_monitor_services_service_uuid_alarms_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Alarms
        api_response = api_instance.search_alarms_monitor_services_service_uuid_alarms_get(service_uuid, page=page, page_size=page_size, search=search, search_on=search_on, sort_on=sort_on, sort_desc=sort_desc)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling MonitorApi->search_alarms_monitor_services_service_uuid_alarms_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_uuid** | **str**|  |
 **page** | **int**|  | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 25
 **search** | **str**|  | [optional]
 **search_on** | **str**|  | [optional]
 **sort_on** | **str**|  | [optional]
 **sort_desc** | **bool**|  | [optional] if omitted the server will use the default value of False

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

# **show_service_monitor_services_service_uuid_stages_stage_show_post**
> bool, date, datetime, dict, float, int, list, str, none_type show_service_monitor_services_service_uuid_stages_stage_show_post(service_uuid, stage)

Show Service

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import monitor_api
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
    api_instance = monitor_api.MonitorApi(api_client)
    service_uuid = "service_uuid_example" # str | 
    stage = "stage_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Show Service
        api_response = api_instance.show_service_monitor_services_service_uuid_stages_stage_show_post(service_uuid, stage)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling MonitorApi->show_service_monitor_services_service_uuid_stages_stage_show_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_uuid** | **str**|  |
 **stage** | **str**|  |

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

# **terminate_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_terminate_post**
> bool, date, datetime, dict, float, int, list, str, none_type terminate_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_terminate_post(service_uuid, stage, alarm_uuid, body_terminate_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_terminate_post)

Terminate Alarm

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import monitor_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.body_terminate_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_terminate_post import BodyTerminateAlarmMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidTerminatePost
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)
    service_uuid = "service_uuid_example" # str | 
    stage = "stage_example" # str | 
    alarm_uuid = "alarm_uuid_example" # str | 
    body_terminate_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_terminate_post = BodyTerminateAlarmMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidTerminatePost(
        terminate=AlarmTerminate(
            terminater_uuid="terminater_uuid_example",
        ),
    ) # BodyTerminateAlarmMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidTerminatePost | 

    # example passing only required values which don't have defaults set
    try:
        # Terminate Alarm
        api_response = api_instance.terminate_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_terminate_post(service_uuid, stage, alarm_uuid, body_terminate_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_terminate_post)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling MonitorApi->terminate_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_terminate_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_uuid** | **str**|  |
 **stage** | **str**|  |
 **alarm_uuid** | **str**|  |
 **body_terminate_alarm_monitor_services_service_uuid_stages_stage_alarms_alarm_uuid_terminate_post** | [**BodyTerminateAlarmMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidTerminatePost**](BodyTerminateAlarmMonitorServicesServiceUuidStagesStageAlarmsAlarmUuidTerminatePost.md)|  |

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

# **trigger_alarm_monitor_services_service_uuid_stages_stage_alarms_post**
> bool, date, datetime, dict, float, int, list, str, none_type trigger_alarm_monitor_services_service_uuid_stages_stage_alarms_post(service_uuid, stage, body_trigger_alarm_monitor_services_service_uuid_stages_stage_alarms_post)

Trigger Alarm

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import monitor_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.body_trigger_alarm_monitor_services_service_uuid_stages_stage_alarms_post import BodyTriggerAlarmMonitorServicesServiceUuidStagesStageAlarmsPost
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)
    service_uuid = "service_uuid_example" # str | 
    stage = "stage_example" # str | 
    body_trigger_alarm_monitor_services_service_uuid_stages_stage_alarms_post = BodyTriggerAlarmMonitorServicesServiceUuidStagesStageAlarmsPost(
        alarm=AlarmCreate(
            process="process_example",
            severity="severity_example",
            name="name_example",
            summary="summary_example",
            description="description_example",
        ),
    ) # BodyTriggerAlarmMonitorServicesServiceUuidStagesStageAlarmsPost | 

    # example passing only required values which don't have defaults set
    try:
        # Trigger Alarm
        api_response = api_instance.trigger_alarm_monitor_services_service_uuid_stages_stage_alarms_post(service_uuid, stage, body_trigger_alarm_monitor_services_service_uuid_stages_stage_alarms_post)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling MonitorApi->trigger_alarm_monitor_services_service_uuid_stages_stage_alarms_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_uuid** | **str**|  |
 **stage** | **str**|  |
 **body_trigger_alarm_monitor_services_service_uuid_stages_stage_alarms_post** | [**BodyTriggerAlarmMonitorServicesServiceUuidStagesStageAlarmsPost**](BodyTriggerAlarmMonitorServicesServiceUuidStagesStageAlarmsPost.md)|  |

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

