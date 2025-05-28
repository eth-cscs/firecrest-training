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

client.upload(
    system_name="daint",
    local_file="/home/local_user/local_file_7mb.out",
    directory="/capstor/scratch/cscs/<username>",
    filename="uploaded_file.out",
    account="crs02",
    blocking=True
)

# Uncomment the following lines to test the individual steps of the upload process

# upload_obj = client.upload(
#     system_name="daint",
#     local_file="/home/local_user/local_file_7mb.out",
#     directory="/capstor/scratch/cscs/<username>",
#     filename="uploaded_file.out",
#     account="crs02",
#     blocking=False
# )
# # For small files the upload will return `None` and the file will be directly
# # available in the target directory.
# # For large files the upload will return an object with information about the job.
# if upload_obj:
#     print(upload_obj.transfer_info)
#     upload_obj.upload_file_to_stage()
#     # You can also set an optional timeout for the job
#     upload_obj.wait_for_transfer_job(timeout=None)
