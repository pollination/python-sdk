# FunctionArrayOutput

Function array output.  This output loads the content from a JSON file which must be a JSON Array.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**description** | **str** | Optional description for output. | [optional] 
**items_type** | [**ItemType**](ItemType.md) | Type of items in this array. All the items in an array must be from the same type. | [optional] 
**name** | **str** | Output name. | 
**path** | **str** | Path to the output file relative to where the function command is executed. | 
**type** | **str** |  | [optional] [readonly] [default to 'FunctionArrayOutput']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


