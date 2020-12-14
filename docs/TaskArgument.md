# TaskArgument

Task argument for receiving inputs that are not files or folders.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**_from** | [**AnyOfobjectobjectobjectobject**](AnyOfobjectobjectobjectobject.md) | A reference to a DAG input, a DAG output or another task output. You can also use the ValueReference type to hard-code an input value. | 
**name** | **str** | Argument name. The name must match one of the input names from Task&#39;s template which can be a function or DAG. | 
**type** | **str** |  | [optional] [readonly] [default to 'TaskArgument']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


