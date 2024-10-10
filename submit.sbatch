#!/bin/bash
#SBATCH -w cn-m-1
#SBATCH -p soundbendor
#SBATCH -A soundbendor
#SBATCH --job-name=compost_bin_cv
#SBATCH --time=0
#SBATCH --gres=gpu:1 
#SBATCH --export=ALL

source /nfs/guille/eecs_research/soundbendor/beerya/miniconda/bin/activate
source activate /nfs/guille/eecs_research/soundbendor/beerya/miniconda/envs/food-waste-inference-api
./startup.sh
