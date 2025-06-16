# DAGGenericOutput

DAG generic output.  In most cases, you should not be using the generic output unless you need a dynamic output that changes its type in different platforms because of returning different objects in handler.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | [**List[DAGArrayOutputAliasInner]**](DAGArrayOutputAliasInner.md) | A list of additional processes for loading this output on different platforms. | [optional] 
**annotations** | **Dict[str, str]** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**description** | **str** | Optional description for output. | [optional] 
**var_from** | **object** |  | 
**name** | **str** | Output name. | 
**type** | **str** |  | [optional] [readonly] [default to 'DAGGenericOutput']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


