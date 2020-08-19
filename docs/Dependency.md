# Dependency

Configuration to fetch a Recipe or Operator that another Recipe depends on.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DependencyType**](DependencyType.md) |  | 
**name** | **str** | Workflow name. This name should be unique among all the resources in your resource. Use an alias if this is not the case. | 
**hash** | **str** | The digest hash of the dependency when retrieved from its source. This is locked when the resource dependencies are downloaded. | [optional] 
**alias** | **str** | An optional alias to refer to this dependency. Useful if the name is already used somewhere else. | [optional] 
**tag** | **str** | Tag of the resource. | 
**source** | **str** | URL to a repository where this resource can be found. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


