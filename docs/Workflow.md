# Workflow

A DAG Workflow.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** |  | 
**id** | **str** |  | [optional] [default to '483395fd-6e1e-4c14-89fe-66de4b627c6d']
**inputs** | [**Arguments**](Arguments.md) |  | [optional] 
**operators** | [**list[Operator]**](Operator.md) |  | 
**templates** | **list[object]** | A list of templates. Templates can be Function, DAG or a Workflow. | 
**flow** | [**DAG**](DAG.md) | A list of tasks to create a DAG workflow. | 
**outputs** | [**Arguments**](Arguments.md) |  | [optional] 
**artifact_locations** | **list[object]** | A list of artifact locations which can be used by flow objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


