# ehelply-python-sdk.SupportApi

All URIs are relative to *https://api.prod.ehelply.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contact_support_contact_post**](SupportApi.md#create_contact_support_contact_post) | **POST** /sam/support/contact | Create Contact
[**create_ticket_support_projects_project_uuid_members_member_uuid_tickets_post**](SupportApi.md#create_ticket_support_projects_project_uuid_members_member_uuid_tickets_post) | **POST** /sam/support/projects/{project_uuid}/members/{member_uuid}/tickets | Create Ticket
[**delete_contact_support_contact_delete**](SupportApi.md#delete_contact_support_contact_delete) | **DELETE** /sam/support/contact | Delete Contact
[**list_tickets_support_projects_project_uuid_members_member_uuid_tickets_get**](SupportApi.md#list_tickets_support_projects_project_uuid_members_member_uuid_tickets_get) | **GET** /sam/support/projects/{project_uuid}/members/{member_uuid}/tickets | List Tickets
[**update_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_put**](SupportApi.md#update_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_put) | **PUT** /sam/support/projects/{project_uuid}/members/{member_uuid}/tickets/{ticket_id} | Update Ticket
[**view_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_get**](SupportApi.md#view_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_get) | **GET** /sam/support/projects/{project_uuid}/members/{member_uuid}/tickets/{ticket_id} | View Ticket


# **create_contact_support_contact_post**
> ContactResponse create_contact_support_contact_post(contact)

Create Contact

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import support_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.contact import Contact
from ehelply-python-sdk.model.contact_response import ContactResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = support_api.SupportApi(api_client)
    contact = Contact(
        first_name="first_name_example",
        last_name="last_name_example",
        email="email_example",
        phone="phone_example",
    ) # Contact | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Contact
        api_response = api_instance.create_contact_support_contact_post(contact)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling SupportApi->create_contact_support_contact_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Contact
        api_response = api_instance.create_contact_support_contact_post(contact, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling SupportApi->create_contact_support_contact_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact** | [**Contact**](Contact.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**ContactResponse**](ContactResponse.md)

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

# **create_ticket_support_projects_project_uuid_members_member_uuid_tickets_post**
> TicketResponse create_ticket_support_projects_project_uuid_members_member_uuid_tickets_post(project_uuid, member_uuid, create_ticket)

Create Ticket

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import support_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.create_ticket import CreateTicket
from ehelply-python-sdk.model.ticket_response import TicketResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = support_api.SupportApi(api_client)
    project_uuid = "project_uuid_example" # str | 
    member_uuid = "member_uuid_example" # str | 
    create_ticket = CreateTicket(
        priority="priority_example",
        subject="subject_example",
    ) # CreateTicket | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Ticket
        api_response = api_instance.create_ticket_support_projects_project_uuid_members_member_uuid_tickets_post(project_uuid, member_uuid, create_ticket)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling SupportApi->create_ticket_support_projects_project_uuid_members_member_uuid_tickets_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Ticket
        api_response = api_instance.create_ticket_support_projects_project_uuid_members_member_uuid_tickets_post(project_uuid, member_uuid, create_ticket, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling SupportApi->create_ticket_support_projects_project_uuid_members_member_uuid_tickets_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**|  |
 **member_uuid** | **str**|  |
 **create_ticket** | [**CreateTicket**](CreateTicket.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**TicketResponse**](TicketResponse.md)

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

# **delete_contact_support_contact_delete**
> bool, date, datetime, dict, float, int, list, str, none_type delete_contact_support_contact_delete()

Delete Contact

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import support_api
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
    api_instance = support_api.SupportApi(api_client)
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Contact
        api_response = api_instance.delete_contact_support_contact_delete(x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling SupportApi->delete_contact_support_contact_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **list_tickets_support_projects_project_uuid_members_member_uuid_tickets_get**
> [TicketsResponse] list_tickets_support_projects_project_uuid_members_member_uuid_tickets_get(project_uuid, member_uuid)

List Tickets

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import support_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.tickets_response import TicketsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = support_api.SupportApi(api_client)
    project_uuid = "project_uuid_example" # str | 
    member_uuid = "member_uuid_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Tickets
        api_response = api_instance.list_tickets_support_projects_project_uuid_members_member_uuid_tickets_get(project_uuid, member_uuid)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling SupportApi->list_tickets_support_projects_project_uuid_members_member_uuid_tickets_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Tickets
        api_response = api_instance.list_tickets_support_projects_project_uuid_members_member_uuid_tickets_get(project_uuid, member_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling SupportApi->list_tickets_support_projects_project_uuid_members_member_uuid_tickets_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**|  |
 **member_uuid** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**[TicketsResponse]**](TicketsResponse.md)

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
**404** | Record does not exist |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_put**
> TicketResponse update_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_put(project_uuid, member_uuid, ticket_id, create_ticket)

Update Ticket

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import support_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.create_ticket import CreateTicket
from ehelply-python-sdk.model.ticket_response import TicketResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = support_api.SupportApi(api_client)
    project_uuid = "project_uuid_example" # str | 
    member_uuid = "member_uuid_example" # str | 
    ticket_id = "ticket_id_example" # str | 
    create_ticket = CreateTicket(
        priority="priority_example",
        subject="subject_example",
    ) # CreateTicket | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Ticket
        api_response = api_instance.update_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_put(project_uuid, member_uuid, ticket_id, create_ticket)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling SupportApi->update_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Ticket
        api_response = api_instance.update_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_put(project_uuid, member_uuid, ticket_id, create_ticket, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling SupportApi->update_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**|  |
 **member_uuid** | **str**|  |
 **ticket_id** | **str**|  |
 **create_ticket** | [**CreateTicket**](CreateTicket.md)|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**TicketResponse**](TicketResponse.md)

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

# **view_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_get**
> TicketResponse view_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_get(project_uuid, member_uuid, ticket_id)

View Ticket

### Example


```python
import time
import ehelply-python-sdk
from ehelply-python-sdk.api import support_api
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError
from ehelply-python-sdk.model.ticket_response import TicketResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply-python-sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply-python-sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = support_api.SupportApi(api_client)
    project_uuid = "project_uuid_example" # str | 
    member_uuid = "member_uuid_example" # str | 
    ticket_id = "ticket_id_example" # str | 
    x_access_token = "x-access-token_example" # str |  (optional)
    x_secret_token = "x-secret-token_example" # str |  (optional)
    authorization = "authorization_example" # str |  (optional)
    ehelply_active_participant = "ehelply-active-participant_example" # str |  (optional)
    ehelply_project = "ehelply-project_example" # str |  (optional)
    ehelply_data = "ehelply-data_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # View Ticket
        api_response = api_instance.view_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_get(project_uuid, member_uuid, ticket_id)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling SupportApi->view_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # View Ticket
        api_response = api_instance.view_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_get(project_uuid, member_uuid, ticket_id, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply-python-sdk.ApiException as e:
        print("Exception when calling SupportApi->view_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | **str**|  |
 **member_uuid** | **str**|  |
 **ticket_id** | **str**|  |
 **x_access_token** | **str**|  | [optional]
 **x_secret_token** | **str**|  | [optional]
 **authorization** | **str**|  | [optional]
 **ehelply_active_participant** | **str**|  | [optional]
 **ehelply_project** | **str**|  | [optional]
 **ehelply_data** | **str**|  | [optional]

### Return type

[**TicketResponse**](TicketResponse.md)

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

