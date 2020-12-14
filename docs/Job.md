# Job

Queenbee Job.  A Job is an object to submit a list of arguments to execute a Queenbee recipe.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**api_version** | **str** |  | [optional] [default to 'v1beta1']
**arguments** | [**list[AnyOfJobArgumentJobPathArgument]**](AnyOfJobArgumentJobPathArgument.md) | Input arguments for this job. | [optional] 
**description** | **str** | Run description. | [optional] 
**labels** | **dict(str, str)** | Optional user data as a dictionary. User data is for user reference only and will not be used in the execution of the job. | [optional] 
**name** | **str** | An optional name for this job. This name will be used a the display name for the run. | [optional] 
**source** | **str** | The source url for downloading the recipe. | 
**type** | **str** |  | [optional] [readonly] [default to 'Job']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


