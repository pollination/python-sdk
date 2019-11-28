# pollination_sdk.SensorGridApi

All URIs are relative to *https://api.pollination.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](SensorGridApi.md#create) | **POST** /sensor-grids | Create a Sensor Grid
[**delete**](SensorGridApi.md#delete) | **DELETE** /sensor-grids/{gid} | Delete a Sensor Grid
[**get**](SensorGridApi.md#get) | **GET** /sensor-grids/{gid} | Get a Sensor Grid
[**get_sensors**](SensorGridApi.md#get_sensors) | **GET** /sensor-grids/{gid}/sensors | Get Sensors
[**list**](SensorGridApi.md#list) | **GET** /sensor-grids | Get Sensor Grids


# **create**
> CreatedContent create(sensor_grid_in1)

Create a Sensor Grid

Create a new grid of sensors.

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
api_instance = pollination_sdk.SensorGridApi(pollination_sdk.ApiClient(configuration))
sensor_grid_in1 = pollination_sdk.SensorGridIn1() # SensorGridIn1 | 

try:
    # Create a Sensor Grid
    api_response = api_instance.create(sensor_grid_in1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorGridApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_grid_in1** | [**SensorGridIn1**](SensorGridIn1.md)|  | 

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
**401** | Unauthorized |  -  |
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**201** | Created successfully |  * Location - Location of the newly created resource. <br>  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> object delete(gid)

Delete a Sensor Grid

Delete a sensor grid.

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
api_instance = pollination_sdk.SensorGridApi(pollination_sdk.ApiClient(configuration))
gid = 'gid_example' # str | Grid id.

try:
    # Delete a Sensor Grid
    api_response = api_instance.delete(gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorGridApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gid** | [**str**](.md)| Grid id. | 

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
**401** | Unauthorized |  -  |
**403** | Access forbidden |  -  |
**500** | Server error |  -  |
**404** | Not found |  -  |
**204** | Success |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> SensorGridOut get(gid)

Get a Sensor Grid

Retrieve a sensor grid.

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
api_instance = pollination_sdk.SensorGridApi(pollination_sdk.ApiClient(configuration))
gid = 'gid_example' # str | 

try:
    # Get a Sensor Grid
    api_response = api_instance.get(gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorGridApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gid** | [**str**](.md)|  | 

### Return type

[**SensorGridOut**](SensorGridOut.md)

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

# **get_sensors**
> list[Sensor] get_sensors(gid, page=page, per_page=per_page)

Get Sensors

Retrieve list of sensors for a sensor grid.     See Location in response headers for paging links.     

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
api_instance = pollination_sdk.SensorGridApi(pollination_sdk.ApiClient(configuration))
gid = 'gid_example' # str | 
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)

try:
    # Get Sensors
    api_response = api_instance.get_sensors(gid, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorGridApi->get_sensors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gid** | [**str**](.md)|  | 
 **page** | **int**| Page number starting from 1 | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**list[Sensor]**](Sensor.md)

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
> list[SensorGridOut] list(page=page, per_page=per_page)

Get Sensor Grids

Retrieve a list of sensor grids.

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
api_instance = pollination_sdk.SensorGridApi(pollination_sdk.ApiClient(configuration))
page = 1 # int | Page number starting from 1 (optional) (default to 1)
per_page = 25 # int | Number of items per page (optional) (default to 25)

try:
    # Get Sensor Grids
    api_response = api_instance.list(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorGridApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number starting from 1 | [optional] [default to 1]
 **per_page** | **int**| Number of items per page | [optional] [default to 25]

### Return type

[**list[SensorGridOut]**](SensorGridOut.md)

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

