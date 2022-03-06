# Subscription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_info** | [**BillingInfo**](BillingInfo.md) | The billing info for the subscription | [optional] 
**external_id** | **str** | The ID of this subscription | [optional] 
**id** | **str** | The unique ID of this subscription | 
**owner** | [**AccountPublic**](AccountPublic.md) | The owner of the repository | 
**period_end** | **datetime** | The end of the current subscription period | 
**period_start** | **datetime** | The start of the current subscription period | 
**plan_multiplier** | **int** | The number of times to multiply the plan limit by | [optional] [default to 1]
**plan_slug** | **str** | The slug of the plan used to create this subscription | 
**type** | [**PlanType**](PlanType.md) | The type of subscription | [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


