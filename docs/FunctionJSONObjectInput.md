# FunctionJSONObjectInput

A JSON object input.  JSON objects are similar to Python dictionaries.  You can add additional validation by defining a JSONSchema specification.  See http://json-schema.org/understanding-json-schema/reference/object.html for more information.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | [**list[AnyOfDAGGenericInputAliasDAGStringInputAliasDAGIntegerInputAliasDAGNumberInputAliasDAGBooleanInputAliasDAGFolderInputAliasDAGFileInputAliasDAGPathInputAliasDAGArrayInputAliasDAGJSONObjectInputAliasDAGLinkedInputAlias]**](AnyOfDAGGenericInputAliasDAGStringInputAliasDAGIntegerInputAliasDAGNumberInputAliasDAGBooleanInputAliasDAGFolderInputAliasDAGFileInputAliasDAGPathInputAliasDAGArrayInputAliasDAGJSONObjectInputAliasDAGLinkedInputAlias.md) | A list of aliases for this input in different platforms. | [optional] 
**annotations** | **dict(str, str)** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**default** | **object** | Default value to use for an input if a value was not supplied. | [optional] 
**description** | **str** | Optional description for input. | [optional] 
**name** | **str** | Input name. | 
**required** | **bool** | A field to indicate if this input is required. This input needs to be set explicitly even when a default value is provided. | [optional] [default to False]
**spec** | **object** | An optional JSON Schema specification to validate the input value. You can use validate_spec method to validate a value against the spec. | [optional] 
**type** | **str** |  | [optional] [readonly] [default to 'FunctionJSONObjectInput']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


