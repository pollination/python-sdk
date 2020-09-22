# RecipeVersion

Resource Version  A Metadata object to distinguish a specific resource version within a repository index.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | 
**deprecated** | **bool** | Whether this recipe is deprecated | [optional] 
**description** | **str** | A description of what this recipe does | [optional] 
**digest** | **str** |  | 
**home** | **str** | The URL of this recipe&#39;s home page | [optional] 
**icon** | **str** | A URL to an SVG or PNG image to be used as an icon | [optional] 
**keywords** | **list[str]** | A list of keywords to search the recipe by | [optional] 
**license** | [**License**](License.md) | The license information. | [optional] 
**maintainers** | [**list[QueenbeeRecipeMetadataMaintainer]**](QueenbeeRecipeMetadataMaintainer.md) | A list of maintainers for the recipe | [optional] 
**name** | **str** | Recipe name. Make it descriptive and helpful ;) | 
**sources** | **list[str]** | A list of URLs to source code for this project | [optional] 
**tag** | **str** | The tag of the recipe | 
**url** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


