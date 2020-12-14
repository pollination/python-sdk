# JobPathArgument

BaseModel with functionality to return the object as a yaml string.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**name** | **str** | Argument name. The name must match one of the input names from Job&#39;s template which can be a function or DAG. | 
**source** | [**AnyOfHTTPS3ProjectFolder**](AnyOfHTTPS3ProjectFolder.md) | The path to source the file from. | 
**type** | **str** |  | [optional] [readonly] [default to 'JobPathArgument']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


