# SubscriptionUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**promotion_code** | **str** | A promotion code to apply a discount to the subscription | [optional] 
**to_add** | [**list[NewSubscriptionItem]**](NewSubscriptionItem.md) | The items to add | [optional] [default to []]
**to_delete** | [**list[SubscriptionItem]**](SubscriptionItem.md) | The items to delete | [optional] [default to []]
**to_subscribe** | [**Price**](Price.md) | The Pollination plan to subscribe to | [optional] 
**to_update** | [**list[SubscriptionItem]**](SubscriptionItem.md) | The items to update | [optional] [default to []]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


