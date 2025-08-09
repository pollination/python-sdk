# RunResultListResourcesInnerInner

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | [**List[DAGArrayInputAliasInner]**](DAGArrayInputAliasInner.md) | A list of aliases for this input in different platforms. | [optional] 
**annotations** | **Dict[str, str]** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**default** | **object** | Default value to use for an input if a value was not supplied. | [optional] 
**description** | **str** | Optional description for output. | [optional] 
**name** | **str** | Output name. | 
**required** | **bool** | A boolean to indicate if an artifact output is required. A False value makes the artifact optional. | [optional] [default to True]
**spec** | **object** | An optional JSON Schema specification to validate the input value. You can use validate_spec method to validate a value against the spec. | [optional] 
**type** | **str** |  | [optional] [readonly] [default to 'StepJSONObjectOutput']
**value** | **object** |  | 
**path** | **str** | Path to the output file relative to where the function command is executed. | 
**source** | [**Source**](Source.md) |  | 
**extensions** | **List[str]** | Optional list of extensions for file. The check for extension is case-insensitive. | [optional] 
**items_type** | [**ItemType**](ItemType.md) | Type of items in this array. All the items in an array must be from the same type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


