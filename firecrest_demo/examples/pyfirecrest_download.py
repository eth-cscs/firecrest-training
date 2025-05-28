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

client.download(
    system_name="daint",
    source_path="/capstor/scratch/cscs/<username>/7mb_file.obj",
    target_path="./local_file.txt",
    account="crs02",
    blocking=True
)

# Uncomment the following lines to test the individual steps of the download process

# download_obj = client.download(
#     system_name="daint",
#     source_path="/capstor/scratch/cscs/<username>/7mb_file.obj",
#     target_path="./local_file.txt",
#     account="crs02",
#     blocking=False
# )
# # For small files the download will return `None` and the file will be available in the target directory
# # For large files the download will return an object with information about the job
# if download_obj:
#     print(download_obj.transfer_info)
#     # You can also set an optional timeout for the job
#     download_obj.wait_for_transfer_job(timeout=None)
#     # You can download the file multiple times in different localion by setting
#     # the optional argument file_path. By default the original `target_path`
#     # will be used
#     download_obj.download_file_from_stage(file_path=None)
