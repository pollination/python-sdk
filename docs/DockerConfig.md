# DockerConfig

Operator Configuration to run in a Docker container
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **str** | Docker image name. Must include tag. | 
**registry** | **str** | The container registry URLs that this container should be pulled from. Will default to Dockerhub if none is specified. | [optional] 
**workdir** | **str** | The working directory the entrypoint command of the container runsin. This is used to determine where to load artifacts when running in the container. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


