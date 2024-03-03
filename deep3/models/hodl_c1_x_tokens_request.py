# coding: utf-8

"""
    Deep3 Labs API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, conlist
from deep3.models.hodl_c1_x_tokens_request_addresses_inner import HodlC1XTokensRequestAddressesInner

class HodlC1XTokensRequest(BaseModel):
    """
    HodlC1XTokensRequest
    """
    addresses: Optional[conlist(HodlC1XTokensRequestAddressesInner)] = None
    __properties = ["addresses"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> HodlC1XTokensRequest:
        """Create an instance of HodlC1XTokensRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in addresses (list)
        _items = []
        if self.addresses:
            for _item in self.addresses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['addresses'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HodlC1XTokensRequest:
        """Create an instance of HodlC1XTokensRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HodlC1XTokensRequest.parse_obj(obj)

        _obj = HodlC1XTokensRequest.parse_obj({
            "addresses": [HodlC1XTokensRequestAddressesInner.from_dict(_item) for _item in obj.get("addresses")] if obj.get("addresses") is not None else None
        })
        return _obj

