# DAGTask

A single task in a DAG flow.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**arguments** | [**list[AnyOfTaskArgumentTaskPathArgument]**](AnyOfTaskArgumentTaskPathArgument.md) | The input arguments for this task. | [optional] 
**loop** | [**DAGTaskLoop**](DAGTaskLoop.md) | Loop configuration for this task. | [optional] 
**name** | **str** | Name for this task. It must be unique in a DAG. | 
**needs** | **list[str]** | List of DAG tasks that this task depends on and needs to be executed before this task. | [optional] 
**returns** | [**list[AnyOfTaskReturnTaskPathReturn]**](AnyOfTaskReturnTaskPathReturn.md) | List of task returns. | [optional] 
**sub_folder** | **str** | A path relative to the current folder context where artifacts should be saved. This is useful when performing a loop or invoking another workflow and wanting to save results in a specific sub_folder. | [optional] 
**template** | **str** | Template name. A template is a Function or a DAG. This template must be available in the dependencies. | 
**type** | **str** |  | [optional] [readonly] [default to 'DAGTask']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


