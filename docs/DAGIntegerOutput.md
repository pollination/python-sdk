# DAGIntegerOutput

DAG integer output.  This output loads the content from a file as an integer.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | [**List[DAGArrayOutputAliasInner]**](DAGArrayOutputAliasInner.md) | A list of additional processes for loading this output on different platforms. | [optional] 
**annotations** | **Dict[str, str]** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**description** | **str** | Optional description for output. | [optional] 
**var_from** | [**ModelFrom**](ModelFrom.md) |  | 
**name** | **str** | Output name. | 
**required** | **bool** | A boolean to indicate if an artifact output is required. A False value makes the artifact optional. | [optional] [default to True]
**type** | **str** |  | [optional] [readonly] [default to 'DAGIntegerOutput']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


