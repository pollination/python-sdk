# pollination_sdk.BillingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_billing_subscription**](BillingApi.md#cancel_billing_subscription) | **DELETE** /billing/subscriptions/{subscription_id} | Cancel a Paddle Billing subscription
[**create_billing_subscription_direct**](BillingApi.md#create_billing_subscription_direct) | **POST** /billing/subscriptions | Create a Paddle Billing subscription directly
[**create_billing_subscription_transaction**](BillingApi.md#create_billing_subscription_transaction) | **POST** /billing/transactions | Create a Paddle Billing subscription transaction
[**delete_subscription_payment_method**](BillingApi.md#delete_subscription_payment_method) | **DELETE** /billing/subscriptions/{subscription_id}/payment-methods/{payment_method_id} | Delete a payment method
[**get_billing_subscription**](BillingApi.md#get_billing_subscription) | **GET** /billing/subscriptions/{subscription_id} | Get a Paddle Billing subscription by ID
[**list_billing_products**](BillingApi.md#list_billing_products) | **GET** /billing/products | List available Paddle Billing products
[**list_billing_subscription_transactions**](BillingApi.md#list_billing_subscription_transactions) | **GET** /billing/subscriptions/{subscription_id}/transactions | List Paddle Billing transactions for a subscription
[**list_billing_subscriptions**](BillingApi.md#list_billing_subscriptions) | **GET** /billing/subscriptions | List all Paddle Billing subscriptions
[**list_subscription_payment_methods**](BillingApi.md#list_subscription_payment_methods) | **GET** /billing/subscriptions/{subscription_id}/payment-methods | List payment methods for a subscription
[**preview_billing_subscription**](BillingApi.md#preview_billing_subscription) | **POST** /billing/subscriptions/{subscription_id}/preview | Preview a Paddle Billing subscription transaction
[**update_billing_subscription**](BillingApi.md#update_billing_subscription) | **PUT** /billing/subscriptions/{subscription_id} | Update a Paddle Billing subscription
[**update_subscription_payment_method**](BillingApi.md#update_subscription_payment_method) | **PUT** /billing/subscriptions/{subscription_id}/payment-methods | Update a payment method for a subscription


# **cancel_billing_subscription**
> object cancel_billing_subscription(subscription_id)

Cancel a Paddle Billing subscription

Cancel a subscription directly via Paddle Billing API

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
    api_instance = pollination_sdk.BillingApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Cancel a Paddle Billing subscription
        api_response = api_instance.cancel_billing_subscription(subscription_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingApi->cancel_billing_subscription: %s\n" % e)
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
    api_instance = pollination_sdk.BillingApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Cancel a Paddle Billing subscription
        api_response = api_instance.cancel_billing_subscription(subscription_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingApi->cancel_billing_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

**object**

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

# **create_billing_subscription_direct**
> AppServerRestBillingDtoPayLink create_billing_subscription_direct(billing_subscription_create)

Create a Paddle Billing subscription directly

Create a subscription directly via Paddle Billing API

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
    api_instance = pollination_sdk.BillingApi(api_client)
    billing_subscription_create = pollination_sdk.BillingSubscriptionCreate() # BillingSubscriptionCreate | 

    try:
        # Create a Paddle Billing subscription directly
        api_response = api_instance.create_billing_subscription_direct(billing_subscription_create)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingApi->create_billing_subscription_direct: %s\n" % e)
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
    api_instance = pollination_sdk.BillingApi(api_client)
    billing_subscription_create = pollination_sdk.BillingSubscriptionCreate() # BillingSubscriptionCreate | 

    try:
        # Create a Paddle Billing subscription directly
        api_response = api_instance.create_billing_subscription_direct(billing_subscription_create)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingApi->create_billing_subscription_direct: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_subscription_create** | [**BillingSubscriptionCreate**](BillingSubscriptionCreate.md)|  | 

### Return type

[**AppServerRestBillingDtoPayLink**](AppServerRestBillingDtoPayLink.md)

### Authorization

[JWTAuth](../README.md#JWTAuth), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_billing_subscription_transaction**
> AppServerRestBillingDtoPayLink create_billing_subscription_transaction(billing_subscription_create)

Create a Paddle Billing subscription transaction

Create a Paddle Billing subscription transaction

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
    api_instance = pollination_sdk.BillingApi(api_client)
    billing_subscription_create = pollination_sdk.BillingSubscriptionCreate() # BillingSubscriptionCreate | 

    try:
        # Create a Paddle Billing subscription transaction
        api_response = api_instance.create_billing_subscription_transaction(billing_subscription_create)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingApi->create_billing_subscription_transaction: %s\n" % e)
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
    api_instance = pollination_sdk.BillingApi(api_client)
    billing_subscription_create = pollination_sdk.BillingSubscriptionCreate() # BillingSubscriptionCreate | 

    try:
        # Create a Paddle Billing subscription transaction
        api_response = api_instance.create_billing_subscription_transaction(billing_subscription_create)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingApi->create_billing_subscription_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_subscription_create** | [**BillingSubscriptionCreate**](BillingSubscriptionCreate.md)|  | 

### Return type

[**AppServerRestBillingDtoPayLink**](AppServerRestBillingDtoPayLink.md)

### Authorization

[JWTAuth](../README.md#JWTAuth), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscription_payment_method**
> delete_subscription_payment_method(subscription_idpayment_method_id)

Delete a payment method

Delete a payment method

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
    api_instance = pollination_sdk.BillingApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
payment_method_id = 'payment_method_id_example' # str | 

    try:
        # Delete a payment method
        api_instance.delete_subscription_payment_method(subscription_idpayment_method_id)
    except ApiException as e:
        print("Exception when calling BillingApi->delete_subscription_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **payment_method_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_subscription**
> BillingSubscription get_billing_subscription(subscription_id)

Get a Paddle Billing subscription by ID

Get a Paddle Billing subscription by its ID

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
    api_instance = pollination_sdk.BillingApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Get a Paddle Billing subscription by ID
        api_response = api_instance.get_billing_subscription(subscription_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingApi->get_billing_subscription: %s\n" % e)
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
    api_instance = pollination_sdk.BillingApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Get a Paddle Billing subscription by ID
        api_response = api_instance.get_billing_subscription(subscription_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingApi->get_billing_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**BillingSubscription**](BillingSubscription.md)

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

# **list_billing_products**
> List[BillingProduct] list_billing_products()

List available Paddle Billing products

List all available products from Paddle Billing API

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
    api_instance = pollination_sdk.BillingApi(api_client)
    
    try:
        # List available Paddle Billing products
        api_response = api_instance.list_billing_products()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingApi->list_billing_products: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[BillingProduct]**](BillingProduct.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_billing_subscription_transactions**
> List[BillingTransaction] list_billing_subscription_transactions(subscription_id)

List Paddle Billing transactions for a subscription

List all Billing API transactions for a subscription

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
    api_instance = pollination_sdk.BillingApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # List Paddle Billing transactions for a subscription
        api_response = api_instance.list_billing_subscription_transactions(subscription_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingApi->list_billing_subscription_transactions: %s\n" % e)
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
    api_instance = pollination_sdk.BillingApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # List Paddle Billing transactions for a subscription
        api_response = api_instance.list_billing_subscription_transactions(subscription_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingApi->list_billing_subscription_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**List[BillingTransaction]**](BillingTransaction.md)

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

# **list_billing_subscriptions**
> List[BillingSubscription] list_billing_subscriptions(account=account)

List all Paddle Billing subscriptions

List all Paddle Billing subscriptions

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
    api_instance = pollination_sdk.BillingApi(api_client)
    account = 'account_example' # str |  (optional)

    try:
        # List all Paddle Billing subscriptions
        api_response = api_instance.list_billing_subscriptions(account=account)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingApi->list_billing_subscriptions: %s\n" % e)
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
    api_instance = pollination_sdk.BillingApi(api_client)
    account = 'account_example' # str |  (optional)

    try:
        # List all Paddle Billing subscriptions
        api_response = api_instance.list_billing_subscriptions(account=account)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingApi->list_billing_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**|  | [optional] 

### Return type

[**List[BillingSubscription]**](BillingSubscription.md)

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

# **list_subscription_payment_methods**
> List[BillingPaymentMethod] list_subscription_payment_methods(subscription_id)

List payment methods for a subscription

List all payment methods for a subscription's customer

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
    api_instance = pollination_sdk.BillingApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # List payment methods for a subscription
        api_response = api_instance.list_subscription_payment_methods(subscription_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingApi->list_subscription_payment_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**List[BillingPaymentMethod]**](BillingPaymentMethod.md)

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

# **preview_billing_subscription**
> BillingTransactionPreview preview_billing_subscription(subscription_idbilling_subscription_update)

Preview a Paddle Billing subscription transaction

Preview the cost and details of a Billing subscription before creation

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
    api_instance = pollination_sdk.BillingApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
billing_subscription_update = pollination_sdk.BillingSubscriptionUpdate() # BillingSubscriptionUpdate | 

    try:
        # Preview a Paddle Billing subscription transaction
        api_response = api_instance.preview_billing_subscription(subscription_idbilling_subscription_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingApi->preview_billing_subscription: %s\n" % e)
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
    api_instance = pollination_sdk.BillingApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
billing_subscription_update = pollination_sdk.BillingSubscriptionUpdate() # BillingSubscriptionUpdate | 

    try:
        # Preview a Paddle Billing subscription transaction
        api_response = api_instance.preview_billing_subscription(subscription_idbilling_subscription_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingApi->preview_billing_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **billing_subscription_update** | [**BillingSubscriptionUpdate**](BillingSubscriptionUpdate.md)|  | 

### Return type

[**BillingTransactionPreview**](BillingTransactionPreview.md)

### Authorization

[JWTAuth](../README.md#JWTAuth), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_billing_subscription**
> BillingSubscription update_billing_subscription(subscription_idbilling_subscription_update)

Update a Paddle Billing subscription

Update a subscription directly via Paddle Billing API

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
    api_instance = pollination_sdk.BillingApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
billing_subscription_update = pollination_sdk.BillingSubscriptionUpdate() # BillingSubscriptionUpdate | 

    try:
        # Update a Paddle Billing subscription
        api_response = api_instance.update_billing_subscription(subscription_idbilling_subscription_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingApi->update_billing_subscription: %s\n" % e)
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
    api_instance = pollination_sdk.BillingApi(api_client)
    subscription_id = 'subscription_id_example' # str | 
billing_subscription_update = pollination_sdk.BillingSubscriptionUpdate() # BillingSubscriptionUpdate | 

    try:
        # Update a Paddle Billing subscription
        api_response = api_instance.update_billing_subscription(subscription_idbilling_subscription_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingApi->update_billing_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **billing_subscription_update** | [**BillingSubscriptionUpdate**](BillingSubscriptionUpdate.md)|  | 

### Return type

[**BillingSubscription**](BillingSubscription.md)

### Authorization

[JWTAuth](../README.md#JWTAuth), [APIKeyAuth](../README.md#APIKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subscription_payment_method**
> BillingTransaction update_subscription_payment_method(subscription_id)

Update a payment method for a subscription

Update a payment method for a subscription

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
    api_instance = pollination_sdk.BillingApi(api_client)
    subscription_id = 'subscription_id_example' # str | 

    try:
        # Update a payment method for a subscription
        api_response = api_instance.update_subscription_payment_method(subscription_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingApi->update_subscription_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**BillingTransaction**](BillingTransaction.md)

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

