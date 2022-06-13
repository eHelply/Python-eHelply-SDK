# coding: utf-8

"""
    eHelply SDK - 1.1.78

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.78
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


class NotesHTTPValidationError(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    
    class detail(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['NotesValidationError']:
            return NotesValidationError


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        detail: typing.Union[detail, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'NotesHTTPValidationError':
        return super().__new__(
            cls,
            *args,
            detail=detail,
            _configuration=_configuration,
            **kwargs,
        )

from ehelply_python_sdk.model.notes_validation_error import NotesValidationError
