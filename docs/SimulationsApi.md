# pollination_sdk.SimulationsApi

All URIs are relative to *https://api.pollination.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_simulation**](SimulationsApi.md#create_simulation) | **POST** /projects/{owner}/{name}/simulations | Schedule a simulation
[**download_simulation_artifact**](SimulationsApi.md#download_simulation_artifact) | **GET** /projects/{owner}/{name}/simulations/{simulation_id}/artifacts/download | Download an artifact from the simulation folder
[**get_simulation**](SimulationsApi.md#get_simulation) | **GET** /projects/{owner}/{name}/simulations/{simulation_id} | Get a Simulation
[**get_simulation_inputs**](SimulationsApi.md#get_simulation_inputs) | **GET** /projects/{owner}/{name}/simulations/{simulation_id}/inputs | Get simulation inputs
[**get_simulation_logs**](SimulationsApi.md#get_simulation_logs) | **GET** /projects/{owner}/{name}/simulations/{simulation_id}/logs | Get simulation logs
[**get_simulation_output_artifact**](SimulationsApi.md#get_simulation_output_artifact) | **GET** /projects/{owner}/{name}/simulations/{simulation_id}/outputs/artifacts/{artifact_name} | Get simulation output artifact by name
[**get_simulation_outputs**](SimulationsApi.md#get_simulation_outputs) | **GET** /projects/{owner}/{name}/simulations/{simulation_id}/outputs | Get simulation outputs
[**get_simulation_task_logs**](SimulationsApi.md#get_simulation_task_logs) | **GET** /projects/{owner}/{name}/simulations/{simulation_id}/task/{task_id}/logs | Get simulation logs
[**list_simulation_artifacts**](SimulationsApi.md#list_simulation_artifacts) | **GET** /projects/{owner}/{name}/simulations/{simulation_id}/artifacts | List artifacts in a simulation folder
[**list_simulations**](SimulationsApi.md#list_simulations) | **GET** /projects/{owner}/{name}/simulations | List simulations
[**resume_simulation**](SimulationsApi.md#resume_simulation) | **PUT** /projects/{owner}/{name}/simulations/{simulation_id}/resume | resume a simulation
[**stop_simulation**](SimulationsApi.md#stop_simulation) | **PUT** /projects/{owner}/{name}/simulations/{simulation_id}/stop | Stop a simulation
[**suspend_simulation**](SimulationsApi.md#suspend_simulation) | **PUT** /projects/{owner}/{name}/simulations/{simulation_id}/suspend | Suspend a simulation


# **create_simulation**
> CreatedContent create_simulation(owner, name, submit_simulation, authorization=authorization)

Schedule a simulation

Create a new simulation.

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
    api_instance = pollination_sdk.SimulationsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
submit_simulation = pollination_sdk.SubmitSimulation() # SubmitSimulation | 
authorization = 'authorization_example' # str |  (optional)

    try:
        # Schedule a simulation
        api_response = api_instance.create_simulation(owner, name, submit_simulation, authorization=authorization)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SimulationsApi->create_simulation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **submit_simulation** | [**SubmitSimulation**](SubmitSimulation.md)|  | 
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
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_simulation_artifact**
> object download_simulation_artifact(owner, name, simulation_id, path=path)

Download an artifact from the simulation folder

Get a download link for an artifact in a simulation folder

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
    api_instance = pollination_sdk.SimulationsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
simulation_id = 'simulation_id_example' # str | 
path = 'path_example' # str | The path to an file within a project folder (optional)

    try:
        # Download an artifact from the simulation folder
        api_response = api_instance.download_simulation_artifact(owner, name, simulation_id, path=path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SimulationsApi->download_simulation_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **simulation_id** | **str**|  | 
 **path** | **str**| The path to an file within a project folder | [optional] 

### Return type

**object**

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

# **get_simulation**
> SimulationStatus get_simulation(owner, name, simulation_id)

Get a Simulation

Retrieve a simulation.

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
    api_instance = pollination_sdk.SimulationsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
simulation_id = 'simulation_id_example' # str | 

    try:
        # Get a Simulation
        api_response = api_instance.get_simulation(owner, name, simulation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SimulationsApi->get_simulation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **simulation_id** | **str**|  | 

### Return type

[**SimulationStatus**](SimulationStatus.md)

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

# **get_simulation_inputs**
> object get_simulation_inputs(owner, name, simulation_id)

Get simulation inputs

get simulation inputs

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
    api_instance = pollination_sdk.SimulationsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
simulation_id = 'simulation_id_example' # str | 

    try:
        # Get simulation inputs
        api_response = api_instance.get_simulation_inputs(owner, name, simulation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SimulationsApi->get_simulation_inputs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **simulation_id** | **str**|  | 

### Return type

**object**

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

# **get_simulation_logs**
> object get_simulation_logs(owner, name, simulation_id)

Get simulation logs

get simulation logs

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
    api_instance = pollination_sdk.SimulationsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
simulation_id = 'simulation_id_example' # str | 

    try:
        # Get simulation logs
        api_response = api_instance.get_simulation_logs(owner, name, simulation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SimulationsApi->get_simulation_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **simulation_id** | **str**|  | 

### Return type

**object**

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

# **get_simulation_output_artifact**
> object get_simulation_output_artifact(owner, name, simulation_id, artifact_name)

Get simulation output artifact by name

get simulation output artifact

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
    api_instance = pollination_sdk.SimulationsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
simulation_id = 'simulation_id_example' # str | 
artifact_name = 'artifact_name_example' # str | 

    try:
        # Get simulation output artifact by name
        api_response = api_instance.get_simulation_output_artifact(owner, name, simulation_id, artifact_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SimulationsApi->get_simulation_output_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **simulation_id** | **str**|  | 
 **artifact_name** | **str**|  | 

### Return type

**object**

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

# **get_simulation_outputs**
> object get_simulation_outputs(owner, name, simulation_id)

Get simulation outputs

get simulation outputs

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
    api_instance = pollination_sdk.SimulationsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
simulation_id = 'simulation_id_example' # str | 

    try:
        # Get simulation outputs
        api_response = api_instance.get_simulation_outputs(owner, name, simulation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SimulationsApi->get_simulation_outputs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **simulation_id** | **str**|  | 

### Return type

**object**

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

# **get_simulation_task_logs**
> str get_simulation_task_logs(owner, name, simulation_id, task_id)

Get simulation logs

get simulation task logs

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
    api_instance = pollination_sdk.SimulationsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
simulation_id = 'simulation_id_example' # str | 
task_id = 'task_id_example' # str | 

    try:
        # Get simulation logs
        api_response = api_instance.get_simulation_task_logs(owner, name, simulation_id, task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SimulationsApi->get_simulation_task_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **simulation_id** | **str**|  | 
 **task_id** | **str**|  | 

### Return type

**str**

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

# **list_simulation_artifacts**
> list[FileMeta] list_simulation_artifacts(owner, name, simulation_id, page=page, per_page=per_page, path=path)

List artifacts in a simulation folder

Retrieve a list of artifacts in a simulation folder

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
    api_instance = pollination_sdk.SimulationsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
simulation_id = 'simulation_id_example' # str | 
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)
path = ['path_example'] # list[str] | The path to an file within a project folder (optional)

    try:
        # List artifacts in a simulation folder
        api_response = api_instance.list_simulation_artifacts(owner, name, simulation_id, page=page, per_page=per_page, path=path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SimulationsApi->list_simulation_artifacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **simulation_id** | **str**|  | 
 **page** | **int**| Page number starting from 1 | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 25]
 **path** | [**list[str]**](str.md)| The path to an file within a project folder | [optional] 

### Return type

[**list[FileMeta]**](FileMeta.md)

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

# **list_simulations**
> SimulationList list_simulations(owner, name, page=page, per_page=per_page, id=id, status=status)

List simulations

Retrieve a list of simulations.

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
    api_instance = pollination_sdk.SimulationsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)
id = ['id_example'] # list[str] | The ID of a simulation to search for (optional)
status = ['status_example'] # list[str] | The status of the simulation to filter by (optional)

    try:
        # List simulations
        api_response = api_instance.list_simulations(owner, name, page=page, per_page=per_page, id=id, status=status)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SimulationsApi->list_simulations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **page** | **int**| Page number starting from 1 | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 25]
 **id** | [**list[str]**](str.md)| The ID of a simulation to search for | [optional] 
 **status** | [**list[str]**](str.md)| The status of the simulation to filter by | [optional] 

### Return type

[**SimulationList**](SimulationList.md)

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

# **resume_simulation**
> Accepted resume_simulation(owner, name, simulation_id)

resume a simulation

resume a simulation

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
    api_instance = pollination_sdk.SimulationsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
simulation_id = 'simulation_id_example' # str | 

    try:
        # resume a simulation
        api_response = api_instance.resume_simulation(owner, name, simulation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SimulationsApi->resume_simulation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **simulation_id** | **str**|  | 

### Return type

[**Accepted**](Accepted.md)

### Authorization

[CompulsoryAuth](../README.md#CompulsoryAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_simulation**
> Accepted stop_simulation(owner, name, simulation_id)

Stop a simulation

Stop a simulation.

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
    api_instance = pollination_sdk.SimulationsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
simulation_id = 'simulation_id_example' # str | 

    try:
        # Stop a simulation
        api_response = api_instance.stop_simulation(owner, name, simulation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SimulationsApi->stop_simulation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **simulation_id** | **str**|  | 

### Return type

[**Accepted**](Accepted.md)

### Authorization

[CompulsoryAuth](../README.md#CompulsoryAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_simulation**
> Accepted suspend_simulation(owner, name, simulation_id)

Suspend a simulation

Suspend a simulation.

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
    api_instance = pollination_sdk.SimulationsApi(api_client)
    owner = 'owner_example' # str | 
name = 'name_example' # str | 
simulation_id = 'simulation_id_example' # str | 

    try:
        # Suspend a simulation
        api_response = api_instance.suspend_simulation(owner, name, simulation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SimulationsApi->suspend_simulation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **simulation_id** | **str**|  | 

### Return type

[**Accepted**](Accepted.md)

### Authorization

[CompulsoryAuth](../README.md#CompulsoryAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

