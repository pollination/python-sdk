# Operator

Task operator.  A task operator includes the information for executing tasks from command line or in a container.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'operator']
**name** | **str** | Operator name. This name should be unique among all the operators in your workflow. | 
**version** | **str** | Optional version input for operator. | [optional] 
**image** | **str** | Docker image name. | 
**local** | [**LocalRequirements**](LocalRequirements.md) | An optional requirement object to specify requirements for local execution of the commands. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


