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
from deep3.models.hodl_c1_x_tokens_request_addresses_inner import HodlC1XTokensRequestAddressesInner  # noqa: E501
from deep3.rest import ApiException

class TestHodlC1XTokensRequestAddressesInner(unittest.TestCase):
    """HodlC1XTokensRequestAddressesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test HodlC1XTokensRequestAddressesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HodlC1XTokensRequestAddressesInner`
        """
        model = deep3.models.hodl_c1_x_tokens_request_addresses_inner.HodlC1XTokensRequestAddressesInner()  # noqa: E501
        if include_optional :
            return HodlC1XTokensRequestAddressesInner(
                address = '', 
                mappings = [
                    deep3.models.hodl_c1_x_token_request_mappings_inner.HodlC1XTokenRequest_mappings_inner(
                        chain_id = 1.337, 
                        address = '', )
                    ]
            )
        else :
            return HodlC1XTokensRequestAddressesInner(
                address = '',
        )
        """

    def testHodlC1XTokensRequestAddressesInner(self):
        """Test HodlC1XTokensRequestAddressesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
