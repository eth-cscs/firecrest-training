# FirecREST demo

## Requirements

- The requests examples will be shown in Python, so previous experience with the language can help you follow more easily.
- In order to follow the `pyfirecrest` part of the demo you will need `Python>=3.7` and to install pyfirecrest in your local env.

```bash
cd firecrest-demo
python -m venv pyfirecrest-demo-env
. pyfirecrest-demo-env/bin/activate
python -m pip install -r requirements.txt
```

Setup environment with credentials and the necessary URLs:

```bash
#!/bin/bash

export FIRECREST_CLIENT_ID=
export FIRECREST_CLIENT_SECRET=
export FIRECREST_URL=https://api.cscs.ch/hpc/firecrest/v2
export AUTH_TOKEN_URL=https://auth.cscs.ch/auth/realms/firecrest-clients/protocol/openid-connect/token

# Optional for the CLI
export FIRECREST_API_VERSION="2.0.0"
export FIRECREST_SYSTEM=daint
```

## Contents

1. [Basic usage of FirecREST through the API directly](part1.md)

2. [Using pyfirecrest to access the API](part2.md)

3. [More advanced use cases of pyfirecrest](part3.md)
