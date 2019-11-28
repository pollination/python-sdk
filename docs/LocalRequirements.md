# LocalRequirements

Operator requirements for local runs.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'operator']
**platform** | **list[str]** | List of valid platforms that operator can execute the commands. | [optional] [default to ["linux","windows","mac"]]
**language** | [**list[Language]**](Language.md) | List of required programming languages to execute the commands with an operator. | [optional] 
**app** | [**list[App]**](App.md) | List of applications that are required for operator to execute the commands locally. You must follow pip requirement specifiers: https://pip.pypa.io/en/stable/reference/pip_install/#requirement-specifiers For instance use rtrace&gt;&#x3D;5.2 for radiance 5.2 or newer. Command will run  rtrace --version and tries to parse version from command. | [optional] 
**pip** | [**list[Package]**](Package.md) | List of Python packages that are required for operator to execute the commands locally. You must follow pip requirement specifiers: https://pip.pypa.io/en/stable/reference/pip_install/#requirement-specifiers | [optional] 
**npm** | [**list[Package]**](Package.md) | List of npm packages that are required for operator to execute the commands locally. You must follow npm install requirements: https://docs.npmjs.com/cli/install#synopsis | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


