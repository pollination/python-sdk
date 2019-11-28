# DAGTask

DAGTask defines a single step in a Directed Acyclic Graph (DAG) workflow.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name for this step. It must be unique in DAG. | 
**arguments** | [**Arguments**](Arguments.md) | Input arguments for template. | [optional] 
**template** | **str** | Template name. | 
**dependencies** | **list[str]** | Dependencies are name of other DAG steps which this depends on. | [optional] 
**loop** | [**object**](.md) |  | [optional] 
**loop_control** | [**LoopControl**](LoopControl.md) | Control parameters for loop. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


