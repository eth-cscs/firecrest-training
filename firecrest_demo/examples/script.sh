#!/bin/bash -l

#SBATCH --job-name=firecrest_job_test
#SBATCH --time=5:00
#SBATCH --nodes=2
#SBATCH -Cgpu

#SBATCH --reservation=firecrest
#SBATCH -Acrs02

# Very silly script
srun hostname
sleep 100
srun echo 'Bye'
