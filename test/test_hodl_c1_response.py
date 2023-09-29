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
from deep3.models.hodl_c1_response import HodlC1Response  # noqa: E501
from deep3.rest import ApiException

class TestHodlC1Response(unittest.TestCase):
    """HodlC1Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test HodlC1Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HodlC1Response`
        """
        model = deep3.models.hodl_c1_response.HodlC1Response()  # noqa: E501
        if include_optional :
            return HodlC1Response(
                code = 1.337, 
                result = 1.337
            )
        else :
            return HodlC1Response(
                code = 1.337,
        )
        """

    def testHodlC1Response(self):
        """Test HodlC1Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
