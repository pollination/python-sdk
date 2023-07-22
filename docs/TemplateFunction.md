# TemplateFunction

Function template.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**command** | **str** | Full shell command for this function. Each function accepts only one command. The command will be executed as a shell command in plugin. For running several commands after each other use &amp;&amp; between the commands or pipe data from one to another using | | [optional] 
**config** | [**PluginConfig**](PluginConfig.md) | The plugin config to use for this function | 
**description** | **str** | Function description. A short human readable description for this function. | [optional] 
**inputs** | [**list[AnyOfFunctionStringInputFunctionIntegerInputFunctionNumberInputFunctionBooleanInputFunctionFolderInputFunctionFileInputFunctionPathInputFunctionArrayInputFunctionJSONObjectInput]**](AnyOfFunctionStringInputFunctionIntegerInputFunctionNumberInputFunctionBooleanInputFunctionFolderInputFunctionFileInputFunctionPathInputFunctionArrayInputFunctionJSONObjectInput.md) | Input arguments for this function. | [optional] 
**language** | [**ScriptingLanguages**](ScriptingLanguages.md) | Programming language of the script. Currently only Python is supported. | [optional] 
**name** | **str** | Function name. Must be unique within a plugin. | 
**outputs** | [**list[AnyOfFunctionStringOutputFunctionIntegerOutputFunctionNumberOutputFunctionBooleanOutputFunctionFolderOutputFunctionFileOutputFunctionPathOutputFunctionArrayOutputFunctionJSONObjectOutput]**](AnyOfFunctionStringOutputFunctionIntegerOutputFunctionNumberOutputFunctionBooleanOutputFunctionFolderOutputFunctionFileOutputFunctionPathOutputFunctionArrayOutputFunctionJSONObjectOutput.md) | List of output arguments. | [optional] 
**source** | **str** | Source contains the source code of the script to execute. | [optional] 
**type** | **str** |  | [optional] [readonly] [default to 'TemplateFunction']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


