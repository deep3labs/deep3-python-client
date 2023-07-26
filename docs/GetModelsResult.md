# GetModelsResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**chains** | **List[float]** |  | 

## Example

```python
from deep3.models.get_models_result import GetModelsResult

# TODO update the JSON string below
json = "{}"
# create an instance of GetModelsResult from a JSON string
get_models_result_instance = GetModelsResult.from_json(json)
# print the JSON string representation of the object
print GetModelsResult.to_json()

# convert the object into a dict
get_models_result_dict = get_models_result_instance.to_dict()
# create an instance of GetModelsResult from a dict
get_models_result_form_dict = get_models_result.from_dict(get_models_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


