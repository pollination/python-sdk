# Function

A Function with a single command
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** | Full shell command for this function. Each function accepts only one command. The command will be executed as a shell command in operator. For running several commands after each other use &amp;&amp; between the commands or pipe data from one to another using | | 
**description** | **str** | Function description. A short human readable description for this function. | [optional] 
**inputs** | [**FunctionInputs**](FunctionInputs.md) | Input arguments for this function. | [optional] 
**name** | **str** | Function name. Must be unique within an operator. | 
**outputs** | [**FunctionOutputs**](FunctionOutputs.md) | List of output arguments. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


