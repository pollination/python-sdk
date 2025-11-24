# BillingInvoiceRequestCreate

DTO for creating an invoice request with customer billing information
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** |  | 
**additional_emails** | **List[str]** | Additional email addresses to send the invoice to | [optional] 
**address_line1** | **str** | First line of address | 
**address_line2** | **str** | Second line of address (optional) | [optional] 
**city** | **str** | City | 
**country** | [**CountryChoice**](CountryChoice.md) | Country (human-readable name) | 
**items** | [**List[BillingSubscriptionItem]**](BillingSubscriptionItem.md) |  | 
**postal_code** | **str** | Postal/Zip code | 
**region** | **str** | Region/State | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


