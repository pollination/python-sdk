# pollination_sdk.UserApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_password**](UserApi.md#change_password) | **POST** /user/change_password | Make a password change request
[**get_me**](UserApi.md#get_me) | **GET** /user | Get authenticated user profile.
[**get_roles**](UserApi.md#get_roles) | **GET** /user/roles | Get the authenticated user roles
[**list_refresh_tokens**](UserApi.md#list_refresh_tokens) | **GET** /user/tokens | Get a list of token names
[**login**](UserApi.md#login) | **POST** /user/login | Login to the platform and get a JWT back
[**signup**](UserApi.md#signup) | **POST** /user/signup | Sign Up to the platform!
[**upsert_refresh_token**](UserApi.md#upsert_refresh_token) | **POST** /user/tokens | Get refresh token and delete previous one if it exists


# **change_password**
> object change_password(email_request)

Make a password change request

Make a password change request

### Example

```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pollination_sdk.UserApi()
email_request = pollination_sdk.EmailRequest() # EmailRequest | 

try:
    # Make a password change request
    api_response = api_instance.change_password(email_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->change_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_request** | [**EmailRequest**](EmailRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**400** | Invalid request |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_me**
> PrivateUserDto get_me()

Get authenticated user profile.

Get authenticated user profile

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
api_instance = pollination_sdk.UserApi(pollination_sdk.ApiClient(configuration))

try:
    # Get authenticated user profile.
    api_response = api_instance.get_me()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_me: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PrivateUserDto**](PrivateUserDto.md)

### Authorization

[Compulsory Auth](../README.md#Compulsory Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_roles**
> list[str] get_roles()

Get the authenticated user roles

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
api_instance = pollination_sdk.UserApi(pollination_sdk.ApiClient(configuration))

try:
    # Get the authenticated user roles
    api_response = api_instance.get_roles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_roles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[Compulsory Auth](../README.md#Compulsory Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_refresh_tokens**
> list[RefreshTokenDto] list_refresh_tokens()

Get a list of token names

Get a list of token names

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
api_instance = pollination_sdk.UserApi(pollination_sdk.ApiClient(configuration))

try:
    # Get a list of token names
    api_response = api_instance.list_refresh_tokens()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_refresh_tokens: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RefreshTokenDto]**](RefreshTokenDto.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> LoginToken login(login_dto)

Login to the platform and get a JWT back

Login a user

### Example

```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pollination_sdk.UserApi()
login_dto = pollination_sdk.LoginDto() # LoginDto | 

try:
    # Login to the platform and get a JWT back
    api_response = api_instance.login(login_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_dto** | [**LoginDto**](LoginDto.md)|  | 

### Return type

[**LoginToken**](LoginToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signup**
> object signup(sign_up_dto)

Sign Up to the platform!

Sign Up a new user

### Example

```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pollination_sdk.UserApi()
sign_up_dto = pollination_sdk.SignUpDto() # SignUpDto | 

try:
    # Sign Up to the platform!
    api_response = api_instance.signup(sign_up_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->signup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sign_up_dto** | [**SignUpDto**](SignUpDto.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**400** | Invalid request |  -  |
**202** | Accepted |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_refresh_token**
> str upsert_refresh_token(create_token_dto)

Get refresh token and delete previous one if it exists

Get refresh token and delete previous one if it exists

### Example

```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = pollination_sdk.UserApi()
create_token_dto = pollination_sdk.CreateTokenDto() # CreateTokenDto | 

try:
    # Get refresh token and delete previous one if it exists
    api_response = api_instance.upsert_refresh_token(create_token_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->upsert_refresh_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_token_dto** | [**CreateTokenDto**](CreateTokenDto.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

