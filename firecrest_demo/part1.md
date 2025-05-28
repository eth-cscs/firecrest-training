# Basic usage of FirecREST through the API directly

## HTTP requests

[FirecREST API]((https://firecrest-api.cscs.ch/)) is based on REST principles: data resources are accessed via standard HTTP requests to an API endpoint.

Every request is made of:

1. the endpoint or requested URL
1. the method (one of GET, POST, PUT and DELETE depending on the appropriate action)
1. the headers (metadata necessary for the request)
1. the body (form data, files to be uploaded, etc)

The necessary information for every call is passed through query parameters, the headers and the body of the request.

Here is a quick overview of the methods:
| Method | Description                            |
| ------ | -------------------------------------- |
| GET    | Used for retrieving resources.         |
| POST   | Used for creating/updating resources.  |
| PUT    | Used for creating/updating resources.* |
| DELETE | Used for deleting resources.           |

> \* The difference between `POST` and `PUT` is that `PUT` requests are idempotent. That is, calling the same `PUT` request multiple times will always produce the same result. In contrast, calling a `POST` request repeatedly have side effects of creating the same resource multiple times.

Similar to the requests, the response of FirecREST will consist of:

1. a status code
1. the headers
1. the body in json form

Here is a quick overview of the status codes and their meaning.
| #   | Category      | Description |
| --- | ------------- | ----------- |
| 1xx | Informational | Communicates transfer protocol-level information. |
| 2xx | Success | Indicates that the client’s request was accepted successfully. |
| 3xx | Redirection | Indicates that the client must take some additional action in order to complete their request. |
| 4xx | Client Error | This category of error status codes points the finger at clients. |
| 5xx | Server Error | The server takes responsibility for these error status codes. |


## Obtain credentials

All the requests in the FirecREST API require authorization, in the form of an *access token*.
This token allows you to make requests on behalf of the authenticated user and is provided by Keycloak.
It has to be included in the header of all the API calls, but you should keep in mind that validation tokens usually have an expiration date and are short-lived.

In order to get an access token we need to make a `GET` request to `https://auth.cscs.ch/auth/realms/firecrest-clients/protocol/openid-connect/token`:

In python you can try it like this:

```python
import requests
import os
import json


CLIENT_ID = os.environ.get("FIRECREST_CLIENT_ID")
CLIENT_SECRET = os.environ.get("FIRECREST_CLIENT_SECRET")
AUTH_TOKEN_URL = os.environ.get("AUTH_TOKEN_URL")

data = {
    "grant_type": "client_credentials",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
}
response = requests.post(
    AUTH_TOKEN_URL,
    data=data,
)

print(f"Status code: {response.status_code}")
print(f"Headers:\n{json.dumps(dict(response.headers), indent=4)}")
print(f"JSON:\n{json.dumps(response.json(), indent=4)}")
```

If you have `curl` installed the request will look like this:
```bash
curl -s -X POST "${AUTH_TOKEN_URL}" \
     --data "grant_type=client_credentials" \
     --data "client_id=${FIRECREST_CLIENT_ID}" \
     --data "client_secret=${FIRECREST_CLIENT_SECRET}"
```

Example response:
```json
{
    "access_token":"ey...",
    "expires_in":300,
    "refresh_expires_in":0,
    "token_type":"Bearer",
    "not-before-policy":0,
    "scope":"firecrest profile email"
}
```

### [Optional] Inspecting the token with jwt

You can try inspecting an access token with

```python
decoded = jwt.decode(
    response.json()["access_token"],
    options={"verify_signature": False},
)
print("Decoded token:", json.dumps(decoded, indent=4))
```

## Making our first request to the API

After we obtain the token we can use this to make our first request to FirecREST:

To test the credentials we can make a request to [/status/systems](https://eth-cscs.github.io/firecrest-v2/openapi/#/status/get_systems_status_systems_get) endpoint with a `GET` operation to get more information about the systems that are available through this deployment fo FirecREST. The access token has to be included in the header.

```python

FIRECREST_URL = os.environ.get("FIRECREST_URL")

response = requests.get(
    url=f'{FIRECREST_URL}/status/systems',
    headers={'Authorization': f'Bearer {TOKEN}'}
)

print(json.dumps(response.json(), indent=4))
```

We should get some response like this:
```json
{
    "systems": [
        {
            "name": "eiger",
            ...
        {
            "name": "daint",
            "ssh": {
                "host": "daint.alps.cscs.ch",
                "port": 22,
                "proxyHost": null,
                "proxyPort": null,
                "maxClients": 100,
                "timeout": {
                    "connection": 5,
                    "login": 5,
                    "commandExecution": 5,
                    "idleTimeout": 60,
                    "keepAlive": 5
                }
            },
            "scheduler": {
                "type": "slurm",
                "version": "24.05.4",
                "apiUrl": null,
                "apiVersion": null,
                "timeout": 10
            },
            "servicesHealth": [
                {
                    "serviceType": "scheduler",
                    "lastChecked": "2025-05-27T10:38:56.581838Z",
                    "latency": 1.6268017292022705,
                    "healthy": true,
                    "message": null,
                    "nodes": {
                        "available": 14,
                        "total": 1020
                    }
                },
                {
                    "serviceType": "ssh",
                    "lastChecked": "2025-05-27T10:38:56.669635Z",
                    "latency": 1.7143478393554688,
                    "healthy": true,
                    "message": null
                },
                {
                    "serviceType": "filesystem",
                    "lastChecked": "2025-05-27T10:38:56.128036Z",
                    "latency": 1.1726181507110596,
                    "healthy": true,
                    "message": null,
                    "path": "/capstor/scratch/cscs"
                },
                {
                    "serviceType": "filesystem",
                    "lastChecked": "2025-05-27T10:38:55.343629Z",
                    "latency": 0.38807177543640137,
                    "healthy": true,
                    "message": null,
                    "path": "/users"
                },
                {
                    "serviceType": "filesystem",
                    "lastChecked": "2025-05-27T10:38:56.214138Z",
                    "latency": 1.2584686279296875,
                    "healthy": true,
                    "message": null,
                    "path": "/capstor/store/cscs"
                },
                {
                    "serviceType": "s3",
                    "lastChecked": "2025-05-27T10:38:55.078636Z",
                    "latency": 0.11069488525390625,
                    "healthy": true,
                    "message": null
                }
            ],
            "probing": {
                "interval": 300,
                "timeout": 10
            },
            "fileSystems": [
                {
                    "path": "/capstor/scratch/cscs",
                    "dataType": "scratch",
                    "defaultWorkDir": true
                },
                {
                    "path": "/users",
                    "dataType": "users",
                    "defaultWorkDir": false
                },
                {
                    "path": "/capstor/store/cscs",
                    "dataType": "store",
                    "defaultWorkDir": false
                }
            ],
            "datatransferJobsDirectives": [
                "#SBATCH --nodes=1",
                "#SBATCH --time=0-00:15:00",
                "#SBATCH --account={account}",
                "#SBATCH --partition=xfer"
            ]
        }
    ]
}
```

## Interracting with the scheduler

FirecREST offers three basic functionalities of the scheduler:
1. submit jobs on behalf of a user,
1. poll for the jobs of the user and
1. cancel jobs.

## The `compute` workflow

On FirecREST v2 may be interacting with Slurm through the [Slurm API](https://slurm.schedmd.com/rest.html) or by dispatching the relevant commands on the login node and parsing the results, eg. `sbatch`, `sacct`, `scancel` etc.


```python
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
```

And the output will be simply the job ID:

```json
{
    "jobId": 1090103
}
```