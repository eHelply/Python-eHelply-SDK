"""
    eHelply SDK - 1.1.107

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.107
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
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.page import Page
from ehelply_python_sdk.model.tag_base import TagBase
from ehelply_python_sdk.model.tag_db import TagDb


class TagsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_tag_endpoint = _Endpoint(
            settings={
                'response_type': (TagDb,),
                'auth': [],
                'endpoint_path': '/places/tags',
                'operation_id': 'create_tag',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'tag_base',
                    'x_access_token',
                    'x_secret_token',
                    'authorization',
                    'ehelply_active_participant',
                    'ehelply_project',
                    'ehelply_data',
                ],
                'required': [
                    'tag_base',
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
                    'tag_base':
                        (TagBase,),
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
                    'tag_base': 'body',
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
        self.get_tag_endpoint = _Endpoint(
            settings={
                'response_type': (TagBase,),
                'auth': [],
                'endpoint_path': '/places/tags/{tag_uuid}',
                'operation_id': 'get_tag',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'tag_uuid',
                    'x_access_token',
                    'x_secret_token',
                    'authorization',
                    'ehelply_active_participant',
                    'ehelply_project',
                    'ehelply_data',
                ],
                'required': [
                    'tag_uuid',
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
                    'tag_uuid':
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
                    'tag_uuid': 'tag_uuid',
                    'x_access_token': 'x-access-token',
                    'x_secret_token': 'x-secret-token',
                    'authorization': 'authorization',
                    'ehelply_active_participant': 'ehelply-active-participant',
                    'ehelply_project': 'ehelply-project',
                    'ehelply_data': 'ehelply-data',
                },
                'location_map': {
                    'tag_uuid': 'path',
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
        self.search_tag_endpoint = _Endpoint(
            settings={
                'response_type': (Page,),
                'auth': [],
                'endpoint_path': '/places/tags',
                'operation_id': 'search_tag',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_uuid',
                    'name',
                    'page',
                    'page_size',
                    'sort_on',
                    'sort_desc',
                    'x_access_token',
                    'x_secret_token',
                    'authorization',
                    'ehelply_active_participant',
                    'ehelply_project',
                    'ehelply_data',
                ],
                'required': [],
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
                    'name':
                        (str,),
                    'page':
                        (int,),
                    'page_size':
                        (int,),
                    'sort_on':
                        (str,),
                    'sort_desc':
                        (bool,),
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
                    'name': 'name',
                    'page': 'page',
                    'page_size': 'page_size',
                    'sort_on': 'sort_on',
                    'sort_desc': 'sort_desc',
                    'x_access_token': 'x-access-token',
                    'x_secret_token': 'x-secret-token',
                    'authorization': 'authorization',
                    'ehelply_active_participant': 'ehelply-active-participant',
                    'ehelply_project': 'ehelply-project',
                    'ehelply_data': 'ehelply-data',
                },
                'location_map': {
                    'project_uuid': 'query',
                    'name': 'query',
                    'page': 'query',
                    'page_size': 'query',
                    'sort_on': 'query',
                    'sort_desc': 'query',
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
        self.update_tag_endpoint = _Endpoint(
            settings={
                'response_type': (TagBase,),
                'auth': [],
                'endpoint_path': '/places/tags/{tag_uuid}',
                'operation_id': 'update_tag',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'tag_uuid',
                    'tag_base',
                    'x_access_token',
                    'x_secret_token',
                    'authorization',
                    'ehelply_active_participant',
                    'ehelply_project',
                    'ehelply_data',
                ],
                'required': [
                    'tag_uuid',
                    'tag_base',
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
                    'tag_uuid':
                        (str,),
                    'tag_base':
                        (TagBase,),
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
                    'tag_uuid': 'tag_uuid',
                    'x_access_token': 'x-access-token',
                    'x_secret_token': 'x-secret-token',
                    'authorization': 'authorization',
                    'ehelply_active_participant': 'ehelply-active-participant',
                    'ehelply_project': 'ehelply-project',
                    'ehelply_data': 'ehelply-data',
                },
                'location_map': {
                    'tag_uuid': 'path',
                    'tag_base': 'body',
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

    def create_tag(
        self,
        tag_base,
        **kwargs
    ):
        """Createtag  # noqa: E501

        Creates a tag  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_tag(tag_base, async_req=True)
        >>> result = thread.get()

        Args:
            tag_base (TagBase):

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
            TagDb
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
        kwargs['tag_base'] = \
            tag_base
        return self.create_tag_endpoint.call_with_http_info(**kwargs)

    def get_tag(
        self,
        tag_uuid,
        **kwargs
    ):
        """Gettag  # noqa: E501

        Gets the tag member information given the tag ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_tag(tag_uuid, async_req=True)
        >>> result = thread.get()

        Args:
            tag_uuid (str):

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
            TagBase
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
        kwargs['tag_uuid'] = \
            tag_uuid
        return self.get_tag_endpoint.call_with_http_info(**kwargs)

    def search_tag(
        self,
        **kwargs
    ):
        """Searchtag  # noqa: E501

        TODO Item return format: ``` {     uuid                                **type:** string     project_uuid                        **type:** string or None      name                                **type:** string or None      meta                                **type:** dict or None      created_at                          **type:** string or None      updated_at                          **type:** string or None      deleted_at                          **type:** string or None  } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_tag(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            project_uuid (str): [optional]
            name (str): [optional]
            page (int): [optional] if omitted the server will use the default value of 1
            page_size (int): [optional] if omitted the server will use the default value of 25
            sort_on (str): [optional]
            sort_desc (bool): [optional] if omitted the server will use the default value of False
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
            Page
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
        return self.search_tag_endpoint.call_with_http_info(**kwargs)

    def update_tag(
        self,
        tag_uuid,
        tag_base,
        **kwargs
    ):
        """Updatetag  # noqa: E501

        Update tag with given info, only updating the fields supplied. Tag Uuid must be sent however.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_tag(tag_uuid, tag_base, async_req=True)
        >>> result = thread.get()

        Args:
            tag_uuid (str):
            tag_base (TagBase):

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
            TagBase
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
        kwargs['tag_uuid'] = \
            tag_uuid
        kwargs['tag_base'] = \
            tag_base
        return self.update_tag_endpoint.call_with_http_info(**kwargs)

