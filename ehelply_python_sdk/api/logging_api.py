# coding: utf-8

"""
    eHelply SDK - 1.1.84

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.84
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""

from ehelply_python_sdk.api_client import ApiClient
from ehelply_python_sdk.api.logging_api_endpoints.get_logs_logging_logs_get import GetLogsLoggingLogsGet
from ehelply_python_sdk.api.logging_api_endpoints.get_service_logs_logging_logs_services_service_get import GetServiceLogsLoggingLogsServicesServiceGet
from ehelply_python_sdk.api.logging_api_endpoints.get_subject_logs_logging_logs_services_service_subjects_subject_get import GetSubjectLogsLoggingLogsServicesServiceSubjectsSubjectGet


class LoggingApi(
    GetLogsLoggingLogsGet,
    GetServiceLogsLoggingLogsServicesServiceGet,
    GetSubjectLogsLoggingLogsServicesServiceSubjectsSubjectGet,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
