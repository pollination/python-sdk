# ArgoStatus

An argo workflow status object
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stored_templates** | [**dict(str, ArgoTemplate)**](ArgoTemplate.md) |  | 
**phase** | **str** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**finished_at** | **datetime** |  | [optional] 
**message** | **str** |  | [optional] 
**compressed_nodes** | **str** |  | [optional] 
**nodes** | [**dict(str, ArgoNodeStatus)**](ArgoNodeStatus.md) |  | [optional] 
**persistent_volume_claims** | **list[object]** |  | [optional] [default to []]
**outputs** | [**ArgoOutputs**](ArgoOutputs.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


