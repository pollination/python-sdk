# pollination_sdk.PluginsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_plugin**](PluginsApi.md#create_plugin) | **POST** /plugins/{owner} | Create a Plugin
[**create_plugin_package**](PluginsApi.md#create_plugin_package) | **POST** /plugins/{owner}/{name}/tags | Create a new Plugin package
[**delete_plugin**](PluginsApi.md#delete_plugin) | **DELETE** /plugins/{owner}/{name} | Delete a Plugin
[**delete_plugin_org_permission**](PluginsApi.md#delete_plugin_org_permission) | **DELETE** /plugins/{owner}/{name}/permissions | Remove a Repository permissions
[**get_plugin**](PluginsApi.md#get_plugin) | **GET** /plugins/{owner}/{name} | Get a plugin
[**get_plugin_access_permissions**](PluginsApi.md#get_plugin_access_permissions) | **GET** /plugins/{owner}/{name}/permissions | Get plugin access permissions
[**get_plugin_by_tag**](PluginsApi.md#get_plugin_by_tag) | **GET** /plugins/{owner}/{name}/tags/{tag} | Get a plugin tag
[**list_plugin_tags**](PluginsApi.md#list_plugin_tags) | **GET** /plugins/{owner}/{name}/tags | Get a plugin tags
[**list_plugins**](PluginsApi.md#list_plugins) | **GET** /plugins | List plugins
[**update_plugin**](PluginsApi.md#update_plugin) | **PUT** /plugins/{owner}/{name} | Update a Plugin
[**upsert_plugin_permission**](PluginsApi.md#upsert_plugin_permission) | **PATCH** /plugins/{owner}/{name}/permissions | Upsert a new permission to a plugin


# **create_plugin**
> CreatedContent create_plugin(ownerrepository_create)

Create a Plugin

Create a new plugin.

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
    api_instance = pollination_sdk.PluginsApi(api_client)
    owner = 'owner_example' # str | 
repository_create = pollination_sdk.RepositoryCreate() # RepositoryCreate | 

    try:
        # Create a Plugin
        api_response = api_instance.create_plugin(ownerrepository_create)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PluginsApi->create_plugin: %s\n" % e)
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
    api_instance = pollination_sdk.PluginsApi(api_client)
    owner = 'owner_example' # str | 
repository_create = pollination_sdk.RepositoryCreate() # RepositoryCreate | 

    try:
        # Create a Plugin
        api_response = api_instance.create_plugin(ownerrepository_create)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PluginsApi->create_plugin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **repository_create** | [**RepositoryCreate**](RepositoryCreate.md)|  | 

### Return type

[**CreatedContent**](CreatedContent.md)

### Authorization

[JWTAuth](../README.md#JWTAuth), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**202** | Accepted |  -  |
**400** | Invalid request |  -  |
**403** | Access forbidden |  -  |
**422** | Validation Error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_plugin_package**
> CreatedContent create_plugin_package(ownernamenew_plugin_package)

Create a new Plugin package

Create a new plugin package version

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
    api_instance = pollination_sdk.PluginsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
new_plugin_package = pollination_sdk.NewPluginPackage() # NewPluginPackage | 

    try:
        # Create a new Plugin package
        api_response = api_instance.create_plugin_package(ownernamenew_plugin_package)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PluginsApi->create_plugin_package: %s\n" % e)
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
    api_instance = pollination_sdk.PluginsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
new_plugin_package = pollination_sdk.NewPluginPackage() # NewPluginPackage | 

    try:
        # Create a new Plugin package
        api_response = api_instance.create_plugin_package(ownernamenew_plugin_package)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PluginsApi->create_plugin_package: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **new_plugin_package** | [**NewPluginPackage**](NewPluginPackage.md)|  | 

### Return type

[**CreatedContent**](CreatedContent.md)

### Authorization

[JWTAuth](../README.md#JWTAuth), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**403** | Access forbidden |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_plugin**
> delete_plugin(ownername)

Delete a Plugin

Delete a plugin (must have `admin` permission)

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
    api_instance = pollination_sdk.PluginsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 

    try:
        # Delete a Plugin
        api_instance.delete_plugin(ownername)
    except ApiException as e:
        print("Exception when calling PluginsApi->delete_plugin: %s\n" % e)
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
    api_instance = pollination_sdk.PluginsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 

    try:
        # Delete a Plugin
        api_instance.delete_plugin(ownername)
    except ApiException as e:
        print("Exception when calling PluginsApi->delete_plugin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 

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
**204** | Accepted |  -  |
**400** | Invalid request |  -  |
**403** | Access forbidden |  -  |
**422** | Validation Error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_plugin_org_permission**
> delete_plugin_org_permission(ownernamerepository_policy_subject)

Remove a Repository permissions

Delete a plugin's access policy (must have `admin` permission)

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
    api_instance = pollination_sdk.PluginsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
repository_policy_subject = pollination_sdk.RepositoryPolicySubject() # RepositoryPolicySubject | 

    try:
        # Remove a Repository permissions
        api_instance.delete_plugin_org_permission(ownernamerepository_policy_subject)
    except ApiException as e:
        print("Exception when calling PluginsApi->delete_plugin_org_permission: %s\n" % e)
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
    api_instance = pollination_sdk.PluginsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
repository_policy_subject = pollination_sdk.RepositoryPolicySubject() # RepositoryPolicySubject | 

    try:
        # Remove a Repository permissions
        api_instance.delete_plugin_org_permission(ownernamerepository_policy_subject)
    except ApiException as e:
        print("Exception when calling PluginsApi->delete_plugin_org_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **repository_policy_subject** | [**RepositoryPolicySubject**](RepositoryPolicySubject.md)|  | 

### Return type

void (empty response body)

### Authorization

[JWTAuth](../README.md#JWTAuth), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**400** | Invalid request |  -  |
**403** | Access forbidden |  -  |
**422** | Validation Error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugin**
> Repository get_plugin(ownername)

Get a plugin

Retrieve a plugin by name

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
    api_instance = pollination_sdk.PluginsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 

    try:
        # Get a plugin
        api_response = api_instance.get_plugin(ownername)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PluginsApi->get_plugin: %s\n" % e)
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
    api_instance = pollination_sdk.PluginsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 

    try:
        # Get a plugin
        api_response = api_instance.get_plugin(ownername)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PluginsApi->get_plugin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**Repository**](Repository.md)

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

# **get_plugin_access_permissions**
> RepositoryAccessPolicyList get_plugin_access_permissions(ownernamepage=pageper_page=per_pagesubject_type=subject_typepermission=permission)

Get plugin access permissions

Retrieve a plugin's access permissions (must have `write` permission)

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
    api_instance = pollination_sdk.PluginsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)
subject_type = ['subject_type_example'] # List[str] | The type of access policy subject (optional)
permission = ['permission_example'] # List[str] | An access policy permission string (optional)

    try:
        # Get plugin access permissions
        api_response = api_instance.get_plugin_access_permissions(ownernamepage=pageper_page=per_pagesubject_type=subject_typepermission=permission)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PluginsApi->get_plugin_access_permissions: %s\n" % e)
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
    api_instance = pollination_sdk.PluginsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)
subject_type = ['subject_type_example'] # List[str] | The type of access policy subject (optional)
permission = ['permission_example'] # List[str] | An access policy permission string (optional)

    try:
        # Get plugin access permissions
        api_response = api_instance.get_plugin_access_permissions(ownernamepage=pageper_page=per_pagesubject_type=subject_typepermission=permission)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PluginsApi->get_plugin_access_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **page** | **int**| Page number starting from 1 | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 25]
 **subject_type** | [**List[str]**](str.md)| The type of access policy subject | [optional] 
 **permission** | [**List[str]**](str.md)| An access policy permission string | [optional] 

### Return type

[**RepositoryAccessPolicyList**](RepositoryAccessPolicyList.md)

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
**422** | Validation Error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugin_by_tag**
> PluginPackage get_plugin_by_tag(ownernametag)

Get a plugin tag

Retrieve a plugin tag by name and tag

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
    api_instance = pollination_sdk.PluginsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
tag = 'tag_example' # str | 

    try:
        # Get a plugin tag
        api_response = api_instance.get_plugin_by_tag(ownernametag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PluginsApi->get_plugin_by_tag: %s\n" % e)
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
    api_instance = pollination_sdk.PluginsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
tag = 'tag_example' # str | 

    try:
        # Get a plugin tag
        api_response = api_instance.get_plugin_by_tag(ownernametag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PluginsApi->get_plugin_by_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **tag** | **str**|  | 

### Return type

[**PluginPackage**](PluginPackage.md)

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

# **list_plugin_tags**
> PluginPackageList list_plugin_tags(ownernamesort_by=sort_bysort_order=sort_orderpage=pageper_page=per_page)

Get a plugin tags

Retrieve a plugin by name

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
    api_instance = pollination_sdk.PluginsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
sort_by = pollination_sdk.PackageSortKey() # PackageSortKey | Key to sort the list by (optional)
sort_order = pollination_sdk.SortEnum() # SortEnum | The order to sort the list (optional)
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # Get a plugin tags
        api_response = api_instance.list_plugin_tags(ownernamesort_by=sort_bysort_order=sort_orderpage=pageper_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PluginsApi->list_plugin_tags: %s\n" % e)
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
    api_instance = pollination_sdk.PluginsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
sort_by = pollination_sdk.PackageSortKey() # PackageSortKey | Key to sort the list by (optional)
sort_order = pollination_sdk.SortEnum() # SortEnum | The order to sort the list (optional)
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # Get a plugin tags
        api_response = api_instance.list_plugin_tags(ownernamesort_by=sort_bysort_order=sort_orderpage=pageper_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PluginsApi->list_plugin_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **sort_by** | [**PackageSortKey**](.md)| Key to sort the list by | [optional] 
 **sort_order** | [**SortEnum**](.md)| The order to sort the list | [optional] 
 **page** | **int**| Page number starting from 1 | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**PluginPackageList**](PluginPackageList.md)

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

# **list_plugins**
> RepositoryList list_plugins(search=searchname=nameowner=ownerpublic=publickeyword=keywordpermission=permissionsort_by=sort_bysort_order=sort_orderpage=pageper_page=per_page)

List plugins

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
    api_instance = pollination_sdk.PluginsApi(api_client)
    search = ['search_example'] # List[str] | You know, for search (optional)
name = ['name_example'] # List[str] | The account name (optional)
owner = ['owner_example'] # List[str] | Owner of the project (optional)
public = True # bool | Boolean check for public/private projects (optional)
keyword = ['keyword_example'] # List[str] | A keyword to index the repository by (optional)
permission = ['permission_example'] # List[str] | Filter by permission on given resource (optional)
sort_by = pollination_sdk.RepositorySortKey() # RepositorySortKey | Key to sort the list by (optional)
sort_order = pollination_sdk.SortEnum() # SortEnum | The order to sort the list (optional)
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List plugins
        api_response = api_instance.list_plugins(search=searchname=nameowner=ownerpublic=publickeyword=keywordpermission=permissionsort_by=sort_bysort_order=sort_orderpage=pageper_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PluginsApi->list_plugins: %s\n" % e)
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
    api_instance = pollination_sdk.PluginsApi(api_client)
    search = ['search_example'] # List[str] | You know, for search (optional)
name = ['name_example'] # List[str] | The account name (optional)
owner = ['owner_example'] # List[str] | Owner of the project (optional)
public = True # bool | Boolean check for public/private projects (optional)
keyword = ['keyword_example'] # List[str] | A keyword to index the repository by (optional)
permission = ['permission_example'] # List[str] | Filter by permission on given resource (optional)
sort_by = pollination_sdk.RepositorySortKey() # RepositorySortKey | Key to sort the list by (optional)
sort_order = pollination_sdk.SortEnum() # SortEnum | The order to sort the list (optional)
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List plugins
        api_response = api_instance.list_plugins(search=searchname=nameowner=ownerpublic=publickeyword=keywordpermission=permissionsort_by=sort_bysort_order=sort_orderpage=pageper_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PluginsApi->list_plugins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | [**List[str]**](str.md)| You know, for search | [optional] 
 **name** | [**List[str]**](str.md)| The account name | [optional] 
 **owner** | [**List[str]**](str.md)| Owner of the project | [optional] 
 **public** | **bool**| Boolean check for public/private projects | [optional] 
 **keyword** | [**List[str]**](str.md)| A keyword to index the repository by | [optional] 
 **permission** | [**List[str]**](str.md)| Filter by permission on given resource | [optional] 
 **sort_by** | [**RepositorySortKey**](.md)| Key to sort the list by | [optional] 
 **sort_order** | [**SortEnum**](.md)| The order to sort the list | [optional] 
 **page** | **int**| Page number starting from 1 | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**RepositoryList**](RepositoryList.md)

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

# **update_plugin**
> UpdateAccepted update_plugin(ownernamerepository_update)

Update a Plugin

Update a plugin (must have `contribute` permission)

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
    api_instance = pollination_sdk.PluginsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
repository_update = pollination_sdk.RepositoryUpdate() # RepositoryUpdate | 

    try:
        # Update a Plugin
        api_response = api_instance.update_plugin(ownernamerepository_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PluginsApi->update_plugin: %s\n" % e)
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
    api_instance = pollination_sdk.PluginsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
repository_update = pollination_sdk.RepositoryUpdate() # RepositoryUpdate | 

    try:
        # Update a Plugin
        api_response = api_instance.update_plugin(ownernamerepository_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PluginsApi->update_plugin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **repository_update** | [**RepositoryUpdate**](RepositoryUpdate.md)|  | 

### Return type

[**UpdateAccepted**](UpdateAccepted.md)

### Authorization

[JWTAuth](../README.md#JWTAuth), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Invalid request |  -  |
**403** | Access forbidden |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_plugin_permission**
> UpdateAccepted upsert_plugin_permission(ownernamerepository_access_policy)

Upsert a new permission to a plugin

Upsert a plugin's access policy (must have `admin` permission)

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
    api_instance = pollination_sdk.PluginsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
repository_access_policy = pollination_sdk.RepositoryAccessPolicy() # RepositoryAccessPolicy | 

    try:
        # Upsert a new permission to a plugin
        api_response = api_instance.upsert_plugin_permission(ownernamerepository_access_policy)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PluginsApi->upsert_plugin_permission: %s\n" % e)
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
    api_instance = pollination_sdk.PluginsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
repository_access_policy = pollination_sdk.RepositoryAccessPolicy() # RepositoryAccessPolicy | 

    try:
        # Upsert a new permission to a plugin
        api_response = api_instance.upsert_plugin_permission(ownernamerepository_access_policy)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PluginsApi->upsert_plugin_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **repository_access_policy** | [**RepositoryAccessPolicy**](RepositoryAccessPolicy.md)|  | 

### Return type

[**UpdateAccepted**](UpdateAccepted.md)

### Authorization

[JWTAuth](../README.md#JWTAuth), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Invalid request |  -  |
**403** | Access forbidden |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

