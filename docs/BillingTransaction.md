# BillingTransaction

DTO for Paddle Billing Transaction
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_id** | **str** |  | [optional] 
**billed_at** | **datetime** |  | [optional] 
**billing_details** | [**BillingDetails**](BillingDetails.md) |  | [optional] 
**billing_period** | [**BillingPeriod**](BillingPeriod.md) |  | [optional] 
**business_id** | **str** |  | [optional] 
**checkout** | [**PaddleBillingCheckout**](PaddleBillingCheckout.md) |  | [optional] 
**collection_mode** | **str** |  | 
**created_at** | **datetime** |  | 
**currency_code** | **str** |  | 
**custom_data** | **object** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**details** | [**PaddleBillingTransactionDetails**](PaddleBillingTransactionDetails.md) |  | [optional] 
**discount_id** | **str** |  | [optional] 
**id** | **str** |  | 
**invoice_id** | **str** |  | [optional] 
**invoice_number** | **str** |  | [optional] 
**items** | [**List[PaddleBillingTransactionItem]**](PaddleBillingTransactionItem.md) |  | 
**origin** | **str** |  | 
**payments** | [**List[TransactionPayment]**](TransactionPayment.md) |  | [optional] [default to []]
**revised_at** | **datetime** |  | [optional] 
**status** | **str** |  | 
**subscription_id** | **str** |  | [optional] 
**updated_at** | **datetime** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


