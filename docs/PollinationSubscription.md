# PollinationSubscription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The ID of the account this subscription applies to | 
**current_period_end** | **datetime** | The end of the current subscription period | 
**current_period_start** | **datetime** | The_start of the current subscription period | 
**external_id** | **str** | The ID of this subscription | [optional] 
**id** | **str** | The unique ID of this subscription | [optional] 
**quota_extensions** | [**list[QuotaExtension]**](QuotaExtension.md) | A list of quota extension plans for a given subscription | [optional] [default to []]
**subscription_plan** | [**SubscriptionPlan**](SubscriptionPlan.md) | A subscription plan | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


