# coding: utf-8

"""
    eHelply SDK - 1.1.78

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.78
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""

import unittest

import ehelply_python_sdk
from ehelply_python_sdk.api.places_api import PlacesApi  # noqa: E501


class TestPlacesApi(unittest.TestCase):
    """PlacesApi unit test stubs"""

    def setUp(self):
        self.api = PlacesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_place_places_places_post(self):
        """Test case for create_place_places_places_post

        Create Place  # noqa: E501
        """
        pass

    def test_delete_place_places_places_place_uuid_delete(self):
        """Test case for delete_place_places_places_place_uuid_delete

        Delete Place  # noqa: E501
        """
        pass

    def test_forward_geocoding_places_geocoding_forward_get(self):
        """Test case for forward_geocoding_places_geocoding_forward_get

        Forward Geocoding  # noqa: E501
        """
        pass

    def test_get_place_places_places_place_uuid_get(self):
        """Test case for get_place_places_places_place_uuid_get

        Get Place  # noqa: E501
        """
        pass

    def test_reverse_geocoding_places_geocoding_reverse_get(self):
        """Test case for reverse_geocoding_places_geocoding_reverse_get

        Reverse Geocoding  # noqa: E501
        """
        pass

    def test_search_places_by_search_string_places_search_places_string_get(self):
        """Test case for search_places_by_search_string_places_search_places_string_get

        Search Places By Search String  # noqa: E501
        """
        pass

    def test_search_places_places_places_get(self):
        """Test case for search_places_places_places_get

        Search Places  # noqa: E501
        """
        pass

    def test_update_place_places_places_place_uuid_put(self):
        """Test case for update_place_places_places_place_uuid_put

        Update Place  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
