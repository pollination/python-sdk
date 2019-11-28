# Template

An argo workflow template object
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**template** | **str** |  | [optional] 
**arguments** | [**QueenbeeArgoSchemaArgumentsArguments**](QueenbeeArgoSchemaArgumentsArguments.md) |  | [optional] 
**template_ref** | [**TemplateRef**](TemplateRef.md) |  | [optional] 
**inputs** | [**QueenbeeArgoSchemaArgumentsArguments**](QueenbeeArgoSchemaArgumentsArguments.md) |  | [optional] 
**outputs** | [**Outputs**](Outputs.md) |  | [optional] 
**daemon** | **bool** |  | [optional] 
**steps** | [**list[Step]**](Step.md) |  | [optional] 
**container** | [**TaskContainer**](TaskContainer.md) |  | [optional] 
**dag** | [**DAG**](DAG.md) |  | [optional] 
**suspend** | [**Suspend**](Suspend.md) |  | [optional] 
**active_deadline_seconds** | **int** |  | [optional] 
**retry_strategy** | [**RetryStrategy**](RetryStrategy.md) |  | [optional] 
**parallelism** | **int** |  | [optional] 
**service_account_name** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


