# DAGGenericInput

Base class for DAG inputs.  This class adds a handler to input to handle the process of loading the input from different graphical interfaces.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | [**list[AnyOfDAGGenericInputAliasDAGStringInputAliasDAGIntegerInputAliasDAGNumberInputAliasDAGBooleanInputAliasDAGFolderInputAliasDAGFileInputAliasDAGPathInputAliasDAGArrayInputAliasDAGJSONObjectInputAliasDAGLinkedInputAlias]**](AnyOfDAGGenericInputAliasDAGStringInputAliasDAGIntegerInputAliasDAGNumberInputAliasDAGBooleanInputAliasDAGFolderInputAliasDAGFileInputAliasDAGPathInputAliasDAGArrayInputAliasDAGJSONObjectInputAliasDAGLinkedInputAlias.md) | A list of aliases for this input in different platforms. | [optional] 
**annotations** | **dict(str, str)** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**default** | **str** | Default value for generic input. | [optional] 
**description** | **str** | Optional description for input. | [optional] 
**name** | **str** | Input name. | 
**required** | **bool** | A field to indicate if this input is required. This input needs to be set explicitly even when a default value is provided. | [optional] [default to False]
**spec** | **object** | An optional JSON Schema specification to validate the input value. You can use validate_spec method to validate a value against the spec. | [optional] 
**type** | **str** |  | [optional] [readonly] [default to 'DAGGenericInput']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


