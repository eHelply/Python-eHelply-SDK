# ehelply_python_sdk.PlacesApi

All URIs are relative to *https://api.prod.ehelply.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_place_places_places_post**](PlacesApi.md#create_place_places_places_post) | **POST** /places/places | Create Place
[**delete_place_places_places_place_uuid_delete**](PlacesApi.md#delete_place_places_places_place_uuid_delete) | **DELETE** /places/places/{place_uuid} | Delete Place
[**forward_geocoding_places_places_geocoding_forward_get**](PlacesApi.md#forward_geocoding_places_places_geocoding_forward_get) | **GET** /places/places/geocoding/forward | Forward Geocoding
[**get_place_places_places_place_uuid_get**](PlacesApi.md#get_place_places_places_place_uuid_get) | **GET** /places/places/{place_uuid} | Get Place
[**reverse_geocoding_places_places_geocoding_reverse_get**](PlacesApi.md#reverse_geocoding_places_places_geocoding_reverse_get) | **GET** /places/places/geocoding/reverse | Reverse Geocoding
[**search_places_by_search_string_places_places_search_string_get**](PlacesApi.md#search_places_by_search_string_places_places_search_string_get) | **GET** /places/places/search/string | Search Places By Search String
[**search_places_places_places_get**](PlacesApi.md#search_places_places_places_get) | **GET** /places/places | Search Places
[**update_place_places_places_place_uuid_put**](PlacesApi.md#update_place_places_places_place_uuid_put) | **PUT** /places/places/{place_uuid} | Update Place


# **create_place_places_places_post**
> PlaceResponse create_place_places_places_post(place_base)

Create Place

Creates a Place.

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import places_api
from ehelply_python_sdk.model.place_base import PlaceBase
from ehelply_python_sdk.model.place_response import PlaceResponse
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
    api_instance = places_api.PlacesApi(api_client)
    place_base = PlaceBase(
        name="Example Clinic",
        summary="Summary of the clinic",
        public=True,
        meta={},
        addresses=[
            AddressBase(
                address_type="Mailing",
                address_line_1="1234 Street Name",
                address_line_2="Unit #2",
                postal_zip_code="123 456",
                city="city name",
                province_state="province",
                country="Canada",
                lat="123",
                lng="-123",
            ),
        ],
        contact=ContactBase(
            phones={},
            email="test@example.com",
            website="www.ehelply.com",
            socials={},
        ),
    ) # PlaceBase | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Place
        api_response = api_instance.create_place_places_places_post(place_base)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling PlacesApi->create_place_places_places_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Place
        api_response = api_instance.create_place_places_places_post(place_base, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling PlacesApi->create_place_places_places_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **place_base** | [**PlaceBase**](PlaceBase.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**PlaceResponse**](PlaceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Route not found - Denied by eHelply |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_place_places_places_place_uuid_delete**
> bool, date, datetime, dict, float, int, list, str, none_type delete_place_places_places_place_uuid_delete(place_uuid)

Delete Place

Deletes the place with the given ID and returns True if successful

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import places_api
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
    api_instance = places_api.PlacesApi(api_client)
    place_uuid = "place_uuid_example" # str | 
    soft_delete = True # bool |  (optional) if omitted the server will use the default value of True
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete Place
        api_response = api_instance.delete_place_places_places_place_uuid_delete(place_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling PlacesApi->delete_place_places_places_place_uuid_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Place
        api_response = api_instance.delete_place_places_places_place_uuid_delete(place_uuid, soft_delete=soft_delete, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling PlacesApi->delete_place_places_places_place_uuid_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **place_uuid** | **str**|  |
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
**404** | Route not found - Denied by eHelply |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forward_geocoding_places_places_geocoding_forward_get**
> bool, date, datetime, dict, float, int, list, str, none_type forward_geocoding_places_places_geocoding_forward_get(searching_place)

Forward Geocoding

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import places_api
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
    api_instance = places_api.PlacesApi(api_client)
    searching_place = "searching_place_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Forward Geocoding
        api_response = api_instance.forward_geocoding_places_places_geocoding_forward_get(searching_place)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling PlacesApi->forward_geocoding_places_places_geocoding_forward_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Forward Geocoding
        api_response = api_instance.forward_geocoding_places_places_geocoding_forward_get(searching_place, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling PlacesApi->forward_geocoding_places_places_geocoding_forward_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searching_place** | **str**|  |
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
**404** | Route not found - Denied by eHelply |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_place_places_places_place_uuid_get**
> PlaceResponse get_place_places_places_place_uuid_get(place_uuid)

Get Place

Gets the place information given the Place ID

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import places_api
from ehelply_python_sdk.model.place_response import PlaceResponse
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
    api_instance = places_api.PlacesApi(api_client)
    place_uuid = "place_uuid_example" # str | 
    with_meta = False # bool |  (optional) if omitted the server will use the default value of False
    with_catalog = False # bool |  (optional) if omitted the server will use the default value of False
    with_reviews = False # bool |  (optional) if omitted the server will use the default value of False
    with_schedule = False # bool |  (optional) if omitted the server will use the default value of False
    with_collection = False # bool |  (optional) if omitted the server will use the default value of False
    with_blog = False # bool |  (optional) if omitted the server will use the default value of False
    with_tags = False # bool |  (optional) if omitted the server will use the default value of False
    with_categories = False # bool |  (optional) if omitted the server will use the default value of False
    with_company = False # bool |  (optional) if omitted the server will use the default value of False
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Place
        api_response = api_instance.get_place_places_places_place_uuid_get(place_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling PlacesApi->get_place_places_places_place_uuid_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Place
        api_response = api_instance.get_place_places_places_place_uuid_get(place_uuid, with_meta=with_meta, with_catalog=with_catalog, with_reviews=with_reviews, with_schedule=with_schedule, with_collection=with_collection, with_blog=with_blog, with_tags=with_tags, with_categories=with_categories, with_company=with_company, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling PlacesApi->get_place_places_places_place_uuid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **place_uuid** | **str**|  |
 **with_meta** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_catalog** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_reviews** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_schedule** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_collection** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_blog** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_tags** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_categories** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_company** | **bool**|  | [optional] if omitted the server will use the default value of False
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**PlaceResponse**](PlaceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Route not found - Denied by eHelply |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reverse_geocoding_places_places_geocoding_reverse_get**
> bool, date, datetime, dict, float, int, list, str, none_type reverse_geocoding_places_places_geocoding_reverse_get(long, lat)

Reverse Geocoding

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import places_api
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
    api_instance = places_api.PlacesApi(api_client)
    long = 3.14 # float | 
    lat = 3.14 # float | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Reverse Geocoding
        api_response = api_instance.reverse_geocoding_places_places_geocoding_reverse_get(long, lat)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling PlacesApi->reverse_geocoding_places_places_geocoding_reverse_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Reverse Geocoding
        api_response = api_instance.reverse_geocoding_places_places_geocoding_reverse_get(long, lat, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling PlacesApi->reverse_geocoding_places_places_geocoding_reverse_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **long** | **float**|  |
 **lat** | **float**|  |
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
**404** | Route not found - Denied by eHelply |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_places_by_search_string_places_places_search_string_get**
> Page search_places_by_search_string_places_places_search_string_get()

Search Places By Search String

Search places by a search string

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import places_api
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
    api_instance = places_api.PlacesApi(api_client)
    search_string = "" # str |  (optional) if omitted the server will use the default value of ""
    page = 1 # int |  (optional) if omitted the server will use the default value of 1
    page_size = 25 # int |  (optional) if omitted the server will use the default value of 25
    sort_on = "sort_on_example" # str |  (optional)
    sort_desc = False # bool |  (optional) if omitted the server will use the default value of False
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Places By Search String
        api_response = api_instance.search_places_by_search_string_places_places_search_string_get(search_string=search_string, page=page, page_size=page_size, sort_on=sort_on, sort_desc=sort_desc, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling PlacesApi->search_places_by_search_string_places_places_search_string_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_string** | **str**|  | [optional] if omitted the server will use the default value of ""
 **page** | **int**|  | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 25
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
**404** | Route not found - Denied by eHelply |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_places_places_places_get**
> Page search_places_places_places_get()

Search Places

Search all places and returns paginated results with Places being stored in items field. Can search by `project_uuid, name, address, address_line_2, city, province_state, country, postal_zip_code, lat, lng email` string fields or the `is_public and is_deleted` boolean fields. To search with these fields use query params with string values. For sorting fill out \"sort_desc\" field with either true/false and the \"sort_on\" query parameter with column you want to sort on (ex: name). Max pagination items per page is 50. Item return format: ``` {     uuid                                **type:** string     project_uuid                        **type:** string or None      meta_uuid                           **type:** string or None      catalog_data                        **type:** dict or None      review_group_data                   **type:** dict or None      schedule_data                       **type:** dict or None      collection_data                     **type:** dict or None      blog_data                           **type:** dict or None      tags                                **type:** [TagBase] or None      categories                          **type:** [CategoryBase] or None      company                             **type:** CompanyBase or None      created_at                          **type:** string or None      updated_at                          **type:** string or None      deleted_at                          **type:** string or None  } ```

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import places_api
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
    api_instance = places_api.PlacesApi(api_client)
    project_uuid = "project_uuid_example" # str |  (optional)
    name = "name_example" # str |  (optional)
    address_line_1 = "address_line_1_example" # str |  (optional)
    address_line_2 = "address_line_2_example" # str |  (optional)
    city = "city_example" # str |  (optional)
    province_state = "province_state_example" # str |  (optional)
    country = "country_example" # str |  (optional)
    postal_zip_code = "postal_zip_code_example" # str |  (optional)
    lat = "lat_example" # str |  (optional)
    lng = "lng_example" # str |  (optional)
    email = "email_example" # str |  (optional)
    is_public = True # bool |  (optional) if omitted the server will use the default value of True
    is_deleted = False # bool |  (optional) if omitted the server will use the default value of False
    with_company = False # bool |  (optional) if omitted the server will use the default value of False
    with_meta = False # bool |  (optional) if omitted the server will use the default value of False
    with_catalog = False # bool |  (optional) if omitted the server will use the default value of False
    with_reviews = False # bool |  (optional) if omitted the server will use the default value of False
    with_schedule = False # bool |  (optional) if omitted the server will use the default value of False
    with_collection = False # bool |  (optional) if omitted the server will use the default value of False
    with_blog = False # bool |  (optional) if omitted the server will use the default value of False
    with_tags = False # bool |  (optional) if omitted the server will use the default value of False
    with_categories = False # bool |  (optional) if omitted the server will use the default value of False
    page = 1 # int |  (optional) if omitted the server will use the default value of 1
    page_size = 25 # int |  (optional) if omitted the server will use the default value of 25
    sort_on = "sort_on_example" # str |  (optional)
    sort_desc = False # bool |  (optional) if omitted the server will use the default value of False
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Places
        api_response = api_instance.search_places_places_places_get(project_uuid=project_uuid, name=name, address_line_1=address_line_1, address_line_2=address_line_2, city=city, province_state=province_state, country=country, postal_zip_code=postal_zip_code, lat=lat, lng=lng, email=email, is_public=is_public, is_deleted=is_deleted, with_company=with_company, with_meta=with_meta, with_catalog=with_catalog, with_reviews=with_reviews, with_schedule=with_schedule, with_collection=with_collection, with_blog=with_blog, with_tags=with_tags, with_categories=with_categories, page=page, page_size=page_size, sort_on=sort_on, sort_desc=sort_desc, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling PlacesApi->search_places_places_places_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**|  | [optional]
 **name** | **str**|  | [optional]
 **address_line_1** | **str**|  | [optional]
 **address_line_2** | **str**|  | [optional]
 **city** | **str**|  | [optional]
 **province_state** | **str**|  | [optional]
 **country** | **str**|  | [optional]
 **postal_zip_code** | **str**|  | [optional]
 **lat** | **str**|  | [optional]
 **lng** | **str**|  | [optional]
 **email** | **str**|  | [optional]
 **is_public** | **bool**|  | [optional] if omitted the server will use the default value of True
 **is_deleted** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_company** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_meta** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_catalog** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_reviews** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_schedule** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_collection** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_blog** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_tags** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_categories** | **bool**|  | [optional] if omitted the server will use the default value of False
 **page** | **int**|  | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 25
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
**404** | Route not found - Denied by eHelply |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_place_places_places_place_uuid_put**
> PlaceResponse update_place_places_places_place_uuid_put(place_uuid, place_base)

Update Place

Update Place with given info, only updating the fields supplied. Place Uuid must be sent however.

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import places_api
from ehelply_python_sdk.model.place_base import PlaceBase
from ehelply_python_sdk.model.place_response import PlaceResponse
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
    api_instance = places_api.PlacesApi(api_client)
    place_uuid = "place_uuid_example" # str | 
    place_base = PlaceBase(
        name="Example Clinic",
        summary="Summary of the clinic",
        public=True,
        meta={},
        addresses=[
            AddressBase(
                address_type="Mailing",
                address_line_1="1234 Street Name",
                address_line_2="Unit #2",
                postal_zip_code="123 456",
                city="city name",
                province_state="province",
                country="Canada",
                lat="123",
                lng="-123",
            ),
        ],
        contact=ContactBase(
            phones={},
            email="test@example.com",
            website="www.ehelply.com",
            socials={},
        ),
    ) # PlaceBase | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Place
        api_response = api_instance.update_place_places_places_place_uuid_put(place_uuid, place_base)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling PlacesApi->update_place_places_places_place_uuid_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Place
        api_response = api_instance.update_place_places_places_place_uuid_put(place_uuid, place_base, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling PlacesApi->update_place_places_places_place_uuid_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **place_uuid** | **str**|  |
 **place_base** | [**PlaceBase**](PlaceBase.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**PlaceResponse**](PlaceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Route not found - Denied by eHelply |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

