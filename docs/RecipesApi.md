# pollination_sdk.RecipesApi

All URIs are relative to *https://api.pollination.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_recipe**](RecipesApi.md#create_recipe) | **POST** /recipes/{owner} | Create a Recipe
[**create_recipe_package**](RecipesApi.md#create_recipe_package) | **POST** /recipes/{owner}/{name}/tags | Create a new Recipe package
[**delete_recipe**](RecipesApi.md#delete_recipe) | **DELETE** /recipes/{owner}/{name} | Delete a Recipe
[**delete_recipe_org_permission**](RecipesApi.md#delete_recipe_org_permission) | **DELETE** /recipes/{owner}/{name}/permissions | Remove a Repository permissions
[**get_recipe**](RecipesApi.md#get_recipe) | **GET** /recipes/{owner}/{name} | Get a recipe
[**get_recipe_access_permissions**](RecipesApi.md#get_recipe_access_permissions) | **GET** /recipes/{owner}/{name}/permissions | Get recipe access permissions
[**get_recipe_by_tag**](RecipesApi.md#get_recipe_by_tag) | **GET** /recipes/{owner}/{name}/tags/{tag} | Get a recipe tag
[**list_recipe_tags**](RecipesApi.md#list_recipe_tags) | **GET** /recipes/{owner}/{name}/tags | Get a recipe tags
[**list_recipes**](RecipesApi.md#list_recipes) | **GET** /recipes | List recipes
[**update_recipe**](RecipesApi.md#update_recipe) | **PUT** /recipes/{owner}/{name} | Update a Recipe
[**upsert_recipe_permission**](RecipesApi.md#upsert_recipe_permission) | **PATCH** /recipes/{owner}/{name}/permissions | Upsert a new permission to a recipe


# **create_recipe**
> CreatedContent create_recipe(owner, repository_create)

Create a Recipe

Create a new recipe.

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
    api_instance = pollination_sdk.RecipesApi(api_client)
    owner = 'owner_example' # str | 
repository_create = pollination_sdk.RepositoryCreate() # RepositoryCreate | 

    try:
        # Create a Recipe
        api_response = api_instance.create_recipe(owner, repository_create)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RecipesApi->create_recipe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **repository_create** | [**RepositoryCreate**](RepositoryCreate.md)|  | 

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

# **create_recipe_package**
> CreatedContent create_recipe_package(owner, name, new_recipe_package, authorization=authorization)

Create a new Recipe package

Create a new recipe package version

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
    api_instance = pollination_sdk.RecipesApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
new_recipe_package = pollination_sdk.NewRecipePackage() # NewRecipePackage | 
authorization = 'authorization_example' # str |  (optional)

    try:
        # Create a new Recipe package
        api_response = api_instance.create_recipe_package(owner, name, new_recipe_package, authorization=authorization)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RecipesApi->create_recipe_package: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **new_recipe_package** | [**NewRecipePackage**](NewRecipePackage.md)|  | 
 **authorization** | **str**|  | [optional] 

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
**200** | Success |  -  |
**400** | Invalid request |  -  |
**403** | Access forbidden |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recipe**
> delete_recipe(owner, name)

Delete a Recipe

Delete a recipe (must have `admin` permission)

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
    api_instance = pollination_sdk.RecipesApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 

    try:
        # Delete a Recipe
        api_instance.delete_recipe(owner, name)
    except ApiException as e:
        print("Exception when calling RecipesApi->delete_recipe: %s\n" % e)
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

# **delete_recipe_org_permission**
> delete_recipe_org_permission(owner, name, repository_policy_subject)

Remove a Repository permissions

Delete a recipe's access policy (must have `admin` permission)

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
    api_instance = pollination_sdk.RecipesApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
repository_policy_subject = pollination_sdk.RepositoryPolicySubject() # RepositoryPolicySubject | 

    try:
        # Remove a Repository permissions
        api_instance.delete_recipe_org_permission(owner, name, repository_policy_subject)
    except ApiException as e:
        print("Exception when calling RecipesApi->delete_recipe_org_permission: %s\n" % e)
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

# **get_recipe**
> Repository get_recipe(owner, name)

Get a recipe

Retrieve a recipe by name

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
    api_instance = pollination_sdk.RecipesApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 

    try:
        # Get a recipe
        api_response = api_instance.get_recipe(owner, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RecipesApi->get_recipe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**Repository**](Repository.md)

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

# **get_recipe_access_permissions**
> RepositoryAccessPolicyList get_recipe_access_permissions(owner, name, page=page, per_page=per_page, subject_type=subject_type, permission=permission)

Get recipe access permissions

Retrieve a recipe's access permissions (must have `contribute` permission)

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
    api_instance = pollination_sdk.RecipesApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)
subject_type = ['subject_type_example'] # list[str] | The type of access policy subject (optional)
permission = ['permission_example'] # list[str] | An access policy permission string (optional)

    try:
        # Get recipe access permissions
        api_response = api_instance.get_recipe_access_permissions(owner, name, page=page, per_page=per_page, subject_type=subject_type, permission=permission)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RecipesApi->get_recipe_access_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **page** | **int**| Page number starting from 1 | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 25]
 **subject_type** | [**list[str]**](str.md)| The type of access policy subject | [optional] 
 **permission** | [**list[str]**](str.md)| An access policy permission string | [optional] 

### Return type

[**RepositoryAccessPolicyList**](RepositoryAccessPolicyList.md)

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

# **get_recipe_by_tag**
> RecipePackage get_recipe_by_tag(owner, name, tag)

Get a recipe tag

Retrieve a recipe tag by name and tag

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
    api_instance = pollination_sdk.RecipesApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
tag = 'tag_example' # str | 

    try:
        # Get a recipe tag
        api_response = api_instance.get_recipe_by_tag(owner, name, tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RecipesApi->get_recipe_by_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **tag** | **str**|  | 

### Return type

[**RecipePackage**](RecipePackage.md)

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

# **list_recipe_tags**
> RepositoryPackageList list_recipe_tags(owner, name)

Get a recipe tags

Retrieve a recipe by name

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
    api_instance = pollination_sdk.RecipesApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 

    try:
        # Get a recipe tags
        api_response = api_instance.list_recipe_tags(owner, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RecipesApi->list_recipe_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**RepositoryPackageList**](RepositoryPackageList.md)

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

# **list_recipes**
> RepositoryList list_recipes(page=page, per_page=per_page, name=name, owner=owner, public=public, keyword=keyword, permission=permission)

List recipes

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
    api_instance = pollination_sdk.RecipesApi(api_client)
    page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)
name = ['name_example'] # list[str] | The account name (optional)
owner = ['owner_example'] # list[str] | Owner of the project (optional)
public = True # bool | Boolean check for public/private projects (optional)
keyword = ['keyword_example'] # list[str] | A keyword to index the repository by (optional)
permission = ['permission_example'] # list[str] |  (optional)

    try:
        # List recipes
        api_response = api_instance.list_recipes(page=page, per_page=per_page, name=name, owner=owner, public=public, keyword=keyword, permission=permission)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RecipesApi->list_recipes: %s\n" % e)
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
 **permission** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**RepositoryList**](RepositoryList.md)

### Authorization

[OptionalAuth](../README.md#OptionalAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_recipe**
> UpdateAccepted update_recipe(owner, name, repository_update)

Update a Recipe

Update a recipe (must have `contribute` permission)

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
    api_instance = pollination_sdk.RecipesApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
repository_update = pollination_sdk.RepositoryUpdate() # RepositoryUpdate | 

    try:
        # Update a Recipe
        api_response = api_instance.update_recipe(owner, name, repository_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RecipesApi->update_recipe: %s\n" % e)
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

# **upsert_recipe_permission**
> UpdateAccepted upsert_recipe_permission(owner, name, repository_access_policy)

Upsert a new permission to a recipe

Upsert a recipe's access policy (must have `admin` permission)

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
    api_instance = pollination_sdk.RecipesApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
repository_access_policy = pollination_sdk.RepositoryAccessPolicy() # RepositoryAccessPolicy | 

    try:
        # Upsert a new permission to a recipe
        api_response = api_instance.upsert_recipe_permission(owner, name, repository_access_policy)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RecipesApi->upsert_recipe_permission: %s\n" % e)
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

