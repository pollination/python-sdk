from __future__ import print_function
import time
import pollination_sdk
from pollination_sdk.rest import ApiException
from pprint import pprint
import json
configuration = pollination_sdk.Configuration()

# Retrieve a temporary Acces Token (JWT) using your API key id and secret
API_KEY_ID = 'f15be412fe6f41dc01440f2363a13fed'
API_KEY_SECRET = 'y3yCOW92PPAHuLNrCDnZ'

auth = pollination_sdk.AuthenticationApi()
api_token = pollination_sdk.Token(
  id=API_KEY_ID,
  secret=API_KEY_SECRET
)

auth_response = auth.login(api_token)

# Configure Bearer authorization: JWT
configuration.access_token = auth_response.access_token

# Defining host is optional and default to https://api.pollination.cloud
configuration.host = "https://api.pollination.cloud"
# Create an instance of the API class
# api_instance = pollination_sdk.SimulationsApi(pollination_sdk.ApiClient(configuration))
# submit_simulation = pollination_sdk.SubmitSimulation(
#     workflow='dd02dcb1-b07d-448e-ab1d-c0e1d5600f4b',
#     inputs={}
# ) # SubmitSimulation | 

# try:
#     # Schedule a simulation
#     api_response = api_instance.create(submit_simulation)
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling SimulationsApi->create: %s\n" % e)

api_instance = pollination_sdk.SimulationsApi(pollination_sdk.ApiClient(configuration))
# id = '87909cd6-b814-4fad-8f28-fdb8adfde97b' # str | 

# try:
#     # Get a Simulation
#     api_response = api_instance.get(id)
#     pprint(api_response)
#     with open('dump.json', 'w') as f:
#       json.dump(
#         api_instance.api_client.sanitize_for_serialization(api_response.to_dict()), f, indent=2)
# except ApiException as e:
#     print("Exception when calling SimulationsApi->get: %s\n" % e)

# id = '87909cd6-b814-4fad-8f28-fdb8adfde97b' # str | 
# task_id = '87909cd6-b814-4fad-8f28-fdb8adfde97b-1335860711' # str | 

# try:
#     # Get a simulation task's logs
#     api_response = api_instance.get_task_logs(id, task_id)
#     # pprint(api_response)
#     print(api_response.logs)
# except ApiException as e:
#     print("Exception when calling SimulationsApi->get_task_logs: %s\n" % e)

id = '87909cd6-b814-4fad-8f28-fdb8adfde97b' # str | 
template_name = 'list-message' # str | Name of a simulation task template.

try:
    # Get simulation logs
    api_response = api_instance.get_simulation_logs(id, template_name)
    # pprint(api_response)
    for item in api_response:
      print(item.logs)
except ApiException as e:
    print("Exception when calling SimulationsApi->get_simulation_logs: %s\n" % e)
