# ModelsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**chains** | **List[float]** |  | 

## Example

```python
from deep3.models.models_response import ModelsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsResponse from a JSON string
models_response_instance = ModelsResponse.from_json(json)
# print the JSON string representation of the object
print ModelsResponse.to_json()

# convert the object into a dict
models_response_dict = models_response_instance.to_dict()
# create an instance of ModelsResponse from a dict
models_response_form_dict = models_response.from_dict(models_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


