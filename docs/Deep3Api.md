# deep3.Deep3Api

All URIs are relative to *https://api.deep3.ai/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_chains**](Deep3Api.md#get_chains) | **GET** /chains | Get currently supported chains and the active machine learning models
[**get_hodl_c1_prediction**](Deep3Api.md#get_hodl_c1_prediction) | **GET** /hodl-c1/chain/{chainId}/account/{address} | Get a HODL-C1 prediction
[**get_hodl_c1_x_token_prediction**](Deep3Api.md#get_hodl_c1_x_token_prediction) | **POST** /hodl-c1/x/token | Get a HODL-C1 cross-chain token prediction
[**get_hodl_c1_x_token_predictions**](Deep3Api.md#get_hodl_c1_x_token_predictions) | **POST** /hodl-c1/x/tokens | Get HODL-C1 cross-chain token predictions
[**get_hodler_prediction**](Deep3Api.md#get_hodler_prediction) | **GET** /hodler/{chainId}/{publicAddress} | Get a Hodler prediction
[**get_models**](Deep3Api.md#get_models) | **GET** /models | Get active machine learning models and the chains they support
[**get_prediction**](Deep3Api.md#get_prediction) | **GET** /prediction/{model}/{chainId}/{publicAddress} | Get a prediction
[**get_stake_sage_h_prediction**](Deep3Api.md#get_stake_sage_h_prediction) | **GET** /stakesage-h/chain/{chainId}/account/{address} | Get a StakeSage-H prediction
[**get_stake_sage_l_prediction**](Deep3Api.md#get_stake_sage_l_prediction) | **GET** /stakesage-l/chain/{chainId}/account/{address} | Get a StakeSage-L prediction


# **get_chains**
> ChainsResponse get_chains()

Get currently supported chains and the active machine learning models

Will return currently supported chains

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import deep3
from deep3.models.chains_response import ChainsResponse
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

[**ChainsResponse**](ChainsResponse.md)

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

# **get_hodl_c1_prediction**
> HodlC1Response get_hodl_c1_prediction(chain_id, address)

Get a HODL-C1 prediction

Will return the prediction

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import deep3
from deep3.models.hodl_c1_response import HodlC1Response
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
    address = 'address_example' # str | The address for the account

    try:
        # Get a HODL-C1 prediction
        api_response = api_instance.get_hodl_c1_prediction(chain_id, address)
        print("The response of Deep3Api->get_hodl_c1_prediction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Deep3Api->get_hodl_c1_prediction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_id** | **float**| The chain id for the prediction | 
 **address** | **str**| The address for the account | 

### Return type

[**HodlC1Response**](HodlC1Response.md)

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

# **get_hodl_c1_x_token_prediction**
> HodlC1XTokenResponse get_hodl_c1_x_token_prediction(hodl_c1_x_token_request)

Get a HODL-C1 cross-chain token prediction

Will return the prediction

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import deep3
from deep3.models.hodl_c1_x_token_request import HodlC1XTokenRequest
from deep3.models.hodl_c1_x_token_response import HodlC1XTokenResponse
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
    hodl_c1_x_token_request = deep3.HodlC1XTokenRequest() # HodlC1XTokenRequest | An object with a primary token address and any mappings for different chain addresses

    try:
        # Get a HODL-C1 cross-chain token prediction
        api_response = api_instance.get_hodl_c1_x_token_prediction(hodl_c1_x_token_request)
        print("The response of Deep3Api->get_hodl_c1_x_token_prediction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Deep3Api->get_hodl_c1_x_token_prediction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hodl_c1_x_token_request** | [**HodlC1XTokenRequest**](HodlC1XTokenRequest.md)| An object with a primary token address and any mappings for different chain addresses | 

### Return type

[**HodlC1XTokenResponse**](HodlC1XTokenResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A prediction object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hodl_c1_x_token_predictions**
> List[HodlC1XTokensResponseInner] get_hodl_c1_x_token_predictions(hodl_c1_x_tokens_request)

Get HODL-C1 cross-chain token predictions

Will return the predictions

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import deep3
from deep3.models.hodl_c1_x_tokens_request import HodlC1XTokensRequest
from deep3.models.hodl_c1_x_tokens_response_inner import HodlC1XTokensResponseInner
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
    hodl_c1_x_tokens_request = deep3.HodlC1XTokensRequest() # HodlC1XTokensRequest | An array of objects with a primary token address and any mappings for different chain addresses

    try:
        # Get HODL-C1 cross-chain token predictions
        api_response = api_instance.get_hodl_c1_x_token_predictions(hodl_c1_x_tokens_request)
        print("The response of Deep3Api->get_hodl_c1_x_token_predictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Deep3Api->get_hodl_c1_x_token_predictions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hodl_c1_x_tokens_request** | [**HodlC1XTokensRequest**](HodlC1XTokensRequest.md)| An array of objects with a primary token address and any mappings for different chain addresses | 

### Return type

[**List[HodlC1XTokensResponseInner]**](HodlC1XTokensResponseInner.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A prediction object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hodler_prediction**
> HodlerResponse get_hodler_prediction(chain_id, public_address)

Get a Hodler prediction

Will return the prediction

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import deep3
from deep3.models.hodler_response import HodlerResponse
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

[**HodlerResponse**](HodlerResponse.md)

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
> ModelsResponse get_models()

Get active machine learning models and the chains they support

Will return active machine learning models

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import deep3
from deep3.models.models_response import ModelsResponse
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

[**ModelsResponse**](ModelsResponse.md)

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
> PredictionResponse get_prediction(model, chain_id, public_address)

Get a prediction

Will return the prediction

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import deep3
from deep3.models.prediction_response import PredictionResponse
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

[**PredictionResponse**](PredictionResponse.md)

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

# **get_stake_sage_h_prediction**
> StakeSageHResponse get_stake_sage_h_prediction(chain_id, address)

Get a StakeSage-H prediction

Will return the prediction

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import deep3
from deep3.models.stake_sage_h_response import StakeSageHResponse
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
    address = 'address_example' # str | The address for the account

    try:
        # Get a StakeSage-H prediction
        api_response = api_instance.get_stake_sage_h_prediction(chain_id, address)
        print("The response of Deep3Api->get_stake_sage_h_prediction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Deep3Api->get_stake_sage_h_prediction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_id** | **float**| The chain id for the prediction | 
 **address** | **str**| The address for the account | 

### Return type

[**StakeSageHResponse**](StakeSageHResponse.md)

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

# **get_stake_sage_l_prediction**
> StakeSageLResponse get_stake_sage_l_prediction(chain_id, address)

Get a StakeSage-L prediction

Will return the prediction

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import deep3
from deep3.models.stake_sage_l_response import StakeSageLResponse
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
    address = 'address_example' # str | The address for the account

    try:
        # Get a StakeSage-L prediction
        api_response = api_instance.get_stake_sage_l_prediction(chain_id, address)
        print("The response of Deep3Api->get_stake_sage_l_prediction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Deep3Api->get_stake_sage_l_prediction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_id** | **float**| The chain id for the prediction | 
 **address** | **str**| The address for the account | 

### Return type

[**StakeSageLResponse**](StakeSageLResponse.md)

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

