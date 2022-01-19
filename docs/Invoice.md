# Invoice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_advance** | **bool** |  | [optional] 
**collection_method** | **str** |  | 
**currency** | **str** |  | 
**customer** | **str** |  | 
**description** | **str** |  | [optional] 
**discount** | [**Discount**](Discount.md) |  | [optional] 
**hosted_invoice_url** | **str** |  | [optional] 
**id** | **str** |  | 
**lines** | [**LineItemList**](LineItemList.md) |  | 
**metadata** | **object** |  | [optional] 
**period_end** | **datetime** |  | 
**period_start** | **datetime** |  | 
**status** | [**InvoiceStatus**](InvoiceStatus.md) |  | 
**status_transitions** | [**InvoiceStatusTransitions**](InvoiceStatusTransitions.md) |  | 
**subscription** | **str** |  | [optional] 
**subtotal** | **int** |  | 
**tax** | **int** |  | [optional] 
**total** | **int** |  | 
**total_discount_amounts** | [**list[DiscountAmount]**](DiscountAmount.md) |  | [optional] [default to []]
**total_tax_amounts** | [**list[TaxAmount]**](TaxAmount.md) |  | [optional] [default to []]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


