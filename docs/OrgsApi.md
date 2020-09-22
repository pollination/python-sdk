# pollination_sdk.OrgsApi

All URIs are relative to *https://api.pollination.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_org**](OrgsApi.md#create_org) | **POST** /orgs | Create an Org
[**delete_org**](OrgsApi.md#delete_org) | **DELETE** /orgs/{name} | Delete an Org
[**delete_org_member**](OrgsApi.md#delete_org_member) | **DELETE** /orgs/{name}/members/{username} | Remove an Org member
[**get_org**](OrgsApi.md#get_org) | **GET** /orgs/{name} | Get an Org
[**get_org_members**](OrgsApi.md#get_org_members) | **GET** /orgs/{name}/members | List an Org&#39;s members
[**list_orgs**](OrgsApi.md#list_orgs) | **GET** /orgs | List Orgs
[**update_org**](OrgsApi.md#update_org) | **PUT** /orgs/{name} | Update an Org
[**upsert_org_member**](OrgsApi.md#upsert_org_member) | **PATCH** /orgs/{name}/members/{username}/{role} | Add or update the role of an Org Member


# **create_org**
> CreatedContent create_org(create_org_dto)

Create an Org

Create a new org.

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
    api_instance = pollination_sdk.OrgsApi(api_client)
    create_org_dto = pollination_sdk.CreateOrgDto() # CreateOrgDto | 

    try:
        # Create an Org
        api_response = api_instance.create_org(create_org_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrgsApi->create_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_org_dto** | [**CreateOrgDto**](CreateOrgDto.md)|  | 

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

# **delete_org**
> delete_org(name)

Delete an Org

Delete a org (must have `admin` permission)

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
    api_instance = pollination_sdk.OrgsApi(api_client)
    name = 'name_example' # str | 

    try:
        # Delete an Org
        api_instance.delete_org(name)
    except ApiException as e:
        print("Exception when calling OrgsApi->delete_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **delete_org_member**
> delete_org_member(name, username)

Remove an Org member

Remove a member from the org (must have org `owner` role)

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
    api_instance = pollination_sdk.OrgsApi(api_client)
    name = 'name_example' # str | 
username = 'username_example' # str | 

    try:
        # Remove an Org member
        api_instance.delete_org_member(name, username)
    except ApiException as e:
        print("Exception when calling OrgsApi->delete_org_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **username** | **str**|  | 

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

# **get_org**
> OrgDto get_org(name)

Get an Org

Retrieve a org by name

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
    api_instance = pollination_sdk.OrgsApi(api_client)
    name = 'name_example' # str | 

    try:
        # Get an Org
        api_response = api_instance.get_org(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrgsApi->get_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**OrgDto**](OrgDto.md)

### Authorization

No authorization required

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

# **get_org_members**
> list[OrgMemberDto] get_org_members(name)

List an Org's members

Retrieve a org's members

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
    api_instance = pollination_sdk.OrgsApi(api_client)
    name = 'name_example' # str | 

    try:
        # List an Org's members
        api_response = api_instance.get_org_members(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrgsApi->get_org_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**list[OrgMemberDto]**](OrgMemberDto.md)

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

# **list_orgs**
> list[OrgDto] list_orgs(page=page, per_page=per_page, name=name, member=member)

List Orgs

search for orgs using query parameters

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
    api_instance = pollination_sdk.OrgsApi(api_client)
    page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)
name = ['name_example'] # list[str] | The account name (optional)
member = ['member_example'] # list[str] | The ID of a user (optional)

    try:
        # List Orgs
        api_response = api_instance.list_orgs(page=page, per_page=per_page, name=name, member=member)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrgsApi->list_orgs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number starting from 1 | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 25]
 **name** | [**list[str]**](str.md)| The account name | [optional] 
 **member** | [**list[str]**](str.md)| The ID of a user | [optional] 

### Return type

[**list[OrgDto]**](OrgDto.md)

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

# **update_org**
> UpdateAccepted update_org(name, patch_org_dto)

Update an Org

Update a org (must have org `owner` role)

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
    api_instance = pollination_sdk.OrgsApi(api_client)
    name = 'name_example' # str | 
patch_org_dto = pollination_sdk.PatchOrgDto() # PatchOrgDto | 

    try:
        # Update an Org
        api_response = api_instance.update_org(name, patch_org_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrgsApi->update_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **patch_org_dto** | [**PatchOrgDto**](PatchOrgDto.md)|  | 

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

# **upsert_org_member**
> UpdateAccepted upsert_org_member(name, username, role)

Add or update the role of an Org Member

Upsert a member role to the org (must have org `owner` role)

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
    api_instance = pollination_sdk.OrgsApi(api_client)
    name = 'name_example' # str | 
username = 'username_example' # str | 
role = pollination_sdk.OrgRoleEnum() # OrgRoleEnum | 

    try:
        # Add or update the role of an Org Member
        api_response = api_instance.upsert_org_member(name, username, role)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrgsApi->upsert_org_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **username** | **str**|  | 
 **role** | [**OrgRoleEnum**](.md)|  | 

### Return type

[**UpdateAccepted**](UpdateAccepted.md)

### Authorization

[CompulsoryAuth](../README.md#CompulsoryAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

