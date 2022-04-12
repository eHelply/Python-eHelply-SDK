# ehelply_python_sdk.UsersApi

All URIs are relative to *https://api.prod.ehelply.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirm_signup**](UsersApi.md#confirm_signup) | **POST** /sam/users/auth/signup/confirm | Confirmsignup
[**create_participant**](UsersApi.md#create_participant) | **POST** /sam/users/participants | Createparticipant
[**create_user**](UsersApi.md#create_user) | **POST** /sam/users | Createuser
[**delete_participant**](UsersApi.md#delete_participant) | **DELETE** /sam/users/participants/{participant_id} | Deleteparticipant
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /sam/users/{user_id} | Deleteuser
[**get_participant**](UsersApi.md#get_participant) | **GET** /sam/users/participants/{participant_id} | Getparticipant
[**get_user**](UsersApi.md#get_user) | **GET** /sam/users/{user_id} | Getuser
[**login**](UsersApi.md#login) | **POST** /sam/users/auth/login | Login
[**refresh_token**](UsersApi.md#refresh_token) | **POST** /sam/users/auth/{app_client}/refresh-token | Refreshtoken
[**reset_password**](UsersApi.md#reset_password) | **POST** /sam/users/auth/password/reset | Resetpassword
[**reset_password_confirmation_users_auth_password_reset_confirm_post**](UsersApi.md#reset_password_confirmation_users_auth_password_reset_confirm_post) | **POST** /sam/users/auth/password/reset/confirm | Reset Password Confirmation
[**search_participants**](UsersApi.md#search_participants) | **GET** /sam/users/participants | Searchparticipants
[**signup**](UsersApi.md#signup) | **POST** /sam/users/auth/signup | Signup
[**update_participant**](UsersApi.md#update_participant) | **PUT** /sam/users/participants/{participant_id} | Updateparticipant
[**update_user**](UsersApi.md#update_user) | **PUT** /sam/users/{user_id} | Updateuser
[**user_validations**](UsersApi.md#user_validations) | **POST** /sam/users/validations/{field} | Uservalidations


# **confirm_signup**
> bool, date, datetime, dict, float, int, list, str, none_type confirm_signup(user_confirmation)

Confirmsignup

Validates a user signup with a given confirmation

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import users_api
from ehelply_python_sdk.model.user_confirmation import UserConfirmation
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
    api_instance = users_api.UsersApi(api_client)
    user_confirmation = UserConfirmation(
        email="email_example",
        verification_code="verification_code_example",
    ) # UserConfirmation | 

    # example passing only required values which don't have defaults set
    try:
        # Confirmsignup
        api_response = api_instance.confirm_signup(user_confirmation)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling UsersApi->confirm_signup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_confirmation** | [**UserConfirmation**](UserConfirmation.md)|  |

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

# **create_participant**
> ParticipantUserReturn create_participant(participant_create)

Createparticipant

Creates a participant given the participant info (meta and user_id)

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import users_api
from ehelply_python_sdk.model.participant_user_return import ParticipantUserReturn
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.participant_create import ParticipantCreate
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    participant_create = ParticipantCreate(
        meta={},
        user_uuid="user_uuid_example",
    ) # ParticipantCreate | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Createparticipant
        api_response = api_instance.create_participant(participant_create)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling UsersApi->create_participant: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Createparticipant
        api_response = api_instance.create_participant(participant_create, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling UsersApi->create_participant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_create** | [**ParticipantCreate**](ParticipantCreate.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**ParticipantUserReturn**](ParticipantUserReturn.md)

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

# **create_user**
> bool, date, datetime, dict, float, int, list, str, none_type create_user()

Createuser

Usually ran after login and will do the following: - If no user exists (AKA signed in with social media) it will create a new user and default participant - If a user exists, sync Cognito data from Cognito to the user - Determine missing fields that SHOULD be filled

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    authorization = "authorization_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Createuser
        api_response = api_instance.create_user(authorization=authorization)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional]

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

# **delete_participant**
> bool delete_participant(participant_id)

Deleteparticipant

Delete participants related to the given participant_id, returns True if successful

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    participant_id = "participant_id_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deleteparticipant
        api_response = api_instance.delete_participant(participant_id)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling UsersApi->delete_participant: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deleteparticipant
        api_response = api_instance.delete_participant(participant_id, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling UsersApi->delete_participant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_id** | **str**|  |
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

# **delete_user**
> bool delete_user(user_id)

Deleteuser

Soft deletes the user with the provided user id, granted the deleter is the same person or an admin. Returns True if successful

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    user_id = "user_id_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deleteuser
        api_response = api_instance.delete_user(user_id)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deleteuser
        api_response = api_instance.delete_user(user_id, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
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

# **get_participant**
> ParticipantUserReturn get_participant(participant_id)

Getparticipant

Gets a participant given their participant ID

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import users_api
from ehelply_python_sdk.model.participant_user_return import ParticipantUserReturn
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
    api_instance = users_api.UsersApi(api_client)
    participant_id = "participant_id_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Getparticipant
        api_response = api_instance.get_participant(participant_id)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling UsersApi->get_participant: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Getparticipant
        api_response = api_instance.get_participant(participant_id, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling UsersApi->get_participant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_id** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**ParticipantUserReturn**](ParticipantUserReturn.md)

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

# **get_user**
> UserResponse get_user(user_id)

Getuser

Gets the user object given user id (uuid) or cognito id (cognito)

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import users_api
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.user_response import UserResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    user_id = "user_id_example" # str | 
    id_type = "cognito OR uuid" # str |  (optional)
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Getuser
        api_response = api_instance.get_user(user_id)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Getuser
        api_response = api_instance.get_user(user_id, id_type=id_type, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **id_type** | **str**|  | [optional]
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**UserResponse**](UserResponse.md)

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

# **login**
> UserLoginReturn login(user_login)

Login

Login endpoint, returns tokens. EMAIL NEEDS TO BE VERIFIED (can be done through the email the user received).

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import users_api
from ehelply_python_sdk.model.user_login_return import UserLoginReturn
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.user_login import UserLogin
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    user_login = UserLogin(
        username="username_example",
        password="password_example",
    ) # UserLogin | 

    # example passing only required values which don't have defaults set
    try:
        # Login
        api_response = api_instance.login(user_login)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling UsersApi->login: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_login** | [**UserLogin**](UserLogin.md)|  |

### Return type

[**UserLoginReturn**](UserLoginReturn.md)

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

# **refresh_token**
> UserTokenReturn refresh_token(app_client, body)

Refreshtoken

Refreshes tokens given a refresh token.

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import users_api
from ehelply_python_sdk.model.user_token_return import UserTokenReturn
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
    api_instance = users_api.UsersApi(api_client)
    app_client = "app_client_example" # str | 
    body = "body_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Refreshtoken
        api_response = api_instance.refresh_token(app_client, body)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling UsersApi->refresh_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_client** | **str**|  |
 **body** | **str**|  |

### Return type

[**UserTokenReturn**](UserTokenReturn.md)

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

# **reset_password**
> bool, date, datetime, dict, float, int, list, str, none_type reset_password(user_password_reset)

Resetpassword

Sends the user an email with a confirmation code so they can reset their password

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import users_api
from ehelply_python_sdk.model.user_password_reset import UserPasswordReset
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
    api_instance = users_api.UsersApi(api_client)
    user_password_reset = UserPasswordReset(
        email="email_example",
    ) # UserPasswordReset | 

    # example passing only required values which don't have defaults set
    try:
        # Resetpassword
        api_response = api_instance.reset_password(user_password_reset)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling UsersApi->reset_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_password_reset** | [**UserPasswordReset**](UserPasswordReset.md)|  |

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

# **reset_password_confirmation_users_auth_password_reset_confirm_post**
> bool, date, datetime, dict, float, int, list, str, none_type reset_password_confirmation_users_auth_password_reset_confirm_post(user_password_reset_confirmation)

Reset Password Confirmation

Resets the given user's password to the given password when the proper code is provided

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
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
        print("Exception when calling UsersApi->reset_password_confirmation_users_auth_password_reset_confirm_post: %s\n" % e)
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

# **search_participants**
> Page search_participants()

Searchparticipants

Search participants using a user uuid, returns pagination information and list of `items` (ParticipantUserReturn from GET Participant). Can search on \"user_uuid\", and sort on any field. To search enter search value into \"search\" query param and the field into \"search on\" (currently only \"user\"uuid\"). For sorting fill out \"sort_desc\" field with either true/false and the \"sort_on\" query parameter with column you want to sort on (ex: date_created). Max pagination items per page is 50.

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import users_api
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
    api_instance = users_api.UsersApi(api_client)
    page = 1 # int |  (optional) if omitted the server will use the default value of 1
    page_size = 25 # int |  (optional) if omitted the server will use the default value of 25
    search = "search_example" # str |  (optional)
    search_on = "search_on_example" # str |  (optional)
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
        # Searchparticipants
        api_response = api_instance.search_participants(page=page, page_size=page_size, search=search, search_on=search_on, sort_on=sort_on, sort_desc=sort_desc, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling UsersApi->search_participants: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 25
 **search** | **str**|  | [optional]
 **search_on** | **str**|  | [optional]
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

# **signup**
> UserSignupReturn signup(user_signup)

Signup

Signup to eHelply, creates a user and default participant behind the scenes. Does not verify email.

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import users_api
from ehelply_python_sdk.model.user_signup import UserSignup
from ehelply_python_sdk.model.user_signup_return import UserSignupReturn
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
    api_instance = users_api.UsersApi(api_client)
    user_signup = UserSignup(
        username="username_example",
        password="password_example",
        email="email_example",
        first_name="first_name_example",
        last_name="last_name_example",
        phone_number="phone_number_example",
        country="country_example",
        lat="lat_example",
        lng="lng_example",
        verified_legal_terms=False,
        picture="picture_example",
        newsletters=True,
    ) # UserSignup | 

    # example passing only required values which don't have defaults set
    try:
        # Signup
        api_response = api_instance.signup(user_signup)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling UsersApi->signup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_signup** | [**UserSignup**](UserSignup.md)|  |

### Return type

[**UserSignupReturn**](UserSignupReturn.md)

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

# **update_participant**
> ParticipantUserReturn update_participant(participant_id, participant_update)

Updateparticipant

Update participant data given

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import users_api
from ehelply_python_sdk.model.participant_user_return import ParticipantUserReturn
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.participant_update import ParticipantUpdate
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    participant_id = "participant_id_example" # str | 
    participant_update = ParticipantUpdate(
        meta={},
        user_uuid="user_uuid_example",
        uuid="uuid_example",
    ) # ParticipantUpdate | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updateparticipant
        api_response = api_instance.update_participant(participant_id, participant_update)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling UsersApi->update_participant: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updateparticipant
        api_response = api_instance.update_participant(participant_id, participant_update, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling UsersApi->update_participant: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **participant_id** | **str**|  |
 **participant_update** | [**ParticipantUpdate**](ParticipantUpdate.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**ParticipantUserReturn**](ParticipantUserReturn.md)

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

# **update_user**
> UserResponse update_user(user_id, user)

Updateuser

Update the given user and sync the cognito data

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import users_api
from ehelply_python_sdk.model.user import User
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.user_response import UserResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    user_id = "user_id_example" # str | 
    user = User(
        cognito_id="cognito_id_example",
        cognito_data={},
        first_name="first_name_example",
        last_name="last_name_example",
        email="email_example",
        phone_number="phone_number_example",
        country="country_example",
        picture="picture_example",
        gps_location={},
        verified_legal_terms=False,
        date_created=dateutil_parser('1970-01-01T00:00:00.00Z'),
        date_updated=dateutil_parser('1970-01-01T00:00:00.00Z'),
        date_deleted=dateutil_parser('1970-01-01T00:00:00.00Z'),
        uuid="uuid_example",
        last_login=dateutil_parser('1970-01-01T00:00:00.00Z'),
        first_login=True,
    ) # User | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updateuser
        api_response = api_instance.update_user(user_id, user)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updateuser
        api_response = api_instance.update_user(user_id, user, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **user** | [**User**](User.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**UserResponse**](UserResponse.md)

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

# **user_validations**
> bool user_validations(field, user_validations)

Uservalidations

Validates a certain field.

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import users_api
from ehelply_python_sdk.model.user_validations import UserValidations
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
    api_instance = users_api.UsersApi(api_client)
    field = "email" # str | 
    user_validations = UserValidations(
        value="value_example",
        type="type_example",
    ) # UserValidations | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Uservalidations
        api_response = api_instance.user_validations(field, user_validations)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling UsersApi->user_validations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Uservalidations
        api_response = api_instance.user_validations(field, user_validations, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling UsersApi->user_validations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**|  |
 **user_validations** | [**UserValidations**](UserValidations.md)|  |
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

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

