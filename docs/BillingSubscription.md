# BillingSubscription

DTO for Paddle Billing Subscription
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_cycle** | [**Duration**](Duration.md) |  | [optional] 
**billing_details** | **object** |  | [optional] 
**canceled_at** | **datetime** |  | [optional] 
**collection_mode** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**currency_code** | **str** |  | 
**current_billing_period** | [**BillingPeriod**](BillingPeriod.md) |  | [optional] 
**custom_data** | **object** |  | [optional] 
**customer_id** | **str** |  | 
**discount** | **object** |  | [optional] 
**first_billed_at** | **datetime** |  | [optional] 
**id** | **str** |  | 
**items** | [**List[PaddleBillingSubscriptionItem]**](PaddleBillingSubscriptionItem.md) |  | 
**next_billed_at** | **datetime** |  | [optional] 
**paused_at** | **datetime** |  | [optional] 
**scheduled_change** | **object** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**status** | [**PaddleBillingSubscriptionStatus**](PaddleBillingSubscriptionStatus.md) |  | 
**updated_at** | **datetime** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


