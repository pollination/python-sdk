# BakedRecipe

Baked Recipe.  A Baked Recipe contains all the templates referred to in the DAG within a templates list.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**api_version** | **str** |  | [optional] [readonly] [default to 'v1beta1']
**dependencies** | [**list[Dependency]**](Dependency.md) | A list of plugins and other recipes this recipe depends on. | [optional] 
**digest** | **str** |  | 
**flow** | [**list[DAG]**](DAG.md) | A list of tasks to create a DAG recipe. | 
**metadata** | [**MetaData**](MetaData.md) | Recipe metadata information. | [optional] 
**templates** | [**list[AnyOfTemplateFunctionDAG]**](AnyOfTemplateFunctionDAG.md) | A list of templates. Templates can be Function or a DAG. | 
**type** | **str** |  | [optional] [readonly] [default to 'BakedRecipe']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


