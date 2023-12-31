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
from deep3.models.get_stake_sage_l_response import GetStakeSageLResponse  # noqa: E501
from deep3.rest import ApiException

class TestGetStakeSageLResponse(unittest.TestCase):
    """GetStakeSageLResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetStakeSageLResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetStakeSageLResponse`
        """
        model = deep3.models.get_stake_sage_l_response.GetStakeSageLResponse()  # noqa: E501
        if include_optional :
            return GetStakeSageLResponse(
                code = 1.337, 
                result = 1.337
            )
        else :
            return GetStakeSageLResponse(
                code = 1.337,
        )
        """

    def testGetStakeSageLResponse(self):
        """Test GetStakeSageLResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
