# ehelply_python_sdk.MetaApi

All URIs are relative to *https://api.prod.ehelply.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_meta**](MetaApi.md#create_meta) | **POST** /meta/meta/service/{service}/type/{type_name}/entity/{entity_uuid} | Createmeta
[**create_slug**](MetaApi.md#create_slug) | **POST** /meta/slug | Createslug
[**delete_meta**](MetaApi.md#delete_meta) | **DELETE** /meta/meta/{meta_uuid} | Deletemeta
[**delete_meta_from_parts**](MetaApi.md#delete_meta_from_parts) | **DELETE** /meta/meta/service/{service}/type/{type_name}/entity/{entity_uuid} | Deletemetafromparts
[**get_meta**](MetaApi.md#get_meta) | **GET** /meta/meta/{meta_uuid} | Getmeta
[**get_meta_from_parts**](MetaApi.md#get_meta_from_parts) | **GET** /meta/meta/service/{service}/type/{type_name}/entity/{entity_uuid} | Getmetafromparts
[**touch_meta**](MetaApi.md#touch_meta) | **POST** /meta/meta/{meta_uuid}/touch | Touchmeta
[**update_meta**](MetaApi.md#update_meta) | **PUT** /meta/meta/{meta_uuid} | Updatemeta
[**update_meta_from_parts**](MetaApi.md#update_meta_from_parts) | **PUT** /meta/meta/service/{service}/type/{type_name}/entity/{entity_uuid} | Updatemetafromparts


# **create_meta**
> CreateMeta200Response create_meta(service, type_name, entity_uuid, meta_create)

Createmeta

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import meta_api
from ehelply_python_sdk.model.create_meta200_response import CreateMeta200Response
from ehelply_python_sdk.model.meta_create import MetaCreate
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
    api_instance = meta_api.MetaApi(api_client)
    service = "service_example" # str | 
    type_name = "type_name_example" # str | 
    entity_uuid = "entity_uuid_example" # str | 
    meta_create = MetaCreate(
        basic=BasicMetaCreate(
            name="name_example",
            slug=True,
        ),
        detailed=DetailedMetaCreate(
            summary="summary_example",
            description="description_example",
        ),
        custom=MetaCustom(
            name="name_example",
            description="description_example",
            list=[
                CustomList(
                    name="name_example",
                    description="description_example",
                ),
            ],
        ),
        fields=[
            Field(
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
            ),
        ],
        children=[
            MetaChildren(
                child_name="child_name_example",
                child_description="child_description_example",
                child_uuid="child_uuid_example",
            ),
        ],
        parent_uuid="parent_uuid_example",
    ) # MetaCreate | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Createmeta
        api_response = api_instance.create_meta(service, type_name, entity_uuid, meta_create)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->create_meta: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Createmeta
        api_response = api_instance.create_meta(service, type_name, entity_uuid, meta_create, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->create_meta: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **type_name** | **str**|  |
 **entity_uuid** | **str**|  |
 **meta_create** | [**MetaCreate**](MetaCreate.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**CreateMeta200Response**](CreateMeta200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Something went wrong while trying to create a meta |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_slug**
> CreateSlug200Response create_slug(slugger)

Createslug

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import meta_api
from ehelply_python_sdk.model.create_slug200_response import CreateSlug200Response
from ehelply_python_sdk.model.get_appointment403_response import GetAppointment403Response
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.slugger import Slugger
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = meta_api.MetaApi(api_client)
    slugger = Slugger(
        name="name_example",
    ) # Slugger | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Createslug
        api_response = api_instance.create_slug(slugger)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->create_slug: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Createslug
        api_response = api_instance.create_slug(slugger, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->create_slug: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slugger** | [**Slugger**](Slugger.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**CreateSlug200Response**](CreateSlug200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Unable to create slug |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_meta**
> DeleteMeta200Response delete_meta(meta_uuid)

Deletemeta

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import meta_api
from ehelply_python_sdk.model.delete_meta200_response import DeleteMeta200Response
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
    api_instance = meta_api.MetaApi(api_client)
    meta_uuid = "meta_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deletemeta
        api_response = api_instance.delete_meta(meta_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->delete_meta: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deletemeta
        api_response = api_instance.delete_meta(meta_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->delete_meta: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meta_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**DeleteMeta200Response**](DeleteMeta200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Unable to delete meta(s) |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_meta_from_parts**
> DeleteMeta200Response delete_meta_from_parts(service, type_name, entity_uuid)

Deletemetafromparts

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import meta_api
from ehelply_python_sdk.model.delete_meta200_response import DeleteMeta200Response
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
    api_instance = meta_api.MetaApi(api_client)
    service = "service_example" # str | 
    type_name = "type_name_example" # str | 
    entity_uuid = "entity_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deletemetafromparts
        api_response = api_instance.delete_meta_from_parts(service, type_name, entity_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->delete_meta_from_parts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deletemetafromparts
        api_response = api_instance.delete_meta_from_parts(service, type_name, entity_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->delete_meta_from_parts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **type_name** | **str**|  |
 **entity_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**DeleteMeta200Response**](DeleteMeta200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Unable to delete meta(s) |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meta**
> MetaDynamo get_meta(meta_uuid)

Getmeta

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import meta_api
from ehelply_python_sdk.model.meta_dynamo import MetaDynamo
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
    api_instance = meta_api.MetaApi(api_client)
    meta_uuid = "meta_uuid_example" # str | 
    detailed = False # bool |  (optional) if omitted the server will use the default value of False
    custom = False # bool |  (optional) if omitted the server will use the default value of False
    history = 0 # int |  (optional) if omitted the server will use the default value of 0
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Getmeta
        api_response = api_instance.get_meta(meta_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->get_meta: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Getmeta
        api_response = api_instance.get_meta(meta_uuid, detailed=detailed, custom=custom, history=history, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->get_meta: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meta_uuid** | **str**|  |
 **detailed** | **bool**|  | [optional] if omitted the server will use the default value of False
 **custom** | **bool**|  | [optional] if omitted the server will use the default value of False
 **history** | **int**|  | [optional] if omitted the server will use the default value of 0
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**MetaDynamo**](MetaDynamo.md)

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
**404** | meta does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meta_from_parts**
> MetaDynamo get_meta_from_parts(service, type_name, entity_uuid)

Getmetafromparts

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import meta_api
from ehelply_python_sdk.model.meta_dynamo import MetaDynamo
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
    api_instance = meta_api.MetaApi(api_client)
    service = "service_example" # str | 
    type_name = "type_name_example" # str | 
    entity_uuid = "entity_uuid_example" # str | 
    detailed = False # bool |  (optional) if omitted the server will use the default value of False
    custom = False # bool |  (optional) if omitted the server will use the default value of False
    history = 0 # int |  (optional) if omitted the server will use the default value of 0
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Getmetafromparts
        api_response = api_instance.get_meta_from_parts(service, type_name, entity_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->get_meta_from_parts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Getmetafromparts
        api_response = api_instance.get_meta_from_parts(service, type_name, entity_uuid, detailed=detailed, custom=custom, history=history, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->get_meta_from_parts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **type_name** | **str**|  |
 **entity_uuid** | **str**|  |
 **detailed** | **bool**|  | [optional] if omitted the server will use the default value of False
 **custom** | **bool**|  | [optional] if omitted the server will use the default value of False
 **history** | **int**|  | [optional] if omitted the server will use the default value of 0
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**MetaDynamo**](MetaDynamo.md)

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
**404** | meta does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **touch_meta**
> TouchMeta200Response touch_meta(meta_uuid)

Touchmeta

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import meta_api
from ehelply_python_sdk.model.touch_meta200_response import TouchMeta200Response
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
    api_instance = meta_api.MetaApi(api_client)
    meta_uuid = "meta_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Touchmeta
        api_response = api_instance.touch_meta(meta_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->touch_meta: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Touchmeta
        api_response = api_instance.touch_meta(meta_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->touch_meta: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meta_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**TouchMeta200Response**](TouchMeta200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Unable to touch meta(s) |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_meta**
> UpdateMeta200Response update_meta(meta_uuid, meta_create)

Updatemeta

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import meta_api
from ehelply_python_sdk.model.meta_create import MetaCreate
from ehelply_python_sdk.model.update_meta200_response import UpdateMeta200Response
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
    api_instance = meta_api.MetaApi(api_client)
    meta_uuid = "meta_uuid_example" # str | 
    meta_create = MetaCreate(
        basic=BasicMetaCreate(
            name="name_example",
            slug=True,
        ),
        detailed=DetailedMetaCreate(
            summary="summary_example",
            description="description_example",
        ),
        custom=MetaCustom(
            name="name_example",
            description="description_example",
            list=[
                CustomList(
                    name="name_example",
                    description="description_example",
                ),
            ],
        ),
        fields=[
            Field(
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
            ),
        ],
        children=[
            MetaChildren(
                child_name="child_name_example",
                child_description="child_description_example",
                child_uuid="child_uuid_example",
            ),
        ],
        parent_uuid="parent_uuid_example",
    ) # MetaCreate | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updatemeta
        api_response = api_instance.update_meta(meta_uuid, meta_create)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->update_meta: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updatemeta
        api_response = api_instance.update_meta(meta_uuid, meta_create, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->update_meta: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meta_uuid** | **str**|  |
 **meta_create** | [**MetaCreate**](MetaCreate.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**UpdateMeta200Response**](UpdateMeta200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Something went wrong while updating meta |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | meta does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_meta_from_parts**
> UpdateMeta200Response update_meta_from_parts(service, type_name, entity_uuid, meta_create)

Updatemetafromparts

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import meta_api
from ehelply_python_sdk.model.meta_create import MetaCreate
from ehelply_python_sdk.model.update_meta200_response import UpdateMeta200Response
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
    api_instance = meta_api.MetaApi(api_client)
    service = "service_example" # str | 
    type_name = "type_name_example" # str | 
    entity_uuid = "entity_uuid_example" # str | 
    meta_create = MetaCreate(
        basic=BasicMetaCreate(
            name="name_example",
            slug=True,
        ),
        detailed=DetailedMetaCreate(
            summary="summary_example",
            description="description_example",
        ),
        custom=MetaCustom(
            name="name_example",
            description="description_example",
            list=[
                CustomList(
                    name="name_example",
                    description="description_example",
                ),
            ],
        ),
        fields=[
            Field(
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
            ),
        ],
        children=[
            MetaChildren(
                child_name="child_name_example",
                child_description="child_description_example",
                child_uuid="child_uuid_example",
            ),
        ],
        parent_uuid="parent_uuid_example",
    ) # MetaCreate | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updatemetafromparts
        api_response = api_instance.update_meta_from_parts(service, type_name, entity_uuid, meta_create)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->update_meta_from_parts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updatemetafromparts
        api_response = api_instance.update_meta_from_parts(service, type_name, entity_uuid, meta_create, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->update_meta_from_parts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **type_name** | **str**|  |
 **entity_uuid** | **str**|  |
 **meta_create** | [**MetaCreate**](MetaCreate.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**UpdateMeta200Response**](UpdateMeta200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Something went wrong while updating meta |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | meta does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

