# Dependency

Configuration to fetch a Recipe or Plugin that another Recipe depends on.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | An optional alias to refer to this dependency. Useful if the name is already used somewhere else. | [optional] 
**annotations** | **dict(str, str)** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**hash** | **str** | The digest hash of the dependency when retrieved from its source. This is locked when the resource dependencies are downloaded. | [optional] 
**kind** | [**DependencyKind**](DependencyKind.md) | The kind of dependency. It can be a recipe or an plugin. | 
**name** | **str** | Workflow name. This name should be unique among all the resources in your resource. Use an alias if this is not the case. | 
**source** | **str** | URL to a repository where this resource can be found. | 
**tag** | **str** | Tag of the resource. | 
**type** | **str** |  | [optional] [readonly] [default to 'Dependency']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


