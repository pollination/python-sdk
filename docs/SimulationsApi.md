# pollination_sdk.SimulationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_simulation**](SimulationsApi.md#create_simulation) | **POST** /projects/{owner}/{name}/simulations | Schedule a simulation
[**get_simulation**](SimulationsApi.md#get_simulation) | **GET** /projects/{owner}/{name}/simulations/{simulation_id} | Get a Simulation
[**get_simulation_inputs**](SimulationsApi.md#get_simulation_inputs) | **GET** /projects/{owner}/{name}/simulations/{simulation_id}/inputs | Get simulation inputs
[**get_simulation_logs**](SimulationsApi.md#get_simulation_logs) | **GET** /projects/{owner}/{name}/simulations/{simulation_id}/logs | Get simulation logs
[**get_simulation_outputs**](SimulationsApi.md#get_simulation_outputs) | **GET** /projects/{owner}/{name}/simulations/{simulation_id}/outputs | Get simulation outputs
[**get_simulation_task_logs**](SimulationsApi.md#get_simulation_task_logs) | **GET** /projects/{owner}/{name}/simulations/{simulation_id}/task/{task_id}/logs | Get a simulation task&#39;s logs
[**list_simulations**](SimulationsApi.md#list_simulations) | **GET** /projects/{owner}/{name}/simulations | List simulations
[**resubmit_simulation**](SimulationsApi.md#resubmit_simulation) | **POST** /projects/{owner}/{name}/simulations/{simulation_id}/re-submit | re-submit a simulation
[**resume_simulation**](SimulationsApi.md#resume_simulation) | **PUT** /projects/{owner}/{name}/simulations/{simulation_id}/resume | resume a simulation
[**suspend_simulation**](SimulationsApi.md#suspend_simulation) | **PUT** /projects/{owner}/{name}/simulations/{simulation_id}/suspend | Suspend a simulation


# **create_simulation**
> CreatedContent create_simulation(owner, name, unknown_base_type)

Schedule a simulation

Create a new simulation.

### Example

* Bearer Authentication (JWT):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint
configuration = pollination_sdk.Configuration()

# Retrieve a temporary Acces Token (JWT) using your API key id and secret
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
api_instance = pollination_sdk.SimulationsApi(pollination_sdk.ApiClient(configuration))
owner = 'owner_example' # str | 
name = 'name_example' # str | 
unknown_base_type = pollination_sdk.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | 

try:
    # Schedule a simulation
    api_response = api_instance.create_simulation(owner, name, unknown_base_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->create_simulation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | 

### Return type

[**CreatedContent**](CreatedContent.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_simulation**
> SimulationStatus get_simulation(owner, name, simulation_id)

Get a Simulation

Retrieve a simulation.

### Example

* Bearer Authentication (JWT):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint
configuration = pollination_sdk.Configuration()

# Retrieve a temporary Acces Token (JWT) using your API key id and secret
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
api_instance = pollination_sdk.SimulationsApi(pollination_sdk.ApiClient(configuration))
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

[JWT](../README.md#JWT)

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

* Bearer Authentication (JWT):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint
configuration = pollination_sdk.Configuration()

# Retrieve a temporary Acces Token (JWT) using your API key id and secret
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
api_instance = pollination_sdk.SimulationsApi(pollination_sdk.ApiClient(configuration))
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

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**400** | Invalid request |  -  |
**200** | Retrieved |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_simulation_logs**
> object get_simulation_logs(owner, name, simulation_id)

Get simulation logs

get simulation logs

### Example

* Bearer Authentication (JWT):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint
configuration = pollination_sdk.Configuration()

# Retrieve a temporary Acces Token (JWT) using your API key id and secret
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
api_instance = pollination_sdk.SimulationsApi(pollination_sdk.ApiClient(configuration))
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

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**400** | Invalid request |  -  |
**200** | Retrieved |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_simulation_outputs**
> object get_simulation_outputs(owner, name, simulation_id)

Get simulation outputs

get simulation outputs

### Example

* Bearer Authentication (JWT):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint
configuration = pollination_sdk.Configuration()

# Retrieve a temporary Acces Token (JWT) using your API key id and secret
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
api_instance = pollination_sdk.SimulationsApi(pollination_sdk.ApiClient(configuration))
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

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**400** | Invalid request |  -  |
**200** | Retrieved |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_simulation_task_logs**
> str get_simulation_task_logs(owner, name, simulation_id, task_id)

Get a simulation task's logs

get simulation task logs

### Example

* Bearer Authentication (JWT):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint
configuration = pollination_sdk.Configuration()

# Retrieve a temporary Acces Token (JWT) using your API key id and secret
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
api_instance = pollination_sdk.SimulationsApi(pollination_sdk.ApiClient(configuration))
owner = 'owner_example' # str | 
name = 'name_example' # str | 
simulation_id = 'simulation_id_example' # str | 
task_id = 'task_id_example' # str | 

try:
    # Get a simulation task's logs
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

[JWT](../README.md#JWT)

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
> list[SimulationStatus] list_simulations(owner, name, page=page, per_page=per_page, id=id, workflow=workflow, status=status)

List simulations

Retrieve a list of simulations.

### Example

* Bearer Authentication (JWT):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint
configuration = pollination_sdk.Configuration()

# Retrieve a temporary Acces Token (JWT) using your API key id and secret
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
api_instance = pollination_sdk.SimulationsApi(pollination_sdk.ApiClient(configuration))
owner = 'owner_example' # str | 
name = 'name_example' # str | 
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)
id = ['id_example'] # list[str] | The ID of a simulation to search for (optional)
workflow = ['workflow_example'] # list[str] | The ID of the workflow used for this simulation (optional)
status = ['status_example'] # list[str] | The status of the simulation to filter by (optional)

try:
    # List simulations
    api_response = api_instance.list_simulations(owner, name, page=page, per_page=per_page, id=id, workflow=workflow, status=status)
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
 **workflow** | [**list[str]**](str.md)| The ID of the workflow used for this simulation | [optional] 
 **status** | [**list[str]**](str.md)| The status of the simulation to filter by | [optional] 

### Return type

[**list[SimulationStatus]**](SimulationStatus.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resubmit_simulation**
> CreatedContent resubmit_simulation(owner, name, simulation_id)

re-submit a simulation

re-submit a simulation

### Example

* Bearer Authentication (JWT):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint
configuration = pollination_sdk.Configuration()

# Retrieve a temporary Acces Token (JWT) using your API key id and secret
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
api_instance = pollination_sdk.SimulationsApi(pollination_sdk.ApiClient(configuration))
owner = 'owner_example' # str | 
name = 'name_example' # str | 
simulation_id = 'simulation_id_example' # str | 

try:
    # re-submit a simulation
    api_response = api_instance.resubmit_simulation(owner, name, simulation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->resubmit_simulation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **name** | **str**|  | 
 **simulation_id** | **str**|  | 

### Return type

[**CreatedContent**](CreatedContent.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Accepted |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_simulation**
> Accepted resume_simulation(owner, name, simulation_id)

resume a simulation

resume a simulation

### Example

* Bearer Authentication (JWT):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint
configuration = pollination_sdk.Configuration()

# Retrieve a temporary Acces Token (JWT) using your API key id and secret
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
api_instance = pollination_sdk.SimulationsApi(pollination_sdk.ApiClient(configuration))
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

[JWT](../README.md#JWT)

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

* Bearer Authentication (JWT):
```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint
configuration = pollination_sdk.Configuration()

# Retrieve a temporary Acces Token (JWT) using your API key id and secret
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
api_instance = pollination_sdk.SimulationsApi(pollination_sdk.ApiClient(configuration))
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

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

