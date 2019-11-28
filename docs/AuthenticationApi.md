# pollination_sdk.AuthenticationApi

All URIs are relative to *https://api.pollination.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_token**](AuthenticationApi.md#create_api_token) | **POST** /auth/api-token | Create an API Token
[**delete_api_token**](AuthenticationApi.md#delete_api_token) | **DELETE** /auth/api-token | Delete an API Token
[**get_api_token**](AuthenticationApi.md#get_api_token) | **GET** /auth/api-token | Get your API Token ID
[**login**](AuthenticationApi.md#login) | **POST** /auth/login | Login with API Token
[**rotate_api_token_secret**](AuthenticationApi.md#rotate_api_token_secret) | **PUT** /auth/api-token | Rotate an API token secret


# **create_api_token**
> Token create_api_token()

Create an API Token

Create a new api token.

### Example

* Bearer Authentication (JWT):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint
configuration = pollination_sdk.Configuration()

# Retrieve a temporary Acces Token (JWT) using your API key id and secret
API_KEY_ID = 'some-long-id'
API_KEY_SECRET = 'some-long-secret'

auth = pollination_sdk.AuthenticationApi()
api_token = pollination_sdk.Token(
  id=API_KEY_ID,
  secret=API_KEY_SECRET
)

auth_response = auth.login(token)

# Configure Bearer authorization: JWT
configuration.access_token = auth_response.access_token

# Defining host is optional and default to https://api.pollination.cloud
configuration.host = "https://api.pollination.cloud"
# Create an instance of the API class
api_instance = pollination_sdk.AuthenticationApi(pollination_sdk.ApiClient(configuration))

try:
    # Create an API Token
    api_response = api_instance.create_api_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->create_api_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Token**](Token.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_token**
> object delete_api_token()

Delete an API Token

Delete an API Token.

### Example

* Bearer Authentication (JWT):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint
configuration = pollination_sdk.Configuration()

# Retrieve a temporary Acces Token (JWT) using your API key id and secret
API_KEY_ID = 'some-long-id'
API_KEY_SECRET = 'some-long-secret'

auth = pollination_sdk.AuthenticationApi()
api_token = pollination_sdk.Token(
  id=API_KEY_ID,
  secret=API_KEY_SECRET
)

auth_response = auth.login(token)

# Configure Bearer authorization: JWT
configuration.access_token = auth_response.access_token

# Defining host is optional and default to https://api.pollination.cloud
configuration.host = "https://api.pollination.cloud"
# Create an instance of the API class
api_instance = pollination_sdk.AuthenticationApi(pollination_sdk.ApiClient(configuration))

try:
    # Delete an API Token
    api_response = api_instance.delete_api_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->delete_api_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**404** | Not found |  -  |
**204** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_token**
> NewToken get_api_token()

Get your API Token ID

Retrieve an API Token Name.

### Example

* Bearer Authentication (JWT):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint
configuration = pollination_sdk.Configuration()

# Retrieve a temporary Acces Token (JWT) using your API key id and secret
API_KEY_ID = 'some-long-id'
API_KEY_SECRET = 'some-long-secret'

auth = pollination_sdk.AuthenticationApi()
api_token = pollination_sdk.Token(
  id=API_KEY_ID,
  secret=API_KEY_SECRET
)

auth_response = auth.login(token)

# Configure Bearer authorization: JWT
configuration.access_token = auth_response.access_token

# Defining host is optional and default to https://api.pollination.cloud
configuration.host = "https://api.pollination.cloud"
# Create an instance of the API class
api_instance = pollination_sdk.AuthenticationApi(pollination_sdk.ApiClient(configuration))

try:
    # Get your API Token ID
    api_response = api_instance.get_api_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->get_api_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NewToken**](NewToken.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**404** | Not found |  -  |
**200** | Retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> Auth0TokenResponse login(token)

Login with API Token

Login user with token data

### Example

```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pollination_sdk.AuthenticationApi()
token = pollination_sdk.Token() # Token | 

try:
    # Login with API Token
    api_response = api_instance.login(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | [**Token**](Token.md)|  | 

### Return type

[**Auth0TokenResponse**](Auth0TokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Success |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_api_token_secret**
> Token rotate_api_token_secret()

Rotate an API token secret

Rotate a token's secret.

### Example

* Bearer Authentication (JWT):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint
configuration = pollination_sdk.Configuration()

# Retrieve a temporary Acces Token (JWT) using your API key id and secret
API_KEY_ID = 'some-long-id'
API_KEY_SECRET = 'some-long-secret'

auth = pollination_sdk.AuthenticationApi()
api_token = pollination_sdk.Token(
  id=API_KEY_ID,
  secret=API_KEY_SECRET
)

auth_response = auth.login(token)

# Configure Bearer authorization: JWT
configuration.access_token = auth_response.access_token

# Defining host is optional and default to https://api.pollination.cloud
configuration.host = "https://api.pollination.cloud"
# Create an instance of the API class
api_instance = pollination_sdk.AuthenticationApi(pollination_sdk.ApiClient(configuration))

try:
    # Rotate an API token secret
    api_response = api_instance.rotate_api_token_secret()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->rotate_api_token_secret: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Token**](Token.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**404** | Not found |  -  |
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

