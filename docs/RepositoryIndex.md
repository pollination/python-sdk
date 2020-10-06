# RepositoryIndex

A searchable index for a Queenbee Operator and Recipe repository
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generated** | **datetime** | The timestamp at which the index was generated | [optional] 
**metadata** | [**RepositoryMetadata**](RepositoryMetadata.md) | Extra information about the repository | [optional] 
**operator** | **dict(str, list[PackageVersion])** | A dict of operators accessible by name. Each name key points to a list of operator versions | [optional] 
**recipe** | **dict(str, list[PackageVersion])** | A dict of recipes accessible by name. Each name key points to a list of recipesversions | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


