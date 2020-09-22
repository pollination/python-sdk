# pollination_sdk.ProjectsApi

All URIs are relative to *https://api.pollination.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectsApi.md#create_project) | **POST** /projects/{owner} | Create a Project
[**delete_project**](ProjectsApi.md#delete_project) | **DELETE** /projects/{owner}/{name} | Delete a Project
[**delete_project_org_permission**](ProjectsApi.md#delete_project_org_permission) | **DELETE** /projects/{owner}/{name}/permissions | Remove a Project permissions
[**get_project**](ProjectsApi.md#get_project) | **GET** /projects/{owner}/{name} | Get a project
[**get_project_access_permissions**](ProjectsApi.md#get_project_access_permissions) | **GET** /projects/{owner}/{name}/permissions | Get a project&#39;s access permissions
[**list_projects**](ProjectsApi.md#list_projects) | **GET** /projects | List Projects
[**update**](ProjectsApi.md#update) | **PUT** /projects/{owner}/{name} | Update a Project
[**upsert_project_permission**](ProjectsApi.md#upsert_project_permission) | **PATCH** /projects/{owner}/{name}/permissions | Upsert a new permission to a project


# **create_project**
> CreatedContent create_project(owner, patch_project_dto)

Create a Project

Create a new project.

### Example

* Bearer Authentication (CompulsoryAuth):
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

# Configure Bearer authorization: CompulsoryAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.ProjectsApi(api_client)
    owner = 'owner_example' # str | 
patch_project_dto = pollination_sdk.PatchProjectDto() # PatchProjectDto | 

    try:
        # Create a Project
        api_response = api_instance.create_project(owner, patch_project_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **patch_project_dto** | [**PatchProjectDto**](PatchProjectDto.md)|  | 

### Return type

[**CreatedContent**](CreatedContent.md)

### Authorization

[CompulsoryAuth](../README.md#CompulsoryAuth)

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

# **delete_project**
> delete_project(owner, name)

Delete a Project

Delete a project (must have `admin` permission)

### Example

* Bearer Authentication (CompulsoryAuth):
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

# Configure Bearer authorization: CompulsoryAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.ProjectsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 

    try:
        # Delete a Project
        api_instance.delete_project(owner, name)
    except ApiException as e:
        print("Exception when calling ProjectsApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[CompulsoryAuth](../README.md#CompulsoryAuth)

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

# **delete_project_org_permission**
> delete_project_org_permission(owner, name, project_policy_subject_dto)

Remove a Project permissions

Delete a project's access policy (must have `admin` permission)

### Example

* Bearer Authentication (CompulsoryAuth):
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

# Configure Bearer authorization: CompulsoryAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.ProjectsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
project_policy_subject_dto = pollination_sdk.ProjectPolicySubjectDto() # ProjectPolicySubjectDto | 

    try:
        # Remove a Project permissions
        api_instance.delete_project_org_permission(owner, name, project_policy_subject_dto)
    except ApiException as e:
        print("Exception when calling ProjectsApi->delete_project_org_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **project_policy_subject_dto** | [**ProjectPolicySubjectDto**](ProjectPolicySubjectDto.md)|  | 

### Return type

void (empty response body)

### Authorization

[CompulsoryAuth](../README.md#CompulsoryAuth)

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

# **get_project**
> ProjectDto get_project(owner, name)

Get a project

Retrieve a project by name

### Example

* Bearer Authentication (OptionalAuth):
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

# Configure Bearer authorization: OptionalAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.ProjectsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 

    try:
        # Get a project
        api_response = api_instance.get_project(owner, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**ProjectDto**](ProjectDto.md)

### Authorization

[OptionalAuth](../README.md#OptionalAuth)

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

# **get_project_access_permissions**
> list[ProjectAccessPolicyDto] get_project_access_permissions(owner, name)

Get a project's access permissions

Retrieve a project's access permissions (must have `contribute` permission)

### Example

* Bearer Authentication (CompulsoryAuth):
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

# Configure Bearer authorization: CompulsoryAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.ProjectsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 

    try:
        # Get a project's access permissions
        api_response = api_instance.get_project_access_permissions(owner, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_project_access_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**list[ProjectAccessPolicyDto]**](ProjectAccessPolicyDto.md)

### Authorization

[CompulsoryAuth](../README.md#CompulsoryAuth)

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

# **list_projects**
> list[ProjectDto] list_projects(page=page, per_page=per_page, id=id, name=name, owner=owner, public=public, operator=operator)

List Projects

search for projects using query parameters

### Example

* Bearer Authentication (OptionalAuth):
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

# Configure Bearer authorization: OptionalAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.ProjectsApi(api_client)
    page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)
id = ['id_example'] # list[str] | The ID of a project to search for (optional)
name = ['name_example'] # list[str] | The account name (optional)
owner = ['owner_example'] # list[str] | Owner of the project (optional)
public = True # bool | Boolean check for public/private projects (optional)
operator = ['operator_example'] # list[str] | Name of an operator to search workflows by (optional)

    try:
        # List Projects
        api_response = api_instance.list_projects(page=page, per_page=per_page, id=id, name=name, owner=owner, public=public, operator=operator)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->list_projects: %s\n" % e)
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

[**list[ProjectDto]**](ProjectDto.md)

### Authorization

[OptionalAuth](../README.md#OptionalAuth)

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

# **update**
> UpdateAccepted update(owner, name, patch_project_dto)

Update a Project

Update a project (must have `contribute` permission)

### Example

* Bearer Authentication (CompulsoryAuth):
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

# Configure Bearer authorization: CompulsoryAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.ProjectsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
patch_project_dto = pollination_sdk.PatchProjectDto() # PatchProjectDto | 

    try:
        # Update a Project
        api_response = api_instance.update(owner, name, patch_project_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **patch_project_dto** | [**PatchProjectDto**](PatchProjectDto.md)|  | 

### Return type

[**UpdateAccepted**](UpdateAccepted.md)

### Authorization

[CompulsoryAuth](../README.md#CompulsoryAuth)

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

# **upsert_project_permission**
> UpdateAccepted upsert_project_permission(owner, name, project_access_policy_dto)

Upsert a new permission to a project

Upsert a project's access policy (must have `admin` permission)

### Example

* Bearer Authentication (CompulsoryAuth):
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

# Configure Bearer authorization: CompulsoryAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.ProjectsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
project_access_policy_dto = pollination_sdk.ProjectAccessPolicyDto() # ProjectAccessPolicyDto | 

    try:
        # Upsert a new permission to a project
        api_response = api_instance.upsert_project_permission(owner, name, project_access_policy_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->upsert_project_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **project_access_policy_dto** | [**ProjectAccessPolicyDto**](ProjectAccessPolicyDto.md)|  | 

### Return type

[**UpdateAccepted**](UpdateAccepted.md)

### Authorization

[CompulsoryAuth](../README.md#CompulsoryAuth)

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

