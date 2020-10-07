# SimulationStatus

Workflow Status
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | ID of the account the simulation is running for. | 
**entrypoint** | **str** | The ID of the first task in the workflow | [optional] 
**finished_at** | **datetime** | The time at which the task was completed | [optional] 
**id** | **str** | The ID of the individual workflow run. | 
**message** | **str** | Any message produced by the task. Usually error/debugging hints. | [optional] 
**parallelism** | **int** | The max number of parallel tasks running for this simulation | [optional] 
**project_id** | **str** | ID of the project the simulation belongs to | 
**recipe_account_id** | **str** | ID of the recipe owner | 
**recipe_id** | **str** | ID of the recipe repository used to create the workflow | 
**recipe_package_id** | **str** | ID of the specific recipe package used to create the workflow | 
**started_at** | **datetime** | The time at which the task was started | 
**status** | **str** | The status of this task. Can be \&quot;Running\&quot;, \&quot;Succeeded\&quot;, \&quot;Failed\&quot; or \&quot;Error\&quot; | 
**tasks** | [**dict(str, TaskStatus)**](TaskStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


