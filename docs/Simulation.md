# Simulation

Workflow Status
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entrypoint** | **str** | The ID of the first task in the workflow | [optional] 
**finished_at** | **datetime** | The time at which the task was completed | [optional] 
**id** | **str** | The ID of the individual workflow run. | 
**inputs** | [**SimulationInputs**](SimulationInputs.md) | Simulation inputs | [optional] 
**message** | **str** | Any message produced by the task. Usually error/debugging hints. | [optional] 
**owner** | [**AccountPublic**](AccountPublic.md) |  | 
**parallelism** | **int** | The max number of parallel tasks allowed for this simulation | [optional] 
**recipe** | [**RecipeSelection**](RecipeSelection.md) | The recipe to use | 
**started_at** | **datetime** | The time at which the task was started | 
**status** | **str** | The status of this task. Can be \&quot;Running\&quot;, \&quot;Succeeded\&quot;, \&quot;Failed\&quot; or \&quot;Error\&quot; | 
**tasks** | [**dict(str, TaskStatus)**](TaskStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


