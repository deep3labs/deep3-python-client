# GetChainsResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_id** | **float** |  | 
**name** | **str** |  | 
**models** | **List[str]** |  | 

## Example

```python
from deep3.models.get_chains_result import GetChainsResult

# TODO update the JSON string below
json = "{}"
# create an instance of GetChainsResult from a JSON string
get_chains_result_instance = GetChainsResult.from_json(json)
# print the JSON string representation of the object
print GetChainsResult.to_json()

# convert the object into a dict
get_chains_result_dict = get_chains_result_instance.to_dict()
# create an instance of GetChainsResult from a dict
get_chains_result_form_dict = get_chains_result.from_dict(get_chains_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


