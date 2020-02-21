# pollination_sdk.WorkflowsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workflow**](WorkflowsApi.md#create_workflow) | **POST** /workflows/{owner} | Create a Workflow
[**delete_workflow**](WorkflowsApi.md#delete_workflow) | **DELETE** /workflows/{owner}/{name} | Delete a Workflow
[**delete_workflow_org_permission**](WorkflowsApi.md#delete_workflow_org_permission) | **DELETE** /workflows/{owner}/{name}/permissions/org/{org_role} | Remove a Workflow org level permission
[**delete_workflow_team_permission**](WorkflowsApi.md#delete_workflow_team_permission) | **DELETE** /workflows/{owner}/{name}/permissions/team/{team_name} | Remove a Workflow team level permission
[**get_workflow**](WorkflowsApi.md#get_workflow) | **GET** /workflows/{owner}/{name} | Get a workflow
[**get_workflow_access_permissions**](WorkflowsApi.md#get_workflow_access_permissions) | **GET** /workflows/{owner}/{name}/permissions | Get a workflow&#39;s access permissions
[**list_workflows**](WorkflowsApi.md#list_workflows) | **GET** /workflows | List Workflows
[**update_workflow**](WorkflowsApi.md#update_workflow) | **PUT** /workflows/{owner}/{name} | Update a Workflow
[**upsert_workflow_org_permission**](WorkflowsApi.md#upsert_workflow_org_permission) | **PATCH** /workflows/{owner}/{name}/permissions/org/{org_role}/{permission} | Upsert a Workflow org level permission
[**upsert_workflow_team_permission**](WorkflowsApi.md#upsert_workflow_team_permission) | **PATCH** /workflows/{owner}/{name}/permissions/team/{team_name}/{permission} | Upsert a Workflow team level permission


# **create_workflow**
> CreatedContent create_workflow(owner, create_workflow_dto)

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
api_instance = pollination_sdk.WorkflowsApi(pollination_sdk.ApiClient(configuration))
owner = 'owner_example' # str | 
create_workflow_dto = pollination_sdk.CreateWorkflowDto() # CreateWorkflowDto | 

try:
    # Create a Workflow
    api_response = api_instance.create_workflow(owner, create_workflow_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowsApi->create_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **create_workflow_dto** | [**CreateWorkflowDto**](CreateWorkflowDto.md)|  | 

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
**201** | Success |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workflow**
> delete_workflow(owner, name)

Delete a Workflow

Delete a workflow (must have `admin` permission)

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
api_instance = pollination_sdk.WorkflowsApi(pollination_sdk.ApiClient(configuration))
owner = 'owner_example' # str | 
name = 'name_example' # str | 

try:
    # Delete a Workflow
    api_instance.delete_workflow(owner, name)
except ApiException as e:
    print("Exception when calling WorkflowsApi->delete_workflow: %s\n" % e)
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
**204** | Success |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workflow_org_permission**
> delete_workflow_org_permission(owner, name, org_role)

Remove a Workflow org level permission

Delete a workflow's access policy (must have `admin` permission)

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
api_instance = pollination_sdk.WorkflowsApi(pollination_sdk.ApiClient(configuration))
owner = 'owner_example' # str | 
name = 'name_example' # str | 
org_role = 'org_role_example' # str | 

try:
    # Remove a Workflow org level permission
    api_instance.delete_workflow_org_permission(owner, name, org_role)
except ApiException as e:
    print("Exception when calling WorkflowsApi->delete_workflow_org_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **org_role** | **str**|  | 

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

# **delete_workflow_team_permission**
> delete_workflow_team_permission(owner, name, team_name)

Remove a Workflow team level permission

Delete a workflow's access policy (must have `admin` permission)

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
api_instance = pollination_sdk.WorkflowsApi(pollination_sdk.ApiClient(configuration))
owner = 'owner_example' # str | 
name = 'name_example' # str | 
team_name = 'team_name_example' # str | 

try:
    # Remove a Workflow team level permission
    api_instance.delete_workflow_team_permission(owner, name, team_name)
except ApiException as e:
    print("Exception when calling WorkflowsApi->delete_workflow_team_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **team_name** | **str**|  | 

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

# **get_workflow**
> WorkflowDto get_workflow(owner, name)

Get a workflow

Retrieve a workflow by name

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
api_instance = pollination_sdk.WorkflowsApi(pollination_sdk.ApiClient(configuration))
owner = 'owner_example' # str | 
name = 'name_example' # str | 

try:
    # Get a workflow
    api_response = api_instance.get_workflow(owner, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowsApi->get_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**WorkflowDto**](WorkflowDto.md)

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

# **get_workflow_access_permissions**
> list[WorkflowAccessPolicyDto] get_workflow_access_permissions(owner, name)

Get a workflow's access permissions

Retrieve a workflow's access permissions (must have `contribute` permission)

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
api_instance = pollination_sdk.WorkflowsApi(pollination_sdk.ApiClient(configuration))
owner = 'owner_example' # str | 
name = 'name_example' # str | 

try:
    # Get a workflow's access permissions
    api_response = api_instance.get_workflow_access_permissions(owner, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowsApi->get_workflow_access_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**list[WorkflowAccessPolicyDto]**](WorkflowAccessPolicyDto.md)

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

# **list_workflows**
> list[WorkflowDto] list_workflows(page=page, per_page=per_page, id=id, name=name, owner=owner, public=public, operator=operator)

List Workflows

search for workflows using query parameters

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
api_instance = pollination_sdk.WorkflowsApi(pollination_sdk.ApiClient(configuration))
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)
id = ['id_example'] # list[str] | The ID of a project to search for (optional)
name = ['name_example'] # list[str] | The account name (optional)
owner = ['owner_example'] # list[str] | Owner of the project (optional)
public = True # bool | Boolean check for public/private projects (optional)
operator = ['operator_example'] # list[str] | Name of an operator to search workflows by (optional)

try:
    # List Workflows
    api_response = api_instance.list_workflows(page=page, per_page=per_page, id=id, name=name, owner=owner, public=public, operator=operator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowsApi->list_workflows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number starting from 1 | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 25]
 **id** | [**list[str]**](str.md)| The ID of a project to search for | [optional] 
 **name** | [**list[str]**](str.md)| The account name | [optional] 
 **owner** | [**list[str]**](str.md)| Owner of the project | [optional] 
 **public** | **bool**| Boolean check for public/private projects | [optional] 
 **operator** | [**list[str]**](str.md)| Name of an operator to search workflows by | [optional] 

### Return type

[**list[WorkflowDto]**](WorkflowDto.md)

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

# **update_workflow**
> UpdateAccepted update_workflow(owner, name, patch_workflow)

Update a Workflow

Update a workflow (must have `contribute` permission)

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
api_instance = pollination_sdk.WorkflowsApi(pollination_sdk.ApiClient(configuration))
owner = 'owner_example' # str | 
name = 'name_example' # str | 
patch_workflow = pollination_sdk.PatchWorkflow() # PatchWorkflow | 

try:
    # Update a Workflow
    api_response = api_instance.update_workflow(owner, name, patch_workflow)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowsApi->update_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **patch_workflow** | [**PatchWorkflow**](PatchWorkflow.md)|  | 

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
**202** | Success |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_workflow_org_permission**
> UpdateAccepted upsert_workflow_org_permission(owner, name, org_role, permission)

Upsert a Workflow org level permission

Upsert a workflow's access policy (must have `admin` permission)

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
api_instance = pollination_sdk.WorkflowsApi(pollination_sdk.ApiClient(configuration))
owner = 'owner_example' # str | 
name = 'name_example' # str | 
org_role = 'org_role_example' # str | 
permission = 'permission_example' # str | 

try:
    # Upsert a Workflow org level permission
    api_response = api_instance.upsert_workflow_org_permission(owner, name, org_role, permission)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowsApi->upsert_workflow_org_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **org_role** | **str**|  | 
 **permission** | **str**|  | 

### Return type

[**UpdateAccepted**](UpdateAccepted.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Success |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_workflow_team_permission**
> UpdateAccepted upsert_workflow_team_permission(owner, name, team_name, permission)

Upsert a Workflow team level permission

Upsert a workflow's access policy (must have `admin` permission)

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
api_instance = pollination_sdk.WorkflowsApi(pollination_sdk.ApiClient(configuration))
owner = 'owner_example' # str | 
name = 'name_example' # str | 
team_name = 'team_name_example' # str | 
permission = 'permission_example' # str | 

try:
    # Upsert a Workflow team level permission
    api_response = api_instance.upsert_workflow_team_permission(owner, name, team_name, permission)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowsApi->upsert_workflow_team_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **team_name** | **str**|  | 
 **permission** | **str**|  | 

### Return type

[**UpdateAccepted**](UpdateAccepted.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Success |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

