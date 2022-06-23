# coding: utf-8

"""
    eHelply SDK - 1.1.81

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.81
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


class Options(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    required = BoolSchema
    label = StrSchema
    insetLabel = StrSchema
    placeholder = StrSchema
    hint = StrSchema
    icon = StrSchema
    maxLength = NumberSchema
    counter = BoolSchema
    caption = StrSchema
    color = StrSchema
    size = StrSchema
    type = StrSchema
    iconPosition = StrSchema
    
    
    class selections(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['OptionGroup']:
            return OptionGroup


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        required: typing.Union[required, Unset] = unset,
        label: typing.Union[label, Unset] = unset,
        insetLabel: typing.Union[insetLabel, Unset] = unset,
        placeholder: typing.Union[placeholder, Unset] = unset,
        hint: typing.Union[hint, Unset] = unset,
        icon: typing.Union[icon, Unset] = unset,
        maxLength: typing.Union[maxLength, Unset] = unset,
        counter: typing.Union[counter, Unset] = unset,
        caption: typing.Union[caption, Unset] = unset,
        color: typing.Union[color, Unset] = unset,
        size: typing.Union[size, Unset] = unset,
        type: typing.Union[type, Unset] = unset,
        iconPosition: typing.Union[iconPosition, Unset] = unset,
        selections: typing.Union[selections, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'Options':
        return super().__new__(
            cls,
            *args,
            required=required,
            label=label,
            insetLabel=insetLabel,
            placeholder=placeholder,
            hint=hint,
            icon=icon,
            maxLength=maxLength,
            counter=counter,
            caption=caption,
            color=color,
            size=size,
            type=type,
            iconPosition=iconPosition,
            selections=selections,
            _configuration=_configuration,
            **kwargs,
        )

from ehelply_python_sdk.model.option_group import OptionGroup
