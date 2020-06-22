# OperatorVersion

A version of an Operator
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Operator name. This name should be unique among all the operators in your workflow. | 
**tag** | **str** | The tag of the operator | 
**app_version** | **str** | The version of the app binary backing the operator (CLI tool or container) | [optional] 
**keywords** | **list[str]** | A list of keywords to search the operator by | [optional] 
**maintainers** | [**list[QueenbeeOperatorMetadataMaintainer]**](QueenbeeOperatorMetadataMaintainer.md) | A list of maintainers for the operator | [optional] 
**home** | **str** | The URL of this operator home page | [optional] 
**sources** | **list[str]** | A list of URLs to source code for this operator | [optional] 
**icon** | **str** | A URL to an SVG or PNG image to be used as an icon | [optional] 
**deprecated** | **bool** | Whether this operator is deprecated | [optional] 
**description** | **str** | A description of what this operator does | [optional] 
**url** | **str** |  | 
**created** | **datetime** |  | 
**digest** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


