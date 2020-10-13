#!/bin/bash
#SBATCH --nodes=1
#SBATCH --cpus-per-task=8
#SBATCH --gres=gpu:4
#SBATCH --mem=128G
#SBATCH --partition=gpu
#SBATCH --time=05:00:00
#SBATCH --output=%x-%J.out
#SBATCH --error=%x-%J.err
#SBATCH --job-name=liNER

module load ml-gpu/20200210
module load python/3.8.0-k7w5uj4
#module load ml-gpu/20190715

cd AutoNER
ml-gpu python3 -m pip install tqdm --user

# sh autoner_train_chem.sh
sh autoner_test_chem.sh
