# ehelply_python_sdk.MetaApi

All URIs are relative to *https://api.prod.ehelply.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_field**](MetaApi.md#create_field) | **POST** /meta/field | Create Field
[**create_meta**](MetaApi.md#create_meta) | **POST** /meta/meta/service/{service}/type/{type_str}/entity/{entity_uuid} | Create Meta
[**delete_field**](MetaApi.md#delete_field) | **DELETE** /meta/field/{field_uuid} | Delete Field
[**delete_meta**](MetaApi.md#delete_meta) | **DELETE** /meta/meta/service/{service}/type/{type_str}/entity/{entity_uuid} | Delete Meta
[**delete_meta_from_uuid**](MetaApi.md#delete_meta_from_uuid) | **DELETE** /meta/meta/{meta_uuid} | Delete Meta From Uuid
[**get_field**](MetaApi.md#get_field) | **GET** /meta/field/{field_uuid} | Get Field
[**get_meta**](MetaApi.md#get_meta) | **GET** /meta/meta/service/{service}/type/{type_str}/entity/{entity_uuid} | Get Meta
[**get_meta_from_uuid**](MetaApi.md#get_meta_from_uuid) | **GET** /meta/meta/{meta_uuid} | Get Meta From Uuid
[**make_slug**](MetaApi.md#make_slug) | **POST** /meta/meta/slug | Make Slug
[**touch_meta**](MetaApi.md#touch_meta) | **POST** /meta/meta/service/{service}/type/{type_str}/entity/{entity_uuid}/touch | Touch Meta
[**update_field**](MetaApi.md#update_field) | **PUT** /meta/field/{field_uuid} | Update Field
[**update_meta**](MetaApi.md#update_meta) | **PUT** /meta/meta/service/{service}/type/{type_str}/entity/{entity_uuid} | Update Meta
[**update_meta_from_uuid**](MetaApi.md#update_meta_from_uuid) | **PUT** /meta/meta/{meta_uuid} | Update Meta From Uuid


# **create_field**
> FieldDynamo create_field(field)

Create Field

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import meta_api
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.field import Field
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
    api_instance = meta_api.MetaApi(api_client)
    field = Field(
        uuid="uuid_example",
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
        # Create Field
        api_response = api_instance.create_field(field)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->create_field: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Field
        api_response = api_instance.create_field(field, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->create_field: %s\n" % e)
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

[**FieldDynamo**](FieldDynamo.md)

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

# **create_meta**
> MetaDynamo create_meta(service, type_str, entity_uuid, meta_create)

Create Meta

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import meta_api
from ehelply_python_sdk.model.meta_create import MetaCreate
from ehelply_python_sdk.model.meta_dynamo import MetaDynamo
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
    type_str = "type_str_example" # str | 
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
                uuid="uuid_example",
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
        # Create Meta
        api_response = api_instance.create_meta(service, type_str, entity_uuid, meta_create)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->create_meta: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Meta
        api_response = api_instance.create_meta(service, type_str, entity_uuid, meta_create, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->create_meta: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **type_str** | **str**|  |
 **entity_uuid** | **str**|  |
 **meta_create** | [**MetaCreate**](MetaCreate.md)|  |
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

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_field**
> bool, date, datetime, dict, float, int, list, str, none_type delete_field(field_uuid)

Delete Field

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import meta_api
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
    field_uuid = "field_uuid_example" # str | 
    soft_delete = True # bool |  (optional) if omitted the server will use the default value of True
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete Field
        api_response = api_instance.delete_field(field_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->delete_field: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Field
        api_response = api_instance.delete_field(field_uuid, soft_delete=soft_delete, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->delete_field: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_uuid** | **str**|  |
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
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_meta**
> bool, date, datetime, dict, float, int, list, str, none_type delete_meta(service, type_str, entity_uuid)

Delete Meta

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import meta_api
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
    type_str = "type_str_example" # str | 
    entity_uuid = "entity_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete Meta
        api_response = api_instance.delete_meta(service, type_str, entity_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->delete_meta: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Meta
        api_response = api_instance.delete_meta(service, type_str, entity_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->delete_meta: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **type_str** | **str**|  |
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
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_meta_from_uuid**
> bool, date, datetime, dict, float, int, list, str, none_type delete_meta_from_uuid(meta_uuid)

Delete Meta From Uuid

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import meta_api
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
        # Delete Meta From Uuid
        api_response = api_instance.delete_meta_from_uuid(meta_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->delete_meta_from_uuid: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Meta From Uuid
        api_response = api_instance.delete_meta_from_uuid(meta_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->delete_meta_from_uuid: %s\n" % e)
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

# **get_field**
> FieldDynamo get_field(field_uuid)

Get Field

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import meta_api
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
    api_instance = meta_api.MetaApi(api_client)
    field_uuid = "field_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Field
        api_response = api_instance.get_field(field_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->get_field: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Field
        api_response = api_instance.get_field(field_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->get_field: %s\n" % e)
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
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meta**
> MetaDynamo get_meta(service, type_str, entity_uuid)

Get Meta

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import meta_api
from ehelply_python_sdk.model.meta_dynamo import MetaDynamo
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
    type_str = "type_str_example" # str | 
    entity_uuid = "entity_uuid_example" # str | 
    detailed = False # bool |  (optional) if omitted the server will use the default value of False
    custom = False # bool |  (optional) if omitted the server will use the default value of False
    dates = False # bool |  (optional) if omitted the server will use the default value of False
    history = 0 # int |  (optional) if omitted the server will use the default value of 0
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Meta
        api_response = api_instance.get_meta(service, type_str, entity_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->get_meta: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Meta
        api_response = api_instance.get_meta(service, type_str, entity_uuid, detailed=detailed, custom=custom, dates=dates, history=history, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->get_meta: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **type_str** | **str**|  |
 **entity_uuid** | **str**|  |
 **detailed** | **bool**|  | [optional] if omitted the server will use the default value of False
 **custom** | **bool**|  | [optional] if omitted the server will use the default value of False
 **dates** | **bool**|  | [optional] if omitted the server will use the default value of False
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
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meta_from_uuid**
> MetaDynamo get_meta_from_uuid(meta_uuid)

Get Meta From Uuid

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import meta_api
from ehelply_python_sdk.model.meta_dynamo import MetaDynamo
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
    dates = False # bool |  (optional) if omitted the server will use the default value of False
    history = 0 # int |  (optional) if omitted the server will use the default value of 0
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Meta From Uuid
        api_response = api_instance.get_meta_from_uuid(meta_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->get_meta_from_uuid: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Meta From Uuid
        api_response = api_instance.get_meta_from_uuid(meta_uuid, detailed=detailed, custom=custom, dates=dates, history=history, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->get_meta_from_uuid: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meta_uuid** | **str**|  |
 **detailed** | **bool**|  | [optional] if omitted the server will use the default value of False
 **custom** | **bool**|  | [optional] if omitted the server will use the default value of False
 **dates** | **bool**|  | [optional] if omitted the server will use the default value of False
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
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **make_slug**
> bool, date, datetime, dict, float, int, list, str, none_type make_slug(meta_slugger)

Make Slug

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import meta_api
from ehelply_python_sdk.model.meta_slugger import MetaSlugger
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
    meta_slugger = MetaSlugger(
        name="name_example",
    ) # MetaSlugger | 

    # example passing only required values which don't have defaults set
    try:
        # Make Slug
        api_response = api_instance.make_slug(meta_slugger)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->make_slug: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meta_slugger** | [**MetaSlugger**](MetaSlugger.md)|  |

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

# **touch_meta**
> MetaDynamo touch_meta(service, type_str, entity_uuid)

Touch Meta

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import meta_api
from ehelply_python_sdk.model.meta_dynamo import MetaDynamo
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
    type_str = "type_str_example" # str | 
    entity_uuid = "entity_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Touch Meta
        api_response = api_instance.touch_meta(service, type_str, entity_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->touch_meta: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Touch Meta
        api_response = api_instance.touch_meta(service, type_str, entity_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->touch_meta: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **type_str** | **str**|  |
 **entity_uuid** | **str**|  |
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
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_field**
> bool, date, datetime, dict, float, int, list, str, none_type update_field(field_uuid, field)

Update Field

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import meta_api
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
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
    api_instance = meta_api.MetaApi(api_client)
    field_uuid = "field_uuid_example" # str | 
    field = Field(
        uuid="uuid_example",
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
        # Update Field
        api_response = api_instance.update_field(field_uuid, field)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->update_field: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Field
        api_response = api_instance.update_field(field_uuid, field, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->update_field: %s\n" % e)
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

# **update_meta**
> MetaDynamo update_meta(service, type_str, entity_uuid, meta_create)

Update Meta

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import meta_api
from ehelply_python_sdk.model.meta_create import MetaCreate
from ehelply_python_sdk.model.meta_dynamo import MetaDynamo
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
    type_str = "type_str_example" # str | 
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
                uuid="uuid_example",
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
        # Update Meta
        api_response = api_instance.update_meta(service, type_str, entity_uuid, meta_create)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->update_meta: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Meta
        api_response = api_instance.update_meta(service, type_str, entity_uuid, meta_create, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->update_meta: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **type_str** | **str**|  |
 **entity_uuid** | **str**|  |
 **meta_create** | [**MetaCreate**](MetaCreate.md)|  |
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

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_meta_from_uuid**
> MetaDynamo update_meta_from_uuid(meta_uuid, meta_create)

Update Meta From Uuid

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import meta_api
from ehelply_python_sdk.model.meta_create import MetaCreate
from ehelply_python_sdk.model.meta_dynamo import MetaDynamo
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
                uuid="uuid_example",
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
        # Update Meta From Uuid
        api_response = api_instance.update_meta_from_uuid(meta_uuid, meta_create)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->update_meta_from_uuid: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Meta From Uuid
        api_response = api_instance.update_meta_from_uuid(meta_uuid, meta_create, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->update_meta_from_uuid: %s\n" % e)
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

[**MetaDynamo**](MetaDynamo.md)

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

