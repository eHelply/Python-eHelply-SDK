# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import re  # noqa: F401
import sys  # noqa: F401
import typing
import urllib3
from urllib3._collections import HTTPHeaderDict

from ehelply_python_sdk import api_client, exceptions
import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from ehelply_python_sdk.schemas import (  # noqa: F401
    AnyTypeSchema,
    ComposedSchema,
    DictSchema,
    ListSchema,
    StrSchema,
    IntSchema,
    Int32Schema,
    Int64Schema,
    Float32Schema,
    Float64Schema,
    NumberSchema,
    DateSchema,
    DateTimeSchema,
    DecimalSchema,
    BoolSchema,
    BinarySchema,
    NoneSchema,
    none_type,
    Configuration,
    Unset,
    unset,
    ComposedBase,
    ListBase,
    DictBase,
    NoneBase,
    StrBase,
    IntBase,
    Int32Base,
    Int64Base,
    Float32Base,
    Float64Base,
    NumberBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    BinaryBase,
    Schema,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker
)

from ehelply_python_sdk.model.inline_response403 import InlineResponse403
from ehelply_python_sdk.model.inline_response2005 import InlineResponse2005
from ehelply_python_sdk.model.http_validation_error import HTTPValidationError

# header params
XAccessTokenSchema = StrSchema
XSecretTokenSchema = StrSchema
AuthorizationSchema = StrSchema
EhelplyActiveParticipantSchema = StrSchema
EhelplyProjectSchema = StrSchema
EhelplyDataSchema = StrSchema
RequestRequiredHeaderParams = typing.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'x-access-token': XAccessTokenSchema,
        'x-secret-token': XSecretTokenSchema,
        'authorization': AuthorizationSchema,
        'ehelply-active-participant': EhelplyActiveParticipantSchema,
        'ehelply-project': EhelplyProjectSchema,
        'ehelply-data': EhelplyDataSchema,
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_x_access_token = api_client.HeaderParameter(
    name="x-access-token",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XAccessTokenSchema,
)
request_header_x_secret_token = api_client.HeaderParameter(
    name="x-secret-token",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XSecretTokenSchema,
)
request_header_authorization = api_client.HeaderParameter(
    name="authorization",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AuthorizationSchema,
)
request_header_ehelply_active_participant = api_client.HeaderParameter(
    name="ehelply-active-participant",
    style=api_client.ParameterStyle.SIMPLE,
    schema=EhelplyActiveParticipantSchema,
)
request_header_ehelply_project = api_client.HeaderParameter(
    name="ehelply-project",
    style=api_client.ParameterStyle.SIMPLE,
    schema=EhelplyProjectSchema,
)
request_header_ehelply_data = api_client.HeaderParameter(
    name="ehelply-data",
    style=api_client.ParameterStyle.SIMPLE,
    schema=EhelplyDataSchema,
)
# path params
ProjectUuidSchema = StrSchema
EntityUuidSchema = StrSchema
RequestRequiredPathParams = typing.TypedDict(
    'RequestRequiredPathParams',
    {
        'project_uuid': ProjectUuidSchema,
        'entity_uuid': EntityUuidSchema,
    }
)
RequestOptionalPathParams = typing.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_project_uuid = api_client.PathParameter(
    name="project_uuid",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ProjectUuidSchema,
    required=True,
)
request_path_entity_uuid = api_client.PathParameter(
    name="entity_uuid",
    style=api_client.ParameterStyle.SIMPLE,
    schema=EntityUuidSchema,
    required=True,
)
_path = '/sam/projects/projects/{project_uuid}/members/{entity_uuid}'
_method = 'POST'
SchemaFor200ResponseBodyApplicationJson = InlineResponse2005


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
    ]
    headers: Unset = unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = InlineResponse403


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor403ResponseBodyApplicationJson,
    ]
    headers: Unset = unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = InlineResponse403


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor404ResponseBodyApplicationJson,
    ]
    headers: Unset = unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = HTTPValidationError


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor422ResponseBodyApplicationJson,
    ]
    headers: Unset = unset


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '403': _response_for_403,
    '404': _response_for_404,
    '422': _response_for_422,
}
_all_accept_content_types = (
    'application/json',
)


class AddMemberToProjectProjectsProjectsProjectUuidMembersEntityUuidPost(api_client.Api):

    def add_member_to_project_projects_projects_project_uuid_members_entity_uuid_post(
        self: api_client.Api,
        header_params: RequestHeaderParams = frozendict(),
        path_params: RequestPathParams = frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        """
        Add Member To Project
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs(RequestPathParams, path_params)

        _path_params = {}
        for parameter in (
            request_path_project_uuid,
            request_path_entity_uuid,
        ):
            parameter_data = path_params.get(parameter.name, unset)
            if parameter_data is unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_x_access_token,
            request_header_x_secret_token,
            request_header_authorization,
            request_header_ehelply_active_participant,
            request_header_ehelply_project,
            request_header_ehelply_data,
        ):
            parameter_data = header_params.get(parameter.name, unset)
            if parameter_data is unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=_path,
            method=_method,
            path_params=_path_params,
            headers=_headers,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response
