# ResponseGetPackageJson

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **Dict[str, str]** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**api_version** | **str** |  | [optional] [readonly] [default to 'v1beta1']
**dependencies** | [**List[Dependency]**](Dependency.md) | A list of plugins and other recipes this recipe depends on. | [optional] 
**flow** | [**List[DAG]**](DAG.md) | A list of tasks to create a DAG recipe. | 
**metadata** | [**MetaData**](MetaData.md) | Recipe metadata information. | 
**type** | **str** |  | [optional] [readonly] [default to 'BakedRecipe']
**config** | [**PluginConfig**](PluginConfig.md) | The configuration information to run this plugin | 
**functions** | [**List[Function]**](Function.md) | List of Plugin functions | 
**digest** | **str** |  | 
**templates** | [**List[BakedRecipeTemplatesInner]**](BakedRecipeTemplatesInner.md) | A list of templates. Templates can be Function or a DAG. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


