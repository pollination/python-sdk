# pollination_sdk.ArtifactsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_artifact**](ArtifactsApi.md#create_artifact) | **POST** /projects/{owner}/{name}/artifacts | Get an Artifact upload link.
[**delete_artifact**](ArtifactsApi.md#delete_artifact) | **DELETE** /projects/{owner}/{name}/artifacts | Delete one or many artifacts by key/prefix
[**download_artifact**](ArtifactsApi.md#download_artifact) | **GET** /projects/{owner}/{name}/artifacts/download | Download an artifact from the project folder
[**list_artifacts**](ArtifactsApi.md#list_artifacts) | **GET** /projects/{owner}/{name}/artifacts | List artifacts in a project folder


# **create_artifact**
> S3UploadRequest create_artifact(ownernamekey_request)

Get an Artifact upload link.

### Example

* Bearer (JWT) Authentication (JWTAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization (JWT): JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "http://localhost",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.ArtifactsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
key_request = pollination_sdk.KeyRequest() # KeyRequest | 

    try:
        # Get an Artifact upload link.
        api_response = api_instance.create_artifact(ownernamekey_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ArtifactsApi->create_artifact: %s\n" % e)
```

* Api Key Authentication (APIKeyAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization (JWT): JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "http://localhost",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.ArtifactsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
key_request = pollination_sdk.KeyRequest() # KeyRequest | 

    try:
        # Get an Artifact upload link.
        api_response = api_instance.create_artifact(ownernamekey_request)
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

[JWTAuth](../README.md#JWTAuth), [APIKeyAuth](../README.md#APIKeyAuth)

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
> delete_artifact(ownernamepath=pathpage=pageper_page=per_page)

Delete one or many artifacts by key/prefix

### Example

* Bearer (JWT) Authentication (JWTAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization (JWT): JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "http://localhost",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.ArtifactsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
path = ['path_example'] # List[str] | The path to an file within a project folder (optional)
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # Delete one or many artifacts by key/prefix
        api_instance.delete_artifact(ownernamepath=pathpage=pageper_page=per_page)
    except ApiException as e:
        print("Exception when calling ArtifactsApi->delete_artifact: %s\n" % e)
```

* Api Key Authentication (APIKeyAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization (JWT): JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "http://localhost",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.ArtifactsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
path = ['path_example'] # List[str] | The path to an file within a project folder (optional)
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # Delete one or many artifacts by key/prefix
        api_instance.delete_artifact(ownernamepath=pathpage=pageper_page=per_page)
    except ApiException as e:
        print("Exception when calling ArtifactsApi->delete_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **path** | [**List[str]**](str.md)| The path to an file within a project folder | [optional] 
 **page** | **int**| Page number starting from 1 | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

void (empty response body)

### Authorization

[JWTAuth](../README.md#JWTAuth), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_artifact**
> object download_artifact(ownernamepath=path)

Download an artifact from the project folder

### Example

* Bearer (JWT) Authentication (JWTAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization (JWT): JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "http://localhost",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.ArtifactsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
path = 'path_example' # str | The path to an file within a project folder (optional)

    try:
        # Download an artifact from the project folder
        api_response = api_instance.download_artifact(ownernamepath=path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ArtifactsApi->download_artifact: %s\n" % e)
```

* Api Key Authentication (APIKeyAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization (JWT): JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "http://localhost",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.ArtifactsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
path = 'path_example' # str | The path to an file within a project folder (optional)

    try:
        # Download an artifact from the project folder
        api_response = api_instance.download_artifact(ownernamepath=path)
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

[JWTAuth](../README.md#JWTAuth), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved |  -  |
**400** | Invalid request |  -  |
**403** | Access forbidden |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_artifacts**
> FileMetaList list_artifacts(ownernamepath=pathpage=pageper_page=per_page)

List artifacts in a project folder

### Example

* Bearer (JWT) Authentication (JWTAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization (JWT): JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "http://localhost",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.ArtifactsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
path = ['path_example'] # List[str] | The path to an file within a project folder (optional)
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List artifacts in a project folder
        api_response = api_instance.list_artifacts(ownernamepath=pathpage=pageper_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ArtifactsApi->list_artifacts: %s\n" % e)
```

* Api Key Authentication (APIKeyAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization (JWT): JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "http://localhost",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.ArtifactsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
path = ['path_example'] # List[str] | The path to an file within a project folder (optional)
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List artifacts in a project folder
        api_response = api_instance.list_artifacts(ownernamepath=pathpage=pageper_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ArtifactsApi->list_artifacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **path** | [**List[str]**](str.md)| The path to an file within a project folder | [optional] 
 **page** | **int**| Page number starting from 1 | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**FileMetaList**](FileMetaList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

