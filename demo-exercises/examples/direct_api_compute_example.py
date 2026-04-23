import requests
import os
import json


CLIENT_ID = os.environ.get("FIRECREST_CLIENT_ID")
CLIENT_SECRET = os.environ.get("FIRECREST_CLIENT_SECRET")
AUTH_TOKEN_URL = os.environ.get("AUTH_TOKEN_URL")
FIRECREST_URL = os.environ.get("FIRECREST_URL")

data = {
    "grant_type": "client_credentials",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
}
response = requests.post(
    AUTH_TOKEN_URL,
    data=data,
)

TOKEN = response.json()["access_token"]

# Submit a job
local_path = 'script.sh'
system_name = 'daint'

with open(local_path, 'r') as f:
    data = {
        'job': {
            'script': f.read(),
            'working_directory': '/scratch/snx3000/eirinik',
        }
    }

job = requests.post(
    url=f'{FIRECREST_URL}/compute/{system_name}/jobs',
    headers={'Authorization': f'Bearer {TOKEN}'},
    data=json.dumps(data)
)

print(json.dumps(job.json(), indent=4))

# As an excercise try to poll for a job and cancel it
