# PredictionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | 
**result** | **float** |  | [optional] 

## Example

```python
from deep3.models.prediction_response import PredictionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PredictionResponse from a JSON string
prediction_response_instance = PredictionResponse.from_json(json)
# print the JSON string representation of the object
print PredictionResponse.to_json()

# convert the object into a dict
prediction_response_dict = prediction_response_instance.to_dict()
# create an instance of PredictionResponse from a dict
prediction_response_form_dict = prediction_response.from_dict(prediction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


