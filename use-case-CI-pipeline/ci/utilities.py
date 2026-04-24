#
#  Copyright (c) 2025, ETH Zurich. All rights reserved.
#
#  Please, refer to the LICENSE file in the root directory.
#  SPDX-License-Identifier: BSD-3-Clause
#


def create_batch_script(
    repo, num_nodes=1, account=None, branch="main", constraint=None, reservation=None
):
    script = f"""#!/bin/bash -l
#SBATCH --job-name="ci_job"
#SBATCH --output=job.out
#SBATCH --error=job.err
#SBATCH --time=0:10:0
#SBATCH --nodes={num_nodes}
"""

    if constraint:
        script += f"#SBATCH --constraint={constraint}\n"

    if account:
        script += f"#SBATCH --account={account}\n"

    if reservation:
        script += f"#SBATCH --reservation={reservation}\n"

    script += f"""

# Clone command will fail if the directory already exists
# Remove this first if you are using the same working directory
# every time
# rm -rf firecrest-ci
git clone -b {branch} {repo} firecrest-ci
cd firecrest-ci/use-case-CI-pipeline

unset PYTHONPATH
export PYTHONUSERBASE="$(dirname "$(dirname "$(which python3)")")"
python3 -m venv --system-site-packages testing-venv

source ./testing-venv/bin/activate

python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

python3 --version

srun python3 -m timeit --setup='import mylib; import numpy as np; \
    p = np.arange(1000); q = np.arange(1000) + 2' \
    'mylib.simple_numpy_dist(p, q)'
"""

    return script


def check_output(file_content):
    assert "loops, best of" in file_content
