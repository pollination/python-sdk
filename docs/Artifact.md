# Artifact

Artifact indicates an artifact to be placed at a specified path.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the artifact. Must be unique within a task&#39;s inputs / outputs. | 
**location** | **str** | Name of the artifact_location to source this artifact from. | [optional] 
**source_path** | **str** | Path to the artifact in a url or S3 bucket. | [optional] 
**path** | **str** | Path to the artifact relative to the run-folder artifact location. | [optional] 
**description** | **str** | Optional description for input parameter. | [optional] 
**headers** | **dict(str, str)** | An object with Key Value pairs of HTTP headers. For artifacts from URL location only. | [optional] 
**verb** | **str** | The HTTP verb to use when making the request. For artifacts from URL location only. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


