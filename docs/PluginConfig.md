# PluginConfig

Plugin configuration.  The config is used to schedule functions on a desktop or in other contexts (ie: Docker).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**docker** | [**DockerConfig**](DockerConfig.md) | The configuration to use this plugin in a docker container | 
**local** | [**LocalConfig**](LocalConfig.md) | The configuration to use this plugin locally | [optional] 
**type** | **str** |  | [optional] [readonly] [default to 'PluginConfig']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


