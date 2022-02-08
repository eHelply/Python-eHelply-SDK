# ehelply-python-sdk.NotesApi

All URIs are relative to *https://api.prod.ehelply.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_note_notes_notes_post**](NotesApi.md#create_note_notes_notes_post) | **POST** /notes/notes/notes | Create Note
[**delete_note_notes_notes_note_id_delete**](NotesApi.md#delete_note_notes_notes_note_id_delete) | **DELETE** /notes/notes/notes/{note_id} | Delete Note
[**get_note_notes_notes_note_id_get**](NotesApi.md#get_note_notes_notes_note_id_get) | **GET** /notes/notes/notes/{note_id} | Get Note
[**update_note_notes_notes_note_id_put**](NotesApi.md#update_note_notes_notes_note_id_put) | **PUT** /notes/notes/notes/{note_id} | Update Note


# **create_note_notes_notes_post**
> NoteDynamo create_note_notes_notes_post(body_create_note_notes_notes_post)

Create Note

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import notes_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.body_create_note_notes_notes_post import BodyCreateNoteNotesNotesPost
from ehelply-python-sdk.model.note_dynamo import NoteDynamo
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = notes_api.NotesApi(api_client)
    body_create_note_notes_notes_post = BodyCreateNoteNotesNotesPost(
        note=NoteBase(
            content="content_example",
            time="time_example",
            meta=NoteMeta(
                original_author="original_author_example",
                author="author_example",
                previous_version="previous_version_example",
                next_version="next_version_example",
            ),
        ),
    ) # BodyCreateNoteNotesNotesPost | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Note
        api_response = api_instance.create_note_notes_notes_post(body_create_note_notes_notes_post)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling NotesApi->create_note_notes_notes_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Note
        api_response = api_instance.create_note_notes_notes_post(body_create_note_notes_notes_post, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling NotesApi->create_note_notes_notes_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_create_note_notes_notes_post** | [**BodyCreateNoteNotesNotesPost**](BodyCreateNoteNotesNotesPost.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**NoteDynamo**](NoteDynamo.md)

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

# **delete_note_notes_notes_note_id_delete**
> bool, date, datetime, dict, float, int, list, str, none_type delete_note_notes_notes_note_id_delete(note_id)

Delete Note

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import notes_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = notes_api.NotesApi(api_client)
    note_id = "note_id_example" # str | 
    method = "previous" # str |  (optional) if omitted the server will use the default value of "previous"
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete Note
        api_response = api_instance.delete_note_notes_notes_note_id_delete(note_id)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling NotesApi->delete_note_notes_notes_note_id_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Note
        api_response = api_instance.delete_note_notes_notes_note_id_delete(note_id, method=method, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling NotesApi->delete_note_notes_notes_note_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **str**|  |
 **method** | **str**|  | [optional] if omitted the server will use the default value of "previous"
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

# **get_note_notes_notes_note_id_get**
> bool, date, datetime, dict, float, int, list, str, none_type get_note_notes_notes_note_id_get(note_id)

Get Note

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import notes_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = notes_api.NotesApi(api_client)
    note_id = "note_id_example" # str | 
    history = 0 # int |  (optional) if omitted the server will use the default value of 0
    history_content = True # bool |  (optional) if omitted the server will use the default value of True
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Note
        api_response = api_instance.get_note_notes_notes_note_id_get(note_id)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling NotesApi->get_note_notes_notes_note_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Note
        api_response = api_instance.get_note_notes_notes_note_id_get(note_id, history=history, history_content=history_content, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling NotesApi->get_note_notes_notes_note_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **str**|  |
 **history** | **int**|  | [optional] if omitted the server will use the default value of 0
 **history_content** | **bool**|  | [optional] if omitted the server will use the default value of True
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

# **update_note_notes_notes_note_id_put**
> NoteDynamo update_note_notes_notes_note_id_put(note_id, body_update_note_notes_notes_note_id_put)

Update Note

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import notes_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.body_update_note_notes_notes_note_id_put import BodyUpdateNoteNotesNotesNoteIdPut
from ehelply-python-sdk.model.note_dynamo import NoteDynamo
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = notes_api.NotesApi(api_client)
    note_id = "note_id_example" # str | 
    body_update_note_notes_notes_note_id_put = BodyUpdateNoteNotesNotesNoteIdPut(
        note=NoteBase(
            content="content_example",
            time="time_example",
            meta=NoteMeta(
                original_author="original_author_example",
                author="author_example",
                previous_version="previous_version_example",
                next_version="next_version_example",
            ),
        ),
    ) # BodyUpdateNoteNotesNotesNoteIdPut | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Note
        api_response = api_instance.update_note_notes_notes_note_id_put(note_id, body_update_note_notes_notes_note_id_put)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling NotesApi->update_note_notes_notes_note_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Note
        api_response = api_instance.update_note_notes_notes_note_id_put(note_id, body_update_note_notes_notes_note_id_put, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling NotesApi->update_note_notes_notes_note_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **str**|  |
 **body_update_note_notes_notes_note_id_put** | [**BodyUpdateNoteNotesNotesNoteIdPut**](BodyUpdateNoteNotesNotesNoteIdPut.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**NoteDynamo**](NoteDynamo.md)

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

