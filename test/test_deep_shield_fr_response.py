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
from deep3.models.deep_shield_fr_response import DeepShieldFrResponse  # noqa: E501
from deep3.rest import ApiException

class TestDeepShieldFrResponse(unittest.TestCase):
    """DeepShieldFrResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DeepShieldFrResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeepShieldFrResponse`
        """
        model = deep3.models.deep_shield_fr_response.DeepShieldFrResponse()  # noqa: E501
        if include_optional :
            return DeepShieldFrResponse(
                code = 1.337, 
                result = 1.337
            )
        else :
            return DeepShieldFrResponse(
                code = 1.337,
        )
        """

    def testDeepShieldFrResponse(self):
        """Test DeepShieldFrResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
