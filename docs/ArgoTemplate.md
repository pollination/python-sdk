# ArgoTemplate

An argo workflow template object
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**template** | **str** |  | [optional] 
**arguments** | [**ArgoArguments**](ArgoArguments.md) |  | [optional] 
**template_ref** | [**ArgoTemplateRef**](ArgoTemplateRef.md) |  | [optional] 
**inputs** | [**ArgoArguments**](ArgoArguments.md) |  | [optional] 
**outputs** | [**ArgoOutputs**](ArgoOutputs.md) |  | [optional] 
**daemon** | **bool** |  | [optional] 
**steps** | **list[object]** |  | [optional] 
**container** | [**ArgoTaskContainer**](ArgoTaskContainer.md) |  | [optional] 
**dag** | [**ArgoDAG**](ArgoDAG.md) |  | [optional] 
**suspend** | [**ArgoSuspend**](ArgoSuspend.md) |  | [optional] 
**archive_location** | [**ArgoArchiveLocation**](ArgoArchiveLocation.md) |  | [optional] 
**active_deadline_seconds** | **int** |  | [optional] 
**retry_strategy** | [**ArgoRetryStrategy**](ArgoRetryStrategy.md) |  | [optional] 
**parallelism** | **int** |  | [optional] 
**service_account_name** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


