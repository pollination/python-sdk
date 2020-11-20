# pollination_sdk.UsersApi

All URIs are relative to *https://api.pollination.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_username**](UsersApi.md#check_username) | **GET** /users/check_username/{username} | Check if a username is already taken
[**get_one_user**](UsersApi.md#get_one_user) | **GET** /users/{name} | Get a specific user profile
[**list_users**](UsersApi.md#list_users) | **GET** /users | List Users


# **check_username**
> object check_username(username)

Check if a username is already taken

Check if a username is already taken by a user or an org

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
    api_instance = pollination_sdk.UsersApi(api_client)
    username = 'username_example' # str | 

    try:
        # Check if a username is already taken
        api_response = api_instance.check_username(username)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->check_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

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
**200** | Username not taken |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_user**
> UserPublic get_one_user(name)

Get a specific user profile

Get a specific user profile by name

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
    api_instance = pollination_sdk.UsersApi(api_client)
    name = 'name_example' # str | 

    try:
        # Get a specific user profile
        api_response = api_instance.get_one_user(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->get_one_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**UserPublic**](UserPublic.md)

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

# **list_users**
> UserPublicList list_users(page=page, per_page=per_page, username=username)

List Users

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
    api_instance = pollination_sdk.UsersApi(api_client)
    page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)
username = ['username_example'] # list[str] | Username of the user to search for (optional)

    try:
        # List Users
        api_response = api_instance.list_users(page=page, per_page=per_page, username=username)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number starting from 1 | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 25]
 **username** | [**list[str]**](str.md)| Username of the user to search for | [optional] 

### Return type

[**UserPublicList**](UserPublicList.md)

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

