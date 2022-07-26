# ehelply_python_sdk.ReviewsApi

All URIs are relative to *https://api.prod.ehelply.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_review**](ReviewsApi.md#create_review) | **POST** /products/reviews/types/{entity_type}/entities/{entity_uuid} | Create
[**delete_review**](ReviewsApi.md#delete_review) | **DELETE** /products/reviews/types/{entity_type}/entities/{entity_uuid}/reviews/{review_uuid} | Deletereview
[**get_review**](ReviewsApi.md#get_review) | **GET** /products/reviews/types/{entity_type}/entities/{entity_uuid}/reviews/{review_uuid} | Getreview
[**search_reviews**](ReviewsApi.md#search_reviews) | **GET** /products/reviews/types/{entity_type}/entities/{entity_uuid} | Searchreview
[**update_review**](ReviewsApi.md#update_review) | **PUT** /products/reviews/types/{entity_type}/entities/{entity_uuid}/reviews/{review_uuid} | Updatereview


# **create_review**
> bool, date, datetime, dict, float, int, list, str, none_type create_review(entity_type, entity_uuid, create_review)

Create

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import reviews_api
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.create_review import CreateReview
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = reviews_api.ReviewsApi(api_client)
    entity_type = "entity_type_example" # str | 
    entity_uuid = "entity_uuid_example" # str | 
    create_review = CreateReview(
        rating=1,
        max_rating=1,
        review_text="review_text_example",
    ) # CreateReview | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create
        api_response = api_instance.create_review(entity_type, entity_uuid, create_review)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ReviewsApi->create_review: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create
        api_response = api_instance.create_review(entity_type, entity_uuid, create_review, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ReviewsApi->create_review: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**|  |
 **entity_uuid** | **str**|  |
 **create_review** | [**CreateReview**](CreateReview.md)|  |
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

# **delete_review**
> bool, date, datetime, dict, float, int, list, str, none_type delete_review(entity_type, entity_uuid, review_uuid)

Deletereview

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import reviews_api
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
    api_instance = reviews_api.ReviewsApi(api_client)
    entity_type = "entity_type_example" # str | 
    entity_uuid = "entity_uuid_example" # str | 
    review_uuid = "review_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deletereview
        api_response = api_instance.delete_review(entity_type, entity_uuid, review_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ReviewsApi->delete_review: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deletereview
        api_response = api_instance.delete_review(entity_type, entity_uuid, review_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ReviewsApi->delete_review: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**|  |
 **entity_uuid** | **str**|  |
 **review_uuid** | **str**|  |
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

# **get_review**
> bool, date, datetime, dict, float, int, list, str, none_type get_review(entity_type, entity_uuid, review_uuid)

Getreview

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import reviews_api
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
    api_instance = reviews_api.ReviewsApi(api_client)
    entity_type = "entity_type_example" # str | 
    entity_uuid = "entity_uuid_example" # str | 
    review_uuid = "review_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Getreview
        api_response = api_instance.get_review(entity_type, entity_uuid, review_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ReviewsApi->get_review: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Getreview
        api_response = api_instance.get_review(entity_type, entity_uuid, review_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ReviewsApi->get_review: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**|  |
 **entity_uuid** | **str**|  |
 **review_uuid** | **str**|  |
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

# **search_reviews**
> bool, date, datetime, dict, float, int, list, str, none_type search_reviews(entity_type, entity_uuid)

Searchreview

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import reviews_api
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
    api_instance = reviews_api.ReviewsApi(api_client)
    entity_type = "entity_type_example" # str | 
    entity_uuid = "entity_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Searchreview
        api_response = api_instance.search_reviews(entity_type, entity_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ReviewsApi->search_reviews: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Searchreview
        api_response = api_instance.search_reviews(entity_type, entity_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ReviewsApi->search_reviews: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**|  |
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

# **update_review**
> bool, date, datetime, dict, float, int, list, str, none_type update_review(entity_type, entity_uuid, review_uuid, update_review)

Updatereview

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import reviews_api
from ehelply_python_sdk.model.update_review import UpdateReview
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
    api_instance = reviews_api.ReviewsApi(api_client)
    entity_type = "entity_type_example" # str | 
    entity_uuid = "entity_uuid_example" # str | 
    review_uuid = "review_uuid_example" # str | 
    update_review = UpdateReview(
        rating=1,
        max_rating=1,
        review_text="review_text_example",
    ) # UpdateReview | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updatereview
        api_response = api_instance.update_review(entity_type, entity_uuid, review_uuid, update_review)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ReviewsApi->update_review: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updatereview
        api_response = api_instance.update_review(entity_type, entity_uuid, review_uuid, update_review, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling ReviewsApi->update_review: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**|  |
 **entity_uuid** | **str**|  |
 **review_uuid** | **str**|  |
 **update_review** | [**UpdateReview**](UpdateReview.md)|  |
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

