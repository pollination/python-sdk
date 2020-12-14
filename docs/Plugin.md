# Plugin

A Queenbee Plugin.  A plugin contains runtime configuration for a Command Line Interface (CLI) and a list of functions that can be executed using this CLI tool.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**api_version** | **str** |  | [optional] [default to 'v1beta1']
**config** | [**PluginConfig**](PluginConfig.md) | The configuration information to run this plugin | 
**functions** | [**list[Function]**](Function.md) | List of Plugin functions | 
**metadata** | [**MetaData**](MetaData.md) | The Plugin metadata information | 
**type** | **str** |  | [optional] [readonly] [default to 'Plugin']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


