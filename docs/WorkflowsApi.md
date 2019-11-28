# pollination_sdk.WorkflowsApi

All URIs are relative to *https://api.pollination.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](WorkflowsApi.md#create) | **POST** /workflows | Create a Workflow
[**delete**](WorkflowsApi.md#delete) | **DELETE** /workflows/{id} | Delete a Workflow
[**get**](WorkflowsApi.md#get) | **GET** /workflows/{id} | Get a Workflow
[**list**](WorkflowsApi.md#list) | **GET** /workflows | List Workflows
[**update**](WorkflowsApi.md#update) | **PUT** /workflows/{id} | Update a Workflow


# **create**
> object create(workflow)

Create a Workflow

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
api_instance = pollination_sdk.WorkflowsApi(pollination_sdk.ApiClient(configuration))
workflow = pollination_sdk.Workflow() # Workflow | 

try:
    # Create a Workflow
    api_response = api_instance.create(workflow)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow** | [**Workflow**](Workflow.md)|  | 

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
**201** | Success |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> object delete(id)

Delete a Workflow

Delete a workflow.

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
api_instance = pollination_sdk.WorkflowsApi(pollination_sdk.ApiClient(configuration))
id = 'id_example' # str | Simulation id.

try:
    # Delete a Workflow
    api_response = api_instance.delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowsApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Simulation id. | 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Workflow get(id)

Get a Workflow

Retrieve a workflow.

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
api_instance = pollination_sdk.WorkflowsApi(pollination_sdk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a Workflow
    api_response = api_instance.get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowsApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**Workflow**](Workflow.md)

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> list[Workflow] list(page=page, per_page=per_page)

List Workflows

Retrieve a list of workflows.

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
api_instance = pollination_sdk.WorkflowsApi(pollination_sdk.ApiClient(configuration))
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)

try:
    # List Workflows
    api_response = api_instance.list(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number starting from 1 | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**list[Workflow]**](Workflow.md)

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

# **update**
> Workflow update(id, workflow)

Update a Workflow

Update a workflow.

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
api_instance = pollination_sdk.WorkflowsApi(pollination_sdk.ApiClient(configuration))
id = 'id_example' # str | 
workflow = pollination_sdk.Workflow() # Workflow | 

try:
    # Update a Workflow
    api_response = api_instance.update(id, workflow)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **workflow** | [**Workflow**](Workflow.md)|  | 

### Return type

[**Workflow**](Workflow.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**404** | Not found |  -  |
**200** | Success |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

