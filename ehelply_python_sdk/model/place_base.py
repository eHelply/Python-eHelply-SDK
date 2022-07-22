# coding: utf-8

"""
    eHelply SDK - 1.1.88

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.88
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


class PlaceBase(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    **:param** name                                **type:** string
**:param** summary                             **type:** string or None

**:param** public                              **type:** bool or None

**:param** meta                                **type:** dict or None

**:param** addresses                           **type:** PlaceAddress or None

**:param** contact                             **type:** ContactBase or None
    """
    _required_property_names = set((
        'name',
    ))
    name = StrSchema
    summary = StrSchema
    public = BoolSchema
    meta = DictSchema
    
    
    class addresses(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['AddressBase']:
            return AddressBase

    @classmethod
    @property
    def contact(cls) -> typing.Type['ContactBase']:
        return ContactBase


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        name: name,
        summary: typing.Union[summary, Unset] = unset,
        public: typing.Union[public, Unset] = unset,
        meta: typing.Union[meta, Unset] = unset,
        addresses: typing.Union[addresses, Unset] = unset,
        contact: typing.Union['ContactBase', Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'PlaceBase':
        return super().__new__(
            cls,
            *args,
            name=name,
            summary=summary,
            public=public,
            meta=meta,
            addresses=addresses,
            contact=contact,
            _configuration=_configuration,
            **kwargs,
        )

from ehelply_python_sdk.model.address_base import AddressBase
from ehelply_python_sdk.model.contact_base import ContactBase
