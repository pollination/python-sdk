# pollination_sdk.JobsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_job**](JobsApi.md#create_job) | **POST** /projects/{owner}/{name}/jobs | Schedule a job
[**download_job_artifact**](JobsApi.md#download_job_artifact) | **GET** /projects/{owner}/{name}/jobs/{job_id}/artifacts/download | Download an artifact from the job folder
[**get_job**](JobsApi.md#get_job) | **GET** /projects/{owner}/{name}/jobs/{job_id} | Get a Job
[**list_jobs**](JobsApi.md#list_jobs) | **GET** /projects/{owner}/{name}/jobs | List Jobs
[**search_job_folder**](JobsApi.md#search_job_folder) | **GET** /projects/{owner}/{name}/jobs/{job_id}/artifacts | List files/folders in a job folder


# **create_job**
> CreatedContent create_job(owner, name, job, authorization=authorization, x_pollination_token=x_pollination_token)

Schedule a job

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
    host = "http://localhost",
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
    api_instance = pollination_sdk.JobsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
job = pollination_sdk.Job() # Job | 
authorization = 'authorization_example' # str |  (optional)
x_pollination_token = 'x_pollination_token_example' # str |  (optional)

    try:
        # Schedule a job
        api_response = api_instance.create_job(owner, name, job, authorization=authorization, x_pollination_token=x_pollination_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->create_job: %s\n" % e)
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
    host = "http://localhost",
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
    api_instance = pollination_sdk.JobsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
job = pollination_sdk.Job() # Job | 
authorization = 'authorization_example' # str |  (optional)
x_pollination_token = 'x_pollination_token_example' # str |  (optional)

    try:
        # Schedule a job
        api_response = api_instance.create_job(owner, name, job, authorization=authorization, x_pollination_token=x_pollination_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->create_job: %s\n" % e)
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

# **download_job_artifact**
> object download_job_artifact(owner, name, job_id, path=path)

Download an artifact from the job folder

Get a download link for an artifact in a job folder

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
    host = "http://localhost",
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
    api_instance = pollination_sdk.JobsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
job_id = 'job_id_example' # str | 
path = 'path_example' # str | The path to an file within a project folder (optional)

    try:
        # Download an artifact from the job folder
        api_response = api_instance.download_job_artifact(owner, name, job_id, path=path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->download_job_artifact: %s\n" % e)
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
    host = "http://localhost",
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
    api_instance = pollination_sdk.JobsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
job_id = 'job_id_example' # str | 
path = 'path_example' # str | The path to an file within a project folder (optional)

    try:
        # Download an artifact from the job folder
        api_response = api_instance.download_job_artifact(owner, name, job_id, path=path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->download_job_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **job_id** | **str**|  | 
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

# **get_job**
> CloudJob get_job(owner, name, job_id)

Get a Job

Retrieve a job.

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
    host = "http://localhost",
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
    api_instance = pollination_sdk.JobsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
job_id = 'job_id_example' # str | 

    try:
        # Get a Job
        api_response = api_instance.get_job(owner, name, job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->get_job: %s\n" % e)
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
    host = "http://localhost",
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
    api_instance = pollination_sdk.JobsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
job_id = 'job_id_example' # str | 

    try:
        # Get a Job
        api_response = api_instance.get_job(owner, name, job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->get_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **job_id** | **str**|  | 

### Return type

[**CloudJob**](CloudJob.md)

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

# **list_jobs**
> CloudJobList list_jobs(owner, name, ids=ids, status=status, page=page, per_page=per_page)

List Jobs

Retrieve a list of jobs.

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
    host = "http://localhost",
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
    api_instance = pollination_sdk.JobsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
ids = ['ids_example'] # list[str] |  (optional)
status = 'status_example' # str |  (optional)
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List Jobs
        api_response = api_instance.list_jobs(owner, name, ids=ids, status=status, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->list_jobs: %s\n" % e)
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
    host = "http://localhost",
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
    api_instance = pollination_sdk.JobsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
ids = ['ids_example'] # list[str] |  (optional)
status = 'status_example' # str |  (optional)
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)

    try:
        # List Jobs
        api_response = api_instance.list_jobs(owner, name, ids=ids, status=status, page=page, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->list_jobs: %s\n" % e)
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

[**CloudJobList**](CloudJobList.md)

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

# **search_job_folder**
> list[FileMeta] search_job_folder(owner, name, job_id, page=page, per_page=per_page, path=path)

List files/folders in a job folder

Retrieve a list of artifacts in a job folder

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
    host = "http://localhost",
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
    api_instance = pollination_sdk.JobsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
job_id = 'job_id_example' # str | 
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)
path = ['path_example'] # list[str] | The path to an file within a project folder (optional)

    try:
        # List files/folders in a job folder
        api_response = api_instance.search_job_folder(owner, name, job_id, page=page, per_page=per_page, path=path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->search_job_folder: %s\n" % e)
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
    host = "http://localhost",
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
    api_instance = pollination_sdk.JobsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
job_id = 'job_id_example' # str | 
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)
path = ['path_example'] # list[str] | The path to an file within a project folder (optional)

    try:
        # List files/folders in a job folder
        api_response = api_instance.search_job_folder(owner, name, job_id, page=page, per_page=per_page, path=path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->search_job_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **job_id** | **str**|  | 
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

