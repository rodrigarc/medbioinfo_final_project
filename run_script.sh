#!/bin/bash

CONDA_BASE=$(conda info --base)
conda env create --file=environment.yml
source ${CONDA_BASE}/etc/profile.d/conda.sh
conda activate medbioinfo_rodrigo
make