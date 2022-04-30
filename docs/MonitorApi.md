# ehelply_python_sdk.MonitorApi

All URIs are relative to *https://api.prod.ehelply.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ack_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_acknowledge_post**](MonitorApi.md#ack_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_acknowledge_post) | **POST** /sam/monitor/services/{service}/stages/{stage}/alarms/{alarm_uuid}/acknowledge | Ack Alarm
[**assign_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_assign_post**](MonitorApi.md#assign_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_assign_post) | **POST** /sam/monitor/services/{service}/stages/{stage}/alarms/{alarm_uuid}/assign | Assign Alarm
[**attach_alarm_note_monitor_services_service_stages_stage_alarms_alarm_uuid_note_post**](MonitorApi.md#attach_alarm_note_monitor_services_service_stages_stage_alarms_alarm_uuid_note_post) | **POST** /sam/monitor/services/{service}/stages/{stage}/alarms/{alarm_uuid}/note | Attach Alarm Note
[**attach_alarm_ticket_monitor_services_service_stages_stage_alarms_alarm_uuid_ticket_post**](MonitorApi.md#attach_alarm_ticket_monitor_services_service_stages_stage_alarms_alarm_uuid_ticket_post) | **POST** /sam/monitor/services/{service}/stages/{stage}/alarms/{alarm_uuid}/ticket | Attach Alarm Ticket
[**clear_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_clear_post**](MonitorApi.md#clear_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_clear_post) | **POST** /sam/monitor/services/{service}/stages/{stage}/alarms/{alarm_uuid}/clear | Clear Alarm
[**get_service_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_get**](MonitorApi.md#get_service_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_get) | **GET** /sam/monitor/services/{service}/stages/{stage}/alarms/{alarm_uuid} | Get Service Alarm
[**get_service_alarms_monitor_services_service_stages_stage_alarms_get**](MonitorApi.md#get_service_alarms_monitor_services_service_stages_stage_alarms_get) | **GET** /sam/monitor/services/{service}/stages/{stage}/alarms | Get Service Alarms
[**get_service_heartbeats_monitor_services_service_stages_stage_heartbeats_get**](MonitorApi.md#get_service_heartbeats_monitor_services_service_stages_stage_heartbeats_get) | **GET** /sam/monitor/services/{service}/stages/{stage}/heartbeats | Get Service Heartbeats
[**get_service_kpis_monitor_services_service_kpis_get**](MonitorApi.md#get_service_kpis_monitor_services_service_kpis_get) | **GET** /sam/monitor/services/{service}/kpis | Get Service Kpis
[**get_service_monitor_services_service_get**](MonitorApi.md#get_service_monitor_services_service_get) | **GET** /sam/monitor/services/{service} | Get Service
[**get_service_spec**](MonitorApi.md#get_service_spec) | **GET** /sam/monitor/services/{service}/specs/{spec} | Getservicespec
[**get_service_specs**](MonitorApi.md#get_service_specs) | **GET** /sam/monitor/services/{service}/specs | Getservicespecs
[**get_service_vitals_monitor_services_service_stages_stage_vitals_get**](MonitorApi.md#get_service_vitals_monitor_services_service_stages_stage_vitals_get) | **GET** /sam/monitor/services/{service}/stages/{stage}/vitals | Get Service Vitals
[**get_services_monitor_services_get**](MonitorApi.md#get_services_monitor_services_get) | **GET** /sam/monitor/services | Get Services
[**get_services_with_specs**](MonitorApi.md#get_services_with_specs) | **GET** /sam/monitor/specs/services | Getserviceswithspecs
[**hide_service_monitor_services_service_stages_stage_hide_post**](MonitorApi.md#hide_service_monitor_services_service_stages_stage_hide_post) | **POST** /sam/monitor/services/{service}/stages/{stage}/hide | Hide Service
[**ignore_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_ignore_post**](MonitorApi.md#ignore_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_ignore_post) | **POST** /sam/monitor/services/{service}/stages/{stage}/alarms/{alarm_uuid}/ignore | Ignore Alarm
[**register_service_monitor_services_post**](MonitorApi.md#register_service_monitor_services_post) | **POST** /sam/monitor/services | Register Service
[**search_alarms_monitor_services_service_alarms_get**](MonitorApi.md#search_alarms_monitor_services_service_alarms_get) | **GET** /sam/monitor/services/{service}/alarms | Search Alarms
[**show_service_monitor_services_service_stages_stage_show_post**](MonitorApi.md#show_service_monitor_services_service_stages_stage_show_post) | **POST** /sam/monitor/services/{service}/stages/{stage}/show | Show Service
[**terminate_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_terminate_post**](MonitorApi.md#terminate_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_terminate_post) | **POST** /sam/monitor/services/{service}/stages/{stage}/alarms/{alarm_uuid}/terminate | Terminate Alarm
[**trigger_alarm_monitor_services_service_stages_stage_alarms_post**](MonitorApi.md#trigger_alarm_monitor_services_service_stages_stage_alarms_post) | **POST** /sam/monitor/services/{service}/stages/{stage}/alarms | Trigger Alarm

# **ack_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_acknowledge_post**
> bool, date, datetime, dict, float, int, list, str, none_type ack_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_acknowledge_post(servicestagealarm_uuidbody_ack_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_acknowledge_post)

Ack Alarm

### Example

```python
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.body_ack_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_acknowledge_post import BodyAckAlarmMonitorServicesServiceStagesStageAlarmsAlarmUuidAcknowledgePost
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
        'alarm_uuid': "alarm_uuid_example",
    }
    body = BodyAckAlarmMonitorServicesServiceStagesStageAlarmsAlarmUuidAcknowledgePost(
        acknowledge=AlarmAcknowledge(
            acknowledger_uuid="acknowledger_uuid_example",
        ),
    )
    try:
        # Ack Alarm
        api_response = api_instance.ack_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_acknowledge_post(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->ack_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_acknowledge_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BodyAckAlarmMonitorServicesServiceStagesStageAlarmsAlarmUuidAcknowledgePost**](BodyAckAlarmMonitorServicesServiceStagesStageAlarmsAlarmUuidAcknowledgePost.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
stage | StageSchema | | 
alarm_uuid | AlarmUuidSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### StageSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AlarmUuidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
404 | ApiResponseFor404 | Not found 
422 | ApiResponseFor422 | Validation Error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[dict, frozendict, str, date, datetime, int, float, bool, Decimal, None, list, tuple, bytes] | |

#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_assign_post**
> bool, date, datetime, dict, float, int, list, str, none_type assign_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_assign_post(servicestagealarm_uuidbody_assign_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_assign_post)

Assign Alarm

### Example

```python
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.body_assign_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_assign_post import BodyAssignAlarmMonitorServicesServiceStagesStageAlarmsAlarmUuidAssignPost
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
        'alarm_uuid': "alarm_uuid_example",
    }
    body = BodyAssignAlarmMonitorServicesServiceStagesStageAlarmsAlarmUuidAssignPost(
        assignee=AlarmAssign(
            assignee_uuid="assignee_uuid_example",
        ),
    )
    try:
        # Assign Alarm
        api_response = api_instance.assign_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_assign_post(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->assign_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_assign_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BodyAssignAlarmMonitorServicesServiceStagesStageAlarmsAlarmUuidAssignPost**](BodyAssignAlarmMonitorServicesServiceStagesStageAlarmsAlarmUuidAssignPost.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
stage | StageSchema | | 
alarm_uuid | AlarmUuidSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### StageSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AlarmUuidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
404 | ApiResponseFor404 | Not found 
422 | ApiResponseFor422 | Validation Error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[dict, frozendict, str, date, datetime, int, float, bool, Decimal, None, list, tuple, bytes] | |

#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_alarm_note_monitor_services_service_stages_stage_alarms_alarm_uuid_note_post**
> bool, date, datetime, dict, float, int, list, str, none_type attach_alarm_note_monitor_services_service_stages_stage_alarms_alarm_uuid_note_post(servicestagealarm_uuidbody_attach_alarm_note_monitor_services_service_stages_stage_alarms_alarm_uuid_note_post)

Attach Alarm Note

### Example

```python
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.body_attach_alarm_note_monitor_services_service_stages_stage_alarms_alarm_uuid_note_post import BodyAttachAlarmNoteMonitorServicesServiceStagesStageAlarmsAlarmUuidNotePost
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
        'alarm_uuid': "alarm_uuid_example",
    }
    body = BodyAttachAlarmNoteMonitorServicesServiceStagesStageAlarmsAlarmUuidNotePost(
        note=AlarmNote(
            author_uuid="author_uuid_example",
            message="message_example",
        ),
    )
    try:
        # Attach Alarm Note
        api_response = api_instance.attach_alarm_note_monitor_services_service_stages_stage_alarms_alarm_uuid_note_post(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->attach_alarm_note_monitor_services_service_stages_stage_alarms_alarm_uuid_note_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BodyAttachAlarmNoteMonitorServicesServiceStagesStageAlarmsAlarmUuidNotePost**](BodyAttachAlarmNoteMonitorServicesServiceStagesStageAlarmsAlarmUuidNotePost.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
stage | StageSchema | | 
alarm_uuid | AlarmUuidSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### StageSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AlarmUuidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
404 | ApiResponseFor404 | Not found 
422 | ApiResponseFor422 | Validation Error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[dict, frozendict, str, date, datetime, int, float, bool, Decimal, None, list, tuple, bytes] | |

#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_alarm_ticket_monitor_services_service_stages_stage_alarms_alarm_uuid_ticket_post**
> bool, date, datetime, dict, float, int, list, str, none_type attach_alarm_ticket_monitor_services_service_stages_stage_alarms_alarm_uuid_ticket_post(servicestagealarm_uuidbody_attach_alarm_ticket_monitor_services_service_stages_stage_alarms_alarm_uuid_ticket_post)

Attach Alarm Ticket

### Example

```python
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.body_attach_alarm_ticket_monitor_services_service_stages_stage_alarms_alarm_uuid_ticket_post import BodyAttachAlarmTicketMonitorServicesServiceStagesStageAlarmsAlarmUuidTicketPost
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
        'alarm_uuid': "alarm_uuid_example",
    }
    body = BodyAttachAlarmTicketMonitorServicesServiceStagesStageAlarmsAlarmUuidTicketPost(
        ticket=AlarmTicket(
            ticket_uuid="ticket_uuid_example",
        ),
    )
    try:
        # Attach Alarm Ticket
        api_response = api_instance.attach_alarm_ticket_monitor_services_service_stages_stage_alarms_alarm_uuid_ticket_post(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->attach_alarm_ticket_monitor_services_service_stages_stage_alarms_alarm_uuid_ticket_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BodyAttachAlarmTicketMonitorServicesServiceStagesStageAlarmsAlarmUuidTicketPost**](BodyAttachAlarmTicketMonitorServicesServiceStagesStageAlarmsAlarmUuidTicketPost.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
stage | StageSchema | | 
alarm_uuid | AlarmUuidSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### StageSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AlarmUuidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
404 | ApiResponseFor404 | Not found 
422 | ApiResponseFor422 | Validation Error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[dict, frozendict, str, date, datetime, int, float, bool, Decimal, None, list, tuple, bytes] | |

#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_clear_post**
> bool, date, datetime, dict, float, int, list, str, none_type clear_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_clear_post(servicestagealarm_uuid)

Clear Alarm

### Example

```python
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
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
        'alarm_uuid': "alarm_uuid_example",
    }
    try:
        # Clear Alarm
        api_response = api_instance.clear_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_clear_post(
            path_params=path_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->clear_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_clear_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
stage | StageSchema | | 
alarm_uuid | AlarmUuidSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### StageSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AlarmUuidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
404 | ApiResponseFor404 | Not found 
422 | ApiResponseFor422 | Validation Error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[dict, frozendict, str, date, datetime, int, float, bool, Decimal, None, list, tuple, bytes] | |

#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_get**
> bool, date, datetime, dict, float, int, list, str, none_type get_service_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_get(servicestagealarm_uuid)

Get Service Alarm

### Example

```python
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
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
        'alarm_uuid': "alarm_uuid_example",
    }
    try:
        # Get Service Alarm
        api_response = api_instance.get_service_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_get(
            path_params=path_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
stage | StageSchema | | 
alarm_uuid | AlarmUuidSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### StageSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AlarmUuidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
404 | ApiResponseFor404 | Not found 
422 | ApiResponseFor422 | Validation Error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[dict, frozendict, str, date, datetime, int, float, bool, Decimal, None, list, tuple, bytes] | |

#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_alarms_monitor_services_service_stages_stage_alarms_get**
> bool, date, datetime, dict, float, int, list, str, none_type get_service_alarms_monitor_services_service_stages_stage_alarms_get(servicestage)

Get Service Alarms

### Example

```python
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
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
    }
    query_params = {
    }
    try:
        # Get Service Alarms
        api_response = api_instance.get_service_alarms_monitor_services_service_stages_stage_alarms_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_alarms_monitor_services_service_stages_stage_alarms_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
    }
    query_params = {
        'history': 5,
        'include_terminated': False,
        'include_cleared': False,
    }
    try:
        # Get Service Alarms
        api_response = api_instance.get_service_alarms_monitor_services_service_stages_stage_alarms_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_alarms_monitor_services_service_stages_stage_alarms_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
history | HistorySchema | | optional
include_terminated | IncludeTerminatedSchema | | optional
include_cleared | IncludeClearedSchema | | optional


#### HistorySchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 5

#### IncludeTerminatedSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to False

#### IncludeClearedSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to False

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
stage | StageSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### StageSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
404 | ApiResponseFor404 | Not found 
422 | ApiResponseFor422 | Validation Error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[dict, frozendict, str, date, datetime, int, float, bool, Decimal, None, list, tuple, bytes] | |

#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_heartbeats_monitor_services_service_stages_stage_heartbeats_get**
> bool, date, datetime, dict, float, int, list, str, none_type get_service_heartbeats_monitor_services_service_stages_stage_heartbeats_get(servicestage)

Get Service Heartbeats

### Example

```python
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
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
    }
    query_params = {
    }
    try:
        # Get Service Heartbeats
        api_response = api_instance.get_service_heartbeats_monitor_services_service_stages_stage_heartbeats_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_heartbeats_monitor_services_service_stages_stage_heartbeats_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
    }
    query_params = {
        'history': 5,
    }
    try:
        # Get Service Heartbeats
        api_response = api_instance.get_service_heartbeats_monitor_services_service_stages_stage_heartbeats_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_heartbeats_monitor_services_service_stages_stage_heartbeats_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
history | HistorySchema | | optional


#### HistorySchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 5

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
stage | StageSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### StageSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
404 | ApiResponseFor404 | Not found 
422 | ApiResponseFor422 | Validation Error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[dict, frozendict, str, date, datetime, int, float, bool, Decimal, None, list, tuple, bytes] | |

#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_kpis_monitor_services_service_kpis_get**
> bool, date, datetime, dict, float, int, list, str, none_type get_service_kpis_monitor_services_service_kpis_get(service)

Get Service Kpis

### Example

```python
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
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
    }
    query_params = {
    }
    try:
        # Get Service Kpis
        api_response = api_instance.get_service_kpis_monitor_services_service_kpis_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_kpis_monitor_services_service_kpis_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service': "service_example",
    }
    query_params = {
        'history': 5,
    }
    try:
        # Get Service Kpis
        api_response = api_instance.get_service_kpis_monitor_services_service_kpis_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_kpis_monitor_services_service_kpis_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
history | HistorySchema | | optional


#### HistorySchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 5

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
404 | ApiResponseFor404 | Not found 
422 | ApiResponseFor422 | Validation Error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[dict, frozendict, str, date, datetime, int, float, bool, Decimal, None, list, tuple, bytes] | |

#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_monitor_services_service_get**
> bool, date, datetime, dict, float, int, list, str, none_type get_service_monitor_services_service_get(service)

Get Service

### Example

```python
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
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
    }
    query_params = {
    }
    try:
        # Get Service
        api_response = api_instance.get_service_monitor_services_service_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_monitor_services_service_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service': "service_example",
    }
    query_params = {
        'heartbeats': False,
        'heartbeat_limit': 5,
        'alarms': False,
        'alarm_limit': 5,
        'stage': "stage_example",
    }
    try:
        # Get Service
        api_response = api_instance.get_service_monitor_services_service_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_monitor_services_service_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
heartbeats | HeartbeatsSchema | | optional
heartbeat_limit | HeartbeatLimitSchema | | optional
alarms | AlarmsSchema | | optional
alarm_limit | AlarmLimitSchema | | optional
stage | StageSchema | | optional


#### HeartbeatsSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to False

#### HeartbeatLimitSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 5

#### AlarmsSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to False

#### AlarmLimitSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 5

#### StageSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
404 | ApiResponseFor404 | Not found 
422 | ApiResponseFor422 | Validation Error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[dict, frozendict, str, date, datetime, int, float, bool, Decimal, None, list, tuple, bytes] | |

#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_spec**
> InlineResponse2002 get_service_spec(servicespec)

Getservicespec

### Example

```python
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.inline_response403 import InlineResponse403
from ehelply_python_sdk.model.inline_response2002 import InlineResponse2002
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'spec': "spec_example",
    }
    query_params = {
    }
    try:
        # Getservicespec
        api_response = api_instance.get_service_spec(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_spec: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service': "service_example",
        'spec': "spec_example",
    }
    query_params = {
        'as_json': False,
    }
    try:
        # Getservicespec
        api_response = api_instance.get_service_spec(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_spec: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
as_json | AsJsonSchema | | optional


#### AsJsonSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to False

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
spec | SpecSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### SpecSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
403 | ApiResponseFor403 | Unauthorized - Denied by eHelply 
404 | ApiResponseFor404 | Not found 
422 | ApiResponseFor422 | Validation Error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InlineResponse2002**](InlineResponse2002.md) |  | 


#### ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InlineResponse403**](InlineResponse403.md) |  | 


#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_specs**
> InlineResponse2001 get_service_specs(service)

Getservicespecs

### Example

```python
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.inline_response403 import InlineResponse403
from ehelply_python_sdk.model.inline_response2001 import InlineResponse2001
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
    }
    try:
        # Getservicespecs
        api_response = api_instance.get_service_specs(
            path_params=path_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_specs: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
403 | ApiResponseFor403 | Unauthorized - Denied by eHelply 
404 | ApiResponseFor404 | Not found 
422 | ApiResponseFor422 | Validation Error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InlineResponse2001**](InlineResponse2001.md) |  | 


#### ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InlineResponse403**](InlineResponse403.md) |  | 


#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_vitals_monitor_services_service_stages_stage_vitals_get**
> bool, date, datetime, dict, float, int, list, str, none_type get_service_vitals_monitor_services_service_stages_stage_vitals_get(servicestage)

Get Service Vitals

### Example

```python
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
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
    }
    query_params = {
    }
    try:
        # Get Service Vitals
        api_response = api_instance.get_service_vitals_monitor_services_service_stages_stage_vitals_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_vitals_monitor_services_service_stages_stage_vitals_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
    }
    query_params = {
        'history': 5,
    }
    try:
        # Get Service Vitals
        api_response = api_instance.get_service_vitals_monitor_services_service_stages_stage_vitals_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_service_vitals_monitor_services_service_stages_stage_vitals_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
history | HistorySchema | | optional


#### HistorySchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 5

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
stage | StageSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### StageSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
404 | ApiResponseFor404 | Not found 
422 | ApiResponseFor422 | Validation Error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[dict, frozendict, str, date, datetime, int, float, bool, Decimal, None, list, tuple, bytes] | |

#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_services_monitor_services_get**
> bool, date, datetime, dict, float, int, list, str, none_type get_services_monitor_services_get()

Get Services

### Example

```python
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
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only optional values
    query_params = {
        'heartbeats': False,
        'heartbeat_limit': 5,
        'alarms': False,
        'alarm_limit': 5,
        'include_hidden': False,
        'stage': "stage_example",
        'key': "key_example",
    }
    try:
        # Get Services
        api_response = api_instance.get_services_monitor_services_get(
            query_params=query_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->get_services_monitor_services_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
heartbeats | HeartbeatsSchema | | optional
heartbeat_limit | HeartbeatLimitSchema | | optional
alarms | AlarmsSchema | | optional
alarm_limit | AlarmLimitSchema | | optional
include_hidden | IncludeHiddenSchema | | optional
stage | StageSchema | | optional
key | KeySchema | | optional


#### HeartbeatsSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to False

#### HeartbeatLimitSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 5

#### AlarmsSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to False

#### AlarmLimitSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 5

#### IncludeHiddenSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to False

#### StageSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### KeySchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
404 | ApiResponseFor404 | Not found 
422 | ApiResponseFor422 | Validation Error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[dict, frozendict, str, date, datetime, int, float, bool, Decimal, None, list, tuple, bytes] | |

#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_services_with_specs**
> InlineResponse200 get_services_with_specs()

Getserviceswithspecs

### Example

```python
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.inline_response403 import InlineResponse403
from ehelply_python_sdk.model.inline_response200 import InlineResponse200
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient(configuration) as api_client:
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
403 | ApiResponseFor403 | Unauthorized - Denied by eHelply 
404 | ApiResponseFor404 | Not found 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InlineResponse200**](InlineResponse200.md) |  | 


#### ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InlineResponse403**](InlineResponse403.md) |  | 


#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |


[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hide_service_monitor_services_service_stages_stage_hide_post**
> bool, date, datetime, dict, float, int, list, str, none_type hide_service_monitor_services_service_stages_stage_hide_post(servicestage)

Hide Service

### Example

```python
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
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
    }
    try:
        # Hide Service
        api_response = api_instance.hide_service_monitor_services_service_stages_stage_hide_post(
            path_params=path_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->hide_service_monitor_services_service_stages_stage_hide_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
stage | StageSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### StageSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
404 | ApiResponseFor404 | Not found 
422 | ApiResponseFor422 | Validation Error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[dict, frozendict, str, date, datetime, int, float, bool, Decimal, None, list, tuple, bytes] | |

#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ignore_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_ignore_post**
> bool, date, datetime, dict, float, int, list, str, none_type ignore_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_ignore_post(servicestagealarm_uuidbody_ignore_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_ignore_post)

Ignore Alarm

### Example

```python
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.body_ignore_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_ignore_post import BodyIgnoreAlarmMonitorServicesServiceStagesStageAlarmsAlarmUuidIgnorePost
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
        'alarm_uuid': "alarm_uuid_example",
    }
    body = BodyIgnoreAlarmMonitorServicesServiceStagesStageAlarmsAlarmUuidIgnorePost(
        ignore=AlarmIgnore(
            ignorer_uuid="ignorer_uuid_example",
        ),
    )
    try:
        # Ignore Alarm
        api_response = api_instance.ignore_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_ignore_post(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->ignore_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_ignore_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BodyIgnoreAlarmMonitorServicesServiceStagesStageAlarmsAlarmUuidIgnorePost**](BodyIgnoreAlarmMonitorServicesServiceStagesStageAlarmsAlarmUuidIgnorePost.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
stage | StageSchema | | 
alarm_uuid | AlarmUuidSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### StageSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AlarmUuidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
404 | ApiResponseFor404 | Not found 
422 | ApiResponseFor422 | Validation Error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[dict, frozendict, str, date, datetime, int, float, bool, Decimal, None, list, tuple, bytes] | |

#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_service_monitor_services_post**
> bool, date, datetime, dict, float, int, list, str, none_type register_service_monitor_services_post(body_register_service_monitor_services_post)

Register Service

### Example

```python
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.body_register_service_monitor_services_post import BodyRegisterServiceMonitorServicesPost
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    body = BodyRegisterServiceMonitorServicesPost(
        service=ServiceCreate(
            name="name_example",
            key="key_example",
            version="version_example",
            summary="summary_example",
            authors=[
                "authors_example"
            ],
            author_emails=[
                "author_emails_example"
            ],
        ),
    )
    try:
        # Register Service
        api_response = api_instance.register_service_monitor_services_post(
            body=body,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->register_service_monitor_services_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BodyRegisterServiceMonitorServicesPost**](BodyRegisterServiceMonitorServicesPost.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
404 | ApiResponseFor404 | Not found 
422 | ApiResponseFor422 | Validation Error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[dict, frozendict, str, date, datetime, int, float, bool, Decimal, None, list, tuple, bytes] | |

#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_alarms_monitor_services_service_alarms_get**
> bool, date, datetime, dict, float, int, list, str, none_type search_alarms_monitor_services_service_alarms_get(service)

Search Alarms

### Example

```python
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
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
    }
    query_params = {
    }
    try:
        # Search Alarms
        api_response = api_instance.search_alarms_monitor_services_service_alarms_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->search_alarms_monitor_services_service_alarms_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service': "service_example",
    }
    query_params = {
        'page': 1,
        'page_size': 25,
        'search': "search_example",
        'search_on': "search_on_example",
        'sort_on': "sort_on_example",
        'sort_desc': False,
    }
    try:
        # Search Alarms
        api_response = api_instance.search_alarms_monitor_services_service_alarms_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->search_alarms_monitor_services_service_alarms_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page | PageSchema | | optional
page_size | PageSizeSchema | | optional
search | SearchSchema | | optional
search_on | SearchOnSchema | | optional
sort_on | SortOnSchema | | optional
sort_desc | SortDescSchema | | optional


#### PageSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 1

#### PageSizeSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 25

#### SearchSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### SearchOnSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### SortOnSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### SortDescSchema

Type | Description | Notes
------------- | ------------- | -------------
**bool** |  | defaults to False

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
404 | ApiResponseFor404 | Not found 
422 | ApiResponseFor422 | Validation Error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[dict, frozendict, str, date, datetime, int, float, bool, Decimal, None, list, tuple, bytes] | |

#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_service_monitor_services_service_stages_stage_show_post**
> bool, date, datetime, dict, float, int, list, str, none_type show_service_monitor_services_service_stages_stage_show_post(servicestage)

Show Service

### Example

```python
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
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
    }
    try:
        # Show Service
        api_response = api_instance.show_service_monitor_services_service_stages_stage_show_post(
            path_params=path_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->show_service_monitor_services_service_stages_stage_show_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
stage | StageSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### StageSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
404 | ApiResponseFor404 | Not found 
422 | ApiResponseFor422 | Validation Error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[dict, frozendict, str, date, datetime, int, float, bool, Decimal, None, list, tuple, bytes] | |

#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_terminate_post**
> bool, date, datetime, dict, float, int, list, str, none_type terminate_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_terminate_post(servicestagealarm_uuidbody_terminate_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_terminate_post)

Terminate Alarm

### Example

```python
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.body_terminate_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_terminate_post import BodyTerminateAlarmMonitorServicesServiceStagesStageAlarmsAlarmUuidTerminatePost
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
        'alarm_uuid': "alarm_uuid_example",
    }
    body = BodyTerminateAlarmMonitorServicesServiceStagesStageAlarmsAlarmUuidTerminatePost(
        terminate=AlarmTerminate(
            terminater_uuid="terminater_uuid_example",
        ),
    )
    try:
        # Terminate Alarm
        api_response = api_instance.terminate_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_terminate_post(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->terminate_alarm_monitor_services_service_stages_stage_alarms_alarm_uuid_terminate_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BodyTerminateAlarmMonitorServicesServiceStagesStageAlarmsAlarmUuidTerminatePost**](BodyTerminateAlarmMonitorServicesServiceStagesStageAlarmsAlarmUuidTerminatePost.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
stage | StageSchema | | 
alarm_uuid | AlarmUuidSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### StageSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AlarmUuidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
404 | ApiResponseFor404 | Not found 
422 | ApiResponseFor422 | Validation Error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[dict, frozendict, str, date, datetime, int, float, bool, Decimal, None, list, tuple, bytes] | |

#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_alarm_monitor_services_service_stages_stage_alarms_post**
> bool, date, datetime, dict, float, int, list, str, none_type trigger_alarm_monitor_services_service_stages_stage_alarms_post(servicestagebody_trigger_alarm_monitor_services_service_stages_stage_alarms_post)

Trigger Alarm

### Example

```python
import ehelply_python_sdk
from ehelply_python_sdk.api import monitor_api
from ehelply_python_sdk.model.body_trigger_alarm_monitor_services_service_stages_stage_alarms_post import BodyTriggerAlarmMonitorServicesServiceStagesStageAlarmsPost
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitor_api.MonitorApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service': "service_example",
        'stage': "stage_example",
    }
    body = BodyTriggerAlarmMonitorServicesServiceStagesStageAlarmsPost(
        alarm=AlarmCreate(
            process="process_example",
            severity="severity_example",
            name="name_example",
            summary="summary_example",
            description="description_example",
        ),
    )
    try:
        # Trigger Alarm
        api_response = api_instance.trigger_alarm_monitor_services_service_stages_stage_alarms_post(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MonitorApi->trigger_alarm_monitor_services_service_stages_stage_alarms_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BodyTriggerAlarmMonitorServicesServiceStagesStageAlarmsPost**](BodyTriggerAlarmMonitorServicesServiceStagesStageAlarmsPost.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service | ServiceSchema | | 
stage | StageSchema | | 

#### ServiceSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### StageSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
404 | ApiResponseFor404 | Not found 
422 | ApiResponseFor422 | Validation Error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[dict, frozendict, str, date, datetime, int, float, bool, Decimal, None, list, tuple, bytes] | |

#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

