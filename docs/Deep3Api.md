# deep3.Deep3Api

All URIs are relative to *https://api.deep3.ai/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_chains**](Deep3Api.md#get_chains) | **GET** /chains | Get currently supported chains and the active machine learning models
[**get_hodler_prediction**](Deep3Api.md#get_hodler_prediction) | **GET** /hodler/{chainId}/{publicAddress} | Get a Hodler prediction
[**get_models**](Deep3Api.md#get_models) | **GET** /models | Get active machine learning models and the chains they support
[**get_prediction**](Deep3Api.md#get_prediction) | **GET** /prediction/{model}/{chainId}/{publicAddress} | Get a prediction


# **get_chains**
> GetChainsResult get_chains()

Get currently supported chains and the active machine learning models

Will return currently supported chains

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import deep3
from deep3.models.get_chains_result import GetChainsResult
from deep3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deep3.ai/v0
# See configuration.py for a list of all supported configuration parameters.
configuration = deep3.Configuration(
    host = "https://api.deep3.ai/v0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with deep3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deep3.Deep3Api(api_client)

    try:
        # Get currently supported chains and the active machine learning models
        api_response = api_instance.get_chains()
        print("The response of Deep3Api->get_chains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Deep3Api->get_chains: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetChainsResult**](GetChainsResult.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of chain objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hodler_prediction**
> GetHodlerResult get_hodler_prediction(chain_id, public_address)

Get a Hodler prediction

Will return the prediction

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import deep3
from deep3.models.get_hodler_result import GetHodlerResult
from deep3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deep3.ai/v0
# See configuration.py for a list of all supported configuration parameters.
configuration = deep3.Configuration(
    host = "https://api.deep3.ai/v0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with deep3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deep3.Deep3Api(api_client)
    chain_id = 3.4 # float | The chain id for the prediction
    public_address = 'public_address_example' # str | The public address for the wallet

    try:
        # Get a Hodler prediction
        api_response = api_instance.get_hodler_prediction(chain_id, public_address)
        print("The response of Deep3Api->get_hodler_prediction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Deep3Api->get_hodler_prediction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_id** | **float**| The chain id for the prediction | 
 **public_address** | **str**| The public address for the wallet | 

### Return type

[**GetHodlerResult**](GetHodlerResult.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A prediction object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_models**
> GetModelsResult get_models()

Get active machine learning models and the chains they support

Will return active machine learning models

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import deep3
from deep3.models.get_models_result import GetModelsResult
from deep3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deep3.ai/v0
# See configuration.py for a list of all supported configuration parameters.
configuration = deep3.Configuration(
    host = "https://api.deep3.ai/v0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with deep3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deep3.Deep3Api(api_client)

    try:
        # Get active machine learning models and the chains they support
        api_response = api_instance.get_models()
        print("The response of Deep3Api->get_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Deep3Api->get_models: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetModelsResult**](GetModelsResult.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of model objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prediction**
> GetPredictionResult get_prediction(model, chain_id, public_address)

Get a prediction

Will return the prediction

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import deep3
from deep3.models.get_prediction_result import GetPredictionResult
from deep3.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deep3.ai/v0
# See configuration.py for a list of all supported configuration parameters.
configuration = deep3.Configuration(
    host = "https://api.deep3.ai/v0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with deep3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deep3.Deep3Api(api_client)
    model = 'model_example' # str | The model for the prediction
    chain_id = 3.4 # float | The chain id for the prediction
    public_address = 'public_address_example' # str | The public address to predict

    try:
        # Get a prediction
        api_response = api_instance.get_prediction(model, chain_id, public_address)
        print("The response of Deep3Api->get_prediction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Deep3Api->get_prediction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| The model for the prediction | 
 **chain_id** | **float**| The chain id for the prediction | 
 **public_address** | **str**| The public address to predict | 

### Return type

[**GetPredictionResult**](GetPredictionResult.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A prediction object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

