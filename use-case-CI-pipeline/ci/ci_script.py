#
#  Copyright (c) 2025, ETH Zurich. All rights reserved.
#
#  Please, refer to the LICENSE file in the root directory.
#  SPDX-License-Identifier: BSD-3-Clause
#
import firecrest as fc
import os
import time
import argparse
import utilities as util

from firecrest import FirecrestException


final_slurm_states = {
    "BOOT_FAIL",
    "CANCELLED",
    "COMPLETED",
    "DEADLINE",
    "FAILED",
    "NODE_FAIL",
    "OUT_OF_MEMORY",
    "PREEMPTED",
    "TIMEOUT",
}


def select_dict_by_name(name, list_of_dicts, select_key="name"):
    res = None
    for d in list_of_dicts:
        if d[select_key] == name:
            res = d
            break

    return res


def check_mandatory_env_var(env_var):
    r = os.environ.get(env_var)
    if not r:
        print(f"Mandatory environment variable `{env_var}` is not set")
        exit(1)

    return r


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--system", default=os.environ.get("FIRECREST_SYSTEM"), help="choose system to run"
    )
    parser.add_argument("--branch", default="main", help="branch to be tested")
    parser.add_argument("--account", default="csstaff", help="branch to be tested")
    parser.add_argument("--repo", help="repository to be tested")

    args = parser.parse_args()
    system_name = args.system
    ref = args.branch
    print(f"Will try to run the ci in system {system_name} on branch {ref}")

    # Setup variables of the client
    CLIENT_ID = check_mandatory_env_var("FIRECREST_CLIENT_ID")
    CLIENT_SECRET = check_mandatory_env_var("FIRECREST_CLIENT_SECRET")
    FIRECREST_URL = check_mandatory_env_var("FIRECREST_URL")
    AUTH_TOKEN_URL = check_mandatory_env_var("AUTH_TOKEN_URL")
    SYSTEM_WORKING_DIR = check_mandatory_env_var("SYSTEM_WORKING_DIR")

    keycloak = # Set up the OIDC authentication
    client = # Set up the FirecREST client

    all_systems = client. # Get the list of all available systems and print their names

    script_content = util.create_batch_script(
        repo=args.repo,
        num_nodes=2,
        account=args.account,
        custom_modules=["cray", "cray-python"],
        branch=ref,
    )

    system_state = select_dict_by_name(system_name, all_systems)
    if not system_state:
        print(f"System `{system_name}` is not available")
        exit(1)

    print(f'System info: {system_state}')

    # scheduler information
    scheduler_health_info = select_dict_by_name(
        "scheduler",
        system_state["servicesHealth"],
        "serviceType"
    )

    if scheduler_health_info["healthy"]:
        # Submit a job to the system with the provided script in `script_content` and
        # SYSTEM_WORKING_DIR is the directory where the job will run
        job = client. # TODO
        print(f"Submitted job: {job['jobId']}")
        while True:
            # Check the status of the job every 10 seconds and break
            # when the job is in a final state

        stdout_file_path = os.path.join(SYSTEM_WORKING_DIR, 'job.out')
        stderr_file_path = os.path.join(SYSTEM_WORKING_DIR, 'job.err')

        print(f"\nSTDOUT in {stdout_file_path}")
        stdout_content = # Check the last 1000 lines of the job's stdout file
        print(stdout_content)

        print(f"\nSTDERR in {stderr_file_path}")
        stderr_content = # Check the last 1000 lines of the job's stderr file
        print(stderr_content)

        # Some sanity checks:
        # Check if the job is finished correctly (the state should be `COMPLETED`)

        util.check_output(stdout_content)

    else:
        print(
            f"Scheduler of system `{system_name}` is not healthy"
        )
        exit(1)


if __name__ == "__main__":
    main()
