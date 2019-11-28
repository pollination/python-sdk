# NodeStatus

An argo task node status object
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**template_name** | **str** |  | [optional] 
**template_ref** | [**TemplateRef**](TemplateRef.md) |  | [optional] 
**stored_template_id** | **str** |  | [optional] 
**workflow_template_name** | **str** |  | [optional] 
**phase** | **str** |  | [optional] 
**boundary_id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**finished_at** | **datetime** |  | [optional] 
**pod_ip** | **str** |  | [optional] 
**daemoned** | **str** |  | [optional] 
**inputs** | [**QueenbeeArgoSchemaArgumentsArguments**](QueenbeeArgoSchemaArgumentsArguments.md) |  | [optional] 
**outputs** | [**Outputs**](Outputs.md) |  | [optional] 
**children** | **list[str]** |  | [optional] [default to []]
**outbound_nodes** | **list[str]** |  | [optional] [default to []]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


