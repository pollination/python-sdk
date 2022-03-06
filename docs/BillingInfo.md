# BillingInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel_url** | **str** | The url to cancel the subscription | 
**last_payment** | [**SubscriptionPayment**](SubscriptionPayment.md) | The last payment made | 
**next_payment** | [**SubscriptionPayment**](SubscriptionPayment.md) | The last payment made | [optional] 
**paused_at** | **datetime** | The date the subscription was paused | [optional] 
**paused_from** | **datetime** | The date the subscription will be paused from | [optional] 
**paused_reason** | [**PausedReason**](PausedReason.md) | The reason the subscription was paused | [optional] 
**payment_information** | [**PaymentMethod**](PaymentMethod.md) | The payment method used | 
**signup_date** | **datetime** | The date the subscription was created | 
**update_url** | **str** | The url to update the billing info | 
**user_email** | **str** | The email used for billing on this subscription | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


