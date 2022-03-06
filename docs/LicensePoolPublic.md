# LicensePoolPublic

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessors** | [**list[Accessor]**](Accessor.md) | The entities that can access the license though the pool | [optional] [default to []]
**allowed_activations** | **int** | The number of allowable activations for this license | 
**description** | **str** | The description of the pool | [optional] 
**id** | **str** | The ID of the pool | 
**license_id** | **str** | The ID of the license to which the pool provides access | 
**owner** | [**AccountPublic**](AccountPublic.md) | The account that owns the license | 
**permissions** | [**UserPermission**](UserPermission.md) |  | 
**product** | **str** | The pollination product to which this pool provides access | 
**total_activations** | **int** | The number of current activations for this license | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


