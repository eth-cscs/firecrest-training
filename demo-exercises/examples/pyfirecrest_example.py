import firecrest as f7t
import os
import json


# Get the values from the env or set them directly in your file
CLIENT_ID = os.environ.get("FIRECREST_CLIENT_ID")
CLIENT_SECRET = os.environ.get("FIRECREST_CLIENT_SECRET")
AUTH_TOKEN_URL = os.environ.get("AUTH_TOKEN_URL")
FIRECREST_URL = os.environ.get("FIRECREST_URL")

# Setup the auth object
auth = f7t.ClientCredentialsAuth(
    CLIENT_ID, CLIENT_SECRET, AUTH_TOKEN_URL
)

# Setup the client object
client = f7t.v2.Firecrest(
    firecrest_url=FIRECREST_URL,
    authorization=auth
)

systems = client.systems()
print(json.dumps(systems, indent=4))

# Exercise:

# 1. Get the username of the user
# 2. List the contents of a directory
# 3. Upload and download "small" files
# 4. Submit a job and get the job information
# 5. [Optional] Submit a job and poll until the it is finished
