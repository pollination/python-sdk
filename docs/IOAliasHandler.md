# IOAliasHandler

Input and output alias handler object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**function** | **str** | Name of the function. The input value will be passed to this function as the first argument. | 
**language** | **str** | Declare the language (e.g. python, csharp, etc.). This option allows the recipe to be flexible on handling different programming languages. | 
**module** | **str** | Target module or namespace to load the alias function. | 
**type** | **str** |  | [optional] [readonly] [default to 'IOAliasHandler']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


