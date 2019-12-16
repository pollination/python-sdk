# pollination-sdk

Pollination Cloud API

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements

Python 2.7 and 3.4+

## Installation & Usage

### pip install

The default way to install `pollination-sdk` is through PyPi as follows:

```sh
pip install pollination-sdk
```

If you need a specific branch you can install straight from the repository using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import pollination_sdk 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import pollination_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint

configuration = pollination_sdk.Configuration()

# Retrieve a temporary Acces Token (JWT) using your API key id and secret
API_KEY_ID = 'some-long-id'
API_KEY_SECRET = 'some-long-secret'

auth = pollination_sdk.AuthenticationApi()
api_token = pollination_sdk.Token(
  id=API_KEY_ID,
  secret=API_KEY_SECRET
)

auth_response = auth.login(token)

# Configure Bearer authorization: JWT
configuration.access_token = auth_response.access_token

# Defining host is optional and default to https://api.pollination.cloud
configuration.host = "https://api.pollination.cloud"
# Create an instance of the API class
api_instance = pollination_sdk.WorkflowsApi(pollination_sdk.ApiClient(configuration))
id = 'id_example' # str | 
workflow = pollination_sdk.Workflow() # Workflow | 

try:
    # Update a Workflow
    api_response = api_instance.update(id, workflow)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowsApi->update: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.pollination.cloud*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ArtifactsApi* | [**create**](https://github.com/pollination/python-sdk/blob/master/docs/ArtifactsApi.md#create) | **POST** /artifacts | Get an Artifact upload link.
*ArtifactsApi* | [**list**](https://github.com/pollination/python-sdk/blob/master/docs/ArtifactsApi.md#list) | **GET** /artifacts | List artifacts in user folder
*AuthenticationApi* | [**create_api_token**](https://github.com/pollination/python-sdk/blob/master/docs/AuthenticationApi.md#create_api_token) | **POST** /auth/api-token | Create an API Token
*AuthenticationApi* | [**delete_api_token**](https://github.com/pollination/python-sdk/blob/master/docs/AuthenticationApi.md#delete_api_token) | **DELETE** /auth/api-token | Delete an API Token
*AuthenticationApi* | [**get_api_token**](https://github.com/pollination/python-sdk/blob/master/docs/AuthenticationApi.md#get_api_token) | **GET** /auth/api-token | Get your API Token ID
*AuthenticationApi* | [**login**](https://github.com/pollination/python-sdk/blob/master/docs/AuthenticationApi.md#login) | **POST** /auth/login | Login with API Token
*AuthenticationApi* | [**rotate_api_token_secret**](https://github.com/pollination/python-sdk/blob/master/docs/AuthenticationApi.md#rotate_api_token_secret) | **PUT** /auth/api-token | Rotate an API token secret
*ModelApi* | [**create**](https://github.com/pollination/python-sdk/blob/master/docs/ModelApi.md#create) | **POST** /models | Create a Model
*ModelApi* | [**create_faces**](https://github.com/pollination/python-sdk/blob/master/docs/ModelApi.md#create_faces) | **POST** /models/{id}/faces | Create Model Faces
*ModelApi* | [**delete**](https://github.com/pollination/python-sdk/blob/master/docs/ModelApi.md#delete) | **DELETE** /models/{id} | Delete a Model
*ModelApi* | [**get**](https://github.com/pollination/python-sdk/blob/master/docs/ModelApi.md#get) | **GET** /models/{id} | Get a Model
*ModelApi* | [**get_faces**](https://github.com/pollination/python-sdk/blob/master/docs/ModelApi.md#get_faces) | **GET** /models/{id}/faces | Get Model Faces
*ModelApi* | [**list**](https://github.com/pollination/python-sdk/blob/master/docs/ModelApi.md#list) | **GET** /models | Get Models
*SensorGridApi* | [**create**](https://github.com/pollination/python-sdk/blob/master/docs/SensorGridApi.md#create) | **POST** /sensor-grids | Create a Sensor Grid
*SensorGridApi* | [**delete**](https://github.com/pollination/python-sdk/blob/master/docs/SensorGridApi.md#delete) | **DELETE** /sensor-grids/{gid} | Delete a Sensor Grid
*SensorGridApi* | [**get**](https://github.com/pollination/python-sdk/blob/master/docs/SensorGridApi.md#get) | **GET** /sensor-grids/{gid} | Get a Sensor Grid
*SensorGridApi* | [**get_sensors**](https://github.com/pollination/python-sdk/blob/master/docs/SensorGridApi.md#get_sensors) | **GET** /sensor-grids/{gid}/sensors | Get Sensors
*SensorGridApi* | [**list**](https://github.com/pollination/python-sdk/blob/master/docs/SensorGridApi.md#list) | **GET** /sensor-grids | Get Sensor Grids
*SimulationsApi* | [**create**](https://github.com/pollination/python-sdk/blob/master/docs/SimulationsApi.md#create) | **POST** /simulations | Schedule a simulation
*SimulationsApi* | [**get**](https://github.com/pollination/python-sdk/blob/master/docs/SimulationsApi.md#get) | **GET** /simulations/{id} | Get a Simulation
*SimulationsApi* | [**get_simulation_inputs**](https://github.com/pollination/python-sdk/blob/master/docs/SimulationsApi.md#get_simulation_inputs) | **GET** /simulations/{id}/inputs | Get simulation inputs
*SimulationsApi* | [**get_simulation_logs**](https://github.com/pollination/python-sdk/blob/master/docs/SimulationsApi.md#get_simulation_logs) | **GET** /simulations/{id}/logs | Get simulation logs
*SimulationsApi* | [**get_simulation_outputs**](https://github.com/pollination/python-sdk/blob/master/docs/SimulationsApi.md#get_simulation_outputs) | **GET** /simulations/{id}/outputs | Get simulation outputs
*SimulationsApi* | [**get_task_logs**](https://github.com/pollination/python-sdk/blob/master/docs/SimulationsApi.md#get_task_logs) | **GET** /simulations/{id}/task/{task_id}/logs | Get a simulation task&#39;s logs
*SimulationsApi* | [**list**](https://github.com/pollination/python-sdk/blob/master/docs/SimulationsApi.md#list) | **GET** /simulations | List simulations
*SimulationsApi* | [**resubmit**](https://github.com/pollination/python-sdk/blob/master/docs/SimulationsApi.md#resubmit) | **POST** /simulations/{id}/re-submit | re-submit a simulation
*SimulationsApi* | [**resume**](https://github.com/pollination/python-sdk/blob/master/docs/SimulationsApi.md#resume) | **PUT** /simulations/{id}/resume | resume a simulation
*SimulationsApi* | [**suspend**](https://github.com/pollination/python-sdk/blob/master/docs/SimulationsApi.md#suspend) | **PUT** /simulations/{id}/suspend | Suspend a simulation
*WorkflowsApi* | [**create**](https://github.com/pollination/python-sdk/blob/master/docs/WorkflowsApi.md#create) | **POST** /workflows | Create a Workflow
*WorkflowsApi* | [**delete**](https://github.com/pollination/python-sdk/blob/master/docs/WorkflowsApi.md#delete) | **DELETE** /workflows/{id} | Delete a Workflow
*WorkflowsApi* | [**get**](https://github.com/pollination/python-sdk/blob/master/docs/WorkflowsApi.md#get) | **GET** /workflows/{id} | Get a Workflow
*WorkflowsApi* | [**list**](https://github.com/pollination/python-sdk/blob/master/docs/WorkflowsApi.md#list) | **GET** /workflows | List Workflows
*WorkflowsApi* | [**update**](https://github.com/pollination/python-sdk/blob/master/docs/WorkflowsApi.md#update) | **PUT** /workflows/{id} | Update a Workflow


## Documentation For Models

 - [Accepted](https://github.com/pollination/python-sdk/blob/master/docs/Accepted.md)
 - [Aperture](https://github.com/pollination/python-sdk/blob/master/docs/Aperture.md)
 - [App](https://github.com/pollination/python-sdk/blob/master/docs/App.md)
 - [ArgoArchiveLocation](https://github.com/pollination/python-sdk/blob/master/docs/ArgoArchiveLocation.md)
 - [ArgoArguments](https://github.com/pollination/python-sdk/blob/master/docs/ArgoArguments.md)
 - [ArgoArtifact](https://github.com/pollination/python-sdk/blob/master/docs/ArgoArtifact.md)
 - [ArgoDAG](https://github.com/pollination/python-sdk/blob/master/docs/ArgoDAG.md)
 - [ArgoDAGTask](https://github.com/pollination/python-sdk/blob/master/docs/ArgoDAGTask.md)
 - [ArgoNodeStatus](https://github.com/pollination/python-sdk/blob/master/docs/ArgoNodeStatus.md)
 - [ArgoOutputs](https://github.com/pollination/python-sdk/blob/master/docs/ArgoOutputs.md)
 - [ArgoParameter](https://github.com/pollination/python-sdk/blob/master/docs/ArgoParameter.md)
 - [ArgoRetryStrategy](https://github.com/pollination/python-sdk/blob/master/docs/ArgoRetryStrategy.md)
 - [ArgoS3Location](https://github.com/pollination/python-sdk/blob/master/docs/ArgoS3Location.md)
 - [ArgoStatus](https://github.com/pollination/python-sdk/blob/master/docs/ArgoStatus.md)
 - [ArgoSuspend](https://github.com/pollination/python-sdk/blob/master/docs/ArgoSuspend.md)
 - [ArgoTaskContainer](https://github.com/pollination/python-sdk/blob/master/docs/ArgoTaskContainer.md)
 - [ArgoTemplate](https://github.com/pollination/python-sdk/blob/master/docs/ArgoTemplate.md)
 - [ArgoTemplateRef](https://github.com/pollination/python-sdk/blob/master/docs/ArgoTemplateRef.md)
 - [Arguments](https://github.com/pollination/python-sdk/blob/master/docs/Arguments.md)
 - [Artifact](https://github.com/pollination/python-sdk/blob/master/docs/Artifact.md)
 - [Auth0TokenResponse](https://github.com/pollination/python-sdk/blob/master/docs/Auth0TokenResponse.md)
 - [CreatedContent](https://github.com/pollination/python-sdk/blob/master/docs/CreatedContent.md)
 - [DAG](https://github.com/pollination/python-sdk/blob/master/docs/DAG.md)
 - [DAGTask](https://github.com/pollination/python-sdk/blob/master/docs/DAGTask.md)
 - [Face](https://github.com/pollination/python-sdk/blob/master/docs/Face.md)
 - [FileMeta](https://github.com/pollination/python-sdk/blob/master/docs/FileMeta.md)
 - [Function](https://github.com/pollination/python-sdk/blob/master/docs/Function.md)
 - [Glass](https://github.com/pollination/python-sdk/blob/master/docs/Glass.md)
 - [HTTPLocation](https://github.com/pollination/python-sdk/blob/master/docs/HTTPLocation.md)
 - [HTTPValidationError](https://github.com/pollination/python-sdk/blob/master/docs/HTTPValidationError.md)
 - [InputFolderLocation](https://github.com/pollination/python-sdk/blob/master/docs/InputFolderLocation.md)
 - [KeyRequest](https://github.com/pollination/python-sdk/blob/master/docs/KeyRequest.md)
 - [KeySecret](https://github.com/pollination/python-sdk/blob/master/docs/KeySecret.md)
 - [Language](https://github.com/pollination/python-sdk/blob/master/docs/Language.md)
 - [LocalRequirements](https://github.com/pollination/python-sdk/blob/master/docs/LocalRequirements.md)
 - [LoopControl](https://github.com/pollination/python-sdk/blob/master/docs/LoopControl.md)
 - [Model](https://github.com/pollination/python-sdk/blob/master/docs/Model.md)
 - [Model1](https://github.com/pollination/python-sdk/blob/master/docs/Model1.md)
 - [ModelOut](https://github.com/pollination/python-sdk/blob/master/docs/ModelOut.md)
 - [NewToken](https://github.com/pollination/python-sdk/blob/master/docs/NewToken.md)
 - [Opaque](https://github.com/pollination/python-sdk/blob/master/docs/Opaque.md)
 - [Operator](https://github.com/pollination/python-sdk/blob/master/docs/Operator.md)
 - [Package](https://github.com/pollination/python-sdk/blob/master/docs/Package.md)
 - [Parameter](https://github.com/pollination/python-sdk/blob/master/docs/Parameter.md)
 - [Parent](https://github.com/pollination/python-sdk/blob/master/docs/Parent.md)
 - [Plastic](https://github.com/pollination/python-sdk/blob/master/docs/Plastic.md)
 - [ReferenceWorkflow](https://github.com/pollination/python-sdk/blob/master/docs/ReferenceWorkflow.md)
 - [RunFolderLocation](https://github.com/pollination/python-sdk/blob/master/docs/RunFolderLocation.md)
 - [S3Location](https://github.com/pollination/python-sdk/blob/master/docs/S3Location.md)
 - [S3UploadRequest](https://github.com/pollination/python-sdk/blob/master/docs/S3UploadRequest.md)
 - [Sensor](https://github.com/pollination/python-sdk/blob/master/docs/Sensor.md)
 - [SensorGridIn](https://github.com/pollination/python-sdk/blob/master/docs/SensorGridIn.md)
 - [SensorGridIn1](https://github.com/pollination/python-sdk/blob/master/docs/SensorGridIn1.md)
 - [SensorGridOut](https://github.com/pollination/python-sdk/blob/master/docs/SensorGridOut.md)
 - [ShadeFace](https://github.com/pollination/python-sdk/blob/master/docs/ShadeFace.md)
 - [SubmitSimulation](https://github.com/pollination/python-sdk/blob/master/docs/SubmitSimulation.md)
 - [Token](https://github.com/pollination/python-sdk/blob/master/docs/Token.md)
 - [Transparent](https://github.com/pollination/python-sdk/blob/master/docs/Transparent.md)
 - [ValidationError](https://github.com/pollination/python-sdk/blob/master/docs/ValidationError.md)
 - [Vertex](https://github.com/pollination/python-sdk/blob/master/docs/Vertex.md)
 - [Workflow](https://github.com/pollination/python-sdk/blob/master/docs/Workflow.md)
 - [WorkflowListItem](https://github.com/pollination/python-sdk/blob/master/docs/WorkflowListItem.md)


## Documentation For Authorization


## JWT

- **Type**: Bearer authentication


## Author




