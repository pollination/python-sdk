# DAGBooleanInputAlias

The boolean type matches only two special values: True and False.  Note that values that evaluate to true or false, such as 1 and 0, are not accepted.  You can add additional validation by defining a JSONSchema specification.  See http://json-schema.org/understanding-json-schema/reference/boolean.html for more information.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**default** | **bool** | Default value to use for an input if a value was not supplied. | [optional] 
**description** | **str** | Optional description for input. | [optional] 
**handler** | [**list[IOAliasHandler]**](IOAliasHandler.md) | List of process actions to process the input or output value. | 
**name** | **str** | Input name. | 
**platform** | **list[str]** | Name of the client platform (e.g. Grasshopper, Revit, etc). The value can be any strings as long as it has been agreed between client-side developer and author of the recipe. | 
**required** | **bool** | A field to indicate if this input is required. This input needs to be set explicitly even when a default value is provided. | [optional] [default to False]
**spec** | **object** | An optional JSON Schema specification to validate the input value. You can use validate_spec method to validate a value against the spec. | [optional] 
**type** | **str** |  | [optional] [readonly] [default to 'DAGBooleanInputAlias']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


