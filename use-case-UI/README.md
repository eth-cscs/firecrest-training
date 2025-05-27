# Web UI with Client Credentials

## Introduction

Create a Web UI application on Python (Flask) to interface HCP services at CSCS

In this directory, the file [src/client.py](./src/client.py) provides a number of functions to be completed with [pyFirecREST](https://pyfirecrest.readthedocs.io/en/stable/tutorial_basic_v2.html) or [FirecREST API](https://eth-cscs.github.io/firecrest-v2/). This functions are the ones that has the `_with_f7t` suffix.

Follow the Configuration guide to adapt your client credentials to the app.

## Prerequisites

- CSCS training credentials (provided by the trainers)
- Create your FirecREST API client using the [CSCS Developer Portal](https://developer.cscs.ch)  
- [Docker](https://docs.docker.com/get-started/docker-overview/) installed
- Knowledge of Python

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
        OIDC_CLIENT_ID = "<CLIENT_ID>" # obtained from Developer Portal
        OIDC_CLIENT_SECRET = "<CLIENT_SECRET>" # obtained from Developer Portal
        USER_GROUP="crs02"
        OIDC_AUTH_BASE_URL = "https://auth.cscs.ch"
        OIDC_AUTH_REALM = "firecrest-clients"
        FIRECREST_URL="https://api.cscs.ch/hpc/firecrest/v2"
        SYSTEM_NAME="daint"
        SYSTEM_RESERVATION="firecrest"
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
make build
make run
```

You can check the logs in `log/client.log`

```bash
$ tail -f log/client.log
```

## How does it work for the user

- Open a browser, and enter [http://localhost:9091](http://localhost:9091)
- Set the parameters of the problem (number of steps, nodes, job name, etc)
- Click `Submit Jobs` to run the simulation (you should see the jobs created in the list, and new result files in `Working directory`)
- Click on `Start Postprocessing` to launch a job and after completion see the animated gif result image
