# coding: utf-8

"""
    Deep3 Labs API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import deep3
from deep3.models.chains_response_inner import ChainsResponseInner  # noqa: E501
from deep3.rest import ApiException

class TestChainsResponseInner(unittest.TestCase):
    """ChainsResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ChainsResponseInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChainsResponseInner`
        """
        model = deep3.models.chains_response_inner.ChainsResponseInner()  # noqa: E501
        if include_optional :
            return ChainsResponseInner(
                chain_id = 1.337, 
                name = '', 
                models = [
                    ''
                    ]
            )
        else :
            return ChainsResponseInner(
                chain_id = 1.337,
                name = '',
                models = [
                    ''
                    ],
        )
        """

    def testChainsResponseInner(self):
        """Test ChainsResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
