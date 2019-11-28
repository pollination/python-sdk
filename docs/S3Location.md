# S3Location

S3Location  An S3 bucket
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** | Name is a unique identifier for this particular Artifact Location | 
**root** | **str** | The path inside the bucket to source artifacts from. | [optional] [default to '/']
**endpoint** | **str** | The HTTP endpoint to reach the S3 bucket. | 
**bucket** | **str** | The name of the S3 bucket on the host server. | 
**credentials_path** | **str** | Path to the file holding the AccessKey and SecretAccessKey to authenticate to the bucket | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


