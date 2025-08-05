# Source

The path to source the file from.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **Dict[str, str]** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**type** | **str** |  | [optional] [readonly] [default to 'ProjectFolder']
**url** | **str** | For a HTTP endpoint this can be http://climate.onebuilding.org. | 
**bucket** | **str** | The name of the S3 bucket on the host server. | 
**credentials_path** | **str** | Path to the file holding the AccessKey and SecretAccessKey to authenticate to the bucket. Assumes public bucket access if none are specified. | [optional] 
**endpoint** | **str** | The HTTP endpoint to reach the S3 bucket. | 
**key** | **str** | The path inside the bucket to source artifacts from. | 
**path** | **str** | The path to a folder where files and folders can be sourced. For a local filesystem this can be \&quot;C:\\Users\\me\\jobs\\test\&quot;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


