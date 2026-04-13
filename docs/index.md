# CUG-26 Tutorial: Programmatic Access to HPC resources with FirecREST API

[Entry in the offical program](https://ssl.linklings.net/conferences/cug/cug2026_program/views/by_date.html#tut101)

**Date & Time:** April 27th, 2026 at 13h

???- quote "Abstract"
    > *The use of APIs in High Performance Computing (HPC) aims to simplify access and automate processes in traditional HPC settings. In this context, CSCS has developed FirecREST, a RESTful web interface that has proven to be efficient, streamlining the usage of CI/CD pipelines, UX/UI applications, workflow managers, and interactive computing across various HPC environments. This has been demonstrated on Alps, a Cray HPE EX machine featuring heterogeneous hardware including AMD and Nvidia CPUs and GPUs, as well as Grace-Hopper superchips. Moreover, FirecREST is being deployed in other HPE-powered Centres, such as Bristol Centre for Supercomputing (BriCS-UK); and the CSC - IT Center for Science, in Finland, that operates LUMI the HPE Cray EX supercomputer owned by the EuroHPC and hosted by a consortium of 11 European countries. The objectives of this tutorial are to facilitate automation of users’ workflows on HPC using a standard programming interface, and promote the usage of APIs on HPE centres in search of a common interface to run workflows across facilities. For further references, the FirecREST team has delivered training on FirecREST in 2023 and 2025 for CSCS users and the general public.*

## Agenda

| Time | Topic |
|-----:|-------|
| 13:00 (30 mins) | [FirecREST introduction](#firecrest-introduction) |
| 13:30 (60 mins) | [Hands-on: demo exercises](demo.md) (PyFirecREST and FirecREST CLI examples) in Alps infrastructure at CSCS |
| *14:30 (30 mins)* | *Coffee break* |
| 15:00 (60 mins) | [Hands-on: use cases](use-cases/index.md) (CI/CD pipeline, UI, or Workflow Manager) |
| 16:00 (30 mins) | [Demo: FirecREST in your laptop](container.md): containerized deployment |
| *16:30* | *Final remarks and end of tutorial* |

## FirecREST Introduction

FirecREST is a RESTful API that enables users and developers to create workflows and services on top of HPC computational and storage resources.

This API acts as a lightweight proxy that receives a standard HTTP request, translates it into HPC business logic, and returns a standard web response to the users.

![f7t-proxy](imgs/command_exec_simple.svg)

The idea behind FirecREST is to provide programming standards and documentation to the community to streamline automated access to HPC.

At the same time, for HPC sites FirecREST provides a single point of access for multiple workflows, thus facilitating user support.

### FirecREST OpenAPI Specification

[FirecREST OpenAPI specification](https://eth-cscs.github.io/firecrest-v2/openapi)

!!! tip
    For more information on the details of FirecREST implementation, please visit the official [FirecREST Documentation](https://eth-cscs.github.io/firecrest-v2/).

## Additional Links

- [FirecREST Community Slack](https://join.slack.com/t/firecrest-community/shared_invite/zt-340vthx9j-NLp8FwZe1i08WycWTT3M4w)
- [FirecREST v2 Documentation](https://eth-cscs.github.io/firecrest-v2/)
- [PyFirecREST Documentation](https://pyfirecrest.readthedocs.io)

---

[Next step: Setup :material-arrow-right:](setup.md){ .md-button .md-button--primary }
