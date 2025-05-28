import asyncio
import firecrest
import logging
import os
from firecrest import FirecrestException


# Setup variables for the client
client_id = os.environ.get("FIRECREST_CLIENT_ID")
client_secret = os.environ.get("FIRECREST_CLIENT_SECRET")
token_uri = os.environ.get("AUTH_TOKEN_URL")
firecrest_url = os.environ.get("FIRECREST_URL")

machine = "daint"
local_script_path = "script.sh"
username = "<username>"  # Replace with your username or set it as an environment variable

# This is simply setup for logging, you can ignore it
logger = logging.getLogger("simple_example")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(message)s", datefmt="%H:%M:%S")
ch.setFormatter(formatter)
logger.addHandler(ch)


# This is a helper function to check if the job is still running
def slurm_state_completed(state):
    completion_states = {
        'BOOT_FAIL',
        'CANCELLED',
        'COMPLETED',
        'DEADLINE',
        'FAILED',
        'NODE_FAIL',
        'OUT_OF_MEMORY',
        'PREEMPTED',
        'TIMEOUT',
    }
    if state:
        # Make sure all the steps include one of the completion states
        return all(
            any(cs in s for cs in completion_states) for s in state.split(',')
        )

    return False


async def workflow(client, i):
    logger.info(f"{i}: Starting workflow")
    job = await client.submit(
        machine,
        working_dir=f"/capstor/scratch/cscs/{username}",
        script_local_path=local_script_path,
    )
    logger.info(f"{i}: Submitted job with jobid: {job['jobId']}")
    await asyncio.sleep(5)
    job_id = job["jobId"]
    while True:
        job = await client.job_info(machine, job_id)
        state = job[0]["status"]["state"]
        if isinstance(state, list):
            state = ",".join(state)

        if slurm_state_completed(state):
            logger.info(
                f"Job {job_id} is completed with state: {state}."
            )
            break

        logger.info(
            f"Job {job_id} state is {state}. Will sleep for 30 seconds."
        )
        await asyncio.sleep(30)

    job_metadata = (await client.job_metadata(machine, job_id))[0]
    output_path = job_metadata["standardOutput"]
    logger.info(f"{i}: Job output path: {output_path}")

    output = await client.view(machine, output_path)
    logger.info(f"{i}: job output: {output}")


async def main():
    auth = firecrest.ClientCredentialsAuth(client_id, client_secret, token_uri)
    client = firecrest.v2.AsyncFirecrest(firecrest_url, authorization=auth)

    workflows = [workflow(client, i) for i in range(5)]
    await asyncio.gather(*workflows)


asyncio.run(main())
