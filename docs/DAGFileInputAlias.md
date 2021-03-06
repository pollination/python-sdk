# DAGFileInputAlias

An alias file input.  File is a special string input. Unlike other string inputs, a file will be copied from its location to execution folder when a workflow is executed.  You can add additional validation by defining a JSONSchema specification.  See http://json-schema.org/understanding-json-schema/reference/string.html#string for more information.  .. code-block:: python      # a file with maximum 50 characters with an ``epw`` extension.      \"schema\": {         \"type\": \"string\",         \"maxLength\": 50,         \"pattern\": \"(?i)(^.*\\.epw$)\"     }
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**default** | [**AnyOfHTTPS3ProjectFolder**](AnyOfHTTPS3ProjectFolder.md) | The default source for file if the value is not provided. | [optional] 
**description** | **str** | Optional description for input. | [optional] 
**extensions** | **list[str]** | Optional list of extensions for file. The check for extension is case-insensitive. | [optional] 
**handler** | [**list[IOAliasHandler]**](IOAliasHandler.md) | List of process actions to process the input or output value. | 
**name** | **str** | Input name. | 
**platform** | **list[str]** | Name of the client platform (e.g. Grasshopper, Revit, etc). The value can be any strings as long as it has been agreed between client-side developer and author of the recipe. | 
**required** | **bool** | A field to indicate if this input is required. This input needs to be set explicitly even when a default value is provided. | [optional] [default to False]
**spec** | **object** | An optional JSON Schema specification to validate the input value. You can use validate_spec method to validate a value against the spec. | [optional] 
**type** | **str** |  | [optional] [readonly] [default to 'DAGFileInputAlias']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


