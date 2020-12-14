# DockerConfig

Plugin Configuration to run in a Docker container
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**image** | **str** | Docker image name. Must include tag. | 
**registry** | **str** | The container registry URLs that this container should be pulled from. Will default to Dockerhub if none is specified. | [optional] 
**type** | **str** |  | [optional] [readonly] [default to 'DockerConfig']
**workdir** | **str** | The working directory the entrypoint command of the container runsin. This is used to determine where to load artifacts when running in the container. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


