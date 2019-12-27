# pollination_sdk.SimulationsApi

All URIs are relative to *https://api.pollination.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](SimulationsApi.md#create) | **POST** /simulations | Schedule a simulation
[**get**](SimulationsApi.md#get) | **GET** /simulations/{id} | Get a Simulation
[**get_simulation_inputs**](SimulationsApi.md#get_simulation_inputs) | **GET** /simulations/{id}/inputs | Get simulation inputs
[**get_simulation_logs**](SimulationsApi.md#get_simulation_logs) | **GET** /simulations/{id}/logs | Get simulation logs
[**get_simulation_outputs**](SimulationsApi.md#get_simulation_outputs) | **GET** /simulations/{id}/outputs | Get simulation outputs
[**get_task_logs**](SimulationsApi.md#get_task_logs) | **GET** /simulations/{id}/task/{task_id}/logs | Get a simulation task&#39;s logs
[**list**](SimulationsApi.md#list) | **GET** /simulations | List simulations
[**resubmit**](SimulationsApi.md#resubmit) | **POST** /simulations/{id}/re-submit | re-submit a simulation
[**resume**](SimulationsApi.md#resume) | **PUT** /simulations/{id}/resume | resume a simulation
[**suspend**](SimulationsApi.md#suspend) | **PUT** /simulations/{id}/suspend | Suspend a simulation


# **create**
> CreatedContent create(submit_simulation)

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
API_KEY_ID = 'some-long-id'
API_KEY_SECRET = 'some-long-secret'

auth = pollination_sdk.AuthenticationApi()
api_token = pollination_sdk.Token(
  id=API_KEY_ID,
  secret=API_KEY_SECRET
)

auth_response = auth.login(token)

# Configure Bearer authorization: JWT
configuration.access_token = auth_response.access_token

# Defining host is optional and default to https://api.pollination.cloud
configuration.host = "https://api.pollination.cloud"
# Create an instance of the API class
api_instance = pollination_sdk.SimulationsApi(pollination_sdk.ApiClient(configuration))
submit_simulation = pollination_sdk.SubmitSimulation() # SubmitSimulation | 

try:
    # Schedule a simulation
    api_response = api_instance.create(submit_simulation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submit_simulation** | [**SubmitSimulation**](SubmitSimulation.md)|  | 

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

# **get**
> SimulationStatus get(id)

Get a Simulation

Retrieve a workflow.

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
API_KEY_ID = 'some-long-id'
API_KEY_SECRET = 'some-long-secret'

auth = pollination_sdk.AuthenticationApi()
api_token = pollination_sdk.Token(
  id=API_KEY_ID,
  secret=API_KEY_SECRET
)

auth_response = auth.login(token)

# Configure Bearer authorization: JWT
configuration.access_token = auth_response.access_token

# Defining host is optional and default to https://api.pollination.cloud
configuration.host = "https://api.pollination.cloud"
# Create an instance of the API class
api_instance = pollination_sdk.SimulationsApi(pollination_sdk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a Simulation
    api_response = api_instance.get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

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
**401** | Unauthorized |  -  |
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**404** | Not found |  -  |
**200** | Retrieved |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_simulation_inputs**
> get_simulation_inputs(id)

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
API_KEY_ID = 'some-long-id'
API_KEY_SECRET = 'some-long-secret'

auth = pollination_sdk.AuthenticationApi()
api_token = pollination_sdk.Token(
  id=API_KEY_ID,
  secret=API_KEY_SECRET
)

auth_response = auth.login(token)

# Configure Bearer authorization: JWT
configuration.access_token = auth_response.access_token

# Defining host is optional and default to https://api.pollination.cloud
configuration.host = "https://api.pollination.cloud"
# Create an instance of the API class
api_instance = pollination_sdk.SimulationsApi(pollination_sdk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get simulation inputs
    api_instance.get_simulation_inputs(id)
except ApiException as e:
    print("Exception when calling SimulationsApi->get_simulation_inputs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-gtar-compressed, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**404** | Not found |  -  |
**200** | Retrieved |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_simulation_logs**
> get_simulation_logs(id)

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
API_KEY_ID = 'some-long-id'
API_KEY_SECRET = 'some-long-secret'

auth = pollination_sdk.AuthenticationApi()
api_token = pollination_sdk.Token(
  id=API_KEY_ID,
  secret=API_KEY_SECRET
)

auth_response = auth.login(token)

# Configure Bearer authorization: JWT
configuration.access_token = auth_response.access_token

# Defining host is optional and default to https://api.pollination.cloud
configuration.host = "https://api.pollination.cloud"
# Create an instance of the API class
api_instance = pollination_sdk.SimulationsApi(pollination_sdk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get simulation logs
    api_instance.get_simulation_logs(id)
except ApiException as e:
    print("Exception when calling SimulationsApi->get_simulation_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-gtar-compressed, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**404** | Not found |  -  |
**200** | Retrieved |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_simulation_outputs**
> get_simulation_outputs(id)

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
API_KEY_ID = 'some-long-id'
API_KEY_SECRET = 'some-long-secret'

auth = pollination_sdk.AuthenticationApi()
api_token = pollination_sdk.Token(
  id=API_KEY_ID,
  secret=API_KEY_SECRET
)

auth_response = auth.login(token)

# Configure Bearer authorization: JWT
configuration.access_token = auth_response.access_token

# Defining host is optional and default to https://api.pollination.cloud
configuration.host = "https://api.pollination.cloud"
# Create an instance of the API class
api_instance = pollination_sdk.SimulationsApi(pollination_sdk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get simulation outputs
    api_instance.get_simulation_outputs(id)
except ApiException as e:
    print("Exception when calling SimulationsApi->get_simulation_outputs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-gtar-compressed, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**404** | Not found |  -  |
**200** | Retrieved |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_logs**
> str get_task_logs(id, task_id)

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
API_KEY_ID = 'some-long-id'
API_KEY_SECRET = 'some-long-secret'

auth = pollination_sdk.AuthenticationApi()
api_token = pollination_sdk.Token(
  id=API_KEY_ID,
  secret=API_KEY_SECRET
)

auth_response = auth.login(token)

# Configure Bearer authorization: JWT
configuration.access_token = auth_response.access_token

# Defining host is optional and default to https://api.pollination.cloud
configuration.host = "https://api.pollination.cloud"
# Create an instance of the API class
api_instance = pollination_sdk.SimulationsApi(pollination_sdk.ApiClient(configuration))
id = 'id_example' # str | 
task_id = 'task_id_example' # str | 

try:
    # Get a simulation task's logs
    api_response = api_instance.get_task_logs(id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->get_task_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
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
**401** | Unauthorized |  -  |
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**404** | Not found |  -  |
**200** | Retrieved |  * Link - The Link header with pagination information. For details see [link header](https://pollination.cloud/api/#section/Pagination/Link-header). <br>  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> list[SimulationStatus] list(page=page, per_page=per_page)

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
API_KEY_ID = 'some-long-id'
API_KEY_SECRET = 'some-long-secret'

auth = pollination_sdk.AuthenticationApi()
api_token = pollination_sdk.Token(
  id=API_KEY_ID,
  secret=API_KEY_SECRET
)

auth_response = auth.login(token)

# Configure Bearer authorization: JWT
configuration.access_token = auth_response.access_token

# Defining host is optional and default to https://api.pollination.cloud
configuration.host = "https://api.pollination.cloud"
# Create an instance of the API class
api_instance = pollination_sdk.SimulationsApi(pollination_sdk.ApiClient(configuration))
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)

try:
    # List simulations
    api_response = api_instance.list(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number starting from 1 | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

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
**401** | Unauthorized |  -  |
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**404** | Not found |  -  |
**200** | Retrieved |  * Link - The Link header with pagination information. For details see [link header](https://pollination.cloud/api/#section/Pagination/Link-header). <br>  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resubmit**
> CreatedContent resubmit(id)

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
API_KEY_ID = 'some-long-id'
API_KEY_SECRET = 'some-long-secret'

auth = pollination_sdk.AuthenticationApi()
api_token = pollination_sdk.Token(
  id=API_KEY_ID,
  secret=API_KEY_SECRET
)

auth_response = auth.login(token)

# Configure Bearer authorization: JWT
configuration.access_token = auth_response.access_token

# Defining host is optional and default to https://api.pollination.cloud
configuration.host = "https://api.pollination.cloud"
# Create an instance of the API class
api_instance = pollination_sdk.SimulationsApi(pollination_sdk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # re-submit a simulation
    api_response = api_instance.resubmit(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->resubmit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

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
**401** | Unauthorized |  -  |
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**404** | Not found |  -  |
**200** | Accepted |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume**
> Accepted resume(id)

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
API_KEY_ID = 'some-long-id'
API_KEY_SECRET = 'some-long-secret'

auth = pollination_sdk.AuthenticationApi()
api_token = pollination_sdk.Token(
  id=API_KEY_ID,
  secret=API_KEY_SECRET
)

auth_response = auth.login(token)

# Configure Bearer authorization: JWT
configuration.access_token = auth_response.access_token

# Defining host is optional and default to https://api.pollination.cloud
configuration.host = "https://api.pollination.cloud"
# Create an instance of the API class
api_instance = pollination_sdk.SimulationsApi(pollination_sdk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # resume a simulation
    api_response = api_instance.resume(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->resume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

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
**401** | Unauthorized |  -  |
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**404** | Not found |  -  |
**200** | Accepted |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend**
> Accepted suspend(id)

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
API_KEY_ID = 'some-long-id'
API_KEY_SECRET = 'some-long-secret'

auth = pollination_sdk.AuthenticationApi()
api_token = pollination_sdk.Token(
  id=API_KEY_ID,
  secret=API_KEY_SECRET
)

auth_response = auth.login(token)

# Configure Bearer authorization: JWT
configuration.access_token = auth_response.access_token

# Defining host is optional and default to https://api.pollination.cloud
configuration.host = "https://api.pollination.cloud"
# Create an instance of the API class
api_instance = pollination_sdk.SimulationsApi(pollination_sdk.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Suspend a simulation
    api_response = api_instance.suspend(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->suspend: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

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
**401** | Unauthorized |  -  |
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**404** | Not found |  -  |
**200** | Accepted |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

