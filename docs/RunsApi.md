# pollination_sdk.RunsApi

All URIs are relative to *https://api.pollination.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_run**](RunsApi.md#create_run) | **POST** /projects/{owner}/{name}/runs | Schedule a run
[**download_run_artifact**](RunsApi.md#download_run_artifact) | **GET** /projects/{owner}/{name}/runs/{run_id}/artifacts/download | Download an artifact from the run folder
[**get_run**](RunsApi.md#get_run) | **GET** /projects/{owner}/{name}/runs/{run_id} | Get a Run
[**get_run_output**](RunsApi.md#get_run_output) | **GET** /projects/{owner}/{name}/runs/{run_id}/outputs/{output_name} | Get run output by name
[**get_run_step_logs**](RunsApi.md#get_run_step_logs) | **GET** /projects/{owner}/{name}/runs/{run_id}/steps/{step_id}/logs | Get the logs of a specific step of the run
[**get_run_steps**](RunsApi.md#get_run_steps) | **GET** /projects/{owner}/{name}/runs/{run_id}/steps | Query the steps of a run
[**list_run_artifacts**](RunsApi.md#list_run_artifacts) | **GET** /projects/{owner}/{name}/runs/{run_id}/artifacts | List artifacts in a run folder
[**list_runs**](RunsApi.md#list_runs) | **GET** /projects/{owner}/{name}/runs | List runs
[**resume_run**](RunsApi.md#resume_run) | **PUT** /projects/{owner}/{name}/runs/{run_id}/resume | resume a run
[**stop_run**](RunsApi.md#stop_run) | **PUT** /projects/{owner}/{name}/runs/{run_id}/stop | Stop a run
[**suspend_run**](RunsApi.md#suspend_run) | **PUT** /projects/{owner}/{name}/runs/{run_id}/suspend | Suspend a run


# **create_run**
> CreatedContent create_run(owner, name, job, authorization=authorization, x_pollination_token=x_pollination_token)

Schedule a run

Create a new run.

### Example

* Api Key Authentication (APIKeyAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "https://api.pollination.cloud",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization: JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.RunsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
job = pollination_sdk.Job() # Job | 
authorization = 'authorization_example' # str |  (optional)
x_pollination_token = 'x_pollination_token_example' # str |  (optional)

    try:
        # Schedule a run
        api_response = api_instance.create_run(owner, name, job, authorization=authorization, x_pollination_token=x_pollination_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RunsApi->create_run: %s\n" % e)
```

* Bearer Authentication (JWTAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "https://api.pollination.cloud",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization: JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.RunsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
job = pollination_sdk.Job() # Job | 
authorization = 'authorization_example' # str |  (optional)
x_pollination_token = 'x_pollination_token_example' # str |  (optional)

    try:
        # Schedule a run
        api_response = api_instance.create_run(owner, name, job, authorization=authorization, x_pollination_token=x_pollination_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RunsApi->create_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **job** | [**Job**](Job.md)|  | 
 **authorization** | **str**|  | [optional] 
 **x_pollination_token** | **str**|  | [optional] 

### Return type

[**CreatedContent**](CreatedContent.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth), [JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_run_artifact**
> object download_run_artifact(owner, name, run_id, path=path)

Download an artifact from the run folder

Get a download link for an artifact in a run folder

### Example

* Api Key Authentication (APIKeyAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "https://api.pollination.cloud",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization: JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.RunsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
run_id = 'run_id_example' # str | 
path = 'path_example' # str | The path to an file within a project folder (optional)

    try:
        # Download an artifact from the run folder
        api_response = api_instance.download_run_artifact(owner, name, run_id, path=path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RunsApi->download_run_artifact: %s\n" % e)
```

* Bearer Authentication (JWTAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "https://api.pollination.cloud",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization: JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.RunsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
run_id = 'run_id_example' # str | 
path = 'path_example' # str | The path to an file within a project folder (optional)

    try:
        # Download an artifact from the run folder
        api_response = api_instance.download_run_artifact(owner, name, run_id, path=path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RunsApi->download_run_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **run_id** | **str**|  | 
 **path** | **str**| The path to an file within a project folder | [optional] 

### Return type

**object**

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth), [JWTAuth](../README.md#JWTAuth)

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

# **get_run**
> Run get_run(owner, name, run_id)

Get a Run

Retrieve a run.

### Example

* Api Key Authentication (APIKeyAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "https://api.pollination.cloud",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization: JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.RunsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
run_id = 'run_id_example' # str | 

    try:
        # Get a Run
        api_response = api_instance.get_run(owner, name, run_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RunsApi->get_run: %s\n" % e)
```

* Bearer Authentication (JWTAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "https://api.pollination.cloud",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization: JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.RunsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
run_id = 'run_id_example' # str | 

    try:
        # Get a Run
        api_response = api_instance.get_run(owner, name, run_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RunsApi->get_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **run_id** | **str**|  | 

### Return type

[**Run**](Run.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth), [JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run_output**
> object get_run_output(owner, name, run_id, output_name)

Get run output by name

get run output by name

### Example

* Api Key Authentication (APIKeyAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "https://api.pollination.cloud",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization: JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.RunsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
run_id = 'run_id_example' # str | 
output_name = 'output_name_example' # str | 

    try:
        # Get run output by name
        api_response = api_instance.get_run_output(owner, name, run_id, output_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RunsApi->get_run_output: %s\n" % e)
```

* Bearer Authentication (JWTAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "https://api.pollination.cloud",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization: JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.RunsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
run_id = 'run_id_example' # str | 
output_name = 'output_name_example' # str | 

    try:
        # Get run output by name
        api_response = api_instance.get_run_output(owner, name, run_id, output_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RunsApi->get_run_output: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **run_id** | **str**|  | 
 **output_name** | **str**|  | 

### Return type

**object**

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth), [JWTAuth](../README.md#JWTAuth)

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

# **get_run_step_logs**
> str get_run_step_logs(owner, name, run_id, step_id)

Get the logs of a specific step of the run

get run step logs

### Example

* Api Key Authentication (APIKeyAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "https://api.pollination.cloud",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization: JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.RunsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
run_id = 'run_id_example' # str | 
step_id = 'step_id_example' # str | 

    try:
        # Get the logs of a specific step of the run
        api_response = api_instance.get_run_step_logs(owner, name, run_id, step_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RunsApi->get_run_step_logs: %s\n" % e)
```

* Bearer Authentication (JWTAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "https://api.pollination.cloud",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization: JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.RunsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
run_id = 'run_id_example' # str | 
step_id = 'step_id_example' # str | 

    try:
        # Get the logs of a specific step of the run
        api_response = api_instance.get_run_step_logs(owner, name, run_id, step_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RunsApi->get_run_step_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **run_id** | **str**|  | 
 **step_id** | **str**|  | 

### Return type

**str**

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth), [JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_run_steps**
> StepList get_run_steps(owner, name, run_id, status=status, step_id=step_id, until_generation=until_generation, since_generation=since_generation, page=page, per_page=per_page)

Query the steps of a run

list run steps

### Example

* Api Key Authentication (APIKeyAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "https://api.pollination.cloud",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization: JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.RunsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
run_id = 'run_id_example' # str | 
status = 'status_example' # str |  (optional)
step_id = ['step_id_example'] # list[str] |  (optional)
until_generation = 'until_generation_example' # str |  (optional)
since_generation = 'since_generation_example' # str |  (optional)
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # Query the steps of a run
        api_response = api_instance.get_run_steps(owner, name, run_id, status=status, step_id=step_id, until_generation=until_generation, since_generation=since_generation, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RunsApi->get_run_steps: %s\n" % e)
```

* Bearer Authentication (JWTAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "https://api.pollination.cloud",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization: JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.RunsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
run_id = 'run_id_example' # str | 
status = 'status_example' # str |  (optional)
step_id = ['step_id_example'] # list[str] |  (optional)
until_generation = 'until_generation_example' # str |  (optional)
since_generation = 'since_generation_example' # str |  (optional)
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # Query the steps of a run
        api_response = api_instance.get_run_steps(owner, name, run_id, status=status, step_id=step_id, until_generation=until_generation, since_generation=since_generation, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RunsApi->get_run_steps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **run_id** | **str**|  | 
 **status** | **str**|  | [optional] 
 **step_id** | [**list[str]**](str.md)|  | [optional] 
 **until_generation** | **str**|  | [optional] 
 **since_generation** | **str**|  | [optional] 
 **page** | **int**| Page number starting from 1 | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**StepList**](StepList.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth), [JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_run_artifacts**
> list[FileMeta] list_run_artifacts(owner, name, run_id, page=page, per_page=per_page, path=path)

List artifacts in a run folder

Retrieve a list of artifacts in a run folder

### Example

* Api Key Authentication (APIKeyAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "https://api.pollination.cloud",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization: JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.RunsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
run_id = 'run_id_example' # str | 
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)
path = ['path_example'] # list[str] | The path to an file within a project folder (optional)

    try:
        # List artifacts in a run folder
        api_response = api_instance.list_run_artifacts(owner, name, run_id, page=page, per_page=per_page, path=path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RunsApi->list_run_artifacts: %s\n" % e)
```

* Bearer Authentication (JWTAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "https://api.pollination.cloud",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization: JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.RunsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
run_id = 'run_id_example' # str | 
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)
path = ['path_example'] # list[str] | The path to an file within a project folder (optional)

    try:
        # List artifacts in a run folder
        api_response = api_instance.list_run_artifacts(owner, name, run_id, page=page, per_page=per_page, path=path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RunsApi->list_run_artifacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **run_id** | **str**|  | 
 **page** | **int**| Page number starting from 1 | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 25]
 **path** | [**list[str]**](str.md)| The path to an file within a project folder | [optional] 

### Return type

[**list[FileMeta]**](FileMeta.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth), [JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_runs**
> RunList list_runs(owner, name, ids=ids, status=status, page=page, per_page=per_page)

List runs

Retrieve a list of runs.

### Example

* Api Key Authentication (APIKeyAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "https://api.pollination.cloud",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization: JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.RunsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
ids = ['ids_example'] # list[str] |  (optional)
status = 'status_example' # str |  (optional)
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List runs
        api_response = api_instance.list_runs(owner, name, ids=ids, status=status, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RunsApi->list_runs: %s\n" % e)
```

* Bearer Authentication (JWTAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "https://api.pollination.cloud",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization: JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.RunsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
ids = ['ids_example'] # list[str] |  (optional)
status = 'status_example' # str |  (optional)
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List runs
        api_response = api_instance.list_runs(owner, name, ids=ids, status=status, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RunsApi->list_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **ids** | [**list[str]**](str.md)|  | [optional] 
 **status** | **str**|  | [optional] 
 **page** | **int**| Page number starting from 1 | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**RunList**](RunList.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth), [JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_run**
> Accepted resume_run(owner, name, run_id)

resume a run

resume a run

### Example

* Api Key Authentication (APIKeyAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "https://api.pollination.cloud",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization: JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.RunsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
run_id = 'run_id_example' # str | 

    try:
        # resume a run
        api_response = api_instance.resume_run(owner, name, run_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RunsApi->resume_run: %s\n" % e)
```

* Bearer Authentication (JWTAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "https://api.pollination.cloud",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization: JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.RunsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
run_id = 'run_id_example' # str | 

    try:
        # resume a run
        api_response = api_instance.resume_run(owner, name, run_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RunsApi->resume_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **run_id** | **str**|  | 

### Return type

[**Accepted**](Accepted.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth), [JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_run**
> Accepted stop_run(owner, name, run_id)

Stop a run

Stop a run.

### Example

* Api Key Authentication (APIKeyAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "https://api.pollination.cloud",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization: JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.RunsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
run_id = 'run_id_example' # str | 

    try:
        # Stop a run
        api_response = api_instance.stop_run(owner, name, run_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RunsApi->stop_run: %s\n" % e)
```

* Bearer Authentication (JWTAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "https://api.pollination.cloud",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization: JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.RunsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
run_id = 'run_id_example' # str | 

    try:
        # Stop a run
        api_response = api_instance.stop_run(owner, name, run_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RunsApi->stop_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **run_id** | **str**|  | 

### Return type

[**Accepted**](Accepted.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth), [JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_run**
> Accepted suspend_run(owner, name, run_id)

Suspend a run

Stop a run.

### Example

* Api Key Authentication (APIKeyAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "https://api.pollination.cloud",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization: JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.RunsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
run_id = 'run_id_example' # str | 

    try:
        # Suspend a run
        api_response = api_instance.suspend_run(owner, name, run_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RunsApi->suspend_run: %s\n" % e)
```

* Bearer Authentication (JWTAuth):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyAuth
configuration = pollination_sdk.Configuration(
    host = "https://api.pollination.cloud",
    api_key = {
        'APIKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyAuth'] = 'Bearer'

# Retrieve a temporary Acces Token (JWT) using your API token
API_TOKEN = 'some-token-string'

auth = pollination_sdk.UserApi()
api_token = pollination_sdk.LoginDto(
  api_token=API_TOKEN
)

auth_response = auth.login(api_token)

# Configure Bearer authorization: JWTAuth
configuration = pollination_sdk.Configuration(
    access_token=auth_response.access_token
)

# Enter a context with an instance of the API client
with pollination_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pollination_sdk.RunsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
run_id = 'run_id_example' # str | 

    try:
        # Suspend a run
        api_response = api_instance.suspend_run(owner, name, run_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RunsApi->suspend_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **run_id** | **str**|  | 

### Return type

[**Accepted**](Accepted.md)

### Authorization

[APIKeyAuth](../README.md#APIKeyAuth), [JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

