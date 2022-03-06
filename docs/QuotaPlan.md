# QuotaPlan

A quota plan
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enforced** | **bool** | Whether the limit is triggers a blocking response from the server | [optional] [default to False]
**limit** | **float** | The maximum amount of a resource that a subscription allows | [optional] 
**max_limit** | **float** | The maximum amount of a resource that a subscription allows | [optional] 
**resets** | **bool** | Whether consumption is reset to 0 every month | [optional] [default to False]
**type** | [**QuotaType**](QuotaType.md) | The name of the quota | [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


