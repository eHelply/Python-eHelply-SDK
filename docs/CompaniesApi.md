# ehelply_python_sdk.CompaniesApi

All URIs are relative to *https://api.prod.ehelply.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_company_companies_post**](CompaniesApi.md#create_company_companies_post) | **POST** /companies | Create Company
[**delete_place_companies_company_uuid_delete**](CompaniesApi.md#delete_place_companies_company_uuid_delete) | **DELETE** /companies/{company_uuid} | Delete Place
[**get_company_companies_company_uuid_get**](CompaniesApi.md#get_company_companies_company_uuid_get) | **GET** /companies/{company_uuid} | Get Company
[**search_companies_companies_get**](CompaniesApi.md#search_companies_companies_get) | **GET** /companies | Search Companies
[**update_company_companies_company_uuid_put**](CompaniesApi.md#update_company_companies_company_uuid_put) | **PUT** /companies/{company_uuid} | Update Company


# **create_company_companies_post**
> CompanyResponse create_company_companies_post(company_base)

Create Company

Creates a company

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import companies_api
from ehelply_python_sdk.model.company_response import CompanyResponse
from ehelply_python_sdk.model.company_base import CompanyBase
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
    api_instance = companies_api.CompaniesApi(api_client)
    company_base = CompanyBase(
        name="Example Company",
        summary="Summary of the company",
        public=True,
        meta={},
        contact=ContactBase(
            phones={},
            email="test@example.com",
            website="www.ehelply.com",
            socials={},
        ),
    ) # CompanyBase | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Company
        api_response = api_instance.create_company_companies_post(company_base)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling CompaniesApi->create_company_companies_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Company
        api_response = api_instance.create_company_companies_post(company_base, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling CompaniesApi->create_company_companies_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_base** | [**CompanyBase**](CompanyBase.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**CompanyResponse**](CompanyResponse.md)

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

# **delete_place_companies_company_uuid_delete**
> bool, date, datetime, dict, float, int, list, str, none_type delete_place_companies_company_uuid_delete(company_uuid)

Delete Place

Deletes the company with the given ID and returns True if successful

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import companies_api
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
    api_instance = companies_api.CompaniesApi(api_client)
    company_uuid = "company_uuid_example" # str | 
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
        api_response = api_instance.delete_place_companies_company_uuid_delete(company_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling CompaniesApi->delete_place_companies_company_uuid_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Place
        api_response = api_instance.delete_place_companies_company_uuid_delete(company_uuid, soft_delete=soft_delete, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling CompaniesApi->delete_place_companies_company_uuid_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_uuid** | **str**|  |
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

# **get_company_companies_company_uuid_get**
> CompanyResponse get_company_companies_company_uuid_get(company_uuid)

Get Company

Gets the company information given the Place ID

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import companies_api
from ehelply_python_sdk.model.company_response import CompanyResponse
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
    api_instance = companies_api.CompaniesApi(api_client)
    company_uuid = "company_uuid_example" # str | 
    with_meta = False # bool |  (optional) if omitted the server will use the default value of False
    with_catalog = False # bool |  (optional) if omitted the server will use the default value of False
    with_reviews = False # bool |  (optional) if omitted the server will use the default value of False
    with_schedule = False # bool |  (optional) if omitted the server will use the default value of False
    with_blog = False # bool |  (optional) if omitted the server will use the default value of False
    with_tags = False # bool |  (optional) if omitted the server will use the default value of False
    with_categories = False # bool |  (optional) if omitted the server will use the default value of False
    with_places = False # bool |  (optional) if omitted the server will use the default value of False
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Company
        api_response = api_instance.get_company_companies_company_uuid_get(company_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling CompaniesApi->get_company_companies_company_uuid_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Company
        api_response = api_instance.get_company_companies_company_uuid_get(company_uuid, with_meta=with_meta, with_catalog=with_catalog, with_reviews=with_reviews, with_schedule=with_schedule, with_blog=with_blog, with_tags=with_tags, with_categories=with_categories, with_places=with_places, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling CompaniesApi->get_company_companies_company_uuid_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_uuid** | **str**|  |
 **with_meta** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_catalog** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_reviews** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_schedule** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_blog** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_tags** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_categories** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_places** | **bool**|  | [optional] if omitted the server will use the default value of False
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**CompanyResponse**](CompanyResponse.md)

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

# **search_companies_companies_get**
> Page search_companies_companies_get()

Search Companies

Search all companies and returns paginated results with Companies being stored in items field. Can search by `project_uuid, name, email` string fields or the `is_public and is_deleted` boolean fields. To search with these fields use query params with string values. For sorting fill out \"sort_desc\" field with either true/false and the \"sort_on\" query parameter with column you want to sort on (ex: name). Max pagination items per page is 50. Item return format: ``` {     uuid                                **type:** string     project_uuid                        **type:** string or None      meta_uuid                           **type:** string or None      catalog_data                        **type:** dict or None      review_group_data                   **type:** dict or None      schedule_data                       **type:** dict or None      blog_data                           **type:** dict or None      tags                                **type:** [TagBase] or None      categories                          **type:** [CategoryBase] or None      places                              **type:** PlaceBase or None      created_at                          **type:** string or None      updated_at                          **type:** string or None      deleted_at                          **type:** string or None  } ```

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import companies_api
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
    api_instance = companies_api.CompaniesApi(api_client)
    project_uuid = "project_uuid_example" # str |  (optional)
    name = "name_example" # str |  (optional)
    email = "email_example" # str |  (optional)
    is_public = True # bool |  (optional) if omitted the server will use the default value of True
    is_deleted = False # bool |  (optional) if omitted the server will use the default value of False
    with_places = False # bool |  (optional) if omitted the server will use the default value of False
    with_meta = False # bool |  (optional) if omitted the server will use the default value of False
    with_catalog = False # bool |  (optional) if omitted the server will use the default value of False
    with_reviews = False # bool |  (optional) if omitted the server will use the default value of False
    with_schedule = False # bool |  (optional) if omitted the server will use the default value of False
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
        # Search Companies
        api_response = api_instance.search_companies_companies_get(project_uuid=project_uuid, name=name, email=email, is_public=is_public, is_deleted=is_deleted, with_places=with_places, with_meta=with_meta, with_catalog=with_catalog, with_reviews=with_reviews, with_schedule=with_schedule, with_blog=with_blog, with_tags=with_tags, with_categories=with_categories, page=page, page_size=page_size, sort_on=sort_on, sort_desc=sort_desc, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling CompaniesApi->search_companies_companies_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**|  | [optional]
 **name** | **str**|  | [optional]
 **email** | **str**|  | [optional]
 **is_public** | **bool**|  | [optional] if omitted the server will use the default value of True
 **is_deleted** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_places** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_meta** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_catalog** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_reviews** | **bool**|  | [optional] if omitted the server will use the default value of False
 **with_schedule** | **bool**|  | [optional] if omitted the server will use the default value of False
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

# **update_company_companies_company_uuid_put**
> CompanyResponse update_company_companies_company_uuid_put(company_uuid, company_base)

Update Company

Update company with given info, only updating the fields supplied. Company Uuid must be sent however.

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import companies_api
from ehelply_python_sdk.model.company_response import CompanyResponse
from ehelply_python_sdk.model.company_base import CompanyBase
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
    api_instance = companies_api.CompaniesApi(api_client)
    company_uuid = "company_uuid_example" # str | 
    company_base = CompanyBase(
        name="Example Company",
        summary="Summary of the company",
        public=True,
        meta={},
        contact=ContactBase(
            phones={},
            email="test@example.com",
            website="www.ehelply.com",
            socials={},
        ),
    ) # CompanyBase | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Company
        api_response = api_instance.update_company_companies_company_uuid_put(company_uuid, company_base)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling CompaniesApi->update_company_companies_company_uuid_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Company
        api_response = api_instance.update_company_companies_company_uuid_put(company_uuid, company_base, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling CompaniesApi->update_company_companies_company_uuid_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_uuid** | **str**|  |
 **company_base** | [**CompanyBase**](CompanyBase.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**CompanyResponse**](CompanyResponse.md)

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

