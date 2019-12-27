# TaskStatus

A Task Status
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of this task. Can be \&quot;Running\&quot;, \&quot;Succeeded\&quot;, \&quot;Failed\&quot; or \&quot;Error\&quot; | 
**message** | **str** | Any message produced by the task. Usually error/debugging hints. | [optional] 
**started_at** | **datetime** | The time at which the task was started | 
**finished_at** | **datetime** | The time at which the task was completed | [optional] 
**id** | **str** | The task unique ID | 
**name** | **str** | A human readable name for the task. Usually defined by the             DAG task name but can be extended if the task is part of a loop for example.             This name is unique within the boundary of the DAG/Workflow that generated it. | 
**type** | **str** | The type of task this status is for. Can be \&quot;Function\&quot;, \&quot;DAG\&quot;, \&quot;Workflow\&quot; or \&quot;Loop\&quot; | 
**template_ref** | **str** | The name of the template that spawned this task | 
**operator** | [**Operator**](Operator.md) | The operator used to run this task. Only applies to Function tasks. | [optional] 
**command** | **str** | The command used to run this task. Only applies to Function tasks. | [optional] 
**inputs** | [**Arguments**](Arguments.md) | The inputs used by this task | 
**outputs** | [**Arguments**](Arguments.md) | The outputs produced by this task | 
**boundary_id** | **str** | This indicates the task ID of the associated template root             task in which this task belongs to. A DAG task will have the id of the             parent DAG for example. | [optional] 
**children** | **list[str]** | A list of child task IDs | 
**outbound_tasks** | **list[str]** | A list of the last tasks to ran in the context of this             task. In the case of a DAG or a workflow this will be the last task that has             been executed. It will remain empty for functions. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


