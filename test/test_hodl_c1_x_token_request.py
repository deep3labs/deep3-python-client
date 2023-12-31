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
from deep3.models.hodl_c1_x_token_request import HodlC1XTokenRequest  # noqa: E501
from deep3.rest import ApiException

class TestHodlC1XTokenRequest(unittest.TestCase):
    """HodlC1XTokenRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test HodlC1XTokenRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HodlC1XTokenRequest`
        """
        model = deep3.models.hodl_c1_x_token_request.HodlC1XTokenRequest()  # noqa: E501
        if include_optional :
            return HodlC1XTokenRequest(
                address = '', 
                mappings = [
                    deep3.models.hodl_c1_x_token_request_mappings_inner.HodlC1XTokenRequest_mappings_inner(
                        chain_id = 1.337, 
                        address = '', )
                    ]
            )
        else :
            return HodlC1XTokenRequest(
                address = '',
        )
        """

    def testHodlC1XTokenRequest(self):
        """Test HodlC1XTokenRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
