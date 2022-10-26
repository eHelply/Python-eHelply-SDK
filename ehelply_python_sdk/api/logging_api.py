"""
    eHelply SDK - 1.1.116

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.116
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
from ehelply_python_sdk.model.logging_dynamo import LoggingDynamo


class LoggingApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_subject_logs_endpoint = _Endpoint(
            settings={
                'response_type': ([LoggingDynamo],),
                'auth': [],
                'endpoint_path': '/sam/logging/logs/services/{service}/subjects/{subject}',
                'operation_id': 'get_subject_logs',
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

    def get_subject_logs(
        self,
        service,
        subject,
        **kwargs
    ):
        """Getsubjectlogs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_subject_logs(service, subject, async_req=True)
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
            [LoggingDynamo]
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
        kwargs['service'] = \
            service
        kwargs['subject'] = \
            subject
        return self.get_subject_logs_endpoint.call_with_http_info(**kwargs)

