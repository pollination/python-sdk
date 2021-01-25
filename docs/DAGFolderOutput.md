# DAGFolderOutput

DAG folder output.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | [**list[AnyOfDAGGenericOutputAliasDAGStringOutputAliasDAGIntegerOutputAliasDAGNumberOutputAliasDAGBooleanOutputAliasDAGFolderOutputAliasDAGFileOutputAliasDAGPathOutputAliasDAGArrayOutputAliasDAGJSONObjectOutputAliasDAGLinkedOutputAlias]**](AnyOfDAGGenericOutputAliasDAGStringOutputAliasDAGIntegerOutputAliasDAGNumberOutputAliasDAGBooleanOutputAliasDAGFolderOutputAliasDAGFileOutputAliasDAGPathOutputAliasDAGArrayOutputAliasDAGJSONObjectOutputAliasDAGLinkedOutputAlias.md) | A list of additional processes for loading this output on different platforms. | [optional] 
**annotations** | **dict(str, str)** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**description** | **str** | Optional description for output. | [optional] 
**_from** | [**AnyOfTaskReferenceFolderReference**](AnyOfTaskReferenceFolderReference.md) | Reference to a folder or a task output. Task output must be folder. | 
**name** | **str** | Output name. | 
**required** | **bool** | A boolean to indicate if an artifact output is required. A False value makes the artifact optional. | [optional] [default to True]
**type** | **str** |  | [optional] [readonly] [default to 'DAGFolderOutput']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


