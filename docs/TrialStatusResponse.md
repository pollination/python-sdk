# TrialStatusResponse

Response showing whether an account has activated a trial for a specific product
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The ID of the account | 
**did_trial** | **bool** | Whether the account has previously activated a trial | 
**product** | **str** | The product for which trial status is being checked | 
**trial_activated_at** | **str** | The timestamp when the trial was first activated (if did_trial is true) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


