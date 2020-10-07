# DAGInputArtifact

An artifact used within the DAG.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | Optional annotations for Queenbee objects. | [optional] 
**default** | [**AnyOfHTTPSourceS3SourceProjectFolderSource**](AnyOfHTTPSourceS3SourceProjectFolderSource.md) | If no artifact is specified then pull it from this source location. | [optional] 
**description** | **str** | Optional description for the input artifact | [optional] 
**name** | **str** | The name of the artifact within the scope of the DAG | 
**required** | **bool** | Whether this value must be specified in a task argument. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


