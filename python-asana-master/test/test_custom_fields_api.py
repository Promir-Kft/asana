# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import asana
from asana.api.custom_fields_api import CustomFieldsApi  # noqa: E501
from asana.rest import ApiException


class TestCustomFieldsApi(unittest.TestCase):
    """CustomFieldsApi unit test stubs"""

    def setUp(self):
        self.api = CustomFieldsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_custom_field(self):
        """Test case for create_custom_field

        Create a custom field  # noqa: E501
        """
        pass

    def test_create_enum_option_for_custom_field(self):
        """Test case for create_enum_option_for_custom_field

        Create an enum option  # noqa: E501
        """
        pass

    def test_delete_custom_field(self):
        """Test case for delete_custom_field

        Delete a custom field  # noqa: E501
        """
        pass

    def test_get_custom_field(self):
        """Test case for get_custom_field

        Get a custom field  # noqa: E501
        """
        pass

    def test_get_custom_fields_for_workspace(self):
        """Test case for get_custom_fields_for_workspace

        Get a workspace's custom fields  # noqa: E501
        """
        pass

    def test_insert_enum_option_for_custom_field(self):
        """Test case for insert_enum_option_for_custom_field

        Reorder a custom field's enum  # noqa: E501
        """
        pass

    def test_update_custom_field(self):
        """Test case for update_custom_field

        Update a custom field  # noqa: E501
        """
        pass

    def test_update_enum_option(self):
        """Test case for update_enum_option

        Update an enum option  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
