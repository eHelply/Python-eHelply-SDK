# ehelply_python_sdk.SecurityApi

All URIs are relative to *https://api.prod.ehelply.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_encryption_key_security_encryption_categories_category_keys_post**](SecurityApi.md#create_encryption_key_security_encryption_categories_category_keys_post) | **POST** /sam/security/encryption/categories/{category}/keys | Create Encryption Key
[**create_key_security_keys_post**](SecurityApi.md#create_key_security_keys_post) | **POST** /sam/security/keys | Create Key
[**delete_key_security_keys_key_uuid_delete**](SecurityApi.md#delete_key_security_keys_key_uuid_delete) | **DELETE** /sam/security/keys/{key_uuid} | Delete Key
[**generate_token_security_tokens_post**](SecurityApi.md#generate_token_security_tokens_post) | **POST** /sam/security/tokens | Generate Token
[**get_encryption_key_security_encryption_categories_category_keys_get**](SecurityApi.md#get_encryption_key_security_encryption_categories_category_keys_get) | **GET** /sam/security/encryption/categories/{category}/keys | Get Encryption Key
[**get_key_security_keys_key_uuid_get**](SecurityApi.md#get_key_security_keys_key_uuid_get) | **GET** /sam/security/keys/{key_uuid} | Get Key
[**search_keys_security_keys_get**](SecurityApi.md#search_keys_security_keys_get) | **GET** /sam/security/keys | Search Keys
[**verify_key_security_keys_verify_post**](SecurityApi.md#verify_key_security_keys_verify_post) | **POST** /sam/security/keys/verify | Verify Key


# **create_encryption_key_security_encryption_categories_category_keys_post**
> bool, date, datetime, dict, float, int, list, str, none_type create_encryption_key_security_encryption_categories_category_keys_post(category)

Create Encryption Key

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import security_api
from ehelply_python_sdk.model.sam_http_validation_error import SamHTTPValidationError
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
        # Create Encryption Key
        api_response = api_instance.create_encryption_key_security_encryption_categories_category_keys_post(category)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->create_encryption_key_security_encryption_categories_category_keys_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Encryption Key
        api_response = api_instance.create_encryption_key_security_encryption_categories_category_keys_post(category, ehelply_security_secret_key=ehelply_security_secret_key)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->create_encryption_key_security_encryption_categories_category_keys_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**|  |
 **ehelply_security_secret_key** | **str**|  | [optional]

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

# **create_key_security_keys_post**
> bool, date, datetime, dict, float, int, list, str, none_type create_key_security_keys_post(body_create_key_security_keys_post)

Create Key

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import security_api
from ehelply_python_sdk.model.sam_http_validation_error import SamHTTPValidationError
from ehelply_python_sdk.model.body_create_key_security_keys_post import BodyCreateKeySecurityKeysPost
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
    body_create_key_security_keys_post = BodyCreateKeySecurityKeysPost(
        key=SecurityKeyCreate(
            name="name_example",
            summary="summary_example",
        ),
    ) # BodyCreateKeySecurityKeysPost | 
    access_length = 64 # int |  (optional) if omitted the server will use the default value of 64
    secret_length = 64 # int |  (optional) if omitted the server will use the default value of 64

    # example passing only required values which don't have defaults set
    try:
        # Create Key
        api_response = api_instance.create_key_security_keys_post(body_create_key_security_keys_post)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->create_key_security_keys_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Key
        api_response = api_instance.create_key_security_keys_post(body_create_key_security_keys_post, access_length=access_length, secret_length=secret_length)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->create_key_security_keys_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_create_key_security_keys_post** | [**BodyCreateKeySecurityKeysPost**](BodyCreateKeySecurityKeysPost.md)|  |
 **access_length** | **int**|  | [optional] if omitted the server will use the default value of 64
 **secret_length** | **int**|  | [optional] if omitted the server will use the default value of 64

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
**400** | Access token and secret token lengths must be greater than 48 characters and less than 1024 characters to guarantee adequate security.  |  -  |
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_key_security_keys_key_uuid_delete**
> bool, date, datetime, dict, float, int, list, str, none_type delete_key_security_keys_key_uuid_delete(key_uuid)

Delete Key

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import security_api
from ehelply_python_sdk.model.sam_http_validation_error import SamHTTPValidationError
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
        # Delete Key
        api_response = api_instance.delete_key_security_keys_key_uuid_delete(key_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->delete_key_security_keys_key_uuid_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_uuid** | **str**|  |

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
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_token_security_tokens_post**
> bool, date, datetime, dict, float, int, list, str, none_type generate_token_security_tokens_post(body_generate_token_security_tokens_post)

Generate Token

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import security_api
from ehelply_python_sdk.model.sam_http_validation_error import SamHTTPValidationError
from ehelply_python_sdk.model.body_generate_token_security_tokens_post import BodyGenerateTokenSecurityTokensPost
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
    body_generate_token_security_tokens_post = BodyGenerateTokenSecurityTokensPost(
        token=SecurityCreateToken(
            length=64,
        ),
    ) # BodyGenerateTokenSecurityTokensPost | 

    # example passing only required values which don't have defaults set
    try:
        # Generate Token
        api_response = api_instance.generate_token_security_tokens_post(body_generate_token_security_tokens_post)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->generate_token_security_tokens_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_generate_token_security_tokens_post** | [**BodyGenerateTokenSecurityTokensPost**](BodyGenerateTokenSecurityTokensPost.md)|  |

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
**403** | Unauthorized - Denied by eHelply |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_encryption_key_security_encryption_categories_category_keys_get**
> [SecurityEncryptionKeyGet] get_encryption_key_security_encryption_categories_category_keys_get(category)

Get Encryption Key

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import security_api
from ehelply_python_sdk.model.sam_http_validation_error import SamHTTPValidationError
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
        # Get Encryption Key
        api_response = api_instance.get_encryption_key_security_encryption_categories_category_keys_get(category)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->get_encryption_key_security_encryption_categories_category_keys_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Encryption Key
        api_response = api_instance.get_encryption_key_security_encryption_categories_category_keys_get(category, ehelply_security_secret_key=ehelply_security_secret_key)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->get_encryption_key_security_encryption_categories_category_keys_get: %s\n" % e)
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

# **get_key_security_keys_key_uuid_get**
> SecurityKeyGet get_key_security_keys_key_uuid_get(key_uuid)

Get Key

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import security_api
from ehelply_python_sdk.model.sam_http_validation_error import SamHTTPValidationError
from ehelply_python_sdk.model.security_key_get import SecurityKeyGet
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
        # Get Key
        api_response = api_instance.get_key_security_keys_key_uuid_get(key_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->get_key_security_keys_key_uuid_get: %s\n" % e)
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

# **search_keys_security_keys_get**
> [SecurityKeyGet] search_keys_security_keys_get()

Search Keys

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import security_api
from ehelply_python_sdk.model.security_key_get import SecurityKeyGet
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
        # Search Keys
        api_response = api_instance.search_keys_security_keys_get()
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->search_keys_security_keys_get: %s\n" % e)
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

# **verify_key_security_keys_verify_post**
> SecurityKeyGet verify_key_security_keys_verify_post(body_verify_key_security_keys_verify_post)

Verify Key

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import security_api
from ehelply_python_sdk.model.sam_http_validation_error import SamHTTPValidationError
from ehelply_python_sdk.model.security_key_get import SecurityKeyGet
from ehelply_python_sdk.model.body_verify_key_security_keys_verify_post import BodyVerifyKeySecurityKeysVerifyPost
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
    body_verify_key_security_keys_verify_post = BodyVerifyKeySecurityKeysVerifyPost(
        key=SecurityKeyVerify(
            access="access_example",
            secret="secret_example",
        ),
    ) # BodyVerifyKeySecurityKeysVerifyPost | 

    # example passing only required values which don't have defaults set
    try:
        # Verify Key
        api_response = api_instance.verify_key_security_keys_verify_post(body_verify_key_security_keys_verify_post)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->verify_key_security_keys_verify_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_verify_key_security_keys_verify_post** | [**BodyVerifyKeySecurityKeysVerifyPost**](BodyVerifyKeySecurityKeysVerifyPost.md)|  |

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

