"""
    eHelply SDK - 1.1.115

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.115
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
from ehelply_python_sdk.model.category_base import CategoryBase
from ehelply_python_sdk.model.category_response import CategoryResponse
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError
from ehelply_python_sdk.model.page import Page


class CategoryApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_category_places_categories_post_endpoint = _Endpoint(
            settings={
                'response_type': (CategoryResponse,),
                'auth': [],
                'endpoint_path': '/places/categories',
                'operation_id': 'create_category_places_categories_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'category_base',
                    'x_access_token',
                    'x_secret_token',
                    'authorization',
                    'ehelply_active_participant',
                    'ehelply_project',
                    'ehelply_data',
                ],
                'required': [
                    'category_base',
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
                    'category_base':
                        (CategoryBase,),
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
                    'category_base': 'body',
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
        self.delete_category_places_categories_category_uuid_delete_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [],
                'endpoint_path': '/places/categories/{category_uuid}',
                'operation_id': 'delete_category_places_categories_category_uuid_delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'category_uuid',
                    'x_access_token',
                    'x_secret_token',
                    'authorization',
                    'ehelply_active_participant',
                    'ehelply_project',
                    'ehelply_data',
                ],
                'required': [
                    'category_uuid',
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
                    'category_uuid':
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
                    'category_uuid': 'category_uuid',
                    'x_access_token': 'x-access-token',
                    'x_secret_token': 'x-secret-token',
                    'authorization': 'authorization',
                    'ehelply_active_participant': 'ehelply-active-participant',
                    'ehelply_project': 'ehelply-project',
                    'ehelply_data': 'ehelply-data',
                },
                'location_map': {
                    'category_uuid': 'path',
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
        self.get_category_places_categories_category_uuid_get_endpoint = _Endpoint(
            settings={
                'response_type': (CategoryResponse,),
                'auth': [],
                'endpoint_path': '/places/categories/{category_uuid}',
                'operation_id': 'get_category_places_categories_category_uuid_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'category_uuid',
                    'with_meta',
                    'x_access_token',
                    'x_secret_token',
                    'authorization',
                    'ehelply_active_participant',
                    'ehelply_project',
                    'ehelply_data',
                ],
                'required': [
                    'category_uuid',
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
                    'category_uuid':
                        (str,),
                    'with_meta':
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
                    'category_uuid': 'category_uuid',
                    'with_meta': 'with_meta',
                    'x_access_token': 'x-access-token',
                    'x_secret_token': 'x-secret-token',
                    'authorization': 'authorization',
                    'ehelply_active_participant': 'ehelply-active-participant',
                    'ehelply_project': 'ehelply-project',
                    'ehelply_data': 'ehelply-data',
                },
                'location_map': {
                    'category_uuid': 'path',
                    'with_meta': 'query',
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
        self.search_categories_places_categories_get_endpoint = _Endpoint(
            settings={
                'response_type': (Page,),
                'auth': [],
                'endpoint_path': '/places/categories',
                'operation_id': 'search_categories_places_categories_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_uuid',
                    'name',
                    'with_meta',
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
                    'with_meta':
                        (bool,),
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
                    'with_meta': 'with_meta',
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
                    'with_meta': 'query',
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
        self.update_category_places_categories_category_uuid_put_endpoint = _Endpoint(
            settings={
                'response_type': (CategoryBase,),
                'auth': [],
                'endpoint_path': '/places/categories/{category_uuid}',
                'operation_id': 'update_category_places_categories_category_uuid_put',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'category_uuid',
                    'category_base',
                    'x_access_token',
                    'x_secret_token',
                    'authorization',
                    'ehelply_active_participant',
                    'ehelply_project',
                    'ehelply_data',
                ],
                'required': [
                    'category_uuid',
                    'category_base',
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
                    'category_uuid':
                        (str,),
                    'category_base':
                        (CategoryBase,),
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
                    'category_uuid': 'category_uuid',
                    'x_access_token': 'x-access-token',
                    'x_secret_token': 'x-secret-token',
                    'authorization': 'authorization',
                    'ehelply_active_participant': 'ehelply-active-participant',
                    'ehelply_project': 'ehelply-project',
                    'ehelply_data': 'ehelply-data',
                },
                'location_map': {
                    'category_uuid': 'path',
                    'category_base': 'body',
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

    def create_category_places_categories_post(
        self,
        category_base,
        **kwargs
    ):
        """Create Category  # noqa: E501

        Creates a category  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_category_places_categories_post(category_base, async_req=True)
        >>> result = thread.get()

        Args:
            category_base (CategoryBase):

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
            CategoryResponse
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
        kwargs['category_base'] = \
            category_base
        return self.create_category_places_categories_post_endpoint.call_with_http_info(**kwargs)

    def delete_category_places_categories_category_uuid_delete(
        self,
        category_uuid,
        **kwargs
    ):
        """Delete Category  # noqa: E501

        Deletes the category with the given ID and returns True if successful  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_category_places_categories_category_uuid_delete(category_uuid, async_req=True)
        >>> result = thread.get()

        Args:
            category_uuid (str):

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
            bool, date, datetime, dict, float, int, list, str, none_type
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
        kwargs['category_uuid'] = \
            category_uuid
        return self.delete_category_places_categories_category_uuid_delete_endpoint.call_with_http_info(**kwargs)

    def get_category_places_categories_category_uuid_get(
        self,
        category_uuid,
        **kwargs
    ):
        """Get Category  # noqa: E501

        Gets the category information given the category ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_category_places_categories_category_uuid_get(category_uuid, async_req=True)
        >>> result = thread.get()

        Args:
            category_uuid (str):

        Keyword Args:
            with_meta (bool): [optional] if omitted the server will use the default value of False
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
            CategoryResponse
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
        kwargs['category_uuid'] = \
            category_uuid
        return self.get_category_places_categories_category_uuid_get_endpoint.call_with_http_info(**kwargs)

    def search_categories_places_categories_get(
        self,
        **kwargs
    ):
        """Search Categories  # noqa: E501

        TODO Item return format: ``` {     uuid                                **type:** string     project_uuid                        **type:** string or None      name                                **type:** string or None      meta                                **type:** dict or None      created_at                          **type:** string or None      updated_at                          **type:** string or None      deleted_at                          **type:** string or None  } ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_categories_places_categories_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            project_uuid (str): [optional]
            name (str): [optional]
            with_meta (bool): [optional] if omitted the server will use the default value of False
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
        return self.search_categories_places_categories_get_endpoint.call_with_http_info(**kwargs)

    def update_category_places_categories_category_uuid_put(
        self,
        category_uuid,
        category_base,
        **kwargs
    ):
        """Update Category  # noqa: E501

        Update category with given info, only updating the fields supplied. Category Uuid must be sent however.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_category_places_categories_category_uuid_put(category_uuid, category_base, async_req=True)
        >>> result = thread.get()

        Args:
            category_uuid (str):
            category_base (CategoryBase):

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
            CategoryBase
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
        kwargs['category_uuid'] = \
            category_uuid
        kwargs['category_base'] = \
            category_base
        return self.update_category_places_categories_category_uuid_put_endpoint.call_with_http_info(**kwargs)

