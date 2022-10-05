# ehelply_python_sdk.DefaultApi

All URIs are relative to *https://api.prod.ehelply.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_file**](DefaultApi.md#create_file) | **POST** /files/files | Createfile
[**delete_file**](DefaultApi.md#delete_file) | **DELETE** /files/files/{file_uuid} | Deletefile
[**get_file**](DefaultApi.md#get_file) | **GET** /files/files/{file_uuid} | Getfile
[**update_file**](DefaultApi.md#update_file) | **PUT** /files/files/{file_uuid} | Updatefile


# **create_file**
> CreateFile200Response create_file(file)

Createfile

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import default_api
from ehelply_python_sdk.model.get_appointment403_response import GetAppointment403Response
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.create_file200_response import CreateFile200Response
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
    file = open('/path/to/file', 'rb') # file_type | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Createfile
        api_response = api_instance.create_file(file)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling DefaultApi->create_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Createfile
        api_response = api_instance.create_file(file, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling DefaultApi->create_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file_type**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**CreateFile200Response**](CreateFile200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Cannot create SuperStack internal file |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> DeleteFile200Response delete_file(file_uuid)

Deletefile

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import default_api
from ehelply_python_sdk.model.get_appointment403_response import GetAppointment403Response
from ehelply_python_sdk.model.delete_file200_response import DeleteFile200Response
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
    file_uuid = "file_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deletefile
        api_response = api_instance.delete_file(file_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling DefaultApi->delete_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deletefile
        api_response = api_instance.delete_file(file_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling DefaultApi->delete_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**DeleteFile200Response**](DeleteFile200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Cannot delete SuperStack internal file |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> file_type get_file(file_uuid)

Getfile

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)
    file_uuid = "file_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Getfile
        api_response = api_instance.get_file(file_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Getfile
        api_response = api_instance.get_file(file_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling DefaultApi->get_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

**file_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Cannot get SuperStack internal file |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file**
> UpdateFile200Response update_file(file_uuid, file)

Updatefile

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import default_api
from ehelply_python_sdk.model.get_appointment403_response import GetAppointment403Response
from ehelply_python_sdk.model.update_file200_response import UpdateFile200Response
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
    file_uuid = "file_uuid_example" # str | 
    file = open('/path/to/file', 'rb') # file_type | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updatefile
        api_response = api_instance.update_file(file_uuid, file)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling DefaultApi->update_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updatefile
        api_response = api_instance.update_file(file_uuid, file, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling DefaultApi->update_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_uuid** | **str**|  |
 **file** | **file_type**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**UpdateFile200Response**](UpdateFile200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Cannot update SuperStack internal file |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

