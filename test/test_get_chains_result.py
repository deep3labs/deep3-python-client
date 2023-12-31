# coding: utf-8

"""
    Deep3 Labs API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import deep3
from deep3.models.get_chains_result import GetChainsResult  # noqa: E501
from deep3.rest import ApiException

class TestGetChainsResult(unittest.TestCase):
    """GetChainsResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetChainsResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetChainsResult`
        """
        model = deep3.models.get_chains_result.GetChainsResult()  # noqa: E501
        if include_optional :
            return GetChainsResult(
                chain_id = 1.337, 
                name = '', 
                models = [
                    ''
                    ]
            )
        else :
            return GetChainsResult(
        )
        """

    def testGetChainsResult(self):
        """Test GetChainsResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
