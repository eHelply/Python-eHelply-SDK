# ehelply_python_sdk.SupportApi

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
import ehelply_python_sdk
from ehelply_python_sdk.api import support_api
from ehelply_python_sdk.model.inline_response403 import InlineResponse403
from ehelply_python_sdk.model.contact import Contact
from ehelply_python_sdk.model.contact_response import ContactResponse
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
    api_instance = support_api.SupportApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = Contact(
        first_name="first_name_example",
        last_name="last_name_example",
        email="email_example",
        phone="phone_example",
    )
    try:
        # Create Contact
        api_response = api_instance.create_contact_support_contact_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SupportApi->create_contact_support_contact_post: %s\n" % e)

    # example passing only optional values
    header_params = {
        'x-access-token': "x-access-token_example",
        'x-secret-token': "x-secret-token_example",
        'authorization': "authorization_example",
        'ehelply-active-participant': "ehelply-active-participant_example",
        'ehelply-project': "ehelply-project_example",
        'ehelply-data': "ehelply-data_example",
    }
    body = Contact(
        first_name="first_name_example",
        last_name="last_name_example",
        email="email_example",
        phone="phone_example",
    )
    try:
        # Create Contact
        api_response = api_instance.create_contact_support_contact_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SupportApi->create_contact_support_contact_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Contact**](Contact.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
x-access-token | XAccessTokenSchema | | optional
x-secret-token | XSecretTokenSchema | | optional
authorization | AuthorizationSchema | | optional
ehelply-active-participant | EhelplyActiveParticipantSchema | | optional
ehelply-project | EhelplyProjectSchema | | optional
ehelply-data | EhelplyDataSchema | | optional

#### XAccessTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### XSecretTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AuthorizationSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyActiveParticipantSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyProjectSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyDataSchema

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
[**ContactResponse**](ContactResponse.md) |  | 


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



[**ContactResponse**](ContactResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ticket_support_projects_project_uuid_members_member_uuid_tickets_post**
> TicketResponse create_ticket_support_projects_project_uuid_members_member_uuid_tickets_post(project_uuidmember_uuidcreate_ticket)

Create Ticket

### Example

```python
import ehelply_python_sdk
from ehelply_python_sdk.api import support_api
from ehelply_python_sdk.model.inline_response403 import InlineResponse403
from ehelply_python_sdk.model.create_ticket import CreateTicket
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.ticket_response import TicketResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = support_api.SupportApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'project_uuid': "project_uuid_example",
        'member_uuid': "member_uuid_example",
    }
    header_params = {
    }
    body = CreateTicket(
        priority="priority_example",
        subject="subject_example",
    )
    try:
        # Create Ticket
        api_response = api_instance.create_ticket_support_projects_project_uuid_members_member_uuid_tickets_post(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SupportApi->create_ticket_support_projects_project_uuid_members_member_uuid_tickets_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'project_uuid': "project_uuid_example",
        'member_uuid': "member_uuid_example",
    }
    header_params = {
        'x-access-token': "x-access-token_example",
        'x-secret-token': "x-secret-token_example",
        'authorization': "authorization_example",
        'ehelply-active-participant': "ehelply-active-participant_example",
        'ehelply-project': "ehelply-project_example",
        'ehelply-data': "ehelply-data_example",
    }
    body = CreateTicket(
        priority="priority_example",
        subject="subject_example",
    )
    try:
        # Create Ticket
        api_response = api_instance.create_ticket_support_projects_project_uuid_members_member_uuid_tickets_post(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SupportApi->create_ticket_support_projects_project_uuid_members_member_uuid_tickets_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateTicket**](CreateTicket.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
x-access-token | XAccessTokenSchema | | optional
x-secret-token | XSecretTokenSchema | | optional
authorization | AuthorizationSchema | | optional
ehelply-active-participant | EhelplyActiveParticipantSchema | | optional
ehelply-project | EhelplyProjectSchema | | optional
ehelply-data | EhelplyDataSchema | | optional

#### XAccessTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### XSecretTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AuthorizationSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyActiveParticipantSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyProjectSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyDataSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_uuid | ProjectUuidSchema | | 
member_uuid | MemberUuidSchema | | 

#### ProjectUuidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### MemberUuidSchema

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
[**TicketResponse**](TicketResponse.md) |  | 


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



[**TicketResponse**](TicketResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact_support_contact_delete**
> bool, date, datetime, dict, float, int, list, str, none_type delete_contact_support_contact_delete()

Delete Contact

### Example

```python
import ehelply_python_sdk
from ehelply_python_sdk.api import support_api
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
    api_instance = support_api.SupportApi(api_client)

    # example passing only optional values
    header_params = {
        'x-access-token': "x-access-token_example",
        'x-secret-token': "x-secret-token_example",
        'authorization': "authorization_example",
        'ehelply-active-participant': "ehelply-active-participant_example",
        'ehelply-project': "ehelply-project_example",
        'ehelply-data': "ehelply-data_example",
    }
    try:
        # Delete Contact
        api_response = api_instance.delete_contact_support_contact_delete(
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SupportApi->delete_contact_support_contact_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
x-access-token | XAccessTokenSchema | | optional
x-secret-token | XSecretTokenSchema | | optional
authorization | AuthorizationSchema | | optional
ehelply-active-participant | EhelplyActiveParticipantSchema | | optional
ehelply-project | EhelplyProjectSchema | | optional
ehelply-data | EhelplyDataSchema | | optional

#### XAccessTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### XSecretTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AuthorizationSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyActiveParticipantSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyProjectSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyDataSchema

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

# **list_tickets_support_projects_project_uuid_members_member_uuid_tickets_get**
> [TicketsResponse] list_tickets_support_projects_project_uuid_members_member_uuid_tickets_get(project_uuidmember_uuid)

List Tickets

### Example

```python
import ehelply_python_sdk
from ehelply_python_sdk.api import support_api
from ehelply_python_sdk.model.inline_response403 import InlineResponse403
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.tickets_response import TicketsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = support_api.SupportApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'project_uuid': "project_uuid_example",
        'member_uuid': "member_uuid_example",
    }
    header_params = {
    }
    try:
        # List Tickets
        api_response = api_instance.list_tickets_support_projects_project_uuid_members_member_uuid_tickets_get(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SupportApi->list_tickets_support_projects_project_uuid_members_member_uuid_tickets_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'project_uuid': "project_uuid_example",
        'member_uuid': "member_uuid_example",
    }
    header_params = {
        'x-access-token': "x-access-token_example",
        'x-secret-token': "x-secret-token_example",
        'authorization': "authorization_example",
        'ehelply-active-participant': "ehelply-active-participant_example",
        'ehelply-project': "ehelply-project_example",
        'ehelply-data': "ehelply-data_example",
    }
    try:
        # List Tickets
        api_response = api_instance.list_tickets_support_projects_project_uuid_members_member_uuid_tickets_get(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SupportApi->list_tickets_support_projects_project_uuid_members_member_uuid_tickets_get: %s\n" % e)
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
x-access-token | XAccessTokenSchema | | optional
x-secret-token | XSecretTokenSchema | | optional
authorization | AuthorizationSchema | | optional
ehelply-active-participant | EhelplyActiveParticipantSchema | | optional
ehelply-project | EhelplyProjectSchema | | optional
ehelply-data | EhelplyDataSchema | | optional

#### XAccessTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### XSecretTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AuthorizationSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyActiveParticipantSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyProjectSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyDataSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_uuid | ProjectUuidSchema | | 
member_uuid | MemberUuidSchema | | 

#### ProjectUuidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### MemberUuidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | Successful Response 
403 | ApiResponseFor403 | Unauthorized - Denied by eHelply 
404 | ApiResponseFor404 | Record does not exist 
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
**[TicketsResponse]** |  | 

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



[**[TicketsResponse]**](TicketsResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_put**
> TicketResponse update_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_put(project_uuidmember_uuidticket_idcreate_ticket)

Update Ticket

### Example

```python
import ehelply_python_sdk
from ehelply_python_sdk.api import support_api
from ehelply_python_sdk.model.inline_response403 import InlineResponse403
from ehelply_python_sdk.model.create_ticket import CreateTicket
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.ticket_response import TicketResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = support_api.SupportApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'project_uuid': "project_uuid_example",
        'member_uuid': "member_uuid_example",
        'ticket_id': "ticket_id_example",
    }
    header_params = {
    }
    body = CreateTicket(
        priority="priority_example",
        subject="subject_example",
    )
    try:
        # Update Ticket
        api_response = api_instance.update_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_put(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SupportApi->update_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_put: %s\n" % e)

    # example passing only optional values
    path_params = {
        'project_uuid': "project_uuid_example",
        'member_uuid': "member_uuid_example",
        'ticket_id': "ticket_id_example",
    }
    header_params = {
        'x-access-token': "x-access-token_example",
        'x-secret-token': "x-secret-token_example",
        'authorization': "authorization_example",
        'ehelply-active-participant': "ehelply-active-participant_example",
        'ehelply-project': "ehelply-project_example",
        'ehelply-data': "ehelply-data_example",
    }
    body = CreateTicket(
        priority="priority_example",
        subject="subject_example",
    )
    try:
        # Update Ticket
        api_response = api_instance.update_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_put(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SupportApi->update_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateTicket**](CreateTicket.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
x-access-token | XAccessTokenSchema | | optional
x-secret-token | XSecretTokenSchema | | optional
authorization | AuthorizationSchema | | optional
ehelply-active-participant | EhelplyActiveParticipantSchema | | optional
ehelply-project | EhelplyProjectSchema | | optional
ehelply-data | EhelplyDataSchema | | optional

#### XAccessTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### XSecretTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AuthorizationSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyActiveParticipantSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyProjectSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyDataSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_uuid | ProjectUuidSchema | | 
member_uuid | MemberUuidSchema | | 
ticket_id | TicketIdSchema | | 

#### ProjectUuidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### MemberUuidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### TicketIdSchema

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
[**TicketResponse**](TicketResponse.md) |  | 


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



[**TicketResponse**](TicketResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **view_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_get**
> TicketResponse view_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_get(project_uuidmember_uuidticket_id)

View Ticket

### Example

```python
import ehelply_python_sdk
from ehelply_python_sdk.api import support_api
from ehelply_python_sdk.model.inline_response403 import InlineResponse403
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.ticket_response import TicketResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.ehelply.com
# See configuration.py for a list of all supported configuration parameters.
configuration = ehelply_python_sdk.Configuration(
    host = "https://api.prod.ehelply.com"
)

# Enter a context with an instance of the API client
with ehelply_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = support_api.SupportApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'project_uuid': "project_uuid_example",
        'member_uuid': "member_uuid_example",
        'ticket_id': "ticket_id_example",
    }
    header_params = {
    }
    try:
        # View Ticket
        api_response = api_instance.view_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_get(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SupportApi->view_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'project_uuid': "project_uuid_example",
        'member_uuid': "member_uuid_example",
        'ticket_id': "ticket_id_example",
    }
    header_params = {
        'x-access-token': "x-access-token_example",
        'x-secret-token': "x-secret-token_example",
        'authorization': "authorization_example",
        'ehelply-active-participant': "ehelply-active-participant_example",
        'ehelply-project': "ehelply-project_example",
        'ehelply-data': "ehelply-data_example",
    }
    try:
        # View Ticket
        api_response = api_instance.view_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_get(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except ehelply_python_sdk.ApiException as e:
        print("Exception when calling SupportApi->view_ticket_support_projects_project_uuid_members_member_uuid_tickets_ticket_id_get: %s\n" % e)
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
x-access-token | XAccessTokenSchema | | optional
x-secret-token | XSecretTokenSchema | | optional
authorization | AuthorizationSchema | | optional
ehelply-active-participant | EhelplyActiveParticipantSchema | | optional
ehelply-project | EhelplyProjectSchema | | optional
ehelply-data | EhelplyDataSchema | | optional

#### XAccessTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### XSecretTokenSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AuthorizationSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyActiveParticipantSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyProjectSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### EhelplyDataSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_uuid | ProjectUuidSchema | | 
member_uuid | MemberUuidSchema | | 
ticket_id | TicketIdSchema | | 

#### ProjectUuidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### MemberUuidSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### TicketIdSchema

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
[**TicketResponse**](TicketResponse.md) |  | 


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



[**TicketResponse**](TicketResponse.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

