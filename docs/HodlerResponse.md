# HodlerResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | 
**result** | **float** |  | [optional] 

## Example

```python
from deep3.models.hodler_response import HodlerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HodlerResponse from a JSON string
hodler_response_instance = HodlerResponse.from_json(json)
# print the JSON string representation of the object
print HodlerResponse.to_json()

# convert the object into a dict
hodler_response_dict = hodler_response_instance.to_dict()
# create an instance of HodlerResponse from a dict
hodler_response_form_dict = hodler_response.from_dict(hodler_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


