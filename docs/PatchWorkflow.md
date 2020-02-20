# PatchWorkflow

A DAG Workflow.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** |  | 
**id** | **str** |  | [optional] [default to '8b84c025-d31d-4973-9658-d291ee667f76']
**inputs** | [**Arguments**](Arguments.md) |  | [optional] 
**operators** | [**list[Operator]**](Operator.md) |  | 
**templates** | [**list[AnyOfFunctionDAGWorkflow]**](AnyOfFunctionDAGWorkflow.md) | A list of templates. Templates can be Function, DAG or a Workflow. | 
**flow** | [**DAG**](DAG.md) | A list of tasks to create a DAG workflow. | 
**outputs** | [**Arguments**](Arguments.md) |  | [optional] 
**artifact_locations** | [**list[AnyOfRunFolderLocationInputFolderLocationHTTPLocationS3Location]**](AnyOfRunFolderLocationInputFolderLocationHTTPLocationS3Location.md) | A list of artifact locations which can be used by flow objects. | [optional] 
**public** | **bool** | A boolean indicator of whether workflow is public or not | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


