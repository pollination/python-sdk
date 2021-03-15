# RunStatus

Job Status.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**api_version** | **str** |  | [optional] [readonly] [default to 'v1beta1']
**entrypoint** | **str** | The ID of the first step in the run. | [optional] 
**finished_at** | **datetime** | The time at which the task was completed | [optional] 
**id** | **str** | The ID of the individual run. | 
**inputs** | [**list[AnyOfStepStringInputStepIntegerInputStepNumberInputStepBooleanInputStepFolderInputStepFileInputStepPathInputStepArrayInputStepJSONObjectInput]**](AnyOfStepStringInputStepIntegerInputStepNumberInputStepBooleanInputStepFolderInputStepFileInputStepPathInputStepArrayInputStepJSONObjectInput.md) | The inputs used for this run. | 
**job_id** | **str** | The ID of the job that generated this run. | 
**message** | **str** | Any message produced by the task. Usually error/debugging hints. | [optional] 
**outputs** | [**list[AnyOfStepStringOutputStepIntegerOutputStepNumberOutputStepBooleanOutputStepFolderOutputStepFileOutputStepPathOutputStepArrayOutputStepJSONObjectOutput]**](AnyOfStepStringOutputStepIntegerOutputStepNumberOutputStepBooleanOutputStepFolderOutputStepFileOutputStepPathOutputStepArrayOutputStepJSONObjectOutput.md) | The outputs produced by this run. | 
**source** | **str** | Source url for the status object. It can be a recipe or a function. | [optional] 
**started_at** | **datetime** | The time at which the task was started | 
**status** | [**RunStatusEnum**](RunStatusEnum.md) | The status of this run. | [optional] 
**steps** | [**dict(str, StepStatus)**](StepStatus.md) |  | [optional] 
**type** | **str** |  | [optional] [readonly] [default to 'RunStatus']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


