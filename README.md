# CUG-26 Tutorial “Programmatic Access to HPC resources with FirecREST API.”

**Date & Location:** April 27th, 2026, Nice (France)

## Agenda

|Time|Topic|
|--:|---|
|13:00 (30 mins) | [FirecREST introduction](#firecrest-introduction) |
|13:30 (60 mins) | [Hands-on: demo exercises](#hands-on-demo-exercises) (PyFirecREST and FirecREST CLI examples) in Alps infrastructure at CSCS. |
|*14:30 (30 mins)* | *Coffee break* |
|15:00 (60 mins) | [Hands-on: use cases](#hands-on-use-cases) (CI/CD pipeline, UI, or Workflow Manager) |
|16:00 (30 mins) | Demo: FirecREST in your laptop: containerized deployment|
|*16:30* | *Final remarks and end of tutorial* |

### Prerequisites

Participants must have:

- Laptop (preferebable with Linux or MacOS operative systems) with the following softwares installed
  - `Python >= 3.8`
  - [Docker Compose](https://docs.docker.com/compose/) (or [Podman Compose](https://github.com/containers/podman-compose))
  - [Git](https://git-scm.com/install/)
- Knowledge of Python programming language
- Smartphone with an Multi Factor Authentication (MFA) app installed. It is suggested Google Authenticator.
  - For Android phones: [Google Play](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=en_US)
  - For iOS phones: [App Store](https://apps.apple.com/us/app/google-authenticator/id388497605)

## FirecREST introduction

FirecREST is a RESTful API that enable users and developers to create workflows and services on the top of HPC computational and storage resources.

This API acts as a lightweight proxy that receives an standard HTTP request, translates into HPC business logic, and returns a standard web response to the users.

![f7t-proxy](./imgs/command_exec_simple.svg)

The idea behind FirecREST is to provide programming standards and documentation to the community to streamline automated access to HPC.

At the same time, for HPC sites FirecREST provides a single point of access for multiple workflows, thus facilitating user support.

### FirecREST OpenAPI specification

[FirecREST OpenAPI specification](https://eth-cscs.github.io/firecrest-v2/openapi)

> [!TIP]
> For more information on the details of FirecREST implementation, please visit the official [FirecREST Documentation](https://eth-cscs.github.io/firecrest-v2/)

## Hands on: demo exercises

Before starting with the hands on, we need to guide you to get your API keys.

### Setup

Participants will be guided by the instructors through these steps:

1. Participans will receive course credentials to access a real HPC system at CSCS.
2. Open your preferred web browser and navigate to https://developer.cscs.ch and setup the MFA using your smartphone.
3. Once MFA is configured, you will be able to see the API `FirecREST-HPC` in the Developer Portal.
4. Click on `Applications` on the top of the page, and then click on `DefaultApplication`
5. On the left panel, click on `Subscriptions`. Click on the `(+) Subscribe APIs` button and subscribe to `FirecREST-HPC v2` API by clicking on `Subscribe`
6. Again, on the left panel, click on `Production Keys` and then in `Generate Keys` button located in the bottom of the page.
After this is done, you will see the `Consumer Key` and `Consumer Secret`: you'll need them for the next steps of the tutorial.

  > [!WARNING]
  > The pair Consumer Key and Consumer Secret are access keys to computational resources at CSCS. Are only meant for this course, but please don't share them and keep them securely stored in your laptop.
  > Keys and access to the systems will be removed after the Tutorial.

### Test the setup

1. On the `Production Keys` view, click on `Generate Access Token`, then on `Generate`, and then copy the access token.
2. In your web browser, navigate to the [FirecREST-HPC API specification](https://api.cscs.ch/hpc/firecrest/v2/docs)
3. Once there, click on the `Authorize` button on the right.
4. On the section `HTTPBearer  (http, Bearer)` paste the access token and click on `Authorize` button below.
5. Expand `GET /status/systems` and click in `Try Out` and then in `Execute`

If the setup is correct you should see in the response the code `200` and in the `Response body` something like the following:

```json
{
  "systems": [
    {
      "name": "eiger",
      "ssh": {
        "host": "eiger.alps.cscs.ch",
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
        "version": "24.05.4",
        "apiUrl": null,
        "apiVersion": null,
```

### Now... who are you?

Participants have received courses accounts. The API keys (Consumer Key and Consumer Secret) are bounded to that user, then all the calls to FirecREST API will be on behalf of that user.

> [!NOTE]
> FirecREST doesn't use root execution or impersonation to submit jobs and commands on behalf of the users, all is done with user credentials which is more secure. See this [documentation](https://eth-cscs.github.io/firecrest-v2/setup/arch/systems/) for more information.


### Finally, hands on!

- Using a terminal, clone this repository in your wokstation, create a virtual environment and install PyFirecREST

    ```bash
    $ git clone https://github.com/eth-cscs/firecrest-training.git
    $ cd firecrest-training/demo-exercises
    $ python -m venv pyfirecrest-demo-env
    $ . ./pyfirecrest-demo-env/bin/activate
    $ (pyfirecrest-demo-env) pip install -r requirements.txt
    $ (pyfirecrest-demo-env) ls -la
    total 24
    drwxr-xr-x   6 user  group  192 Apr  3 18:26 .
    drwxr-xr-x  15 user  group  480 Apr  3 18:05 ..
    -rw-r--r--   1 user  group  365 Apr  3 18:26 .env.orig
    -rw-r--r--   1 user  group  835 Apr  3 18:05 pyfirecrest_example.py
    drwxr-xr-x   7 user  group  224 Apr  3 18:06 pyfirecrest-demo-env
    -rw-r--r--   1 user  group   27 Apr  3 18:07 requirements.txt
    ```

- Copy the file `.env.orig` to `.env` and modify in it the `FIRECREST_CLIENT_ID` and `FIRECREST_CLIENT_SECRET` with the values obtained in the [Setup section](#setup) and save it:

    ```bash
    $ (pyfirecrest-demo-env) cp .env.orig .env
    $ (pyfirecrest-demo-env) vi .env
    #!/bin/bash

    export FIRECREST_CLIENT_ID="<Customer-Key>" # <-- update here
    export FIRECREST_CLIENT_SECRET="<Customer-Secret>" # <-- update here
    export FIRECREST_URL="https://api.cscs.ch/hpc/firecrest/v2"
    export AUTH_TOKEN_URL="https://auth.cscs.ch/auth/realms/firecrest-clients/protocol/openid-connect/token"
    export BASE_DIRECTORY="/capstor/scratch/cscs"

    # Optional for the CLI
    export FIRECREST_API_VERSION="2.0.0"
    export FIRECREST_SYSTEM="daint"
    ```

- Load the environment variables

    ```bash
    $ (pyfirecrest-demo-env) source .env    
    ```

#### PyFirecREST Demo

> [!NOTE]
> PyFirecREST is a Python library that targets to facilitate the usage of FirecREST API for scripting and developing on the top of HPC.
> Use this [documentation](https://pyfirecrest.readthedocs.io/en/stable/tutorial_basic_v2.html) as reference for this tutorial.

With your favorite IDE or text editor, open the Python file [`pyfirecrest_example.py`](./demo-exercises/pyfirecrest_example.py) and start working!

#### FirecREST CLI demo

> [!TIP]
> By installing PyFirecREST, it comes along the FirecREST CLI, a commmand line interface to access HPC resources from a terminal.
> More information about FirecREST CLI in this [documentation](https://pyfirecrest.readthedocs.io/en/stable/tutorial_cli.html).

- Start by checking the command options:

    ```bash
    $ (pyfirecrest-demo-env) firecrest --help

    Usage: firecrest [OPTIONS] COMMAND [ARGS]...

    CLI for FirecREST
    Before running you need to setup the following variables or pass them as required options:
    - FIRECREST_URL: FirecREST URL
    (...)
    ```

- Check the command version:

    ```bash
    $ (pyfirecrest-demo-env) firecrest --version
    FirecREST CLI Version: 3.7.1
    ```

- List of systems you have available in this instance:

    ```bash
    (pyfirecrest-demo-env) firecrest systems
    [
        {
            "name": "eiger",
            "ssh": {
                "host": "eiger.alps.cscs.ch",
                "port": 22,
                "proxyHost": null,
                "proxyPort": null,
                "maxClients": 100,
    (...)
    ```

- Verify the username in the remote system:
    > [!TIP]
    > You can use `firecrest <subcommand> --help` for more information on how to use FirecREST CLI subcommands

    ```bash
    (pyfirecrest-demo-env) firecrest id --system daint
    uid=10001(course-user) gid=1999(cug-training) groups=1999(cug-training)
    ```

- List directories in a filesystem

    ```bash
    (pyfirecrest-demo-env) firecrest ls --system daint $BASE_DIRECTORY/course-user
    [
        {
            "name": "dir01",
            "type": "d",
            "linkTarget": null,
            "user": "course-user",
            "group": "cug-training",
            "permissions": "rwxr-x---+",
            "lastModified": "2026-04-11T09:28:18",
            "size": "4096"
        },
        {
            "name": "file02",
            "type": "-",
            "linkTarget": null,
            "user": "course-user",
    (...)
    ```

## Hands on: use cases

For this section, we present a series of use cases that show how using FirecREST streamlines the integration of different cloud-ready applications to interface HPC resources.

### CI Pipeline

- [use-case-CI-pipeline](use-case-CI-pipeline/README.md)

### UI

- [use-case-UI](use-case-UI/README.md)

### Airflow Operator

- [use-case-CI-airflow-operator](use-case-airflow-operator/README.md)

## Additional links

- Join the [FirecREST Community Slack channel](https://join.slack.com/t/firecrest-community/shared_invite/zt-340vthx9j-NLp8FwZe1i08WycWTT3M4w)
