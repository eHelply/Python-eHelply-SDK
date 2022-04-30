# ehelply_python_sdk.AuthApi

All URIs are relative to *https://api.prod.ehelply.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reset_password_confirmation_users_auth_password_reset_confirm_post**](AuthApi.md#reset_password_confirmation_users_auth_password_reset_confirm_post) | **POST** /sam/users/auth/password/reset/confirm | Reset Password Confirmation

# **reset_password_confirmation_users_auth_password_reset_confirm_post**
> bool, date, datetime, dict, float, int, list, str, none_type reset_password_confirmation_users_auth_password_reset_confirm_post(user_password_reset_confirmation)

Reset Password Confirmation

Resets the given user's password to the given password when the proper code is provided

### Example

```python
import ehelply_python_sdk
from ehelply_python_sdk.api import auth_api
from ehelply_python_sdk.model.user_password_reset_confirmation import UserPasswordResetConfirmation
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
    api_instance = auth_api.AuthApi(api_client)

    # example passing only required values which don't have defaults set
    body = UserPasswordResetConfirmation(
        email="email_example",
        confirmation_code="confirmation_code_example",
        password="password_example",
    )
    try:
        # Reset Password Confirmation
        api_response = api_instance.reset_password_confirmation_users_auth_password_reset_confirm_post(
            body=body,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling AuthApi->reset_password_confirmation_users_auth_password_reset_confirm_post: %s\n" % e)
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
[**UserPasswordResetConfirmation**](UserPasswordResetConfirmation.md) |  | 


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

