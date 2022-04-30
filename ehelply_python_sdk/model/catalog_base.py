# coding: utf-8

"""
    eHelply SDK - 1.1.72

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.72
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


class CatalogBase(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    meta_data = DictSchema
    name = StrSchema
    featured = DictSchema
    sub_catalogs = DictSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        meta_data: typing.Union[meta_data, Unset] = unset,
        name: typing.Union[name, Unset] = unset,
        featured: typing.Union[featured, Unset] = unset,
        sub_catalogs: typing.Union[sub_catalogs, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'CatalogBase':
        return super().__new__(
            cls,
            *args,
            meta_data=meta_data,
            name=name,
            featured=featured,
            sub_catalogs=sub_catalogs,
            _configuration=_configuration,
            **kwargs,
        )
