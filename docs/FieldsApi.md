# ehelply_python_sdk.FieldsApi

All URIs are relative to *https://api.prod.ehelply.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_field**](FieldsApi.md#create_field) | **POST** /fields/fields | Createfield
[**delete_field**](FieldsApi.md#delete_field) | **DELETE** /fields/fields/{field_uuid} | Deletefield
[**get_field**](FieldsApi.md#get_field) | **GET** /fields/fields/{field_uuid} | Getfield
[**update_field**](FieldsApi.md#update_field) | **PUT** /fields/fields/{field_uuid} | Updatefield


# **create_field**
> CreateField200Response create_field(field)

Createfield

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import fields_api
from ehelply_python_sdk.model.get_appointment403_response import GetAppointment403Response
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.create_field200_response import CreateField200Response
from ehelply_python_sdk.model.field import Field
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fields_api.FieldsApi(api_client)
    field = Field(
        type=1,
        placeholder="placeholder_example",
        validations=Validations(
            value=[
                "value_example",
            ],
        ),
        hint="hint_example",
        icon="icon_example",
        label="label_example",
        options=Options(
            required=True,
            label="label_example",
            inset_label="inset_label_example",
            placeholder="placeholder_example",
            hint="hint_example",
            icon="icon_example",
            max_length=3.14,
            counter=True,
            caption="caption_example",
            color="color_example",
            size="size_example",
            type="type_example",
            icon_position="icon_position_example",
            selections=[
                OptionGroup(
                    name="name_example",
                    type="type_example",
                    selections=[
                        Selection(
                            name="name_example",
                            value=3.14,
                            icon="icon_example",
                        ),
                    ],
                ),
            ],
        ),
    ) # Field | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Createfield
        api_response = api_instance.create_field(field)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling FieldsApi->create_field: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Createfield
        api_response = api_instance.create_field(field, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling FieldsApi->create_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | [**Field**](Field.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**CreateField200Response**](CreateField200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Something went wrong while trying to create a field |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_field**
> DeleteField200Response delete_field(field_uuid)

Deletefield

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import fields_api
from ehelply_python_sdk.model.get_appointment403_response import GetAppointment403Response
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.delete_field200_response import DeleteField200Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fields_api.FieldsApi(api_client)
    field_uuid = "field_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deletefield
        api_response = api_instance.delete_field(field_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling FieldsApi->delete_field: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deletefield
        api_response = api_instance.delete_field(field_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling FieldsApi->delete_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**DeleteField200Response**](DeleteField200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Unable to delete field(s) |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_field**
> FieldDynamo get_field(field_uuid)

Getfield

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import fields_api
from ehelply_python_sdk.model.get_appointment403_response import GetAppointment403Response
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.field_dynamo import FieldDynamo
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fields_api.FieldsApi(api_client)
    field_uuid = "field_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Getfield
        api_response = api_instance.get_field(field_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling FieldsApi->get_field: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Getfield
        api_response = api_instance.get_field(field_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling FieldsApi->get_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**FieldDynamo**](FieldDynamo.md)

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
**404** | field does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_field**
> UpdateField200Response update_field(field_uuid, field)

Updatefield

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import fields_api
from ehelply_python_sdk.model.get_appointment403_response import GetAppointment403Response
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.field import Field
from ehelply_python_sdk.model.update_field200_response import UpdateField200Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fields_api.FieldsApi(api_client)
    field_uuid = "field_uuid_example" # str | 
    field = Field(
        type=1,
        placeholder="placeholder_example",
        validations=Validations(
            value=[
                "value_example",
            ],
        ),
        hint="hint_example",
        icon="icon_example",
        label="label_example",
        options=Options(
            required=True,
            label="label_example",
            inset_label="inset_label_example",
            placeholder="placeholder_example",
            hint="hint_example",
            icon="icon_example",
            max_length=3.14,
            counter=True,
            caption="caption_example",
            color="color_example",
            size="size_example",
            type="type_example",
            icon_position="icon_position_example",
            selections=[
                OptionGroup(
                    name="name_example",
                    type="type_example",
                    selections=[
                        Selection(
                            name="name_example",
                            value=3.14,
                            icon="icon_example",
                        ),
                    ],
                ),
            ],
        ),
    ) # Field | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updatefield
        api_response = api_instance.update_field(field_uuid, field)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling FieldsApi->update_field: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updatefield
        api_response = api_instance.update_field(field_uuid, field, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling FieldsApi->update_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_uuid** | **str**|  |
 **field** | [**Field**](Field.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**UpdateField200Response**](UpdateField200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Something went wrong while updating field |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | field does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

