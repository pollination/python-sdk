# pollination_sdk.ArtifactsApi

All URIs are relative to *https://api.pollination.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ArtifactsApi.md#create) | **POST** /artifacts | Get an Artifact upload link.
[**list**](ArtifactsApi.md#list) | **GET** /artifacts | List artifacts in user folder


# **create**
> S3UploadRequest create(key_request)

Get an Artifact upload link.

Create a new workflow.

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
api_instance = pollination_sdk.ArtifactsApi(pollination_sdk.ApiClient(configuration))
key_request = pollination_sdk.KeyRequest() # KeyRequest | 

try:
    # Get an Artifact upload link.
    api_response = api_instance.create(key_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_request** | [**KeyRequest**](KeyRequest.md)|  | 

### Return type

[**S3UploadRequest**](S3UploadRequest.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> list[FileMeta] list(page=page, per_page=per_page)

List artifacts in user folder

Retrieve a list of simulations.

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
api_instance = pollination_sdk.ArtifactsApi(pollination_sdk.ApiClient(configuration))
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)

try:
    # List artifacts in user folder
    api_response = api_instance.list(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number starting from 1 | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**list[FileMeta]**](FileMeta.md)

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
**200** | Retrieved |  * Link - The Link header with pagination information. For details see [link header](https://pollination.cloud/api/#section/Pagination/Link-header). <br>  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

