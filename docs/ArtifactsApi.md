# pollination_sdk.ArtifactsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_artifact**](ArtifactsApi.md#create_artifact) | **POST** /projects/{owner}/{name}/artifacts | Get an Artifact upload link.
[**delete_artifact**](ArtifactsApi.md#delete_artifact) | **DELETE** /projects/{owner}/{name}/artifacts | Delete one or many artifacts by key/prefix
[**download_artifact**](ArtifactsApi.md#download_artifact) | **GET** /projects/{owner}/{name}/artifacts/download | Download an artifact from the project folder
[**list_artifacts**](ArtifactsApi.md#list_artifacts) | **GET** /projects/{owner}/{name}/artifacts | List artifacts in a project folder


# **create_artifact**
> S3UploadRequest create_artifact(owner, name, key_request)

Get an Artifact upload link.

Create a new artifact.

### Example

* Bearer Authentication (Compulsory Auth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint
configuration = pollination_sdk.Configuration()

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization: Compulsory Auth
configuration.access_token = auth_response.access_token

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Create an instance of the API class
api_instance = pollination_sdk.ArtifactsApi(pollination_sdk.ApiClient(configuration))
owner = 'owner_example' # str | 
name = 'name_example' # str | 
key_request = pollination_sdk.KeyRequest() # KeyRequest | 

try:
    # Get an Artifact upload link.
    api_response = api_instance.create_artifact(owner, name, key_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactsApi->create_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **key_request** | [**KeyRequest**](KeyRequest.md)|  | 

### Return type

[**S3UploadRequest**](S3UploadRequest.md)

### Authorization

[Compulsory Auth](../README.md#Compulsory Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_artifact**
> UpdateAccepted delete_artifact(owner, name, path=path)

Delete one or many artifacts by key/prefix

Delete one or multiple artifacts based on key prefix

### Example

* Bearer Authentication (Compulsory Auth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint
configuration = pollination_sdk.Configuration()

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization: Compulsory Auth
configuration.access_token = auth_response.access_token

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Create an instance of the API class
api_instance = pollination_sdk.ArtifactsApi(pollination_sdk.ApiClient(configuration))
owner = 'owner_example' # str | 
name = 'name_example' # str | 
path = ['path_example'] # list[str] | The path to an file within a project folder (optional)

try:
    # Delete one or many artifacts by key/prefix
    api_response = api_instance.delete_artifact(owner, name, path=path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactsApi->delete_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **path** | [**list[str]**](str.md)| The path to an file within a project folder | [optional] 

### Return type

[**UpdateAccepted**](UpdateAccepted.md)

### Authorization

[Compulsory Auth](../README.md#Compulsory Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_artifact**
> object download_artifact(owner, name, path=path)

Download an artifact from the project folder

Retrieve a list of artifacts.

### Example

* Bearer Authentication (Optional Auth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint
configuration = pollination_sdk.Configuration()

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization: Optional Auth
configuration.access_token = auth_response.access_token

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Create an instance of the API class
api_instance = pollination_sdk.ArtifactsApi(pollination_sdk.ApiClient(configuration))
owner = 'owner_example' # str | 
name = 'name_example' # str | 
path = 'path_example' # str | The path to an file within a project folder (optional)

try:
    # Download an artifact from the project folder
    api_response = api_instance.download_artifact(owner, name, path=path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactsApi->download_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **path** | **str**| The path to an file within a project folder | [optional] 

### Return type

**object**

### Authorization

[Optional Auth](../README.md#Optional Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved |  -  |
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**400** | Invalid request |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_artifacts**
> list[FileMeta] list_artifacts(owner, name, page=page, per_page=per_page, path=path)

List artifacts in a project folder

Retrieve a list of artifacts.

### Example

* Bearer Authentication (Optional Auth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint
configuration = pollination_sdk.Configuration()

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization: Optional Auth
configuration.access_token = auth_response.access_token

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Create an instance of the API class
api_instance = pollination_sdk.ArtifactsApi(pollination_sdk.ApiClient(configuration))
owner = 'owner_example' # str | 
name = 'name_example' # str | 
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)
path = ['path_example'] # list[str] | The path to an file within a project folder (optional)

try:
    # List artifacts in a project folder
    api_response = api_instance.list_artifacts(owner, name, page=page, per_page=per_page, path=path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArtifactsApi->list_artifacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **page** | **int**| Page number starting from 1 | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 25]
 **path** | [**list[str]**](str.md)| The path to an file within a project folder | [optional] 

### Return type

[**list[FileMeta]**](FileMeta.md)

### Authorization

[Optional Auth](../README.md#Optional Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

