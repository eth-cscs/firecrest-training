#!/bin/bash -l

#SBATCH --job-name=firecrest_job_test
#SBATCH --time=5:00
#SBATCH --nodes=1
#SBATCH --reservation=cug26
#SBATCH --account=ws-iram-cug2026-tutorial

# Very silly script
srun hostname
sleep 100
srun echo 'Bye'
