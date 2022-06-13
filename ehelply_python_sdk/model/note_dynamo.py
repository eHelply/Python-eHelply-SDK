# coding: utf-8

"""
    eHelply SDK - 1.1.89

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.89
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401
import functools  # noqa: F401

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
    UUIDSchema,
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
    UUIDBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    BinaryBase,
    Schema,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker
)


class NoteDynamo(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A note from DynamoDB
    """
    _required_property_names = set((
        'uuid',
        'time',
        'meta',
    ))
    uuid = StrSchema
    content = BinarySchema
    time = StrSchema

    @classmethod
    @property
    def meta(cls) -> typing.Type['NoteMeta']:
        return NoteMeta


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        uuid: uuid,
        time: time,
        meta: meta,
        content: typing.Union[content, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'NoteDynamo':
        return super().__new__(
            cls,
            *args,
            uuid=uuid,
            time=time,
            meta=meta,
            content=content,
            _configuration=_configuration,
            **kwargs,
        )

from ehelply_python_sdk.model.note_meta import NoteMeta
