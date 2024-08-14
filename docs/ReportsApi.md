# pollination_sdk.ReportsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_compute_usage_report**](ReportsApi.md#get_compute_usage_report) | **GET** /reports/{name}/compute-usage | Get compute usage report for an account
[**get_org_member_usage_report**](ReportsApi.md#get_org_member_usage_report) | **GET** /reports/{name}/organization-member-usage | Get organization member usage report for an organization account


# **get_compute_usage_report**
> ReportComputeUsage get_compute_usage_report(namefrom_date=from_dateto_date=to_date)

Get compute usage report for an account

Get compute usage report for an account

### Example

* Bearer (JWT) Authentication (JWTAuth):
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

# Configure Bearer authorization (JWT): JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "http://localhost",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.ReportsApi(api_client)
    name = 'name_example' # str | 
from_date = '2013-10-20' # date |  (optional)
to_date = '2013-10-20' # date |  (optional)

    try:
        # Get compute usage report for an account
        api_response = api_instance.get_compute_usage_report(namefrom_date=from_dateto_date=to_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->get_compute_usage_report: %s\n" % e)
```

* Api Key Authentication (APIKeyAuth):
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

# Configure Bearer authorization (JWT): JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "http://localhost",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.ReportsApi(api_client)
    name = 'name_example' # str | 
from_date = '2013-10-20' # date |  (optional)
to_date = '2013-10-20' # date |  (optional)

    try:
        # Get compute usage report for an account
        api_response = api_instance.get_compute_usage_report(namefrom_date=from_dateto_date=to_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->get_compute_usage_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **from_date** | **date**|  | [optional] 
 **to_date** | **date**|  | [optional] 

### Return type

[**ReportComputeUsage**](ReportComputeUsage.md)

### Authorization

[JWTAuth](../README.md#JWTAuth), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_org_member_usage_report**
> ReportOrganizationMemberUsage get_org_member_usage_report(name)

Get organization member usage report for an organization account

Get compute usage report for an account

### Example

* Bearer (JWT) Authentication (JWTAuth):
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

# Configure Bearer authorization (JWT): JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "http://localhost",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.ReportsApi(api_client)
    name = 'name_example' # str | 

    try:
        # Get organization member usage report for an organization account
        api_response = api_instance.get_org_member_usage_report(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->get_org_member_usage_report: %s\n" % e)
```

* Api Key Authentication (APIKeyAuth):
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

# Configure Bearer authorization (JWT): JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "http://localhost",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.ReportsApi(api_client)
    name = 'name_example' # str | 

    try:
        # Get organization member usage report for an organization account
        api_response = api_instance.get_org_member_usage_report(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportsApi->get_org_member_usage_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**ReportOrganizationMemberUsage**](ReportOrganizationMemberUsage.md)

### Authorization

[JWTAuth](../README.md#JWTAuth), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

