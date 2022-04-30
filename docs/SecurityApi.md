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
import ehelply_python_sdk
from ehelply_python_sdk.api import security_api
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_api.SecurityApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'category': "category_example",
    }
    header_params = {
    }
    try:
        # Create Encryption Key
        api_response = api_instance.create_encryption_key_security_encryption_categories_category_keys_post(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->create_encryption_key_security_encryption_categories_category_keys_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'category': "category_example",
    }
    header_params = {
        'ehelply-security-secret-key': "ehelply-security-secret-key_example",
    }
    try:
        # Create Encryption Key
        api_response = api_instance.create_encryption_key_security_encryption_categories_category_keys_post(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->create_encryption_key_security_encryption_categories_category_keys_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ehelply-security-secret-key | EhelplySecuritySecretKeySchema | | optional

#### EhelplySecuritySecretKeySchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
category | CategorySchema | | 

#### CategorySchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
404 | ApiResponseFor404 | Not found 
422 | ApiResponseFor422 | Validation Error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
typing.Union[dict, frozendict, str, date, datetime, int, float, bool, Decimal, None, list, tuple, bytes] | |

#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_key_security_keys_post**
> InlineResponse2007 create_key_security_keys_post(body_create_key_security_keys_post)

Create Key

### Example

```python
import ehelply_python_sdk
from ehelply_python_sdk.api import security_api
from ehelply_python_sdk.model.inline_response2007 import InlineResponse2007
from ehelply_python_sdk.model.inline_response403 import InlineResponse403
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.body_create_key_security_keys_post import BodyCreateKeySecurityKeysPost
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_api.SecurityApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = BodyCreateKeySecurityKeysPost(
        key=SecurityKeyCreate(
            name="name_example",
            summary="summary_example",
        ),
    )
    try:
        # Create Key
        api_response = api_instance.create_key_security_keys_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->create_key_security_keys_post: %s\n" % e)

    # example passing only optional values
    query_params = {
        'access_length': 64,
        'secret_length': 64,
    }
    body = BodyCreateKeySecurityKeysPost(
        key=SecurityKeyCreate(
            name="name_example",
            summary="summary_example",
        ),
    )
    try:
        # Create Key
        api_response = api_instance.create_key_security_keys_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->create_key_security_keys_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BodyCreateKeySecurityKeysPost**](BodyCreateKeySecurityKeysPost.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
access_length | AccessLengthSchema | | optional
secret_length | SecretLengthSchema | | optional


#### AccessLengthSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 64

#### SecretLengthSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | defaults to 64

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
400 | ApiResponseFor400 | Access token and secret token lengths must be greater than 48 characters and less than 1024 characters to guarantee adequate security.  
403 | ApiResponseFor403 | Unauthorized - Denied by eHelply 
404 | ApiResponseFor404 | Not found 
422 | ApiResponseFor422 | Validation Error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InlineResponse2007**](InlineResponse2007.md) |  | 


#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InlineResponse403**](InlineResponse403.md) |  | 


#### ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InlineResponse403**](InlineResponse403.md) |  | 


#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_key_security_keys_key_uuid_delete**
> InlineResponse2008 delete_key_security_keys_key_uuid_delete(key_uuid)

Delete Key

### Example

```python
import ehelply_python_sdk
from ehelply_python_sdk.api import security_api
from ehelply_python_sdk.model.inline_response403 import InlineResponse403
from ehelply_python_sdk.model.inline_response2008 import InlineResponse2008
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_api.SecurityApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'key_uuid': "key_uuid_example",
    }
    try:
        # Delete Key
        api_response = api_instance.delete_key_security_keys_key_uuid_delete(
            path_params=path_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->delete_key_security_keys_key_uuid_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
key_uuid | KeyUuidSchema | | 

#### KeyUuidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
403 | ApiResponseFor403 | Unauthorized - Denied by eHelply 
404 | ApiResponseFor404 | Not found 
422 | ApiResponseFor422 | Validation Error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InlineResponse2008**](InlineResponse2008.md) |  | 


#### ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InlineResponse403**](InlineResponse403.md) |  | 


#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_token_security_tokens_post**
> InlineResponse2006 generate_token_security_tokens_post(body_generate_token_security_tokens_post)

Generate Token

### Example

```python
import ehelply_python_sdk
from ehelply_python_sdk.api import security_api
from ehelply_python_sdk.model.inline_response403 import InlineResponse403
from ehelply_python_sdk.model.inline_response2006 import InlineResponse2006
from ehelply_python_sdk.model.body_generate_token_security_tokens_post import BodyGenerateTokenSecurityTokensPost
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_api.SecurityApi(api_client)

    # example passing only required values which don't have defaults set
    body = BodyGenerateTokenSecurityTokensPost(
        token=SecurityCreateToken(
            length=64,
        ),
    )
    try:
        # Generate Token
        api_response = api_instance.generate_token_security_tokens_post(
            body=body,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->generate_token_security_tokens_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BodyGenerateTokenSecurityTokensPost**](BodyGenerateTokenSecurityTokensPost.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
403 | ApiResponseFor403 | Unauthorized - Denied by eHelply 
404 | ApiResponseFor404 | Not found 
422 | ApiResponseFor422 | Validation Error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InlineResponse2006**](InlineResponse2006.md) |  | 


#### ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InlineResponse403**](InlineResponse403.md) |  | 


#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_encryption_key_security_encryption_categories_category_keys_get**
> [SecurityEncryptionKeyGet] get_encryption_key_security_encryption_categories_category_keys_get(category)

Get Encryption Key

### Example

```python
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
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_api.SecurityApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'category': "category_example",
    }
    header_params = {
    }
    try:
        # Get Encryption Key
        api_response = api_instance.get_encryption_key_security_encryption_categories_category_keys_get(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->get_encryption_key_security_encryption_categories_category_keys_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'category': "category_example",
    }
    header_params = {
        'ehelply-security-secret-key': "ehelply-security-secret-key_example",
    }
    try:
        # Get Encryption Key
        api_response = api_instance.get_encryption_key_security_encryption_categories_category_keys_get(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->get_encryption_key_security_encryption_categories_category_keys_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ehelply-security-secret-key | EhelplySecuritySecretKeySchema | | optional

#### EhelplySecuritySecretKeySchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
category | CategorySchema | | 

#### CategorySchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
404 | ApiResponseFor404 | Not found 
422 | ApiResponseFor422 | Validation Error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
**[SecurityEncryptionKeyGet]** |  | 

#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



[**[SecurityEncryptionKeyGet]**](SecurityEncryptionKeyGet.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_key_security_keys_key_uuid_get**
> SecurityKeyGet get_key_security_keys_key_uuid_get(key_uuid)

Get Key

### Example

```python
import ehelply_python_sdk
from ehelply_python_sdk.api import security_api
from ehelply_python_sdk.model.inline_response403 import InlineResponse403
from ehelply_python_sdk.model.security_key_get import SecurityKeyGet
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_api.SecurityApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'key_uuid': "key_uuid_example",
    }
    try:
        # Get Key
        api_response = api_instance.get_key_security_keys_key_uuid_get(
            path_params=path_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->get_key_security_keys_key_uuid_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
key_uuid | KeyUuidSchema | | 

#### KeyUuidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
403 | ApiResponseFor403 | Unauthorized - Denied by eHelply 
404 | ApiResponseFor404 | Key does not exist 
422 | ApiResponseFor422 | Validation Error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SecurityKeyGet**](SecurityKeyGet.md) |  | 


#### ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InlineResponse403**](InlineResponse403.md) |  | 


#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InlineResponse403**](InlineResponse403.md) |  | 


#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



[**SecurityKeyGet**](SecurityKeyGet.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_keys_security_keys_get**
> [SecurityKeyGet] search_keys_security_keys_get()

Search Keys

### Example

```python
import ehelply_python_sdk
from ehelply_python_sdk.api import security_api
from ehelply_python_sdk.model.inline_response403 import InlineResponse403
from ehelply_python_sdk.model.security_key_get import SecurityKeyGet
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient(configuration) as api_client:
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
403 | ApiResponseFor403 | Unauthorized - Denied by eHelply 
404 | ApiResponseFor404 | Not found 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson

Type | Description | Notes
------------- | ------------- | -------------
**[SecurityKeyGet]** |  | 

#### ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InlineResponse403**](InlineResponse403.md) |  | 


#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |


[**[SecurityKeyGet]**](SecurityKeyGet.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_key_security_keys_verify_post**
> SecurityKeyGet verify_key_security_keys_verify_post(body_verify_key_security_keys_verify_post)

Verify Key

### Example

```python
import ehelply_python_sdk
from ehelply_python_sdk.api import security_api
from ehelply_python_sdk.model.inline_response403 import InlineResponse403
from ehelply_python_sdk.model.security_key_get import SecurityKeyGet
from ehelply_python_sdk.model.body_verify_key_security_keys_verify_post import BodyVerifyKeySecurityKeysVerifyPost
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = security_api.SecurityApi(api_client)

    # example passing only required values which don't have defaults set
    body = BodyVerifyKeySecurityKeysVerifyPost(
        key=SecurityKeyVerify(
            access="access_example",
            secret="secret_example",
        ),
    )
    try:
        # Verify Key
        api_response = api_instance.verify_key_security_keys_verify_post(
            body=body,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SecurityApi->verify_key_security_keys_verify_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BodyVerifyKeySecurityKeysVerifyPost**](BodyVerifyKeySecurityKeysVerifyPost.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
400 | ApiResponseFor400 | Access token and secret token lengths must be greater than 48 characters and less than 1024 characters to guarantee adequate security.  
403 | ApiResponseFor403 | Key 
404 | ApiResponseFor404 | Not found 
422 | ApiResponseFor422 | Validation Error 

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SecurityKeyGet**](SecurityKeyGet.md) |  | 


#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InlineResponse403**](InlineResponse403.md) |  | 


#### ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InlineResponse403**](InlineResponse403.md) |  | 


#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](HTTPValidationError.md) |  | 



[**SecurityKeyGet**](SecurityKeyGet.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

