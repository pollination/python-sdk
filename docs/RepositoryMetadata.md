# RepositoryMetadata

BaseModel with functionality to return the object as a yaml string.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**description** | **str** | A short description of the repository | [optional] [default to 'A Queenbee package repository']
**name** | **str** | The name of the repository | [optional] 
**plugin_count** | **int** | The number of plugins hosted by the repository | [optional] [default to 0]
**recipe_count** | **int** | The number of recipes hosted by the repository | [optional] [default to 0]
**source** | **str** | The source path (url or local) to the repository | [optional] 
**type** | **str** |  | [optional] [readonly] [default to 'RepositoryMetadata']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


