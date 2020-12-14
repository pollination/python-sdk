# Recipe

A Queenbee Recipe
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**api_version** | **str** |  | [optional] [default to 'v1beta1']
**dependencies** | [**list[Dependency]**](Dependency.md) | A list of plugins and other recipes this recipe depends on. | [optional] 
**flow** | [**list[DAG]**](DAG.md) | A list of tasks to create a DAG recipe. | 
**metadata** | [**MetaData**](MetaData.md) | Recipe metadata information. | [optional] 
**type** | **str** |  | [optional] [readonly] [default to 'Recipe']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


