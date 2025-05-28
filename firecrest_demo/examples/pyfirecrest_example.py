import firecrest as f7t
import os


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

systems = client.all_systems()
print(systems)

## Exercise:

# 1. Get tha different parameters of our deployment
# 2. Get the username of the user
# 3. List the contents of a directory
# 4. Upload and download "small" files
# 5. Submit a job
# 6. [Optional] Submit a job and poll until the it is finished
