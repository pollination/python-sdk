# Workflow

A DAG Workflow.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** |  | 
**operators** | [**list[Operator]**](Operator.md) |  | 
**templates** | **list[object]** |  | 
**id** | **str** |  | [optional] [default to 'de13e43c-9382-4c24-baf1-ea5b92e49bbe']
**inputs** | [**Arguments**](Arguments.md) |  | [optional] 
**flow** | [**DAG**](DAG.md) | A list of steps for using tasks in a DAG workflow | 
**outputs** | [**Arguments**](Arguments.md) |  | [optional] 
**artifact_locations** | **list[object]** | A list of artifact locations which can be used by child flow objects | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


