# coding: utf-8

"""
    Deep3 Labs API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0.0.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import deep3
from deep3.models.hodler_response import HodlerResponse  # noqa: E501
from deep3.rest import ApiException

class TestHodlerResponse(unittest.TestCase):
    """HodlerResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test HodlerResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HodlerResponse`
        """
        model = deep3.models.hodler_response.HodlerResponse()  # noqa: E501
        if include_optional :
            return HodlerResponse(
                code = 1.337, 
                result = 1.337
            )
        else :
            return HodlerResponse(
                code = 1.337,
        )
        """

    def testHodlerResponse(self):
        """Test HodlerResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
