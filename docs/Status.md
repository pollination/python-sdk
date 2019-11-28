# Status

An argo workflow status object
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stored_templates** | [**dict(str, Template)**](Template.md) |  | 
**phase** | **str** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**finished_at** | **datetime** |  | [optional] 
**message** | **str** |  | [optional] 
**compressed_nodes** | **str** |  | [optional] 
**nodes** | [**dict(str, NodeStatus)**](NodeStatus.md) |  | [optional] 
**persistent_volume_claims** | **list[object]** |  | [optional] [default to []]
**outputs** | [**Outputs**](Outputs.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


