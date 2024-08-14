# DAGOutputsInner

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | [**List[DAGArrayOutputAliasInner]**](DAGArrayOutputAliasInner.md) | A list of additional processes for loading this output on different platforms. | [optional] 
**annotations** | **Dict[str, str]** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**description** | **str** | Optional description for output. | [optional] 
**var_from** | [**ModelFrom**](ModelFrom.md) |  | 
**name** | **str** | Output name. | 
**type** | **str** |  | [optional] [readonly] [default to 'DAGJSONObjectOutput']
**required** | **bool** | A boolean to indicate if an artifact output is required. A False value makes the artifact optional. | [optional] [default to True]
**items_type** | [**ItemType**](ItemType.md) | Type of items in this array. All the items in an array must be from the same type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


