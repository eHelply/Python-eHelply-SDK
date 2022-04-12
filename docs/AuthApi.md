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
import time
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
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    user_password_reset_confirmation = UserPasswordResetConfirmation(
        email="email_example",
        confirmation_code="confirmation_code_example",
        password="password_example",
    ) # UserPasswordResetConfirmation | 

    # example passing only required values which don't have defaults set
    try:
        # Reset Password Confirmation
        api_response = api_instance.reset_password_confirmation_users_auth_password_reset_confirm_post(user_password_reset_confirmation)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling AuthApi->reset_password_confirmation_users_auth_password_reset_confirm_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_password_reset_confirmation** | [**UserPasswordResetConfirmation**](UserPasswordResetConfirmation.md)|  |

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

