# ehelply_python_sdk.CatalogsApi

All URIs are relative to *https://api.prod.ehelply.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_product_to_catalog**](CatalogsApi.md#attach_product_to_catalog) | **POST** /products/catalogs/{catalog_uuid}/products/{product_uuid} | Addproducttocatalog
[**create_catalog**](CatalogsApi.md#create_catalog) | **POST** /products/catalogs | Createcatalog
[**delete_catalog**](CatalogsApi.md#delete_catalog) | **DELETE** /products/catalogs/{catalog_uuid} | Deletecatalog
[**detach_product_from_catalog**](CatalogsApi.md#detach_product_from_catalog) | **DELETE** /products/catalogs/{catalog_uuid}/products/{product_uuid} | Removeproductfromcatalog
[**get_catalog**](CatalogsApi.md#get_catalog) | **GET** /products/catalogs/{catalog_uuid} | Getcatalog
[**search_catalog_products**](CatalogsApi.md#search_catalog_products) | **GET** /products/catalogs/{catalog_uuid}/products | Searchcatalogproducts
[**search_catalogs**](CatalogsApi.md#search_catalogs) | **GET** /products/catalogs | Searchcatalogs
[**update_catalog**](CatalogsApi.md#update_catalog) | **PUT** /products/catalogs/{catalog_uuid} | Updatecatalog


# **attach_product_to_catalog**
> bool attach_product_to_catalog(catalog_uuid, product_uuid)

Addproducttocatalog

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import catalogs_api
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    catalog_uuid = "catalog_uuid_example" # str | 
    product_uuid = "product_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Addproducttocatalog
        api_response = api_instance.attach_product_to_catalog(catalog_uuid, product_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling CatalogsApi->attach_product_to_catalog: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Addproducttocatalog
        api_response = api_instance.attach_product_to_catalog(catalog_uuid, product_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling CatalogsApi->attach_product_to_catalog: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_uuid** | **str**|  |
 **product_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

**bool**

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

# **create_catalog**
> CatalogReturn create_catalog(catalog_base)

Createcatalog

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import catalogs_api
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.catalog_base import CatalogBase
from ehelply_python_sdk.model.catalog_return import CatalogReturn
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = catalogs_api.CatalogsApi(api_client)
    catalog_base = CatalogBase(
        meta_data={},
        name="Product Name",
        featured={},
        sub_catalogs={},
    ) # CatalogBase | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Createcatalog
        api_response = api_instance.create_catalog(catalog_base)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling CatalogsApi->create_catalog: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Createcatalog
        api_response = api_instance.create_catalog(catalog_base, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling CatalogsApi->create_catalog: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_base** | [**CatalogBase**](CatalogBase.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**CatalogReturn**](CatalogReturn.md)

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

# **delete_catalog**
> bool delete_catalog(catalog_uuid)

Deletecatalog

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import catalogs_api
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    catalog_uuid = "catalog_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deletecatalog
        api_response = api_instance.delete_catalog(catalog_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling CatalogsApi->delete_catalog: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deletecatalog
        api_response = api_instance.delete_catalog(catalog_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling CatalogsApi->delete_catalog: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

**bool**

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

# **detach_product_from_catalog**
> bool detach_product_from_catalog(catalog_uuid, product_uuid)

Removeproductfromcatalog

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import catalogs_api
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    catalog_uuid = "catalog_uuid_example" # str | 
    product_uuid = "product_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Removeproductfromcatalog
        api_response = api_instance.detach_product_from_catalog(catalog_uuid, product_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling CatalogsApi->detach_product_from_catalog: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Removeproductfromcatalog
        api_response = api_instance.detach_product_from_catalog(catalog_uuid, product_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling CatalogsApi->detach_product_from_catalog: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_uuid** | **str**|  |
 **product_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

**bool**

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

# **get_catalog**
> CatalogReturn get_catalog(catalog_uuid)

Getcatalog

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import catalogs_api
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.catalog_return import CatalogReturn
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = catalogs_api.CatalogsApi(api_client)
    catalog_uuid = "catalog_uuid_example" # str | 
    with_meta = False # bool |  (optional) if omitted the server will use the default value of False
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Getcatalog
        api_response = api_instance.get_catalog(catalog_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling CatalogsApi->get_catalog: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Getcatalog
        api_response = api_instance.get_catalog(catalog_uuid, with_meta=with_meta, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling CatalogsApi->get_catalog: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_uuid** | **str**|  |
 **with_meta** | **bool**|  | [optional] if omitted the server will use the default value of False
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**CatalogReturn**](CatalogReturn.md)

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

# **search_catalog_products**
> Page search_catalog_products(catalog_uuid)

Searchcatalogproducts

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import catalogs_api
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    catalog_uuid = "catalog_uuid_example" # str | 
    with_meta = False # bool |  (optional) if omitted the server will use the default value of False
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
    try:
        # Searchcatalogproducts
        api_response = api_instance.search_catalog_products(catalog_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling CatalogsApi->search_catalog_products: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Searchcatalogproducts
        api_response = api_instance.search_catalog_products(catalog_uuid, with_meta=with_meta, page=page, page_size=page_size, sort_on=sort_on, sort_desc=sort_desc, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling CatalogsApi->search_catalog_products: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_uuid** | **str**|  |
 **with_meta** | **bool**|  | [optional] if omitted the server will use the default value of False
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
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_catalogs**
> Page search_catalogs()

Searchcatalogs

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import catalogs_api
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
    api_instance = catalogs_api.CatalogsApi(api_client)
    with_meta = False # bool |  (optional) if omitted the server will use the default value of False
    name = "name_example" # str |  (optional)
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
        # Searchcatalogs
        api_response = api_instance.search_catalogs(with_meta=with_meta, name=name, page=page, page_size=page_size, sort_on=sort_on, sort_desc=sort_desc, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling CatalogsApi->search_catalogs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **with_meta** | **bool**|  | [optional] if omitted the server will use the default value of False
 **name** | **str**|  | [optional]
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
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_catalog**
> CatalogReturn update_catalog(catalog_uuid, catalog_base)

Updatecatalog

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import catalogs_api
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.catalog_base import CatalogBase
from ehelply_python_sdk.model.catalog_return import CatalogReturn
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = catalogs_api.CatalogsApi(api_client)
    catalog_uuid = "catalog_uuid_example" # str | 
    catalog_base = CatalogBase(
        meta_data={},
        name="Product Name",
        featured={},
        sub_catalogs={},
    ) # CatalogBase | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updatecatalog
        api_response = api_instance.update_catalog(catalog_uuid, catalog_base)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling CatalogsApi->update_catalog: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updatecatalog
        api_response = api_instance.update_catalog(catalog_uuid, catalog_base, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling CatalogsApi->update_catalog: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_uuid** | **str**|  |
 **catalog_base** | [**CatalogBase**](CatalogBase.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**CatalogReturn**](CatalogReturn.md)

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

