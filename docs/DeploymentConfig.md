# DeploymentConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_limit** | **int** | The maximum number of CPU cores that can be used by the application. | [optional] [default to 1]
**entrypoint_file** | **str** | The Streamlit python file to use as an entrypoint to the app | [optional] [default to 'app.py']
**login_required** | **bool** | Whether the application requires login. | [optional] [default to True]
**memory_limit** | **int** | The maximum amount of memory that can be used by the application. | [optional] [default to 2000]
**scale_to_zero** | **bool** | A boolean toggle to scale deployments down to zero replicas when not used. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


