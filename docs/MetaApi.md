# ehelply_python_sdk.MetaApi

All URIs are relative to *https://api.prod.ehelply.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_meta_from_uuid_meta_meta_meta_uuid_delete**](MetaApi.md#delete_meta_from_uuid_meta_meta_meta_uuid_delete) | **DELETE** /meta/meta/meta/{meta_uuid} | Delete Meta From Uuid
[**delete_meta_meta_meta_service_service_type_type_entity_entity_uuid_delete**](MetaApi.md#delete_meta_meta_meta_service_service_type_type_entity_entity_uuid_delete) | **DELETE** /meta/meta/meta/service/{service}/type/{type}/entity/{entity_uuid} | Delete Meta
[**get_meta_from_uuid_meta_meta_meta_uuid_get**](MetaApi.md#get_meta_from_uuid_meta_meta_meta_uuid_get) | **GET** /meta/meta/meta/{meta_uuid} | Get Meta From Uuid
[**get_meta_meta_meta_service_service_type_type_entity_entity_uuid_get**](MetaApi.md#get_meta_meta_meta_service_service_type_type_entity_entity_uuid_get) | **GET** /meta/meta/meta/service/{service}/type/{type}/entity/{entity_uuid} | Get Meta
[**make_slug_meta_meta_slug_post**](MetaApi.md#make_slug_meta_meta_slug_post) | **POST** /meta/meta/meta/slug | Make Slug
[**post_meta_meta_meta_service_service_type_type_str_entity_entity_uuid_post**](MetaApi.md#post_meta_meta_meta_service_service_type_type_str_entity_entity_uuid_post) | **POST** /meta/meta/meta/service/{service}/type/{type_str}/entity/{entity_uuid} | Post Meta
[**touch_meta_meta_meta_service_service_type_type_entity_entity_uuid_touch_post**](MetaApi.md#touch_meta_meta_meta_service_service_type_type_entity_entity_uuid_touch_post) | **POST** /meta/meta/meta/service/{service}/type/{type}/entity/{entity_uuid}/touch | Touch Meta
[**update_meta_from_uuid_meta_meta_meta_uuid_put**](MetaApi.md#update_meta_from_uuid_meta_meta_meta_uuid_put) | **PUT** /meta/meta/meta/{meta_uuid} | Update Meta From Uuid
[**update_meta_meta_meta_service_service_type_type_entity_entity_uuid_put**](MetaApi.md#update_meta_meta_meta_service_service_type_type_entity_entity_uuid_put) | **PUT** /meta/meta/meta/service/{service}/type/{type}/entity/{entity_uuid} | Update Meta


# **delete_meta_from_uuid_meta_meta_meta_uuid_delete**
> bool, date, datetime, dict, float, int, list, str, none_type delete_meta_from_uuid_meta_meta_meta_uuid_delete(meta_uuid)

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
        api_response = api_instance.delete_meta_from_uuid_meta_meta_meta_uuid_delete(meta_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->delete_meta_from_uuid_meta_meta_meta_uuid_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Meta From Uuid
        api_response = api_instance.delete_meta_from_uuid_meta_meta_meta_uuid_delete(meta_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->delete_meta_from_uuid_meta_meta_meta_uuid_delete: %s\n" % e)
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

# **delete_meta_meta_meta_service_service_type_type_entity_entity_uuid_delete**
> bool, date, datetime, dict, float, int, list, str, none_type delete_meta_meta_meta_service_service_type_type_entity_entity_uuid_delete(service, type, entity_uuid)

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
    type = "type_example" # str | 
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
        api_response = api_instance.delete_meta_meta_meta_service_service_type_type_entity_entity_uuid_delete(service, type, entity_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->delete_meta_meta_meta_service_service_type_type_entity_entity_uuid_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Meta
        api_response = api_instance.delete_meta_meta_meta_service_service_type_type_entity_entity_uuid_delete(service, type, entity_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->delete_meta_meta_meta_service_service_type_type_entity_entity_uuid_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **type** | **str**|  |
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

# **get_meta_from_uuid_meta_meta_meta_uuid_get**
> bool, date, datetime, dict, float, int, list, str, none_type get_meta_from_uuid_meta_meta_meta_uuid_get(meta_uuid)

Get Meta From Uuid

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
        api_response = api_instance.get_meta_from_uuid_meta_meta_meta_uuid_get(meta_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->get_meta_from_uuid_meta_meta_meta_uuid_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Meta From Uuid
        api_response = api_instance.get_meta_from_uuid_meta_meta_meta_uuid_get(meta_uuid, detailed=detailed, custom=custom, dates=dates, history=history, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->get_meta_from_uuid_meta_meta_meta_uuid_get: %s\n" % e)
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

# **get_meta_meta_meta_service_service_type_type_entity_entity_uuid_get**
> bool, date, datetime, dict, float, int, list, str, none_type get_meta_meta_meta_service_service_type_type_entity_entity_uuid_get(service, type, entity_uuid)

Get Meta

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
    type = "type_example" # str | 
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
        api_response = api_instance.get_meta_meta_meta_service_service_type_type_entity_entity_uuid_get(service, type, entity_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->get_meta_meta_meta_service_service_type_type_entity_entity_uuid_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Meta
        api_response = api_instance.get_meta_meta_meta_service_service_type_type_entity_entity_uuid_get(service, type, entity_uuid, detailed=detailed, custom=custom, dates=dates, history=history, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->get_meta_meta_meta_service_service_type_type_entity_entity_uuid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **type** | **str**|  |
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

# **make_slug_meta_meta_slug_post**
> bool, date, datetime, dict, float, int, list, str, none_type make_slug_meta_meta_slug_post(meta_slugger)

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
        api_response = api_instance.make_slug_meta_meta_slug_post(meta_slugger)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->make_slug_meta_meta_slug_post: %s\n" % e)
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

# **post_meta_meta_meta_service_service_type_type_str_entity_entity_uuid_post**
> MetaDynamo post_meta_meta_meta_service_service_type_type_str_entity_entity_uuid_post(service, type_str, entity_uuid, body_post_meta_meta_meta_service_service_type_type_str_entity_entity_uuid_post)

Post Meta

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import meta_api
from ehelply_python_sdk.model.meta_dynamo import MetaDynamo
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.body_post_meta_meta_meta_service_service_type_type_str_entity_entity_uuid_post import BodyPostMetaMetaMetaServiceServiceTypeTypeStrEntityEntityUuidPost
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
    body_post_meta_meta_meta_service_service_type_type_str_entity_entity_uuid_post = BodyPostMetaMetaMetaServiceServiceTypeTypeStrEntityEntityUuidPost(
        meta=MetaCreate(
            basic=BasicMetaCreate(
                name="name_example",
                slug=True,
            ),
            detailed=DetailedMetaCreate(
                summary="summary_example",
                description="description_example",
            ),
            custom={},
        ),
    ) # BodyPostMetaMetaMetaServiceServiceTypeTypeStrEntityEntityUuidPost | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Post Meta
        api_response = api_instance.post_meta_meta_meta_service_service_type_type_str_entity_entity_uuid_post(service, type_str, entity_uuid, body_post_meta_meta_meta_service_service_type_type_str_entity_entity_uuid_post)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->post_meta_meta_meta_service_service_type_type_str_entity_entity_uuid_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Post Meta
        api_response = api_instance.post_meta_meta_meta_service_service_type_type_str_entity_entity_uuid_post(service, type_str, entity_uuid, body_post_meta_meta_meta_service_service_type_type_str_entity_entity_uuid_post, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->post_meta_meta_meta_service_service_type_type_str_entity_entity_uuid_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **type_str** | **str**|  |
 **entity_uuid** | **str**|  |
 **body_post_meta_meta_meta_service_service_type_type_str_entity_entity_uuid_post** | [**BodyPostMetaMetaMetaServiceServiceTypeTypeStrEntityEntityUuidPost**](BodyPostMetaMetaMetaServiceServiceTypeTypeStrEntityEntityUuidPost.md)|  |
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

# **touch_meta_meta_meta_service_service_type_type_entity_entity_uuid_touch_post**
> MetaDynamo touch_meta_meta_meta_service_service_type_type_entity_entity_uuid_touch_post(service, type, entity_uuid)

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
    type = "type_example" # str | 
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
        api_response = api_instance.touch_meta_meta_meta_service_service_type_type_entity_entity_uuid_touch_post(service, type, entity_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->touch_meta_meta_meta_service_service_type_type_entity_entity_uuid_touch_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Touch Meta
        api_response = api_instance.touch_meta_meta_meta_service_service_type_type_entity_entity_uuid_touch_post(service, type, entity_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->touch_meta_meta_meta_service_service_type_type_entity_entity_uuid_touch_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **type** | **str**|  |
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

# **update_meta_from_uuid_meta_meta_meta_uuid_put**
> MetaDynamo update_meta_from_uuid_meta_meta_meta_uuid_put(meta_uuid, body_update_meta_from_uuid_meta_meta_meta_uuid_put)

Update Meta From Uuid

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import meta_api
from ehelply_python_sdk.model.meta_dynamo import MetaDynamo
from ehelply_python_sdk.model.body_update_meta_from_uuid_meta_meta_meta_uuid_put import BodyUpdateMetaFromUuidMetaMetaMetaUuidPut
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
    body_update_meta_from_uuid_meta_meta_meta_uuid_put = BodyUpdateMetaFromUuidMetaMetaMetaUuidPut(
        meta=MetaCreate(
            basic=BasicMetaCreate(
                name="name_example",
                slug=True,
            ),
            detailed=DetailedMetaCreate(
                summary="summary_example",
                description="description_example",
            ),
            custom={},
        ),
    ) # BodyUpdateMetaFromUuidMetaMetaMetaUuidPut | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Meta From Uuid
        api_response = api_instance.update_meta_from_uuid_meta_meta_meta_uuid_put(meta_uuid, body_update_meta_from_uuid_meta_meta_meta_uuid_put)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->update_meta_from_uuid_meta_meta_meta_uuid_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Meta From Uuid
        api_response = api_instance.update_meta_from_uuid_meta_meta_meta_uuid_put(meta_uuid, body_update_meta_from_uuid_meta_meta_meta_uuid_put, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->update_meta_from_uuid_meta_meta_meta_uuid_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meta_uuid** | **str**|  |
 **body_update_meta_from_uuid_meta_meta_meta_uuid_put** | [**BodyUpdateMetaFromUuidMetaMetaMetaUuidPut**](BodyUpdateMetaFromUuidMetaMetaMetaUuidPut.md)|  |
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

# **update_meta_meta_meta_service_service_type_type_entity_entity_uuid_put**
> MetaDynamo update_meta_meta_meta_service_service_type_type_entity_entity_uuid_put(service, type, entity_uuid, body_update_meta_meta_meta_service_service_type_type_entity_entity_uuid_put)

Update Meta

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import meta_api
from ehelply_python_sdk.model.meta_dynamo import MetaDynamo
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.body_update_meta_meta_meta_service_service_type_type_entity_entity_uuid_put import BodyUpdateMetaMetaMetaServiceServiceTypeTypeEntityEntityUuidPut
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
    type = "type_example" # str | 
    entity_uuid = "entity_uuid_example" # str | 
    body_update_meta_meta_meta_service_service_type_type_entity_entity_uuid_put = BodyUpdateMetaMetaMetaServiceServiceTypeTypeEntityEntityUuidPut(
        meta=MetaCreate(
            basic=BasicMetaCreate(
                name="name_example",
                slug=True,
            ),
            detailed=DetailedMetaCreate(
                summary="summary_example",
                description="description_example",
            ),
            custom={},
        ),
    ) # BodyUpdateMetaMetaMetaServiceServiceTypeTypeEntityEntityUuidPut | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Meta
        api_response = api_instance.update_meta_meta_meta_service_service_type_type_entity_entity_uuid_put(service, type, entity_uuid, body_update_meta_meta_meta_service_service_type_type_entity_entity_uuid_put)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->update_meta_meta_meta_service_service_type_type_entity_entity_uuid_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Meta
        api_response = api_instance.update_meta_meta_meta_service_service_type_type_entity_entity_uuid_put(service, type, entity_uuid, body_update_meta_meta_meta_service_service_type_type_entity_entity_uuid_put, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling MetaApi->update_meta_meta_meta_service_service_type_type_entity_entity_uuid_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | **str**|  |
 **type** | **str**|  |
 **entity_uuid** | **str**|  |
 **body_update_meta_meta_meta_service_service_type_type_entity_entity_uuid_put** | [**BodyUpdateMetaMetaMetaServiceServiceTypeTypeEntityEntityUuidPut**](BodyUpdateMetaMetaMetaServiceServiceTypeTypeEntityEntityUuidPut.md)|  |
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

