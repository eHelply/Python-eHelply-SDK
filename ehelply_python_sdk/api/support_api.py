"""
    eHelply SDK - 1.1.118

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.118
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ehelply_python_sdk.api_client import ApiClient, Endpoint as _Endpoint
from ehelply_python_sdk.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from ehelply_python_sdk.model.contact import Contact
from ehelply_python_sdk.model.contact_response import ContactResponse
from ehelply_python_sdk.model.create_ticket import CreateTicket
from ehelply_python_sdk.model.get_appointment403_response import GetAppointment403Response
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.ticket_response import TicketResponse
from ehelply_python_sdk.model.tickets_response import TicketsResponse


class SupportApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_contact_endpoint = _Endpoint(
            settings={
                'response_type': (ContactResponse,),
                'auth': [],
                'endpoint_path': '/sam/support/contact',
                'operation_id': 'create_contact',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'contact',
                    'x_access_token',
                    'x_secret_token',
                    'authorization',
                    'ehelply_active_participant',
                    'ehelply_project',
                    'ehelply_data',
                ],
                'required': [
                    'contact',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'contact':
                        (Contact,),
                    'x_access_token':
                        (str,),
                    'x_secret_token':
                        (str,),
                    'authorization':
                        (str,),
                    'ehelply_active_participant':
                        (str,),
                    'ehelply_project':
                        (str,),
                    'ehelply_data':
                        (str,),
                },
                'attribute_map': {
                    'x_access_token': 'x-access-token',
                    'x_secret_token': 'x-secret-token',
                    'authorization': 'authorization',
                    'ehelply_active_participant': 'ehelply-active-participant',
                    'ehelply_project': 'ehelply-project',
                    'ehelply_data': 'ehelply-data',
                },
                'location_map': {
                    'contact': 'body',
                    'x_access_token': 'header',
                    'x_secret_token': 'header',
                    'authorization': 'header',
                    'ehelply_active_participant': 'header',
                    'ehelply_project': 'header',
                    'ehelply_data': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.create_ticket_endpoint = _Endpoint(
            settings={
                'response_type': (TicketResponse,),
                'auth': [],
                'endpoint_path': '/sam/support/projects/{project_uuid}/members/{member_uuid}/tickets',
                'operation_id': 'create_ticket',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_uuid',
                    'member_uuid',
                    'create_ticket',
                    'x_access_token',
                    'x_secret_token',
                    'authorization',
                    'ehelply_active_participant',
                    'ehelply_project',
                    'ehelply_data',
                ],
                'required': [
                    'project_uuid',
                    'member_uuid',
                    'create_ticket',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'project_uuid':
                        (str,),
                    'member_uuid':
                        (str,),
                    'create_ticket':
                        (CreateTicket,),
                    'x_access_token':
                        (str,),
                    'x_secret_token':
                        (str,),
                    'authorization':
                        (str,),
                    'ehelply_active_participant':
                        (str,),
                    'ehelply_project':
                        (str,),
                    'ehelply_data':
                        (str,),
                },
                'attribute_map': {
                    'project_uuid': 'project_uuid',
                    'member_uuid': 'member_uuid',
                    'x_access_token': 'x-access-token',
                    'x_secret_token': 'x-secret-token',
                    'authorization': 'authorization',
                    'ehelply_active_participant': 'ehelply-active-participant',
                    'ehelply_project': 'ehelply-project',
                    'ehelply_data': 'ehelply-data',
                },
                'location_map': {
                    'project_uuid': 'path',
                    'member_uuid': 'path',
                    'create_ticket': 'body',
                    'x_access_token': 'header',
                    'x_secret_token': 'header',
                    'authorization': 'header',
                    'ehelply_active_participant': 'header',
                    'ehelply_project': 'header',
                    'ehelply_data': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.list_tickets_endpoint = _Endpoint(
            settings={
                'response_type': ([TicketsResponse],),
                'auth': [],
                'endpoint_path': '/sam/support/projects/{project_uuid}/members/{member_uuid}/tickets',
                'operation_id': 'list_tickets',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_uuid',
                    'member_uuid',
                    'x_access_token',
                    'x_secret_token',
                    'authorization',
                    'ehelply_active_participant',
                    'ehelply_project',
                    'ehelply_data',
                ],
                'required': [
                    'project_uuid',
                    'member_uuid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'project_uuid':
                        (str,),
                    'member_uuid':
                        (str,),
                    'x_access_token':
                        (str,),
                    'x_secret_token':
                        (str,),
                    'authorization':
                        (str,),
                    'ehelply_active_participant':
                        (str,),
                    'ehelply_project':
                        (str,),
                    'ehelply_data':
                        (str,),
                },
                'attribute_map': {
                    'project_uuid': 'project_uuid',
                    'member_uuid': 'member_uuid',
                    'x_access_token': 'x-access-token',
                    'x_secret_token': 'x-secret-token',
                    'authorization': 'authorization',
                    'ehelply_active_participant': 'ehelply-active-participant',
                    'ehelply_project': 'ehelply-project',
                    'ehelply_data': 'ehelply-data',
                },
                'location_map': {
                    'project_uuid': 'path',
                    'member_uuid': 'path',
                    'x_access_token': 'header',
                    'x_secret_token': 'header',
                    'authorization': 'header',
                    'ehelply_active_participant': 'header',
                    'ehelply_project': 'header',
                    'ehelply_data': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.update_ticket_endpoint = _Endpoint(
            settings={
                'response_type': (TicketResponse,),
                'auth': [],
                'endpoint_path': '/sam/support/projects/{project_uuid}/members/{member_uuid}/tickets/{ticket_id}',
                'operation_id': 'update_ticket',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_uuid',
                    'member_uuid',
                    'ticket_id',
                    'create_ticket',
                    'x_access_token',
                    'x_secret_token',
                    'authorization',
                    'ehelply_active_participant',
                    'ehelply_project',
                    'ehelply_data',
                ],
                'required': [
                    'project_uuid',
                    'member_uuid',
                    'ticket_id',
                    'create_ticket',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'project_uuid':
                        (str,),
                    'member_uuid':
                        (str,),
                    'ticket_id':
                        (str,),
                    'create_ticket':
                        (CreateTicket,),
                    'x_access_token':
                        (str,),
                    'x_secret_token':
                        (str,),
                    'authorization':
                        (str,),
                    'ehelply_active_participant':
                        (str,),
                    'ehelply_project':
                        (str,),
                    'ehelply_data':
                        (str,),
                },
                'attribute_map': {
                    'project_uuid': 'project_uuid',
                    'member_uuid': 'member_uuid',
                    'ticket_id': 'ticket_id',
                    'x_access_token': 'x-access-token',
                    'x_secret_token': 'x-secret-token',
                    'authorization': 'authorization',
                    'ehelply_active_participant': 'ehelply-active-participant',
                    'ehelply_project': 'ehelply-project',
                    'ehelply_data': 'ehelply-data',
                },
                'location_map': {
                    'project_uuid': 'path',
                    'member_uuid': 'path',
                    'ticket_id': 'path',
                    'create_ticket': 'body',
                    'x_access_token': 'header',
                    'x_secret_token': 'header',
                    'authorization': 'header',
                    'ehelply_active_participant': 'header',
                    'ehelply_project': 'header',
                    'ehelply_data': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.view_ticket_endpoint = _Endpoint(
            settings={
                'response_type': (TicketResponse,),
                'auth': [],
                'endpoint_path': '/sam/support/projects/{project_uuid}/members/{member_uuid}/tickets/{ticket_id}',
                'operation_id': 'view_ticket',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_uuid',
                    'member_uuid',
                    'ticket_id',
                    'x_access_token',
                    'x_secret_token',
                    'authorization',
                    'ehelply_active_participant',
                    'ehelply_project',
                    'ehelply_data',
                ],
                'required': [
                    'project_uuid',
                    'member_uuid',
                    'ticket_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'project_uuid':
                        (str,),
                    'member_uuid':
                        (str,),
                    'ticket_id':
                        (str,),
                    'x_access_token':
                        (str,),
                    'x_secret_token':
                        (str,),
                    'authorization':
                        (str,),
                    'ehelply_active_participant':
                        (str,),
                    'ehelply_project':
                        (str,),
                    'ehelply_data':
                        (str,),
                },
                'attribute_map': {
                    'project_uuid': 'project_uuid',
                    'member_uuid': 'member_uuid',
                    'ticket_id': 'ticket_id',
                    'x_access_token': 'x-access-token',
                    'x_secret_token': 'x-secret-token',
                    'authorization': 'authorization',
                    'ehelply_active_participant': 'ehelply-active-participant',
                    'ehelply_project': 'ehelply-project',
                    'ehelply_data': 'ehelply-data',
                },
                'location_map': {
                    'project_uuid': 'path',
                    'member_uuid': 'path',
                    'ticket_id': 'path',
                    'x_access_token': 'header',
                    'x_secret_token': 'header',
                    'authorization': 'header',
                    'ehelply_active_participant': 'header',
                    'ehelply_project': 'header',
                    'ehelply_data': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def create_contact(
        self,
        contact,
        **kwargs
    ):
        """Createcontact  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_contact(contact, async_req=True)
        >>> result = thread.get()

        Args:
            contact (Contact):

        Keyword Args:
            x_access_token (str): [optional]
            x_secret_token (str): [optional]
            authorization (str): [optional]
            ehelply_active_participant (str): [optional]
            ehelply_project (str): [optional]
            ehelply_data (str): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ContactResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['contact'] = \
            contact
        return self.create_contact_endpoint.call_with_http_info(**kwargs)

    def create_ticket(
        self,
        project_uuid,
        member_uuid,
        create_ticket,
        **kwargs
    ):
        """Createticket  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_ticket(project_uuid, member_uuid, create_ticket, async_req=True)
        >>> result = thread.get()

        Args:
            project_uuid (str):
            member_uuid (str):
            create_ticket (CreateTicket):

        Keyword Args:
            x_access_token (str): [optional]
            x_secret_token (str): [optional]
            authorization (str): [optional]
            ehelply_active_participant (str): [optional]
            ehelply_project (str): [optional]
            ehelply_data (str): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            TicketResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['project_uuid'] = \
            project_uuid
        kwargs['member_uuid'] = \
            member_uuid
        kwargs['create_ticket'] = \
            create_ticket
        return self.create_ticket_endpoint.call_with_http_info(**kwargs)

    def list_tickets(
        self,
        project_uuid,
        member_uuid,
        **kwargs
    ):
        """Listtickets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_tickets(project_uuid, member_uuid, async_req=True)
        >>> result = thread.get()

        Args:
            project_uuid (str):
            member_uuid (str):

        Keyword Args:
            x_access_token (str): [optional]
            x_secret_token (str): [optional]
            authorization (str): [optional]
            ehelply_active_participant (str): [optional]
            ehelply_project (str): [optional]
            ehelply_data (str): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            [TicketsResponse]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['project_uuid'] = \
            project_uuid
        kwargs['member_uuid'] = \
            member_uuid
        return self.list_tickets_endpoint.call_with_http_info(**kwargs)

    def update_ticket(
        self,
        project_uuid,
        member_uuid,
        ticket_id,
        create_ticket,
        **kwargs
    ):
        """Updateticket  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_ticket(project_uuid, member_uuid, ticket_id, create_ticket, async_req=True)
        >>> result = thread.get()

        Args:
            project_uuid (str):
            member_uuid (str):
            ticket_id (str):
            create_ticket (CreateTicket):

        Keyword Args:
            x_access_token (str): [optional]
            x_secret_token (str): [optional]
            authorization (str): [optional]
            ehelply_active_participant (str): [optional]
            ehelply_project (str): [optional]
            ehelply_data (str): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            TicketResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['project_uuid'] = \
            project_uuid
        kwargs['member_uuid'] = \
            member_uuid
        kwargs['ticket_id'] = \
            ticket_id
        kwargs['create_ticket'] = \
            create_ticket
        return self.update_ticket_endpoint.call_with_http_info(**kwargs)

    def view_ticket(
        self,
        project_uuid,
        member_uuid,
        ticket_id,
        **kwargs
    ):
        """Viewticket  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.view_ticket(project_uuid, member_uuid, ticket_id, async_req=True)
        >>> result = thread.get()

        Args:
            project_uuid (str):
            member_uuid (str):
            ticket_id (str):

        Keyword Args:
            x_access_token (str): [optional]
            x_secret_token (str): [optional]
            authorization (str): [optional]
            ehelply_active_participant (str): [optional]
            ehelply_project (str): [optional]
            ehelply_data (str): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            TicketResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['project_uuid'] = \
            project_uuid
        kwargs['member_uuid'] = \
            member_uuid
        kwargs['ticket_id'] = \
            ticket_id
        return self.view_ticket_endpoint.call_with_http_info(**kwargs)

