# coding: utf-8

"""
    eHelply SDK - 1.1.91

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.91
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


class MetaDynamo(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A meta from DynamoDB
    """
    _required_property_names = set((
        'uuid',
    ))
    
    
    class basic(
        ComposedSchema
    ):
    
        @classmethod
        @property
        @functools.cache
        def _composed_schemas(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return {
                'allOf': [
                    BasicMeta,
                ],
                'oneOf': [
                ],
                'anyOf': [
                ],
                'not':
                    None
            }
    
        def __new__(
            cls,
            *args: typing.Union[dict, frozendict, str, date, datetime, int, float, decimal.Decimal, None, list, tuple, bytes],
            _configuration: typing.Optional[Configuration] = None,
            **kwargs: typing.Type[Schema],
        ) -> 'basic':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
                **kwargs,
            )
    
    
    class detailed(
        ComposedSchema
    ):
    
        @classmethod
        @property
        @functools.cache
        def _composed_schemas(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return {
                'allOf': [
                    DetailedMeta,
                ],
                'oneOf': [
                ],
                'anyOf': [
                ],
                'not':
                    None
            }
    
        def __new__(
            cls,
            *args: typing.Union[dict, frozendict, str, date, datetime, int, float, decimal.Decimal, None, list, tuple, bytes],
            _configuration: typing.Optional[Configuration] = None,
            **kwargs: typing.Type[Schema],
        ) -> 'detailed':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
                **kwargs,
            )

    @classmethod
    @property
    def custom(cls) -> typing.Type['MetaCustom']:
        return MetaCustom

    @classmethod
    @property
    def dates(cls) -> typing.Type['DatesMeta']:
        return DatesMeta
    
    
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
    uuid = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        uuid: uuid,
        basic: typing.Union[basic, Unset] = unset,
        detailed: typing.Union[detailed, Unset] = unset,
        custom: typing.Union['MetaCustom', Unset] = unset,
        dates: typing.Union['DatesMeta', Unset] = unset,
        fields: typing.Union[fields, Unset] = unset,
        children: typing.Union[children, Unset] = unset,
        parent_uuid: typing.Union[parent_uuid, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'MetaDynamo':
        return super().__new__(
            cls,
            *args,
            uuid=uuid,
            basic=basic,
            detailed=detailed,
            custom=custom,
            dates=dates,
            fields=fields,
            children=children,
            parent_uuid=parent_uuid,
            _configuration=_configuration,
            **kwargs,
        )

from ehelply_python_sdk.model.basic_meta import BasicMeta
from ehelply_python_sdk.model.dates_meta import DatesMeta
from ehelply_python_sdk.model.detailed_meta import DetailedMeta
from ehelply_python_sdk.model.field import Field
from ehelply_python_sdk.model.meta_children import MetaChildren
from ehelply_python_sdk.model.meta_custom import MetaCustom
