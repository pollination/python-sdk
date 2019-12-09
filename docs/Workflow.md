# Workflow

A DAG Workflow.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** |  | 
**operators** | [**list[Operator]**](Operator.md) |  | 
**templates** | **list[object]** |  | 
**id** | **str** |  | [optional] [default to '1de57c40-056e-47f3-83f9-74fb2b2b35f5']
**inputs** | [**Arguments**](Arguments.md) |  | [optional] 
**flow** | [**DAG**](DAG.md) | A list of steps for using tasks in a DAG workflow | 
**outputs** | [**Arguments**](Arguments.md) |  | [optional] 
**artifact_locations** | **list[object]** | A list of artifact locations which can be used by child flow objects | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


