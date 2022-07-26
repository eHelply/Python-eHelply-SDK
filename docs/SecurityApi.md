# ehelply_python_sdk.SecurityApi

All URIs are relative to *https://api.prod.ehelply.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_encryption_key**](SecurityApi.md#create_encryption_key) | **POST** /sam/security/encryption/categories/{category}/keys | Createencryptionkey
[**create_key**](SecurityApi.md#create_key) | **POST** /sam/security/keys | Createkey
[**delete_key**](SecurityApi.md#delete_key) | **DELETE** /sam/security/keys/{key_uuid} | Deletekey
[**generate_token**](SecurityApi.md#generate_token) | **POST** /sam/security/tokens | Generatetoken
[**get_encryption_key**](SecurityApi.md#get_encryption_key) | **GET** /sam/security/encryption/categories/{category}/keys | Getencryptionkey
[**get_key**](SecurityApi.md#get_key) | **GET** /sam/security/keys/{key_uuid} | Getkey
[**search_keys**](SecurityApi.md#search_keys) | **GET** /sam/security/keys | Searchkeys
[**verify_key**](SecurityApi.md#verify_key) | **POST** /sam/security/keys/verify | Verifykey


# **create_encryption_key**
> SecurityEncryptionKeyResponse create_encryption_key(category)

Createencryptionkey

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import security_api
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.security_encryption_key_response import SecurityEncryptionKeyResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = security_api.SecurityApi(api_client)
    category = "category_example" # str | 
    ehelply_security_secret_key = "ehelply-security-secret-key_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Createencryptionkey
        api_response = api_instance.create_encryption_key(category)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->create_encryption_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Createencryptionkey
        api_response = api_instance.create_encryption_key(category, ehelply_security_secret_key=ehelply_security_secret_key)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->create_encryption_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**|  |
 **ehelply_security_secret_key** | **str**|  | [optional]

### Return type

[**SecurityEncryptionKeyResponse**](SecurityEncryptionKeyResponse.md)

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

# **create_key**
> ResponseCreatekey create_key(security_key_create)

Createkey

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import security_api
from ehelply_python_sdk.model.response_createkey import ResponseCreatekey
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.security_key_create import SecurityKeyCreate
from ehelply_python_sdk.model.get_services_with_specs403_response import GetServicesWithSpecs403Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = security_api.SecurityApi(api_client)
    security_key_create = SecurityKeyCreate(
        name="name_example",
        summary="summary_example",
    ) # SecurityKeyCreate | 
    access_length = 64 # int |  (optional) if omitted the server will use the default value of 64
    secret_length = 64 # int |  (optional) if omitted the server will use the default value of 64

    # example passing only required values which don't have defaults set
    try:
        # Createkey
        api_response = api_instance.create_key(security_key_create)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->create_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Createkey
        api_response = api_instance.create_key(security_key_create, access_length=access_length, secret_length=secret_length)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->create_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **security_key_create** | [**SecurityKeyCreate**](SecurityKeyCreate.md)|  |
 **access_length** | **int**|  | [optional] if omitted the server will use the default value of 64
 **secret_length** | **int**|  | [optional] if omitted the server will use the default value of 64

### Return type

[**ResponseCreatekey**](ResponseCreatekey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Access token and secret token lengths must be greater than 48 characters and less than 1024 characters to guarantee adequate security.  |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_key**
> ResponseDeletekey delete_key(key_uuid)

Deletekey

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import security_api
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.get_services_with_specs403_response import GetServicesWithSpecs403Response
from ehelply_python_sdk.model.response_deletekey import ResponseDeletekey
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = security_api.SecurityApi(api_client)
    key_uuid = "key_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Deletekey
        api_response = api_instance.delete_key(key_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->delete_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_uuid** | **str**|  |

### Return type

[**ResponseDeletekey**](ResponseDeletekey.md)

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
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_token**
> ResponseGeneratetoken generate_token(security_create_token)

Generatetoken

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import security_api
from ehelply_python_sdk.model.response_generatetoken import ResponseGeneratetoken
from ehelply_python_sdk.model.security_create_token import SecurityCreateToken
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.get_services_with_specs403_response import GetServicesWithSpecs403Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = security_api.SecurityApi(api_client)
    security_create_token = SecurityCreateToken(
        length=64,
    ) # SecurityCreateToken | 

    # example passing only required values which don't have defaults set
    try:
        # Generatetoken
        api_response = api_instance.generate_token(security_create_token)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->generate_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **security_create_token** | [**SecurityCreateToken**](SecurityCreateToken.md)|  |

### Return type

[**ResponseGeneratetoken**](ResponseGeneratetoken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_encryption_key**
> [SecurityEncryptionKeyGet] get_encryption_key(category)

Getencryptionkey

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import security_api
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.security_encryption_key_get import SecurityEncryptionKeyGet
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = security_api.SecurityApi(api_client)
    category = "category_example" # str | 
    ehelply_security_secret_key = "ehelply-security-secret-key_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Getencryptionkey
        api_response = api_instance.get_encryption_key(category)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->get_encryption_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Getencryptionkey
        api_response = api_instance.get_encryption_key(category, ehelply_security_secret_key=ehelply_security_secret_key)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->get_encryption_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**|  |
 **ehelply_security_secret_key** | **str**|  | [optional]

### Return type

[**[SecurityEncryptionKeyGet]**](SecurityEncryptionKeyGet.md)

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

# **get_key**
> SecurityKeyGet get_key(key_uuid)

Getkey

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import security_api
from ehelply_python_sdk.model.security_key_get import SecurityKeyGet
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.get_services_with_specs403_response import GetServicesWithSpecs403Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = security_api.SecurityApi(api_client)
    key_uuid = "key_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Getkey
        api_response = api_instance.get_key(key_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->get_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_uuid** | **str**|  |

### Return type

[**SecurityKeyGet**](SecurityKeyGet.md)

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
**404** | Key does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_keys**
> [SecurityKeyGet] search_keys()

Searchkeys

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import security_api
from ehelply_python_sdk.model.security_key_get import SecurityKeyGet
from ehelply_python_sdk.model.get_services_with_specs403_response import GetServicesWithSpecs403Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = security_api.SecurityApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Searchkeys
        api_response = api_instance.search_keys()
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->search_keys: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[SecurityKeyGet]**](SecurityKeyGet.md)

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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_key**
> SecurityKeyGet verify_key(security_key_verify)

Verifykey

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import security_api
from ehelply_python_sdk.model.security_key_get import SecurityKeyGet
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.security_key_verify import SecurityKeyVerify
from ehelply_python_sdk.model.get_services_with_specs403_response import GetServicesWithSpecs403Response
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = security_api.SecurityApi(api_client)
    security_key_verify = SecurityKeyVerify(
        access="access_example",
        secret="secret_example",
    ) # SecurityKeyVerify | 

    # example passing only required values which don't have defaults set
    try:
        # Verifykey
        api_response = api_instance.verify_key(security_key_verify)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->verify_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **security_key_verify** | [**SecurityKeyVerify**](SecurityKeyVerify.md)|  |

### Return type

[**SecurityKeyGet**](SecurityKeyGet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Access token and secret token lengths must be greater than 48 characters and less than 1024 characters to guarantee adequate security.  |  -  |
**403** | Key |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

