# ehelply_python_sdk.SupportApi

All URIs are relative to *https://api.prod.ehelply.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contact**](SupportApi.md#create_contact) | **POST** /sam/support/contact | Createcontact
[**create_ticket**](SupportApi.md#create_ticket) | **POST** /sam/support/projects/{project_uuid}/members/{member_uuid}/tickets | Createticket
[**list_tickets**](SupportApi.md#list_tickets) | **GET** /sam/support/projects/{project_uuid}/members/{member_uuid}/tickets | Listtickets
[**update_ticket**](SupportApi.md#update_ticket) | **PUT** /sam/support/projects/{project_uuid}/members/{member_uuid}/tickets/{ticket_id} | Updateticket
[**view_ticket**](SupportApi.md#view_ticket) | **GET** /sam/support/projects/{project_uuid}/members/{member_uuid}/tickets/{ticket_id} | Viewticket


# **create_contact**
> ContactResponse create_contact(contact)

Createcontact

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import support_api
from ehelply_python_sdk.model.contact import Contact
from ehelply_python_sdk.model.contact_response import ContactResponse
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
        # Createcontact
        api_response = api_instance.create_contact(contact)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SupportApi->create_contact: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Createcontact
        api_response = api_instance.create_contact(contact, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SupportApi->create_contact: %s\n" % e)
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

# **create_ticket**
> TicketResponse create_ticket(project_uuid, member_uuid, create_ticket)

Createticket

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import support_api
from ehelply_python_sdk.model.create_ticket import CreateTicket
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.get_services_with_specs403_response import GetServicesWithSpecs403Response
from ehelply_python_sdk.model.ticket_response import TicketResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
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
        # Createticket
        api_response = api_instance.create_ticket(project_uuid, member_uuid, create_ticket)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SupportApi->create_ticket: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Createticket
        api_response = api_instance.create_ticket(project_uuid, member_uuid, create_ticket, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SupportApi->create_ticket: %s\n" % e)
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

# **list_tickets**
> [TicketsResponse] list_tickets(project_uuid, member_uuid)

Listtickets

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import support_api
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.get_services_with_specs403_response import GetServicesWithSpecs403Response
from ehelply_python_sdk.model.tickets_response import TicketsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
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
        # Listtickets
        api_response = api_instance.list_tickets(project_uuid, member_uuid)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SupportApi->list_tickets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Listtickets
        api_response = api_instance.list_tickets(project_uuid, member_uuid, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SupportApi->list_tickets: %s\n" % e)
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

# **update_ticket**
> TicketResponse update_ticket(project_uuid, member_uuid, ticket_id, create_ticket)

Updateticket

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import support_api
from ehelply_python_sdk.model.create_ticket import CreateTicket
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.get_services_with_specs403_response import GetServicesWithSpecs403Response
from ehelply_python_sdk.model.ticket_response import TicketResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
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
        # Updateticket
        api_response = api_instance.update_ticket(project_uuid, member_uuid, ticket_id, create_ticket)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SupportApi->update_ticket: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updateticket
        api_response = api_instance.update_ticket(project_uuid, member_uuid, ticket_id, create_ticket, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SupportApi->update_ticket: %s\n" % e)
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

# **view_ticket**
> TicketResponse view_ticket(project_uuid, member_uuid, ticket_id)

Viewticket

### Example


```python
import time
import ehelply_python_sdk
from ehelply_python_sdk.api import support_api
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.get_services_with_specs403_response import GetServicesWithSpecs403Response
from ehelply_python_sdk.model.ticket_response import TicketResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)


# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient() as api_client:
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
        # Viewticket
        api_response = api_instance.view_ticket(project_uuid, member_uuid, ticket_id)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SupportApi->view_ticket: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Viewticket
        api_response = api_instance.view_ticket(project_uuid, member_uuid, ticket_id, x_access_token=x_access_token, x_secret_token=x_secret_token, authorization=authorization, ehelply_active_participant=ehelply_active_participant, ehelply_project=ehelply_project, ehelply_data=ehelply_data)
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SupportApi->view_ticket: %s\n" % e)
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

