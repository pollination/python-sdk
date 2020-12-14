# DAGArrayOutputAlias

DAG alias array output.  This output loads the content from a JSON file which must be a JSON Array.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**description** | **str** | Optional description for output. | [optional] 
**_from** | [**AnyOfobjectobject**](AnyOfobjectobject.md) | Reference to a file or a task output. Task output must be file. | 
**handler** | [**list[IOAliasHandler]**](IOAliasHandler.md) | List of process actions to process the input or output value. | 
**items_type** | **str** | Type of items in this array. All the items in an array must be from the same type. | [optional] [default to 'String']
**name** | **str** | Output name. | 
**platform** | **list[str]** | Name of the client platform (e.g. Grasshopper, Revit, etc). The value can be any strings as long as it has been agreed between client-side developer and author of the recipe. | 
**type** | **str** |  | [optional] [readonly] [default to 'DAGArrayOutputAlias']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


