# Web UI with Client Credentials

## Introduction

The objective of this exercise is to create a Web UI application on Python (Flask) to interface HCP services at CSCS using FirecREST API.

To accomplish the task, you must edit the file [src/client.py](./src/client.py) and **replace the content of the functions with the suffix `_with_f7t`** using [pyFirecREST](https://pyfirecrest.readthedocs.io/en/stable/tutorial_basic_v2.html) (suggested) or [FirecREST API](https://eth-cscs.github.io/firecrest-v2/).

Each function provides the type of response and parameters requested to fulfill the activity.

Follow the Configuration guide to adapt your client credentials to the app.

## Prerequisites

- API keys training credentials.
- [Docker](https://docs.docker.com/get-started/docker-overview/) or [Podman](https://podman.io/get-started) installed in your workstation.
- Knowledge of Python.

## Configuration

1. Copy the configuration file (`src/config.py.orig`) and rename it as `src/config.py`

    Open a terminal in your laptop and clone the repository, move to the `use-case-UI/src` directory:

    ```bash
    $ git clone https://github.cscs.ch/eth-cscs/firecrest-training
    $ cd use-case-UI/src
    $ cp config.py.orig config.py
    ```

2. Replace the following values with the specifics for this tutorial

    ```python
    ...
    class DevConfig(Config):
        OIDC_CLIENT_ID = "<CLIENT_ID>" # obtained from instructors
        OIDC_CLIENT_SECRET = "<CLIENT_SECRET>" # obtained from instructors
        USER_GROUP="<GROUP>" # obtained from instructors
        OIDC_AUTH_BASE_URL = "https://auth.cscs.ch"
        OIDC_AUTH_REALM = "firecrest-clients"
        FIRECREST_URL="https://api.cscs.ch/hpc/firecrest/v2"
        SYSTEM_NAME="daint"
        SYSTEM_RESERVATION="<RESERVATION>" # obtained from instructors
        (...)
    ```

- For **debugging** purposes, leave the default values in the variables `SBATCH_TEMPLATE`, `PROBLEM_INI_FILE`, `PROBLEM_MSH_FILE`, and `POST_TEMPLATE`.
- For **testing a "real"** case, use:

    ```python
    ...
    class DevConfig(Config):
        (...)
        PROBLEM_INI_FILE = 'inc-cylinder.ini'
        PROBLEM_MSH_FILE = 'inc-cylinder.msh'
        SBATCH_TEMPLATE = "cylinder.sh.tmpl"
        POST_TEMPLATE = "post_proc.sh.tmpl"
    ```

> [!TIP]
> In this case, you would need to use [Sarus](https://products.cscs.ch/sarus/)

## Build and run

Build app and run

```bash
$ # return to the use-Case-UI directory
$ cd ..
$ make build
$ make run
```

> [!Note]
> The [Makefile](./Makefile) file uses `docker` command to build and execute the container. If you wish to use `podman`, replacing the `docker` command by `podman` in `Makefile` should be enough.

You can check the logs in `log/client.log`

```bash
$ tail -f log/client.log
```

## How does it work for the user

- Open a browser, and enter [http://localhost:9091](http://localhost:9091)
- Set the parameters of the problem (number of steps, nodes, job name, etc)
- Click `Submit Jobs` to run the simulation (you should see the jobs created in the list, and new result files in `Working directory`)
- Click on `Start Postprocessing` to launch a job and after completion see the animated gif result image
