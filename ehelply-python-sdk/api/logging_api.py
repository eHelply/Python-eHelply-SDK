"""
    eHelply SDK

    eHelply SDK  # noqa: E501

    The version of the OpenAPI document: 1.1.30
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ehelply-python-sdk.api_client import ApiClient, Endpoint as _Endpoint
from ehelply-python-sdk.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from ehelply-python-sdk.model.http_validation_error import HTTPValidationError


class LoggingApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_logs_logging_logs_get_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [],
                'endpoint_path': '/sam/logging/logs',
                'operation_id': 'get_logs_logging_logs_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'service',
                    'date_start',
                    'date_end',
                    'desc',
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
                    'service':
                        (str,),
                    'date_start':
                        (str,),
                    'date_end':
                        (str,),
                    'desc':
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
                    'service': 'service',
                    'date_start': 'date_start',
                    'date_end': 'date_end',
                    'desc': 'desc',
                    'x_access_token': 'x-access-token',
                    'x_secret_token': 'x-secret-token',
                    'authorization': 'authorization',
                    'ehelply_active_participant': 'ehelply-active-participant',
                    'ehelply_project': 'ehelply-project',
                    'ehelply_data': 'ehelply-data',
                },
                'location_map': {
                    'service': 'query',
                    'date_start': 'query',
                    'date_end': 'query',
                    'desc': 'query',
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
        self.get_service_logs_logging_logs_services_service_get_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [],
                'endpoint_path': '/sam/logging/logs/services/{service}',
                'operation_id': 'get_service_logs_logging_logs_services_service_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'service',
                    'date_start',
                    'date_end',
                    'desc',
                    'limit',
                    'x_access_token',
                    'x_secret_token',
                    'authorization',
                    'ehelply_active_participant',
                    'ehelply_project',
                    'ehelply_data',
                ],
                'required': [
                    'service',
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
                    'service':
                        (str,),
                    'date_start':
                        (str,),
                    'date_end':
                        (str,),
                    'desc':
                        (bool,),
                    'limit':
                        (int,),
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
                    'service': 'service',
                    'date_start': 'date_start',
                    'date_end': 'date_end',
                    'desc': 'desc',
                    'limit': 'limit',
                    'x_access_token': 'x-access-token',
                    'x_secret_token': 'x-secret-token',
                    'authorization': 'authorization',
                    'ehelply_active_participant': 'ehelply-active-participant',
                    'ehelply_project': 'ehelply-project',
                    'ehelply_data': 'ehelply-data',
                },
                'location_map': {
                    'service': 'path',
                    'date_start': 'query',
                    'date_end': 'query',
                    'desc': 'query',
                    'limit': 'query',
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
        self.get_subject_logs_logging_logs_services_service_subjects_subject_get_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [],
                'endpoint_path': '/sam/logging/logs/services/{service}/subjects/{subject}',
                'operation_id': 'get_subject_logs_logging_logs_services_service_subjects_subject_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'service',
                    'subject',
                    'date_start',
                    'date_end',
                    'desc',
                    'limit',
                    'x_access_token',
                    'x_secret_token',
                    'authorization',
                    'ehelply_active_participant',
                    'ehelply_project',
                    'ehelply_data',
                ],
                'required': [
                    'service',
                    'subject',
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
                    'service':
                        (str,),
                    'subject':
                        (str,),
                    'date_start':
                        (str,),
                    'date_end':
                        (str,),
                    'desc':
                        (bool,),
                    'limit':
                        (int,),
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
                    'service': 'service',
                    'subject': 'subject',
                    'date_start': 'date_start',
                    'date_end': 'date_end',
                    'desc': 'desc',
                    'limit': 'limit',
                    'x_access_token': 'x-access-token',
                    'x_secret_token': 'x-secret-token',
                    'authorization': 'authorization',
                    'ehelply_active_participant': 'ehelply-active-participant',
                    'ehelply_project': 'ehelply-project',
                    'ehelply_data': 'ehelply-data',
                },
                'location_map': {
                    'service': 'path',
                    'subject': 'path',
                    'date_start': 'query',
                    'date_end': 'query',
                    'desc': 'query',
                    'limit': 'query',
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

    def get_logs_logging_logs_get(
        self,
        **kwargs
    ):
        """Get Logs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_logs_logging_logs_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            service (str): [optional]
            date_start (str): [optional]
            date_end (str): [optional]
            desc (bool): [optional] if omitted the server will use the default value of True
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
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
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
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.get_logs_logging_logs_get_endpoint.call_with_http_info(**kwargs)

    def get_service_logs_logging_logs_services_service_get(
        self,
        service,
        **kwargs
    ):
        """Get Service Logs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_service_logs_logging_logs_services_service_get(service, async_req=True)
        >>> result = thread.get()

        Args:
            service (str):

        Keyword Args:
            date_start (str): [optional]
            date_end (str): [optional]
            desc (bool): [optional] if omitted the server will use the default value of True
            limit (int): [optional] if omitted the server will use the default value of 50
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
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
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
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['service'] = \
            service
        return self.get_service_logs_logging_logs_services_service_get_endpoint.call_with_http_info(**kwargs)

    def get_subject_logs_logging_logs_services_service_subjects_subject_get(
        self,
        service,
        subject,
        **kwargs
    ):
        """Get Subject Logs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_subject_logs_logging_logs_services_service_subjects_subject_get(service, subject, async_req=True)
        >>> result = thread.get()

        Args:
            service (str):
            subject (str):

        Keyword Args:
            date_start (str): [optional]
            date_end (str): [optional]
            desc (bool): [optional] if omitted the server will use the default value of True
            limit (int): [optional] if omitted the server will use the default value of 50
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
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
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
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['service'] = \
            service
        kwargs['subject'] = \
            subject
        return self.get_subject_logs_logging_logs_services_service_subjects_subject_get_endpoint.call_with_http_info(**kwargs)

