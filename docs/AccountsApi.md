# pollination_sdk.AccountsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_account_name**](AccountsApi.md#check_account_name) | **GET** /accounts/check/{name} | Check if an account with this name exists
[**get_account**](AccountsApi.md#get_account) | **GET** /accounts/{name} | Get an account by name
[**list_accounts**](AccountsApi.md#list_accounts) | **GET** /accounts | List Accounts on the Pollination platform
[**list_quotas**](AccountsApi.md#list_quotas) | **GET** /accounts/{name}/quotas | List Quotas


# **check_account_name**
> object check_account_name(name)

Check if an account with this name exists

Check if an account name is taken

### Example

```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.AccountsApi(api_client)
    name = 'name_example' # str | 

    try:
        # Check if an account with this name exists
        api_response = api_instance.check_account_name(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->check_account_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account**
> AccountPublic get_account(name)

Get an account by name

Retrieve an account by name

### Example

```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.AccountsApi(api_client)
    name = 'name_example' # str | 

    try:
        # Get an account by name
        api_response = api_instance.get_account(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->get_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**AccountPublic**](AccountPublic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_accounts**
> PublicAccountList list_accounts(search=search, type=type, role=role, page=page, per_page=per_page)

List Accounts on the Pollination platform

List accounts

### Example

* Api Key Authentication (APIKeyAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "http://localhost",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

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

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.AccountsApi(api_client)
    search = 'search_example' # str | Search string to find accounts (optional)
type = 'type_example' # str | Whether the account is for a user or an org (optional)
role = pollination_sdk.RoleEnum() # RoleEnum | The role the user has in relation to this account (optional)
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List Accounts on the Pollination platform
        api_response = api_instance.list_accounts(search=search, type=type, role=role, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->list_accounts: %s\n" % e)
```

* Bearer (JWT) Authentication (JWTAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "http://localhost",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

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

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.AccountsApi(api_client)
    search = 'search_example' # str | Search string to find accounts (optional)
type = 'type_example' # str | Whether the account is for a user or an org (optional)
role = pollination_sdk.RoleEnum() # RoleEnum | The role the user has in relation to this account (optional)
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List Accounts on the Pollination platform
        api_response = api_instance.list_accounts(search=search, type=type, role=role, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->list_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search string to find accounts | [optional] 
 **type** | **str**| Whether the account is for a user or an org | [optional] 
 **role** | [**RoleEnum**](.md)| The role the user has in relation to this account | [optional] 
 **page** | **int**| Page number starting from 1 | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**PublicAccountList**](PublicAccountList.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth), [JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_quotas**
> QuotaList list_quotas(name, type=type, exhausted=exhausted, enforced=enforced, page=page, per_page=per_page)

List Quotas

### Example

* Api Key Authentication (APIKeyAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "http://localhost",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

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

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.AccountsApi(api_client)
    name = 'name_example' # str | 
type = [pollination_sdk.QuotaType()] # list[QuotaType] | The types of quotas to get (optional)
exhausted = True # bool | Whether to return only quotas which are exhausted (optional)
enforced = True # bool | Whether to return only quotas which are enforced (optional)
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List Quotas
        api_response = api_instance.list_quotas(name, type=type, exhausted=exhausted, enforced=enforced, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->list_quotas: %s\n" % e)
```

* Bearer (JWT) Authentication (JWTAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "http://localhost",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

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

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.AccountsApi(api_client)
    name = 'name_example' # str | 
type = [pollination_sdk.QuotaType()] # list[QuotaType] | The types of quotas to get (optional)
exhausted = True # bool | Whether to return only quotas which are exhausted (optional)
enforced = True # bool | Whether to return only quotas which are enforced (optional)
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List Quotas
        api_response = api_instance.list_quotas(name, type=type, exhausted=exhausted, enforced=enforced, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountsApi->list_quotas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **type** | [**list[QuotaType]**](QuotaType.md)| The types of quotas to get | [optional] 
 **exhausted** | **bool**| Whether to return only quotas which are exhausted | [optional] 
 **enforced** | **bool**| Whether to return only quotas which are enforced | [optional] 
 **page** | **int**| Page number starting from 1 | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**QuotaList**](QuotaList.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth), [JWTAuth](../README.md#JWTAuth)

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

