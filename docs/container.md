# FirecREST in your laptop

## Introduction

The FirecREST repository contains the definition for a preconfigured containerized FirecREST environment which can deployed locally.

In addition to FirecREST, the environment includes a minimal set of networked containers representing a simple API-accessible supercomputing infrastructure: IAM service, S3 compatible storage, SSH certificate authority, batch compute cluster.

The environment is defined using the [Compose specification][compose-spec], and can be deployed locally using a Compose-compatible tool, such as [Docker Compose][docker-compose]

The containerized is useful for

* Understanding of how FirecREST interacts with other infrastructure components
* Exploring how FirecREST can be configured to interact with your own local supercomputing infrastructure
* Testing and developing user workflows with FirecREST

[compose-spec]: https://compose-spec.io/
[docker-compose]: https://docs.docker.com/compose/

## Learning objectives

This demo will provide attendees with an introduction to the containerized FirecREST environment, covering

* Bringing up the containerized environment on a locally (e.g. on a laptop)
* The structure of the environment and relationship between components
* Making API calls to FirecREST within the environment
* Interacting with other components of the environment

After the session, attendees will be equipped to deploy the environment for themselves and explore the capabilities of FirecREST in self-contained environment.

## 0. Setup

The host on which the containerised environment is deployed requires the following:

1. OCI container engine (**[Podman][podman]**, [Docker][docker], [nerdctl][nerdctl])
1. Compose compatible orchestrator (**[Docker Compose][docker-compose]**, [Podman Compose][podman-compose], [nerdctl][nerdctl])
1. Tool for making HTTP requests (**[curl][curl]**, [httpie][httpie], Python [requests][python-requests])
1. Tool for parsing JSON (**[jq][jq]**, [yq][yq], Python standard library [json][python-json])
1. **[Git][git]** version control system

In this demo, the tools in **bold** above are used, but the instructions should generalise to other combinations.

!!! note "`podman compose`"
    This demo uses the Podman container engine and Docker Compose orchestrator using the [`podman compose`][podman-compose-command-man-page] command. Docker Compose is the reference implementation of the [Compose spec][compose-spec] and widely supported.

    Confusingly, running the `podman compose` command from does not imply using the [Podman Compose][podman-compose] orchestrator. The `podman compose` command will default to using Docker Compose as orchestrator if available on the system (but can also use Podman Compose as orchestrator).

[podman]: https://podman.io/
[docker]: https://www.docker.com/
[nerdctl]: https://github.com/containerd/nerdctl
[podman-compose]: https://github.com/containers/podman-compose
[podman-compose-command-man-page]: https://docs.podman.io/en/latest/markdown/podman-compose.1.html
[curl]: https://curl.se/
[httpie]: https://httpie.io/
[python-requests]: https://docs.python-requests.org/
[jq]: https://jqlang.org/
[yq]: https://github.com/mikefarah/yq
[python-json]: https://docs.python.org/3/library/json.html
[git]: https://git-scm.com/

## 1. Deploy the environment

Clone the [firecrest-v2 GitHub repository][firecrest-v2-github] and check out release v2.5.0

```shell
git clone https://github.com/eth-cscs/firecrest-v2.git
cd firecrest-v2
git switch --detach 2.5.0
```

Bring up the Compose project

```shell
podman compose -f docker-compose.yml up
```

This will pull and build the necessary container images and build the containerised environment as defined in [`docker-compose.yml`][docker-compose-firecrest-v2-github].
The first time this is done, it may take a few minutes to completely bring up the environment.

Confirm that the Compose project is running

```shell-session
$ podman compose ls
NAME                STATUS              CONFIG FILES
firecrest-v2        running(5)          /path/to/firecrest-v2/docker-compose.yml
```
[firecrest-v2-github]: https://github.com/eth-cscs/firecrest-v2
[docker-compose-firecrest-v2-github]: https://github.com/eth-cscs/firecrest-v2/blob/2.5.0/docker-compose.yml

## 2. Explore the environment

## 3. Call the FirecREST API

## 4. Interact with other components
