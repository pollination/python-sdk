# S3Source

S3Source  An S3 bucket artifact Source.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 's3']
**key** | **str** | The path inside the bucket to source artifacts from. | 
**endpoint** | **str** | The HTTP endpoint to reach the S3 bucket. | 
**bucket** | **str** | The name of the S3 bucket on the host server. | 
**credentials_path** | **str** | Path to the file holding the AccessKey and SecretAccessKey to authenticate to the bucket. Assumes public bucket access if none are specified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


