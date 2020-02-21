# ProjectDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the project. Must be unique to a given owner | 
**description** | **str** | A description of the project | [optional] [default to '']
**public** | **bool** | Whether or not a project is publicly viewable | [optional] [default to True]
**id** | **str** | The project ID | 
**owner** | [**AccountPublic**](AccountPublic.md) |  | 
**permissions** | [**ProjectPermissions**](ProjectPermissions.md) |  | 
**slug** | **str** | The project name in slug format | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


