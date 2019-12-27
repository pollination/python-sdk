# SimulationStatus

Workflow Status
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of this task. Can be \&quot;Running\&quot;, \&quot;Succeeded\&quot;, \&quot;Failed\&quot; or \&quot;Error\&quot; | 
**message** | **str** | Any message produced by the task. Usually error/debugging hints. | [optional] 
**started_at** | **datetime** | The time at which the task was started | 
**finished_at** | **datetime** | The time at which the task was completed | [optional] 
**id** | **str** | The ID of the individual workflow run. | 
**tasks** | [**dict(str, TaskStatus)**](TaskStatus.md) |  | [optional] 
**workflow_ref** | [**ReferenceWorkflow**](ReferenceWorkflow.md) |  | [optional] 
**inputs** | [**Arguments**](Arguments.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


