# coding: utf-8

"""
    eHelply SDK - 1.1.95

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.95
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""

from ehelply_python_sdk.api_client import ApiClient
from ehelply_python_sdk.api.places_api_endpoints.create_place_places_places_post import CreatePlacePlacesPlacesPost
from ehelply_python_sdk.api.places_api_endpoints.delete_place_places_places_place_uuid_delete import DeletePlacePlacesPlacesPlaceUuidDelete
from ehelply_python_sdk.api.places_api_endpoints.forward_geocoding_places_geocoding_forward_get import ForwardGeocodingPlacesGeocodingForwardGet
from ehelply_python_sdk.api.places_api_endpoints.get_place_places_places_place_uuid_get import GetPlacePlacesPlacesPlaceUuidGet
from ehelply_python_sdk.api.places_api_endpoints.reverse_geocoding_places_geocoding_reverse_get import ReverseGeocodingPlacesGeocodingReverseGet
from ehelply_python_sdk.api.places_api_endpoints.search_places_by_search_string_places_search_places_string_get import SearchPlacesBySearchStringPlacesSearchPlacesStringGet
from ehelply_python_sdk.api.places_api_endpoints.search_places_places_places_get import SearchPlacesPlacesPlacesGet
from ehelply_python_sdk.api.places_api_endpoints.update_place_places_places_place_uuid_put import UpdatePlacePlacesPlacesPlaceUuidPut


class PlacesApi(
    CreatePlacePlacesPlacesPost,
    DeletePlacePlacesPlacesPlaceUuidDelete,
    ForwardGeocodingPlacesGeocodingForwardGet,
    GetPlacePlacesPlacesPlaceUuidGet,
    ReverseGeocodingPlacesGeocodingReverseGet,
    SearchPlacesBySearchStringPlacesSearchPlacesStringGet,
    SearchPlacesPlacesPlacesGet,
    UpdatePlacePlacesPlacesPlaceUuidPut,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
