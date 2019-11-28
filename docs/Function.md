# Function

A function with a single command.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** | Function name. Must be unique within a workflow. | 
**description** | **str** | Function description. A short human readable description for this function. | [optional] 
**inputs** | [**Arguments**](Arguments.md) | Input arguments for this function. | [optional] 
**command** | **str** | Full shell command for this function. Each function accepts only one command. The command will be executed as a shell command in operator. For running several commands after each other use &amp;&amp; between the commands or pipe data from one to another using | | 
**operator** | **str** | Function operator name. | 
**env** | **dict(str, str)** | A dictionary of key:values for environmental variables. | [optional] 
**outputs** | [**Arguments**](Arguments.md) | List of output arguments. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


