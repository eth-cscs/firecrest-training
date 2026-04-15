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

## 1. Deploy the environment

## 2. Explore the environment

## 3. Call the FirecREST API

## 4. Interact with other components
