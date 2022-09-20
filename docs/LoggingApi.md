# ehelply_python_sdk.LoggingApi

All URIs are relative to *https://api.prod.ehelply.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_subject_logs**](LoggingApi.md#get_subject_logs) | **GET** /sam/logging/logs/services/{service}/subjects/{subject} | Getsubjectlogs


# **get_subject_logs**
> [LoggingDynamo] get_subject_logs(service, subject)

Getsubjectlogs

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import logging_api
from ehelply_python_sdk.model.logging_dynamo import LoggingDynamo
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
    api_instance = logging_api.LoggingApi(api_client)
    service = "service_example" # str | 
    subject = "subject_example" # str | 
    date_start = "date_start_example" # str |  (optional)
    date_end = "date_end_example" # str |  (optional)
    desc = True # bool |  (optional) if omitted the server will use the default value of True
    limit = 50 # int |  (optional) if omitted the server will use the default value of 50
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Getsubjectlogs
        api_response = api_instance.get_subject_logs(service, subject)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling LoggingApi->get_subject_logs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Getsubjectlogs
        api_response = api_instance.get_subject_logs(service, subject, date_start=date_start, date_end=date_end, desc=desc, limit=limit, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling LoggingApi->get_subject_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **subject** | **str**|  |
 **date_start** | **str**|  | [optional]
 **date_end** | **str**|  | [optional]
 **desc** | **bool**|  | [optional] if omitted the server will use the default value of True
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 50
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**[LoggingDynamo]**](LoggingDynamo.md)

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

