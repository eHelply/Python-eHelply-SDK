# coding: utf-8

"""
    eHelply SDK - 1.1.87

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.87
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""

from ehelply_python_sdk.api_client import ApiClient
from ehelply_python_sdk.api.category_api_endpoints.create_category_places_categories_post import CreateCategoryPlacesCategoriesPost
from ehelply_python_sdk.api.category_api_endpoints.delete_category_places_categories_category_uuid_delete import DeleteCategoryPlacesCategoriesCategoryUuidDelete
from ehelply_python_sdk.api.category_api_endpoints.get_category_places_categories_category_uuid_get import GetCategoryPlacesCategoriesCategoryUuidGet
from ehelply_python_sdk.api.category_api_endpoints.search_categories_places_categories_get import SearchCategoriesPlacesCategoriesGet
from ehelply_python_sdk.api.category_api_endpoints.update_category_places_categories_category_uuid_put import UpdateCategoryPlacesCategoriesCategoryUuidPut


class CategoryApi(
    CreateCategoryPlacesCategoriesPost,
    DeleteCategoryPlacesCategoriesCategoryUuidDelete,
    GetCategoryPlacesCategoriesCategoryUuidGet,
    SearchCategoriesPlacesCategoriesGet,
    UpdateCategoryPlacesCategoriesCategoryUuidPut,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
