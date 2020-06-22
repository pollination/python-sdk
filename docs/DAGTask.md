# DAGTask

The instance of a function template matched with DAG inputs and outputs.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name for this step. It must be unique in DAG. | 
**template** | **str** | Template name. | 
**arguments** | [**DAGTaskArgument**](DAGTaskArgument.md) | The input arguments for this task | [optional] 
**dependencies** | **list[str]** | Dependencies are name of other DAG steps which this depends on. | [optional] 
**loop** | [**DAGTaskLoop**](DAGTaskLoop.md) | List of inputs to loop over. | [optional] 
**sub_folder** | **str** | A path relative to the current folder context where artifacts should be saved. This is useful when performing a loop or invoking another workflow and wanting to save results in a specific folder. | [optional] 
**outputs** | [**DAGTaskOutputs**](DAGTaskOutputs.md) | The outputs of this task | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


