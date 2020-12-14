# DAGTaskLoop

Loop configuration for the task.  This will run the template provided multiple times and in parallel relative to an input or task parameter which should be a list.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**_from** | [**AnyOfobjectobjectobject**](AnyOfobjectobjectobject.md) | The task or DAG parameter to loop over (must be iterable). | [optional] 
**type** | **str** |  | [optional] [readonly] [default to 'DAGTaskLoop']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


