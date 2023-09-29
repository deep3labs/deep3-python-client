# HodlC1XTokenRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**mappings** | [**List[HodlC1XTokenRequestMappingsInner]**](HodlC1XTokenRequestMappingsInner.md) |  | [optional] 

## Example

```python
from deep3.models.hodl_c1_x_token_request import HodlC1XTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HodlC1XTokenRequest from a JSON string
hodl_c1_x_token_request_instance = HodlC1XTokenRequest.from_json(json)
# print the JSON string representation of the object
print HodlC1XTokenRequest.to_json()

# convert the object into a dict
hodl_c1_x_token_request_dict = hodl_c1_x_token_request_instance.to_dict()
# create an instance of HodlC1XTokenRequest from a dict
hodl_c1_x_token_request_form_dict = hodl_c1_x_token_request.from_dict(hodl_c1_x_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


