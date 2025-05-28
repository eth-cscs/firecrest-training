## Using pyfirecrest to access the API

## How to use pyfirecrest

### Setting up the authentication

You can take care of the access token by yourself any way you want, or even better use a library to take care of this for you, depending on the **grant type** of your client. What pyFirecREST will need in the end is only a python object with the method `get_access_token()`, that when called will provide a valid access token.

Let’s say for example you have somehow obtained a long-lasting access token. The Authorization class you would need to make and give to Firecrest would look like this:

```python
class MyAuthorizationClass:
    def __init__(self):
        pass

    def get_access_token(self):
        return <TOKEN>
```

If you want to use the `Client Credentials` authorization grant, you can use the `ClientCredentialsAuth` class from pyFirecREST and setup the authorization object like this:

```python
import firecrest as f7t

keycloak = f7t.ClientCredentialsAuth(
    <client_id>, <client_secret>, <token_uri>
)
```

The `ClientCredentialsAuth` object will try to make the minimum requests that are necessary by reusing the access token while it is valid. More info on parameterizing it in the [docs](https://pyfirecrest.readthedocs.io/en/stable/authorization.html).


### Example of calls with pyfirecrest

Your starting point to use pyFirecREST will be the creation of a `FirecREST` object. This is simply a mini client that, in cooperation with the authorization object, will take care of the necessary requests that need to be made and handle the responses.

```python
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
client = f7t.Firecrest(
    firecrest_url=FIRECREST_URL,
    authorization=auth
)

# After this setup, you can go on and try some of the methods of the object


systems = client.all_systems()
print(systems)

## Exercise:

# 1. Get tha different parameters of our deployment
# 2. Get the username of the user
# 3. List the contents of a directory
# 4. Upload and download files
# 5. Submit a job
# 6. [Optional] Submit a job and poll until the it is finished
```


## The storage workflow

For larger files the user cannot directly upload/download a file to/from FirecREST.
A staging area will be used and the process will require multiple requests from the user.

## External download

### Steps of downloading a file:

The requested file will first have to be moved to the staging area.
This could take a long time in case of a large file.
When this process finishes, FirecREST will have created a dedicated space for this file and the user can download the file locally as many times as he wants.

For CSCS, if the user was doing the process manually they would need to do the following steps:

1. The user initiates the transfer by making a request to FirecREST with the remote file path and he will receive a Slurm job ID and a link from S3 to download the file.
2. The user would need to poll the status of the job until it has completed and make sure he checks in the log files that the first transfer finished successfully.
3. If step (2) finishes successfully then the user can use the S3 link to download the file and store it in his local system.

## Using pyfirecrest for downloading files

The client of pyfirecrest can handle the whole process or give more control to the user.

```python
client.download(
    system_name="daint",
    source_path="/capstor/scratch/cscs/<username>/7mb_file.obj",
    target_path="./local_file.txt",
    account="crs02",
    blocking=True
)
```

If you want to do it in steps, you can do each step from the functions of ExternalDownload object or use your own custom functions. Here is the workflow broken down in steps:

```python
download_obj = client.download(
    system_name="daint",
    source_path="/capstor/scratch/cscs/<username>/7mb_file.obj",
    target_path="./local_file.txt",
    account="crs02",
    blocking=False
)
# For small files the download will return `None` and the file will be available in the target directory
# For large files the download will return an object with information about the job
if download_obj:
    print(download_obj.transfer_info)
    # You can also set an optional timeout for the job
    download_obj.wait_for_transfer_job(timeout=None)
    # You can download the file multiple times in different localion by setting
    # the optional argument file_path. By default the original `target_path`
    # will be used
    download_obj.download_file_from_stage(file_path=None)
```

You can check all the details of the external download in the [docs](https://eth-cscs.github.io/firecrest-v2/user_guide/#downloading-large-files) with examples in different programming languages.

**[Optional]** You can also try to do this in the CLI of pyfirecrest.

## External upload with pyfirecrest

Similarly, the upload would require the user to upload the file to a staging area and FirecREST would launch a job that would take care of the transfer from the staging area to the remote filesystem.
For the uploading

### Steps of uploading a file:

If the user was doing the process manually they would need to do the following steps:

1. The user will make a request to FirecREST to start the upload and will get back a job ID and a link for the upload to the staging area.
2. The user will upload the file in chunks to the staging area.
This includes uploading each part individually and using the provided ETags to complete the upload.
3. Then the user will use the job ID that was provided to track the progress of the transfer between staging area and remote filesystem.
This includes checking that the status of the job was successful and there was no error in the process.

In code it would look like with `blocking=True`:

```python
client.upload(
    system_name="daint",
    local_file="/home/local_user/local_file_7mb.out",
    directory="/capstor/scratch/cscs/<username>",
    filename="uploaded_file.out",
    account="crs02",
    blocking=True
)
```

Or broken down in steps:

```python
upload_obj = client.upload(
    system_name="daint",
    local_file="/home/local_user/local_file_7mb.out",
    directory="/capstor/scratch/cscs/<username>",
    filename="uploaded_file.out",
    account="crs02",
    blocking=False
)
# For small files the upload will return `None` and the file will be directly
# available in the target directory.
# For large files the upload will return an object with information about the job.
if upload_obj:
    print(upload_obj.transfer_info)
    upload_obj.upload_file_to_stage()
    # You can also set an optional timeout for the job
    upload_obj.wait_for_transfer_job(timeout=None)
```

**[Optional]** You can also try to do this in the CLI of pyfirecrest.
