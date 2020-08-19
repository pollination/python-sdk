# pollination_sdk.RegistriesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_package**](RegistriesApi.md#get_package) | **GET** /registries/{owner}/{type}/{name}/{digest} | Get Package
[**get_registry_index**](RegistriesApi.md#get_registry_index) | **GET** /registries/{owner}/index.json | Get Registry Index
[**post_operator**](RegistriesApi.md#post_operator) | **POST** /registries/{owner}/operators | Push an Operator to the registry
[**post_recipe**](RegistriesApi.md#post_recipe) | **POST** /registries/{owner}/recipes | Push an Recipe to the registry


# **get_package**
> object get_package(owner, type, name, digest)

Get Package

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
api_instance = pollination_sdk.RegistriesApi(pollination_sdk.ApiClient(configuration))
owner = 'owner_example' # str | 
type = 'type_example' # str | 
name = 'name_example' # str | 
digest = 'digest_example' # str | 

try:
    # Get Package
    api_response = api_instance.get_package(owner, type, name, digest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistriesApi->get_package: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **type** | **str**|  | 
 **name** | **str**|  | 
 **digest** | **str**|  | 

### Return type

**object**

### Authorization

[Optional Auth](../README.md#Optional Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-tar

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registry_index**
> RepositoryIndex get_registry_index(owner)

Get Registry Index

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
api_instance = pollination_sdk.RegistriesApi(pollination_sdk.ApiClient(configuration))
owner = 'owner_example' # str | 

try:
    # Get Registry Index
    api_response = api_instance.get_registry_index(owner)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistriesApi->get_registry_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 

### Return type

[**RepositoryIndex**](RepositoryIndex.md)

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

# **post_operator**
> object post_operator(owner, package)

Push an Operator to the registry

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
api_instance = pollination_sdk.RegistriesApi(pollination_sdk.ApiClient(configuration))
owner = 'owner_example' # str | 
package = '/path/to/file' # file | 

try:
    # Push an Operator to the registry
    api_response = api_instance.post_operator(owner, package)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistriesApi->post_operator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **package** | **file**|  | 

### Return type

**object**

### Authorization

[Compulsory Auth](../README.md#Compulsory Auth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_recipe**
> object post_recipe(owner, package, authorization=authorization)

Push an Recipe to the registry

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
api_instance = pollination_sdk.RegistriesApi(pollination_sdk.ApiClient(configuration))
owner = 'owner_example' # str | 
package = '/path/to/file' # file | 
authorization = 'authorization_example' # str |  (optional)

try:
    # Push an Recipe to the registry
    api_response = api_instance.post_recipe(owner, package, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistriesApi->post_recipe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **package** | **file**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[Compulsory Auth](../README.md#Compulsory Auth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

