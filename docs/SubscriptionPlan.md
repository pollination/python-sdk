# SubscriptionPlan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_types** | [**list[AccountType]**](AccountType.md) | The types of account to which the plan can be applied | 
**billing_options** | [**list[BillingOption]**](BillingOption.md) | The billing options for this plan | [optional] [default to []]
**name** | **str** | A name of the config plan used to create this subscription | 
**quotas** | [**list[QuotaPlan]**](QuotaPlan.md) | A list of quota plans for a given subscription | [optional] [default to []]
**slug** | **str** | A slug of the config plan used to create this subscription | 
**type** | [**PlanType**](PlanType.md) | The type of plan | [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


