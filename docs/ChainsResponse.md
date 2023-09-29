# ChainsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_id** | **float** |  | 
**name** | **str** |  | 
**models** | **List[str]** |  | 

## Example

```python
from deep3.models.chains_response import ChainsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChainsResponse from a JSON string
chains_response_instance = ChainsResponse.from_json(json)
# print the JSON string representation of the object
print ChainsResponse.to_json()

# convert the object into a dict
chains_response_dict = chains_response_instance.to_dict()
# create an instance of ChainsResponse from a dict
chains_response_form_dict = chains_response.from_dict(chains_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


