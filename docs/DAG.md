# DAG

DAG includes different steps of a directed acyclic graph.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A unique name for this dag. | 
**target** | **str** | Target are one or more names of target tasks to execute in a DAG. Multiple targets can be specified as space delimited inputs. When a target is provided only a subset of tasks in DAG that are required to generate the target(s) will be executed. | [optional] 
**fail_fast** | **bool** | Stop scheduling new steps, as soon as it detects that one of the DAG nodes is failed. Default is True. | [optional] [default to True]
**tasks** | [**list[DAGTask]**](DAGTask.md) | Tasks are a list of DAG steps | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


