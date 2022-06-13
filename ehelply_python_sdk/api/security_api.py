# coding: utf-8

"""
    eHelply SDK - 1.1.90

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.90
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""

from ehelply_python_sdk.api_client import ApiClient
from ehelply_python_sdk.api.security_api_endpoints.create_encryption_key import CreateEncryptionKey
from ehelply_python_sdk.api.security_api_endpoints.create_key import CreateKey
from ehelply_python_sdk.api.security_api_endpoints.delete_key import DeleteKey
from ehelply_python_sdk.api.security_api_endpoints.generate_token import GenerateToken
from ehelply_python_sdk.api.security_api_endpoints.get_encryption_key import GetEncryptionKey
from ehelply_python_sdk.api.security_api_endpoints.get_key import GetKey
from ehelply_python_sdk.api.security_api_endpoints.search_keys import SearchKeys
from ehelply_python_sdk.api.security_api_endpoints.verify_key import VerifyKey


class SecurityApi(
    CreateEncryptionKey,
    CreateKey,
    DeleteKey,
    GenerateToken,
    GetEncryptionKey,
    GetKey,
    SearchKeys,
    VerifyKey,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
