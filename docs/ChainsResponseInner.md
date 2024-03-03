# ChainsResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_id** | **float** |  | 
**name** | **str** |  | 
**models** | **List[str]** |  | 

## Example

```python
from deep3.models.chains_response_inner import ChainsResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ChainsResponseInner from a JSON string
chains_response_inner_instance = ChainsResponseInner.from_json(json)
# print the JSON string representation of the object
print ChainsResponseInner.to_json()

# convert the object into a dict
chains_response_inner_dict = chains_response_inner_instance.to_dict()
# create an instance of ChainsResponseInner from a dict
chains_response_inner_form_dict = chains_response_inner.from_dict(chains_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


