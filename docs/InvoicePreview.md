# InvoicePreview

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_advance** | **bool** |  | [optional] 
**collection_method** | **str** |  | 
**currency** | **str** |  | 
**customer** | **str** |  | 
**description** | **str** |  | [optional] 
**hosted_invoice_url** | **str** |  | [optional] 
**lines** | [**LineItemList**](LineItemList.md) |  | 
**payment_method** | [**CardPublic**](CardPublic.md) | The payment method that will be billed when this invoice is due. | [optional] 
**period_end** | **datetime** |  | 
**period_start** | **datetime** |  | 
**status** | [**InvoiceStatus**](InvoiceStatus.md) |  | 
**status_transitions** | [**InvoiceStatusTransitions**](InvoiceStatusTransitions.md) |  | 
**subscription** | **str** |  | [optional] 
**total** | **int** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


