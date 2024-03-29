# Deep3 Labs: Unlocking the potential of Web3.0 with the power of AI

Interested in trying it out? Visit https://developer.deep3.ai to get an API key

## Deep3 Labs python client
This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v0.0.4
- Package version: 0.0.3
- Build package: org.openapitools.codegen.languages.PythonNextgenClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

You can install directly using:

```sh
pip install deep3-python-client
```

Then import the package:
```python
import deep3
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import deep3
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import deep3
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

# Enter a context with an instance of the API client
with deep3.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deep3.Deep3Api(api_client)

    try:
        # Get currently supported chains and the active machine learning models
        api_response = api_instance.get_chains()
        print("The response of Deep3Api->get_chains:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Deep3Api->get_chains: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.deep3.ai/v0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*Deep3Api* | [**get_chains**](docs/Deep3Api.md#get_chains) | **GET** /chains | Get currently supported chains and the active machine learning models
*Deep3Api* | [**get_deep_shield_fr_prediction**](docs/Deep3Api.md#get_deep_shield_fr_prediction) | **GET** /deepshield-fr/chain/{chainId}/account/{address} | Get a DeepShield-FR prediction
*Deep3Api* | [**get_deep_shield_hft_prediction**](docs/Deep3Api.md#get_deep_shield_hft_prediction) | **GET** /deepshield-hft/chain/{chainId}/account/{address} | Get a DeepShield-HFT prediction
*Deep3Api* | [**get_hodl_c1_prediction**](docs/Deep3Api.md#get_hodl_c1_prediction) | **GET** /hodl-c1/chain/{chainId}/account/{address} | Get a HODL-C1 prediction
*Deep3Api* | [**get_hodl_c1_x_token_prediction**](docs/Deep3Api.md#get_hodl_c1_x_token_prediction) | **POST** /hodl-c1/x/token | Get a HODL-C1 cross-chain token prediction
*Deep3Api* | [**get_hodl_c1_x_token_predictions**](docs/Deep3Api.md#get_hodl_c1_x_token_predictions) | **POST** /hodl-c1/x/tokens | Get HODL-C1 cross-chain token predictions
*Deep3Api* | [**get_models**](docs/Deep3Api.md#get_models) | **GET** /models | Get active machine learning models and the chains they support
*Deep3Api* | [**get_prediction**](docs/Deep3Api.md#get_prediction) | **GET** /prediction/{model}/{chainId}/{publicAddress} | Get a prediction
*Deep3Api* | [**get_stake_sage_c_prediction**](docs/Deep3Api.md#get_stake_sage_c_prediction) | **GET** /stakesage-c/chain/{chainId}/account/{address} | Get a StakeSage-C prediction
*Deep3Api* | [**get_stake_sage_h_prediction**](docs/Deep3Api.md#get_stake_sage_h_prediction) | **GET** /stakesage-h/chain/{chainId}/account/{address} | Get a StakeSage-H prediction
*Deep3Api* | [**get_stake_sage_l_prediction**](docs/Deep3Api.md#get_stake_sage_l_prediction) | **GET** /stakesage-l/chain/{chainId}/account/{address} | Get a StakeSage-L prediction


## Documentation For Models

 - [ChainsResponseInner](docs/ChainsResponseInner.md)
 - [DeepShieldFrResponse](docs/DeepShieldFrResponse.md)
 - [DeepShieldHftResponse](docs/DeepShieldHftResponse.md)
 - [HodlC1Response](docs/HodlC1Response.md)
 - [HodlC1XTokenRequest](docs/HodlC1XTokenRequest.md)
 - [HodlC1XTokenRequestMappingsInner](docs/HodlC1XTokenRequestMappingsInner.md)
 - [HodlC1XTokenResponse](docs/HodlC1XTokenResponse.md)
 - [HodlC1XTokensRequest](docs/HodlC1XTokensRequest.md)
 - [HodlC1XTokensRequestAddressesInner](docs/HodlC1XTokensRequestAddressesInner.md)
 - [HodlC1XTokensResponseInner](docs/HodlC1XTokensResponseInner.md)
 - [ModelsResponseInner](docs/ModelsResponseInner.md)
 - [PredictionResponse](docs/PredictionResponse.md)
 - [StakeSageCResponse](docs/StakeSageCResponse.md)
 - [StakeSageHResponse](docs/StakeSageHResponse.md)
 - [StakeSageLResponse](docs/StakeSageLResponse.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="ApiKey"></a>
### ApiKey

- **Type**: API key
- **API key parameter name**: x-api-key
- **Location**: HTTP header
