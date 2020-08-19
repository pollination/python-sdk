# pollination_sdk.TeamsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_team**](TeamsApi.md#create_team) | **POST** /orgs/{org_name}/teams | Create a Team
[**delete_org_team_member**](TeamsApi.md#delete_org_team_member) | **DELETE** /orgs/{org_name}/teams/{team_slug}/members/{username} | Remove a team member
[**delete_team**](TeamsApi.md#delete_team) | **DELETE** /orgs/{org_name}/teams/{team_slug} | Delete a Team
[**get_org_team_members**](TeamsApi.md#get_org_team_members) | **GET** /orgs/{org_name}/teams/{team_slug}/members | List a team&#39;s members
[**get_team**](TeamsApi.md#get_team) | **GET** /orgs/{org_name}/teams/{team_slug} | Get a Team
[**list_org_teams**](TeamsApi.md#list_org_teams) | **GET** /orgs/{org_name}/teams | List Teams
[**update_team**](TeamsApi.md#update_team) | **PUT** /orgs/{org_name}/teams/{team_slug} | Update a Team
[**upsert_org_team_member**](TeamsApi.md#upsert_org_team_member) | **PATCH** /orgs/{org_name}/teams/{team_slug}/members/{username}/{role} | Add or update the role of an Org Member


# **create_team**
> CreatedContent create_team(org_name, patch_team_dto)

Create a Team

Create a new team (must be parent org member)

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
api_instance = pollination_sdk.TeamsApi(pollination_sdk.ApiClient(configuration))
org_name = 'org_name_example' # str | 
patch_team_dto = pollination_sdk.PatchTeamDto() # PatchTeamDto | 

try:
    # Create a Team
    api_response = api_instance.create_team(org_name, patch_team_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->create_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **str**|  | 
 **patch_team_dto** | [**PatchTeamDto**](PatchTeamDto.md)|  | 

### Return type

[**CreatedContent**](CreatedContent.md)

### Authorization

[Compulsory Auth](../README.md#Compulsory Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**400** | Invalid request |  -  |
**202** | Accepted |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_org_team_member**
> delete_org_team_member(org_name, team_slug, username)

Remove a team member

Remove a member from the org (must have org `owner` role)

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
api_instance = pollination_sdk.TeamsApi(pollination_sdk.ApiClient(configuration))
org_name = 'org_name_example' # str | 
team_slug = 'team_slug_example' # str | 
username = 'username_example' # str | 

try:
    # Remove a team member
    api_instance.delete_org_team_member(org_name, team_slug, username)
except ApiException as e:
    print("Exception when calling TeamsApi->delete_org_team_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **str**|  | 
 **team_slug** | **str**|  | 
 **username** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Compulsory Auth](../README.md#Compulsory Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**400** | Invalid request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team**
> delete_team(org_name, team_slug)

Delete a Team

Delete a team (must have team or org `owner` role)

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
api_instance = pollination_sdk.TeamsApi(pollination_sdk.ApiClient(configuration))
org_name = 'org_name_example' # str | 
team_slug = 'team_slug_example' # str | 

try:
    # Delete a Team
    api_instance.delete_team(org_name, team_slug)
except ApiException as e:
    print("Exception when calling TeamsApi->delete_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **str**|  | 
 **team_slug** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Compulsory Auth](../README.md#Compulsory Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**400** | Invalid request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_org_team_members**
> list[TeamMemberDto] get_org_team_members(org_name, team_slug)

List a team's members

Retrieve a tean's members

### Example

```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pollination_sdk.TeamsApi()
org_name = 'org_name_example' # str | 
team_slug = 'team_slug_example' # str | 

try:
    # List a team's members
    api_response = api_instance.get_org_team_members(org_name, team_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_org_team_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **str**|  | 
 **team_slug** | **str**|  | 

### Return type

[**list[TeamMemberDto]**](TeamMemberDto.md)

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

# **get_team**
> TeamDto get_team(org_name, team_slug)

Get a Team

Retrieve a team by name

### Example

```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pollination_sdk.TeamsApi()
org_name = 'org_name_example' # str | 
team_slug = 'team_slug_example' # str | 

try:
    # Get a Team
    api_response = api_instance.get_team(org_name, team_slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **str**|  | 
 **team_slug** | **str**|  | 

### Return type

[**TeamDto**](TeamDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved |  -  |
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**400** | Invalid request |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_org_teams**
> list[TeamDto] list_org_teams(org_name, page=page, per_page=per_page, name=name, member=member)

List Teams

search for orgs using query parameters

### Example

```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pollination_sdk.TeamsApi()
org_name = 'org_name_example' # str | 
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)
name = ['name_example'] # list[str] | The account name (optional)
member = ['member_example'] # list[str] | The ID of a user (optional)

try:
    # List Teams
    api_response = api_instance.list_org_teams(org_name, page=page, per_page=per_page, name=name, member=member)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->list_org_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **str**|  | 
 **page** | **int**| Page number starting from 1 | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 25]
 **name** | [**list[str]**](str.md)| The account name | [optional] 
 **member** | [**list[str]**](str.md)| The ID of a user | [optional] 

### Return type

[**list[TeamDto]**](TeamDto.md)

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

# **update_team**
> UpdateAccepted update_team(org_name, team_slug, patch_team_dto)

Update a Team

Update a team (must have team or org `owner` role)

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
api_instance = pollination_sdk.TeamsApi(pollination_sdk.ApiClient(configuration))
org_name = 'org_name_example' # str | 
team_slug = 'team_slug_example' # str | 
patch_team_dto = pollination_sdk.PatchTeamDto() # PatchTeamDto | 

try:
    # Update a Team
    api_response = api_instance.update_team(org_name, team_slug, patch_team_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->update_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **str**|  | 
 **team_slug** | **str**|  | 
 **patch_team_dto** | [**PatchTeamDto**](PatchTeamDto.md)|  | 

### Return type

[**UpdateAccepted**](UpdateAccepted.md)

### Authorization

[Compulsory Auth](../README.md#Compulsory Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**400** | Invalid request |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_org_team_member**
> UpdateAccepted upsert_org_team_member(org_name, team_slug, username, role)

Add or update the role of an Org Member

Upsert a member role to the team (must have org or team `owner` role)

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
api_instance = pollination_sdk.TeamsApi(pollination_sdk.ApiClient(configuration))
org_name = 'org_name_example' # str | 
team_slug = 'team_slug_example' # str | 
username = 'username_example' # str | 
role = pollination_sdk.TeamRoleEnum() # TeamRoleEnum | 

try:
    # Add or update the role of an Org Member
    api_response = api_instance.upsert_org_team_member(org_name, team_slug, username, role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->upsert_org_team_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **str**|  | 
 **team_slug** | **str**|  | 
 **username** | **str**|  | 
 **role** | [**TeamRoleEnum**](.md)|  | 

### Return type

[**UpdateAccepted**](UpdateAccepted.md)

### Authorization

[Compulsory Auth](../README.md#Compulsory Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**400** | Invalid request |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

