# Arguments

Arguments to a task or a workflow.  Queenbee accepts two types of arguments: parameters and artifacts. A ``parameter`` is a variable that can be passed to a task or a workflow. An ``artifact`` is a file or folder that can be identified by a url or a path.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**list[Parameter]**](Parameter.md) | Parameters is the list of input parameters to pass to the task or workflow. A parameter can have a default value which will be overwritten if an input value is provided. | [optional] 
**artifacts** | [**list[Artifact]**](Artifact.md) | Artifacts is the list of file and folder arguments to pass to the task or workflow. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


