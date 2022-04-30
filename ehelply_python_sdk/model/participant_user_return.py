# coding: utf-8

"""
    eHelply SDK - 1.1.87

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.87
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


class ParticipantUserReturn(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Contains all fields required when doing a Participant GET but also has user fields (name, location, ect). This is
what is returned from all participant endpoints.
    """
    uuid = StrSchema
    user_uuid = StrSchema
    participant_meta = DictSchema
    first_name = StrSchema
    last_name = StrSchema
    
    
    class email(
        ComposedSchema
    ):
    
        @classmethod
        @property
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
                    UserEmail,
                ],
                'oneOf': [
                ],
                'anyOf': [
                ],
            }
    
        def __new__(
            cls,
            *args: typing.Union[dict, frozendict, str, date, datetime, int, float, decimal.Decimal, None, list, tuple, bytes],
            _configuration: typing.Optional[Configuration] = None,
            **kwargs: typing.Type[Schema],
        ) -> 'email':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
                **kwargs,
            )
    phone_number = StrSchema
    country = StrSchema
    gps_location = DictSchema
    picture = StrSchema
    last_login = DateTimeSchema
    verified_legal_terms = BoolSchema
    date_created = DateTimeSchema
    date_updated = DateTimeSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        uuid: typing.Union[uuid, Unset] = unset,
        user_uuid: typing.Union[user_uuid, Unset] = unset,
        participant_meta: typing.Union[participant_meta, Unset] = unset,
        first_name: typing.Union[first_name, Unset] = unset,
        last_name: typing.Union[last_name, Unset] = unset,
        email: typing.Union[email, Unset] = unset,
        phone_number: typing.Union[phone_number, Unset] = unset,
        country: typing.Union[country, Unset] = unset,
        gps_location: typing.Union[gps_location, Unset] = unset,
        picture: typing.Union[picture, Unset] = unset,
        last_login: typing.Union[last_login, Unset] = unset,
        verified_legal_terms: typing.Union[verified_legal_terms, Unset] = unset,
        date_created: typing.Union[date_created, Unset] = unset,
        date_updated: typing.Union[date_updated, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'ParticipantUserReturn':
        return super().__new__(
            cls,
            *args,
            uuid=uuid,
            user_uuid=user_uuid,
            participant_meta=participant_meta,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            country=country,
            gps_location=gps_location,
            picture=picture,
            last_login=last_login,
            verified_legal_terms=verified_legal_terms,
            date_created=date_created,
            date_updated=date_updated,
            _configuration=_configuration,
            **kwargs,
        )

from ehelply_python_sdk.model.user_email import UserEmail
