# PublicAccountList

A list response from a pagination request
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | The current page the pagination request is on | 
**per_page** | **int** | The number of pages per pagination request | 
**next_page** | **int** | The next page, if this on is not the last | [optional] 
**page_count** | **int** | The total number of pages | 
**total_count** | **int** | The total number of resources matching the list request | 
**resources** | [**list[AccountPublic]**](AccountPublic.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


