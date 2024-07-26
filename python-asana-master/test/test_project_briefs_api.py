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
from asana.api.project_briefs_api import ProjectBriefsApi  # noqa: E501
from asana.rest import ApiException


class TestProjectBriefsApi(unittest.TestCase):
    """ProjectBriefsApi unit test stubs"""

    def setUp(self):
        self.api = ProjectBriefsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_project_brief(self):
        """Test case for create_project_brief

        Create a project brief  # noqa: E501
        """
        pass

    def test_delete_project_brief(self):
        """Test case for delete_project_brief

        Delete a project brief  # noqa: E501
        """
        pass

    def test_get_project_brief(self):
        """Test case for get_project_brief

        Get a project brief  # noqa: E501
        """
        pass

    def test_update_project_brief(self):
        """Test case for update_project_brief

        Update a project brief  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
