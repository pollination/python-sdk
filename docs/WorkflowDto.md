# WorkflowDto

A DAG Workflow.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** |  | 
**id** | **str** |  | [optional] [default to 'b713943e-5186-4622-9a39-b0f08cb6b8cc']
**inputs** | [**Arguments**](Arguments.md) |  | [optional] 
**operators** | [**list[Operator]**](Operator.md) |  | 
**templates** | [**list[AnyOfFunctionDAGWorkflow]**](AnyOfFunctionDAGWorkflow.md) | A list of templates. Templates can be Function, DAG or a Workflow. | 
**flow** | [**DAG**](DAG.md) | A list of tasks to create a DAG workflow. | 
**outputs** | [**Arguments**](Arguments.md) |  | [optional] 
**artifact_locations** | [**list[AnyOfRunFolderLocationInputFolderLocationHTTPLocationS3Location]**](AnyOfRunFolderLocationInputFolderLocationHTTPLocationS3Location.md) | A list of artifact locations which can be used by flow objects. | [optional] 
**public** | **bool** | A boolean indicator of whether workflow is public or not | 
**owner** | [**AccountPublic**](AccountPublic.md) |  | 
**slug** | **str** | The workflow slug in format {owner}:{workflow_name} | 
**permissions** | [**AppModulesWorkflowsInterfacePermissions**](AppModulesWorkflowsInterfacePermissions.md) | The permissions the current user has on the workflow. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


