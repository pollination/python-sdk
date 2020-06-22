# DAG

A Directed Acyclic Graph containing a list of tasks.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A unique name for this dag. | 
**inputs** | [**DAGInputs**](DAGInputs.md) | Inputs for the DAG. | [optional] 
**fail_fast** | **bool** | Stop scheduling new steps, as soon as it detects that one of the DAG nodes is failed. Default is True. | [optional] [default to True]
**tasks** | [**list[DAGTask]**](DAGTask.md) | Tasks are a list of DAG steps | 
**outputs** | [**DAGOutputs**](DAGOutputs.md) | Outputs of the DAG that can be used by other DAGs | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


