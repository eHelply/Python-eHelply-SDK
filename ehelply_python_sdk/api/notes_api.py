# coding: utf-8

"""
    eHelply SDK - 1.1.76

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.76
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""

from ehelply_python_sdk.api_client import ApiClient
from ehelply_python_sdk.api.notes_api_endpoints.create_note import CreateNote
from ehelply_python_sdk.api.notes_api_endpoints.delete_note import DeleteNote
from ehelply_python_sdk.api.notes_api_endpoints.get_note import GetNote
from ehelply_python_sdk.api.notes_api_endpoints.update_note import UpdateNote


class NotesApi(
    CreateNote,
    DeleteNote,
    GetNote,
    UpdateNote,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
