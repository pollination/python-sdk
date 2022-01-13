# Quota

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description | [optional] 
**display_name** | **str** | The human-readable name | [optional] 
**enforced** | **bool** | Whether the limit triggers a blocking response from the server | [optional] [default to False]
**exceeded** | **bool** | Whether the resource usage is greater than or equal to the limit | [optional] [default to False]
**id** | **str** | The unique ID for this Quota | [optional] 
**limit** | **float** | The maximum amount of a resource the account can consume | [optional] 
**owner** | [**AccountPublic**](AccountPublic.md) | The quota owner | 
**period_start** | **datetime** | The start of the quota usage tracking period | [optional] 
**resets** | **bool** | Whether consumption is reset to 0 every billing period | [optional] [default to False]
**type** | [**QuotaType**](QuotaType.md) | The type of resource | [readonly] 
**unit** | **str** | The unit in which the usage and limit are measured | [optional] 
**usage** | **float** | The current amount of a resource allocated to the account linked to the subscription | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


