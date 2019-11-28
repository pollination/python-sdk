# Artifact

Artifact indicates an artifact to place at a specified path
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the artifact. must be unique within a task&#39;s inputs / outputs. | 
**location** | **str** | Name of the Artifact Location to source this artifact from. | [optional] 
**source_path** | **str** | Path to the artifact on the local machine, url or S3 bucket. | [optional] 
**path** | **str** | Path the artifact should be copied to in the temporary task folder. | [optional] 
**description** | **str** | Optional description for input parameter. | [optional] 
**headers** | **dict(str, str)** | An object with Key Value pairs of HTTP headers. For artifacts from URL Location only | [optional] 
**verb** | **str** | The HTTP verb to use when making the request. For artifacts from URL Location only | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


