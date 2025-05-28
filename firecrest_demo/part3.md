# More advanced cases of pyfirecrest

## Enable logging in your python code

The simplest way to enable logging in your code would be to add this in the beginning of your file.
The v2 clients in pyFirecREST have all of their messages in `DEBUG` level.
If you want to avoid messages from other packages, you can do the following

```python
import logging

logger = logging.getLogger("firecrest")
logger.setLevel(logging.DEBUG)
ch = logging.FileHandler("firecrest_log.log")
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(message)s", datefmt="%H:%M:%S")
ch.setFormatter(formatter)
logger.addHandler(ch)
```


## How to catch and debug errors

The methods of the `Firecrest`, `ExternalUpload` and `ExternalDownload` objects will raise exceptions in case something goes wrong.
The same happens for their asynchronous counterparts.
When the error comes from the response of some request pyFirecREST will raise `FirecrestException`.
In these cases you can manually examine all the responses from the requests in order to get more information, when the message is not informative enough.
These responses are from the requests package of python and you can get all types of useful information from it, like the status code, the json response, the headers and more.
Here is an example of the code that will handle those failures.


```python
import firecrest as f7t


try:
    files = client.list_files("cluster", "/home/test_user")
    print(f"List of files: {files}")
except fc.FirecrestException as e:
    # You can just print the exception to get more information about the type of error,
    # for example an invalid or expired token.
    print(e)
    # Or you can manually examine the responses.
    print(e.responses[-1])
    print(e.responses[-1].status_code)
    print(e.responses[-1].body)
except Exception as e:
    # You might also get regular exceptions in some cases. For example when you are
    # trying to upload a file that doesn't exist in your local filesystem.
    print(f"A different exception was encountered: {e}")
```


## The asynchronous client of pyfirecrest

Asynchronous programming is a programming paradigm that allows tasks to run independently and asynchronously, meaning that one task doesn't have to wait for another to complete before starting its execution.
This is particularly useful in scenarios where tasks involve waiting for external resources, such as I/O operations or network requests.

In order to take advantage of the asynchronous client you may need to make many changes in your existing code, so the effort is worth it when you develop a code from the start or if you need to make a large number of requests.
You could submit hundreds or thousands of jobs, set a reasonable rate and pyFirecREST will handle it in the background without going over the request rate limit or overflowing the system.

If you are already familiar with the synchronous version of pyFirecREST, you will find it quite straightforward to adapt to the asynchronous paradigm.

We will be going through an example that will use the [asyncio](https://docs.python.org/3/library/asyncio.html) library.
First you will need to create an `AsyncFirecrest` object, instead of the simple `Firecrest` object.

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
client = f7t.v2.AsyncFirecrest(
    firecrest_url=FIRECREST_URL,
    authorization=auth
)
```

As you can see in the reference, the methods of AsyncFirecrest have the same name as the ones from the simple client, with the same arguments and types, but you will need to use the async/await syntax when you call them.

```python
# Getting all the systems
systems = await client.systems()
print(systems)

# Getting the files of a directory
files = await client.list_files("daint", "/scatch/scratch3000/test_user")
print(files)

# Submit a job
job = await client.submit(
    "daint",
    script_local_path="script.sh",
    working_directory="/scatch/scratch3000/test_user"
)
print(job)
```

Let's move to an example in [examples/asyncio_workflow.py](examples/asyncio_workflow.py).

## When to use the asynchronous client of pyfirecrest

### Benefits

1. The pyfirecrest client is IO-bound, it is mostly waiting for the results of the requests, which makes it an ideal candidate for asynchronous programming.
1. In future releases, we would like to allow the user to set their own rate limit of requests and optimise the number of requests the clients sends (for example merging polling requests for jobs from different asyncio tasks).
These features are already available for the v1 client.


### Drawbacks

1. You need to learn how to use asyncio or a similar library.
1. It can make the logic of you code more complicated sometimes.
1. It may require a significant restructuring of your code to take advantage of this client.
