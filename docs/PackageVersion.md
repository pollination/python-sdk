# PackageVersion

Package Version  A MetaData object to distinguish a specific package version within a repository index.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | An optional dictionary to add annotations to inputs. These annotations will be used by the client side libraries. | [optional] 
**app_version** | **str** | The version of the application code underlying the manifest | [optional] 
**created** | **datetime** |  | 
**deprecated** | **bool** | Whether this package is deprecated | [optional] 
**description** | **str** | A description of what this package does | [optional] 
**digest** | **str** |  | 
**home** | **str** | The URL of this package&#39;s home page | [optional] 
**icon** | **str** | A URL to an SVG or PNG image to be used as an icon | [optional] 
**keywords** | **list[str]** | A list of keywords to search the package by | [optional] 
**kind** | **str** | The type of Queenbee package (ie: recipe or plugin) | [optional] [default to '']
**license** | [**License**](License.md) | The license information. | [optional] 
**maintainers** | [**list[Maintainer]**](Maintainer.md) | A list of maintainers for the package | [optional] 
**manifest** | [**AnyOfRecipePlugin**](AnyOfRecipePlugin.md) | The package Recipe or Plugin manifest | [optional] 
**name** | **str** | Package name. Make it descriptive and helpful ;) | 
**readme** | **str** | The README file string for this package | [optional] 
**slug** | **str** | A slug of the repository name and the package name. | [optional] 
**sources** | **list[str]** | A list of URLs to source code for this project | [optional] 
**tag** | **str** | The tag of the package | 
**type** | **str** |  | [optional] [readonly] [default to 'PackageVersion']
**url** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


