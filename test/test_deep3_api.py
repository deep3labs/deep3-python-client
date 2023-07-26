# coding: utf-8

"""
    Deep3 Labs API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import deep3
from deep3.api.deep3_api import Deep3Api  # noqa: E501
from deep3.rest import ApiException


class TestDeep3Api(unittest.TestCase):
    """Deep3Api unit test stubs"""

    def setUp(self):
        self.api = deep3.api.deep3_api.Deep3Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_chains(self):
        """Test case for get_chains

        Get currently supported chains and the active machine learning models  # noqa: E501
        """
        pass

    def test_get_hodler_prediction(self):
        """Test case for get_hodler_prediction

        Get a Hodler prediction  # noqa: E501
        """
        pass

    def test_get_models(self):
        """Test case for get_models

        Get active machine learning models and the chains they support  # noqa: E501
        """
        pass

    def test_get_prediction(self):
        """Test case for get_prediction

        Get a prediction  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
