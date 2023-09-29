# coding: utf-8

"""
    Deep3 Labs API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0.0.3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt

class HodlerResponse(BaseModel):
    """
    HodlerResponse
    """
    code: Union[StrictFloat, StrictInt] = Field(...)
    result: Optional[Union[StrictFloat, StrictInt]] = None
    __properties = ["code", "result"]

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
    def from_json(cls, json_str: str) -> HodlerResponse:
        """Create an instance of HodlerResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HodlerResponse:
        """Create an instance of HodlerResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HodlerResponse.parse_obj(obj)

        _obj = HodlerResponse.parse_obj({
            "code": obj.get("code"),
            "result": obj.get("result")
        })
        return _obj

