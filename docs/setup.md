# Setup

## Prerequisites

Participants must have:

- Laptop (preferably with Linux or macOS) with the following software installed:
    - `Python >= 3.8`
    - [Docker Compose](https://docs.docker.com/compose/) (or [Podman Compose](https://github.com/containers/podman-compose))
    - [Git](https://git-scm.com/install/)

- Knowledge of the Python programming language

- Smartphone with an Multi Factor Authentication (MFA) application installed (e.g. Google Authenticator):
    - Android: [Google Play](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2)
    - iOS: [App Store](https://apps.apple.com/us/app/google-authenticator/id388497605)

## Get Your API Keys

Participants will be guided by the instructors through these steps:

1. Receive course credentials to access a real HPC system at CSCS.
2. Open your web browser and navigate to <https://developer.cscs.ch> and set up MFA using your smartphone.
3. Once MFA is configured, you will be able to see the API `FirecREST-HPC v2` in the Developer Portal.
4. Click on **Applications** at the top of the page, then click on **DefaultApplication**.
5. On the left panel, click on **Subscriptions**. Click **:material-plus-circle-outline: Subscribe APIs** and subscribe to `FirecREST-HPC v2`, chosing `Platinum` **Subscription Status**.
6. On the left panel, click on **Production Keys**, then click **Generate Keys**.

After this, you will see the **Consumer Key** and **Consumer Secret** -- you will need them for the next steps.

!!! warning
    The **Consumer Key** and **Consumer Secret** are access keys to computational resources at CSCS. They are only meant for this course -- please do not share them. Keys and access to the systems will be deactivated after the tutorial.

## Test the Setup

1. On the **Production Keys** view, click **Generate Access Token**, then **Generate**, and finally **:fontawesome-solid-copy:** the access token.
2. Navigate to the [FirecREST-HPC API OpenAPI specification](https://api.cscs.ch/hpc/firecrest/v2/docs).
3. Click the **Authorize  :material-lock-open:** button on the right.
4. Under **HTTPBearer (http, Bearer)**, paste the access token and click **Authorize**.
5. Expand `GET /status/systems`, click **Try it out**, then **Execute**.

A successful setup returns a `200` response with a body similar to:

!!! example "JSON response for `GET /status/systems`"
    ```json
    {
      "systems": [
        (···)
        {
          "name": "daint",
          "ssh": {
            "host": "daint.alps.cscs.ch",
            "port": 22
          },
          "scheduler": {
            "type": "slurm",
            "version": "25.05.4"
          }
        }
      ]
    }
    ```

## What does the access token contain

You can check the content of the access token by using this Python script

??? example "Check access token content"
    ```python
    $ pip3 install jwt
    $ python3
    >>> import jwt, json
    >>> token="..." # paste your token
    >>> decoded_token = jwt.decode(token, options={"verify_signature": False})
    >>> print(json.dumps(decoded_token, indent=2))
    {
        "exp": 1777282411,
        (...)
        "iss": "https://auth.cscs.ch/auth/realms/firecrest-clients",
        (...)
        "preferred_username": "course_XXXXX",
        (...)
        "username": "course_XXXXX"
    }
    ```

!!! tip
    If you face issues setting up your API credentials, visit the [CSCS documentation](https://docs.cscs.ch/services/devportal/#getting-started) for clarification.

---

[:material-arrow-left: Back: Introduction](index.md){ .md-button } [Next step: Demo exercises :material-arrow-right:](demo.md){ .md-button .md-button--primary }
