# Web UI with FirecREST

## Goal

Create a Flask web application that interfaces HPC services at CSCS using the FirecREST API.

Edit [`src/client.py`](https://github.com/eth-cscs/firecrest-training/blob/main/use-case-UI/src/client.py) and **replace the body of every function with the `_with_f7t` suffix** using [PyFirecREST](https://pyfirecrest.readthedocs.io/en/stable/tutorial_basic_v2.html) (recommended) or the [FirecREST API](https://eth-cscs.github.io/firecrest-v2/) directly.

## Prerequisites

- API key training credentials
- [Docker](https://docs.docker.com/get-started/docker-overview/) or [Podman](https://podman.io/get-started) installed

## Configuration

1. Copy and edit the configuration file:

    ```bash
    cd use-case-UI/src
    cp config.py.orig config.py
    ```

2. Fill in your credentials in `config.py`:

    ```python
    class DevConfig(Config):
        OIDC_CLIENT_ID = "<CLIENT_ID>"
        OIDC_CLIENT_SECRET = "<CLIENT_SECRET>"
        USER_GROUP = "<GROUP>"
        OIDC_AUTH_BASE_URL = "https://auth.cscs.ch"
        OIDC_AUTH_REALM = "firecrest-clients"
        FIRECREST_URL = "https://api.cscs.ch/hpc/firecrest/v2"
        SYSTEM_NAME = "daint"
        SYSTEM_RESERVATION = "<RESERVATION>"
    ```

!!! tip
    For **debugging**, leave the default values for `SBATCH_TEMPLATE`, `PROBLEM_INI_FILE`, `PROBLEM_MSH_FILE`, and `POST_TEMPLATE`.

    For a **real** test case, use:
    ```python
    PROBLEM_INI_FILE = 'inc-cylinder.ini'
    PROBLEM_MSH_FILE = 'inc-cylinder.msh'
    SBATCH_TEMPLATE = "cylinder.sh.tmpl"
    POST_TEMPLATE = "post_proc.sh.tmpl"
    ```
    This requires [Sarus](https://products.cscs.ch/sarus/).

## Build and Run

```bash
cd use-case-UI
make build
make run
```

!!! note
    The `Makefile` uses the `docker` command. To use `podman` instead, replace `docker` with `podman` in the `Makefile`.

The application runs at <http://localhost:9091>. Logs are written to `log/client.log`:

```bash
tail -f log/client.log
```

## Using the Application

1. Open <http://localhost:9091> in your browser.
2. Set the simulation parameters (number of steps, nodes, job name, etc.).
3. Click **Submit Jobs** to run the simulation. New jobs appear in the list and result files in the working directory.
4. Click **Start Postprocessing** to launch a post-processing job and view the animated GIF result.
