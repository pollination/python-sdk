# pollination_sdk.OperatorsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_operator**](OperatorsApi.md#create_operator) | **POST** /operators/{owner} | Create an Operator
[**create_operator_package**](OperatorsApi.md#create_operator_package) | **POST** /operators/{owner}/{name}/tags | Create a new Operator package
[**delete_operator**](OperatorsApi.md#delete_operator) | **DELETE** /operators/{owner}/{name} | Delete an Operator
[**get_operator**](OperatorsApi.md#get_operator) | **GET** /operators/{owner}/{name} | Get an operator
[**get_operator_tag**](OperatorsApi.md#get_operator_tag) | **GET** /operators/{owner}/{name}/tags/{tag} | Get an operator tag
[**get_operator_tags**](OperatorsApi.md#get_operator_tags) | **GET** /operators/{owner}/{name}/tags | Get an operator tags
[**list_operators**](OperatorsApi.md#list_operators) | **GET** /operators | List operators
[**update_operator**](OperatorsApi.md#update_operator) | **PUT** /operators/{owner}/{name} | Update an Operator


# **create_operator**
> CreatedContent create_operator(owner, new_repository_dto)

Create an Operator

Create a new operator.

### Example

* Bearer Authentication (JWT):
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

# Configure Bearer authorization: JWT
configuration.access_token = auth_response.access_token

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Create an instance of the API class
api_instance = pollination_sdk.OperatorsApi(pollination_sdk.ApiClient(configuration))
owner = 'owner_example' # str | 
new_repository_dto = pollination_sdk.NewRepositoryDto() # NewRepositoryDto | 

try:
    # Create an Operator
    api_response = api_instance.create_operator(owner, new_repository_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperatorsApi->create_operator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **new_repository_dto** | [**NewRepositoryDto**](NewRepositoryDto.md)|  | 

### Return type

[**CreatedContent**](CreatedContent.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**400** | Invalid request |  -  |
**202** | Success |  -  |
**201** | Success |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_operator_package**
> object create_operator_package(owner, name, new_operator_package)

Create a new Operator package

Create a new operator package version

### Example

* Bearer Authentication (JWT):
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

# Configure Bearer authorization: JWT
configuration.access_token = auth_response.access_token

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Create an instance of the API class
api_instance = pollination_sdk.OperatorsApi(pollination_sdk.ApiClient(configuration))
owner = 'owner_example' # str | 
name = 'name_example' # str | 
new_operator_package = pollination_sdk.NewOperatorPackage() # NewOperatorPackage | 

try:
    # Create a new Operator package
    api_response = api_instance.create_operator_package(owner, name, new_operator_package)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperatorsApi->create_operator_package: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **new_operator_package** | [**NewOperatorPackage**](NewOperatorPackage.md)|  | 

### Return type

**object**

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**400** | Invalid request |  -  |
**200** | Retrieved |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_operator**
> delete_operator(owner, name)

Delete an Operator

Delete an operator (must have `admin` permission)

### Example

* Bearer Authentication (JWT):
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

# Configure Bearer authorization: JWT
configuration.access_token = auth_response.access_token

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Create an instance of the API class
api_instance = pollination_sdk.OperatorsApi(pollination_sdk.ApiClient(configuration))
owner = 'owner_example' # str | 
name = 'name_example' # str | 

try:
    # Delete an Operator
    api_instance.delete_operator(owner, name)
except ApiException as e:
    print("Exception when calling OperatorsApi->delete_operator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**400** | Invalid request |  -  |
**204** | Success |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_operator**
> object get_operator(owner, name)

Get an operator

Retrieve an operator by name

### Example

* Bearer Authentication (JWT):
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

# Configure Bearer authorization: JWT
configuration.access_token = auth_response.access_token

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Create an instance of the API class
api_instance = pollination_sdk.OperatorsApi(pollination_sdk.ApiClient(configuration))
owner = 'owner_example' # str | 
name = 'name_example' # str | 

try:
    # Get an operator
    api_response = api_instance.get_operator(owner, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperatorsApi->get_operator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 

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
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**400** | Invalid request |  -  |
**200** | Retrieved |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_operator_tag**
> object get_operator_tag(owner, name, tag)

Get an operator tag

Retrieve an operator tag by name and tag

### Example

* Bearer Authentication (JWT):
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

# Configure Bearer authorization: JWT
configuration.access_token = auth_response.access_token

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Create an instance of the API class
api_instance = pollination_sdk.OperatorsApi(pollination_sdk.ApiClient(configuration))
owner = 'owner_example' # str | 
name = 'name_example' # str | 
tag = 'tag_example' # str | 

try:
    # Get an operator tag
    api_response = api_instance.get_operator_tag(owner, name, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperatorsApi->get_operator_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **tag** | **str**|  | 

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
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**400** | Invalid request |  -  |
**200** | Retrieved |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_operator_tags**
> object get_operator_tags(owner, name)

Get an operator tags

Retrieve an operator by name

### Example

* Bearer Authentication (JWT):
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

# Configure Bearer authorization: JWT
configuration.access_token = auth_response.access_token

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Create an instance of the API class
api_instance = pollination_sdk.OperatorsApi(pollination_sdk.ApiClient(configuration))
owner = 'owner_example' # str | 
name = 'name_example' # str | 

try:
    # Get an operator tags
    api_response = api_instance.get_operator_tags(owner, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperatorsApi->get_operator_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 

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
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**400** | Invalid request |  -  |
**200** | Retrieved |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_operators**
> RepositoryListDto list_operators(page=page, per_page=per_page, name=name, owner=owner, public=public, keyword=keyword)

List operators

### Example

* Bearer Authentication (JWT):
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

# Configure Bearer authorization: JWT
configuration.access_token = auth_response.access_token

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Create an instance of the API class
api_instance = pollination_sdk.OperatorsApi(pollination_sdk.ApiClient(configuration))
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)
name = ['name_example'] # list[str] | The account name (optional)
owner = ['owner_example'] # list[str] | Owner of the project (optional)
public = True # bool | Boolean check for public/private projects (optional)
keyword = ['keyword_example'] # list[str] | A keyword to index the repository by (optional)

try:
    # List operators
    api_response = api_instance.list_operators(page=page, per_page=per_page, name=name, owner=owner, public=public, keyword=keyword)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperatorsApi->list_operators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number starting from 1 | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 25]
 **name** | [**list[str]**](str.md)| The account name | [optional] 
 **owner** | [**list[str]**](str.md)| Owner of the project | [optional] 
 **public** | **bool**| Boolean check for public/private projects | [optional] 
 **keyword** | [**list[str]**](str.md)| A keyword to index the repository by | [optional] 

### Return type

[**RepositoryListDto**](RepositoryListDto.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_operator**
> UpdateAccepted update_operator(owner, name, update_repository_dto)

Update an Operator

Update an operator (must have `contribute` permission)

### Example

* Bearer Authentication (JWT):
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

# Configure Bearer authorization: JWT
configuration.access_token = auth_response.access_token

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Create an instance of the API class
api_instance = pollination_sdk.OperatorsApi(pollination_sdk.ApiClient(configuration))
owner = 'owner_example' # str | 
name = 'name_example' # str | 
update_repository_dto = pollination_sdk.UpdateRepositoryDto() # UpdateRepositoryDto | 

try:
    # Update an Operator
    api_response = api_instance.update_operator(owner, name, update_repository_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperatorsApi->update_operator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **update_repository_dto** | [**UpdateRepositoryDto**](UpdateRepositoryDto.md)|  | 

### Return type

[**UpdateAccepted**](UpdateAccepted.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**400** | Invalid request |  -  |
**202** | Success |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

