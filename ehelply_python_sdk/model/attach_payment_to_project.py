# coding: utf-8

"""
    eHelply SDK - 1.1.84

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.84
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


class AttachPaymentToProject(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    _required_property_names = set((
        'payment_type',
        'number',
        'exp_month',
        'exp_year',
        'cvc',
    ))
    payment_type = StrSchema
    number = StrSchema
    exp_month = IntSchema
    exp_year = IntSchema
    cvc = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        payment_type: payment_type,
        number: number,
        exp_month: exp_month,
        exp_year: exp_year,
        cvc: cvc,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'AttachPaymentToProject':
        return super().__new__(
            cls,
            *args,
            payment_type=payment_type,
            number=number,
            exp_month=exp_month,
            exp_year=exp_year,
            cvc=cvc,
            _configuration=_configuration,
            **kwargs,
        )
