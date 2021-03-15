# JobStatus

Parametric Job Status.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**api_version** | **str** |  | [optional] [readonly] [default to 'v1beta1']
**finished_at** | **datetime** | The time at which the task was completed | [optional] 
**id** | **str** | The ID of the individual job. | 
**message** | **str** | Any message produced by the job. Usually error/debugging hints. | [optional] 
**runs_cancelled** | **int** | The count of runs that have been cancelled | [optional] [default to 0]
**runs_completed** | **int** | The count of runs that have completed | [optional] [default to 0]
**runs_failed** | **int** | The count of runs that have failed | [optional] [default to 0]
**runs_pending** | **int** | The count of runs that are pending | [optional] [default to 0]
**runs_running** | **int** | The count of runs that are running | [optional] [default to 0]
**source** | **str** | Source url for the status object. It can be a recipe or a function. | [optional] 
**started_at** | **datetime** | The time at which the job was started | 
**status** | [**JobStatusEnum**](JobStatusEnum.md) | The status of this job. | [optional] 
**type** | **str** |  | [optional] [readonly] [default to 'JobStatus']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


