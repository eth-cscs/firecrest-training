# Demo Exercises

## HPC Environment

For this tutorial, use the following parameters:

| Parameter | Value | Hint |
|-----------|-------|------|
| System | `daint` | |
| Scheduler account | `ws-iram-cug2026-tutorial` | always use `#SBATCH --account=ws-iram-cug2026-tutorial` |
| Scheduler reservation | `cug26` | use in `#SBATCH --reservation=cug26` to always get resources |
| Filesystem | `/capstor/scratch/cscs/<username>` |  |

!!! warning
    When submitting a job always use `#SBATCH --account=ws-iram-cug2026-tutorial` otherwise the scheduler job will fail

!!! tip
    FirecREST does not use root execution or impersonation. All calls are made with your user credentials. See the [architecture documentation](https://eth-cscs.github.io/firecrest-v2/setup/arch/systems/) for more information.

## Local Environment Setup

Clone the repository, create a virtual environment, and install PyFirecREST:
!!! example "Setup virtual environment"

    ```bash
    $ git clone https://github.com/eth-cscs/firecrest-training.git
    $ cd firecrest-training/demo-exercises
    $ python -m venv pyfirecrest-demo-env
    $ source pyfirecrest-demo-env/bin/activate
    $ (pyfirecrest-demo-env) pip install -r requirements.txt
    ```

Copy the environment template and fill in your credentials:

!!! example ""
    ```bash
    $ (pyfirecrest-demo-env) cp .env.orig .env
    $ (pyfirecrest-demo-env) vim .env
    ```

Edit `.env` with your **Consumer Key** and **Consumer Secret**

!!! example "Update the `.env` file with the credentials obtained in [Setup](./setup.md#get-your-api-keys)"
    ```bash
    export FIRECREST_CLIENT_ID="<Consumer-Key>" # <-- UPDATE
    export FIRECREST_CLIENT_SECRET="<Consumer-Secret>" # <-- UPDATE
    export FIRECREST_URL="https://api.cscs.ch/hpc/firecrest/v2"
    export AUTH_TOKEN_URL="https://auth.cscs.ch/auth/realms/firecrest-clients/protocol/openid-connect/token"
    export BASE_DIRECTORY="/capstor/scratch/cscs"

    # Optional, for the CLI
    export FIRECREST_API_VERSION="2.0.0"
    export FIRECREST_SYSTEM="daint"
    ```

Load the environment variables:

!!! example "Activate the environment variables"
    ```bash
    (pyfirecrest-demo-env) source .env
    ```

## PyFirecREST Demo

!!! note
    PyFirecREST is a Python library that facilitates the usage of the FirecREST API for scripting and developing on top of HPC. Use the [PyFirecREST documentation](https://pyfirecrest.readthedocs.io/en/stable/tutorial_basic_v2.html) as reference.

Open [`demo-exercises/pyfirecrest_example.py`](https://github.com/eth-cscs/firecrest-training/blob/main/demo-exercises/pyfirecrest_example.py) and work through the exercises.

??? example "`pyfirecrest_example.py`"
    ```python
    import firecrest
    import os
    import json


    # Get the values from the env or set them directly in your file
    CLIENT_ID = os.environ.get("FIRECREST_CLIENT_ID")
    CLIENT_SECRET = os.environ.get("FIRECREST_CLIENT_SECRET")
    AUTH_TOKEN_URL = os.environ.get("AUTH_TOKEN_URL")
    FIRECREST_URL = os.environ.get("FIRECREST_URL")

    # Setup the auth object
    auth = firecrest.ClientCredentialsAuth(
        CLIENT_ID, CLIENT_SECRET, AUTH_TOKEN_URL
    )

    # Setup the client object
    client = firecrest.v2.Firecrest(
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

    ```

!!! note
    To execute this script use `python pyfirecrest_example.py`

## FirecREST CLI Demo

!!! tip
    By installing PyFirecREST, it comes along the FirecREST CLI, a command line interface to access HPC resources from a terminal.
    More information about FirecREST CLI in this [documentation](https://pyfirecrest.readthedocs.io/en/stable/tutorial_cli.html).

### Start by checking the command options

???+ example "Check command options"

    ```bash
    $ (pyfirecrest-demo-env) firecrest --help

    Usage: firecrest [OPTIONS] COMMAND [ARGS]...

    CLI for FirecREST
    Before running you need to setup the following variables or pass them as required options:
    - FIRECREST_URL: FirecREST URL
    (...)
    ```

### Check the command version

??? example "Check command version"

    ```bash
    $ (pyfirecrest-demo-env) firecrest --version
    FirecREST CLI Version: 3.7.1
    ```

### List of systems available in this instance

??? example "List systems"

    ```bash
    $ (pyfirecrest-demo-env) firecrest systems
    [
        {
            "name": "eiger",
            (···)
        },
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
                "connectionMode": "ssh",
                "version": "25.05.4",
                "apiUrl": null,
                "apiVersion": null,
                "timeout": 10
            },
    (···)
    ```

### Verify the username on the remote system

??? example "Verify username"

    ```bash
    $ (pyfirecrest-demo-env) firecrest id --system daint
    uid=99999(course_99999) gid=1209(ws-iram-cug2026-tutorial) groups=1209(ws-iram-cug2026-tutorial)
    ```

### List directories in a filesystem

??? example "List directories"

    ```bash
    $ (pyfirecrest-demo-env) firecrest ls --system daint $BASE_DIRECTORY/course_99999
    [
        {
            "name": "dir01",
            "type": "d",
            "linkTarget": null,
            "user": "course_99999",
            "group": "ws-iram-cug2026-tutorial",
            "permissions": "rwxr-x---+",
            "lastModified": "2026-04-11T09:28:18",
            "size": "4096"
        },
        {
            "name": "file02",
            "type": "-",
            "linkTarget": null,
            "user": "course_99999",
        (...)
    ```

### Submit a job in the scheduler

??? example "Submit job"
    ```bash
    $ (pyfirecrest-demo-env) firecrest submit --system daint \
    --working-dir $BASE_DIRECTORY/course_99999 ./examples/script.sh
    {
        "jobId": "1234567"
    }
    ```

!!! tip
    Use `firecrest <subcommand> --help` for details on any subcommand.

---

[:material-arrow-left: Back: Setup](./setup.md){ .md-button } [Next step: Demo use cases :material-arrow-right:](./use-cases/index.md){ .md-button .md-button--primary }
