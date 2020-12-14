# StepStatus

The Status of a Job Step
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**boundary_id** | **str** | This indicates the step ID of the associated template root             step in which this step belongs to. A DAG step will have the id of the             parent DAG for example. | [optional] 
**children_ids** | **list[str]** | A list of child step IDs | 
**command** | **str** | The command used to run this step. Only applies to Function steps. | [optional] 
**finished_at** | **datetime** | The time at which the task was completed | [optional] 
**id** | **str** | The step unique ID | 
**inputs** | [**list[AnyOfStepStringInputStepIntegerInputStepNumberInputStepBooleanInputStepFolderInputStepFileInputStepPathInputStepArrayInputStepJSONObjectInput]**](AnyOfStepStringInputStepIntegerInputStepNumberInputStepBooleanInputStepFolderInputStepFileInputStepPathInputStepArrayInputStepJSONObjectInput.md) | The inputs used by this step. | 
**message** | **str** | Any message produced by the task. Usually error/debugging hints. | [optional] 
**name** | **str** | A human readable name for the step. Usually defined by the DAG task name but can be extended if the step is part of a loop for example. This name is unique within the boundary of the DAG/Job that generated it. | 
**outbound_steps** | **list[str]** | A list of the last step to ran in the context of this step. In the case of a DAG or a job this will be the last step that has been executed. It will remain empty for functions. | 
**outputs** | [**list[AnyOfStepStringOutputStepIntegerOutputStepNumberOutputStepBooleanOutputStepFolderOutputStepFileOutputStepPathOutputStepArrayOutputStepJSONObjectOutput]**](AnyOfStepStringOutputStepIntegerOutputStepNumberOutputStepBooleanOutputStepFolderOutputStepFileOutputStepPathOutputStepArrayOutputStepJSONObjectOutput.md) | The outputs produced by this step. | 
**source** | **str** | Source url for the status object. It can be a recipe or a function. | [optional] 
**started_at** | **datetime** | The time at which the task was started | 
**status** | **str** | The status of this task. Can be \&quot;Running\&quot;, \&quot;Succeeded\&quot;, \&quot;Failed\&quot; or \&quot;Error\&quot; | 
**status_type** | [**StatusType**](StatusType.md) | The type of step this status is for. Can be \&quot;Function\&quot;, \&quot;DAG\&quot; or \&quot;Loop\&quot; | 
**template_ref** | **str** | The name of the template that spawned this step | 
**type** | **str** |  | [optional] [readonly] [default to 'StepStatus']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


