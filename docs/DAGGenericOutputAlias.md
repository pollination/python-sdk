# DAGGenericOutputAlias

DAG generic alias output.  In most cases, you should not be using the generic output unless you need a dynamic output that changes its type in different platforms because of returning different objects in handler.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**description** | **str** | Optional description for output. | [optional] 
**handler** | [**list[IOAliasHandler]**](IOAliasHandler.md) | List of process actions to process the input or output value. | 
**name** | **str** | Output name. | 
**platform** | **list[str]** | Name of the client platform (e.g. Grasshopper, Revit, etc). The value can be any strings as long as it has been agreed between client-side developer and author of the recipe. | 
**type** | **str** |  | [optional] [readonly] [default to 'DAGGenericOutputAlias']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


