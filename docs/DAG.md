# DAG

A Directed Acyclic Graph containing a list of tasks.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**fail_fast** | **bool** | Stop scheduling new steps, as soon as it detects that one of the DAG nodes is failed. Default is True. | [optional] [default to True]
**inputs** | [**list[AnyOfDAGGenericInputDAGStringInputDAGIntegerInputDAGNumberInputDAGBooleanInputDAGFolderInputDAGFileInputDAGPathInputDAGArrayInputDAGJSONObjectInput]**](AnyOfDAGGenericInputDAGStringInputDAGIntegerInputDAGNumberInputDAGBooleanInputDAGFolderInputDAGFileInputDAGPathInputDAGArrayInputDAGJSONObjectInput.md) | Inputs for the DAG. | [optional] 
**name** | **str** | A unique name for this dag. | 
**outputs** | [**list[AnyOfDAGGenericOutputDAGStringOutputDAGIntegerOutputDAGNumberOutputDAGBooleanOutputDAGFolderOutputDAGFileOutputDAGPathOutputDAGArrayOutputDAGJSONObjectOutput]**](AnyOfDAGGenericOutputDAGStringOutputDAGIntegerOutputDAGNumberOutputDAGBooleanOutputDAGFolderOutputDAGFileOutputDAGPathOutputDAGArrayOutputDAGJSONObjectOutput.md) | Outputs of the DAG that can be used by other DAGs. | [optional] 
**tasks** | [**list[DAGTask]**](DAGTask.md) | Tasks are a list of DAG steps | 
**type** | **str** |  | [optional] [readonly] [default to 'DAG']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


