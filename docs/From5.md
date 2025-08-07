# From5

A reference to a DAG input, a DAG output or another task output. You can also use the ValueReference type to hard-code an input value.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **Dict[str, str]** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**type** | **str** |  | [optional] [readonly] [default to 'ValueFolderReference']
**variable** | **str** | The name of the variable. | 
**name** | **str** | The name of the task to pull output data from. | 
**path** | **str** | A fixed value for this reference. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


