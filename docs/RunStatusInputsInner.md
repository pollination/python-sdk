# RunStatusInputsInner

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | [**List[DAGArrayInputAliasInner]**](DAGArrayInputAliasInner.md) | A list of aliases for this input in different platforms. | [optional] 
**annotations** | **Dict[str, str]** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**default** | **object** | Default value to use for an input if a value was not supplied. | [optional] 
**description** | **str** | Optional description for input. | [optional] 
**name** | **str** | Input name. | 
**required** | **bool** | A field to indicate if this input is required. This input needs to be set explicitly even when a default value is provided. | [optional] [default to False]
**spec** | **object** | An optional JSON Schema specification to validate the input value. You can use validate_spec method to validate a value against the spec. | [optional] 
**type** | **str** |  | [optional] [readonly] [default to 'StepJSONObjectInput']
**value** | **object** |  | 
**path** | **str** | Path to the target location that the input will be copied to.  This path is relative to the working directory where the command is executed. | [optional] 
**source** | [**Source**](Source.md) |  | 
**extensions** | **List[str]** | Optional list of extensions for file. The check for extension is case-insensitive. | [optional] 
**items_type** | [**ItemType**](ItemType.md) | Type of items in an array. All the items in an array must be from the same type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


