# RepositoryIndex

A searchable index for a Queenbee Plugin and Recipe repository
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**api_version** | **str** |  | [optional] [readonly] [default to 'v1beta1']
**generated** | **datetime** | The timestamp at which the index was generated | [optional] 
**metadata** | [**RepositoryMetadata**](RepositoryMetadata.md) | Extra information about the repository | [optional] 
**plugin** | **dict(str, list[PackageVersion])** | A dict of plugins accessible by name. Each name key points to a list of plugin versions | [optional] 
**recipe** | **dict(str, list[PackageVersion])** | A dict of recipes accessible by name. Each name key points to a list of recipesversions | [optional] 
**type** | **str** |  | [optional] [readonly] [default to 'RepositoryIndex']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


