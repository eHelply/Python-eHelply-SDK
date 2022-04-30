# coding: utf-8

"""
    eHelply SDK - 1.1.74

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.74
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401

from frozendict import frozendict  # noqa: F401

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


class BodyCreateKeySecurityKeysPost(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    _required_property_names = set((
        'key',
    ))

    @classmethod
    @property
    def key(cls) -> typing.Type['SecurityKeyCreate']:
        return SecurityKeyCreate


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        key: key,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'BodyCreateKeySecurityKeysPost':
        return super().__new__(
            cls,
            *args,
            key=key,
            _configuration=_configuration,
            **kwargs,
        )

from ehelply_python_sdk.model.security_key_create import SecurityKeyCreate
