# ModelsResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** |  | 
**chains** | **List[float]** |  | 

## Example

```python
from deep3.models.models_response_inner import ModelsResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsResponseInner from a JSON string
models_response_inner_instance = ModelsResponseInner.from_json(json)
# print the JSON string representation of the object
print ModelsResponseInner.to_json()

# convert the object into a dict
models_response_inner_dict = models_response_inner_instance.to_dict()
# create an instance of ModelsResponseInner from a dict
models_response_inner_form_dict = models_response_inner.from_dict(models_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


