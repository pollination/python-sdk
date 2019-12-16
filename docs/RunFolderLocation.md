# RunFolderLocation

Run Folder Location  This is the folder a workflow will use as it's root path when running a simulation. When run on a local machine (using queenbee-luigi for example) the root path should be a path on the user's machine. If running on the Pollination platform the `root` value is ignored and the data is persisted to a run specific folder in S3 within the Pollination backend.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** | Name is a unique identifier for this particular Artifact Location | 
**root** | **str** | For a local filesystem this can be \&quot;C:\\Users\\me\\simulations\\test\&quot;.            Will be ignored when running on the Pollination platform. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


