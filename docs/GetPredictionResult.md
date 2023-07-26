# GetPredictionResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | 
**result** | **float** |  | [optional] 

## Example

```python
from deep3.models.get_prediction_result import GetPredictionResult

# TODO update the JSON string below
json = "{}"
# create an instance of GetPredictionResult from a JSON string
get_prediction_result_instance = GetPredictionResult.from_json(json)
# print the JSON string representation of the object
print GetPredictionResult.to_json()

# convert the object into a dict
get_prediction_result_dict = get_prediction_result_instance.to_dict()
# create an instance of GetPredictionResult from a dict
get_prediction_result_form_dict = get_prediction_result.from_dict(get_prediction_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


