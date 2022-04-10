# pollination_sdk.SubscriptionPlansApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_subscription_plans**](SubscriptionPlansApi.md#list_subscription_plans) | **GET** /subscription-plans/ | Cython Function Or Method


# **list_subscription_plans**
> list[SubscriptionPlan] list_subscription_plans(plan_type=plan_type)

Cython Function Or Method

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
    api_instance = pollination_sdk.SubscriptionPlansApi(api_client)
    plan_type = pollination_sdk.PlanType() # PlanType | Plan Type (optional)

    try:
        # Cython Function Or Method
        api_response = api_instance.list_subscription_plans(plan_type=plan_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubscriptionPlansApi->list_subscription_plans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_type** | [**PlanType**](.md)| Plan Type | [optional] 

### Return type

[**list[SubscriptionPlan]**](SubscriptionPlan.md)

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

