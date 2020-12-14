# TaskPathArgument

BaseModel with functionality to return the object as a yaml string.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**_from** | [**AnyOfobjectobjectobjectobjectobjectobjectobjectobject**](AnyOfobjectobjectobjectobjectobjectobjectobjectobject.md) | A reference to a DAG input, a DAG output or another task output. You can also use the ValueReference type to hard-code an input value. | 
**name** | **str** | Argument name. The name must match one of the input names from Task&#39;s template which can be a function or DAG. | 
**sub_path** | **str** | A sub_path inside the path that is provided in the &#x60;&#x60;from&#x60;&#x60; field. Use sub_path to only access part of the Path that is needed instead of copying all the files and folders inside the path. | [optional] 
**type** | **str** |  | [optional] [readonly] [default to 'TaskPathArgument']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


