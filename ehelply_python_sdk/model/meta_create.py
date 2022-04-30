# coding: utf-8

"""
    eHelply SDK - 1.1.70

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.70
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


class MetaCreate(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Meta
    """

    @classmethod
    @property
    def basic(cls) -> typing.Type['BasicMetaCreate']:
        return BasicMetaCreate

    @classmethod
    @property
    def detailed(cls) -> typing.Type['DetailedMetaCreate']:
        return DetailedMetaCreate

    @classmethod
    @property
    def custom(cls) -> typing.Type['MetaCustom']:
        return MetaCustom
    
    
    class fields(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['Field']:
            return Field
    
    
    class children(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['MetaChildren']:
            return MetaChildren
    parent_uuid = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        basic: typing.Union['BasicMetaCreate', Unset] = unset,
        detailed: typing.Union['DetailedMetaCreate', Unset] = unset,
        custom: typing.Union['MetaCustom', Unset] = unset,
        fields: typing.Union[fields, Unset] = unset,
        children: typing.Union[children, Unset] = unset,
        parent_uuid: typing.Union[parent_uuid, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'MetaCreate':
        return super().__new__(
            cls,
            *args,
            basic=basic,
            detailed=detailed,
            custom=custom,
            fields=fields,
            children=children,
            parent_uuid=parent_uuid,
            _configuration=_configuration,
            **kwargs,
        )

from ehelply_python_sdk.model.basic_meta_create import BasicMetaCreate
from ehelply_python_sdk.model.detailed_meta_create import DetailedMetaCreate
from ehelply_python_sdk.model.field import Field
from ehelply_python_sdk.model.meta_children import MetaChildren
from ehelply_python_sdk.model.meta_custom import MetaCustom
