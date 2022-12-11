# ApplicationCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_config** | [**DeploymentConfig**](DeploymentConfig.md) | The deployment configuration for the application | [optional] 
**description** | **str** | A description of the application | [optional] [default to '']
**image** | **str** | An image associated with the application | [optional] [default to 'https://picsum.photos/400']
**is_paid** | **bool** | Whether or not the application is paid | [optional] [default to False]
**keywords** | **list[str]** | A list of keywords associated with the application | [optional] [default to []]
**license** | **str** | The license of the application | [optional] 
**name** | **str** | The name of the application. Must be unique to a given owner | 
**public** | **bool** | Whether or not a application is publicly viewable | [optional] [default to True]
**source** | **str** | A link to the source code of the application | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


