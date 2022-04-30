# coding: utf-8

"""
    eHelply SDK - 1.1.73

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.73
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""

from ehelply_python_sdk.api_client import ApiClient
from ehelply_python_sdk.api.users_api_endpoints.confirm_signup import ConfirmSignup
from ehelply_python_sdk.api.users_api_endpoints.create_participant import CreateParticipant
from ehelply_python_sdk.api.users_api_endpoints.create_user import CreateUser
from ehelply_python_sdk.api.users_api_endpoints.delete_participant import DeleteParticipant
from ehelply_python_sdk.api.users_api_endpoints.delete_user import DeleteUser
from ehelply_python_sdk.api.users_api_endpoints.get_participant import GetParticipant
from ehelply_python_sdk.api.users_api_endpoints.get_user import GetUser
from ehelply_python_sdk.api.users_api_endpoints.login import Login
from ehelply_python_sdk.api.users_api_endpoints.refresh_token import RefreshToken
from ehelply_python_sdk.api.users_api_endpoints.reset_password import ResetPassword
from ehelply_python_sdk.api.users_api_endpoints.reset_password_confirmation_users_auth_password_reset_confirm_post import ResetPasswordConfirmationUsersAuthPasswordResetConfirmPost
from ehelply_python_sdk.api.users_api_endpoints.search_participants import SearchParticipants
from ehelply_python_sdk.api.users_api_endpoints.signup import Signup
from ehelply_python_sdk.api.users_api_endpoints.update_participant import UpdateParticipant
from ehelply_python_sdk.api.users_api_endpoints.update_user import UpdateUser
from ehelply_python_sdk.api.users_api_endpoints.user_validations import UserValidations


class UsersApi(
    ConfirmSignup,
    CreateParticipant,
    CreateUser,
    DeleteParticipant,
    DeleteUser,
    GetParticipant,
    GetUser,
    Login,
    RefreshToken,
    ResetPassword,
    ResetPasswordConfirmationUsersAuthPasswordResetConfirmPost,
    SearchParticipants,
    Signup,
    UpdateParticipant,
    UpdateUser,
    UserValidations,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
