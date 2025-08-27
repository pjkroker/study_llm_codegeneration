#!/usr/bin/env bash
set -euo pipefail

# ----------------------------
# Config
# ----------------------------
PROJECT_DIR="OpenCodeInterpreter"
CONDA_ENV="opencode"
PYTHON_VERSION="3.10"
MODEL_NAME="${1:-m-a-p/OpenCodeInterpreter-DS-6.7B}"


# ----------------------------
# 1. Clone repository
# ----------------------------
if [ ! -d "$PROJECT_DIR" ]; then
  git clone https://github.com/OpenCodeInterpreter/OpenCodeInterpreter.git
fi
#cd "$PROJECT_DIR"
#cd demo

# ----------------------------
# 2. Create conda environment
# ----------------------------
if ! conda env list | grep -q "$CONDA_ENV"; then
  conda create -y -n "$CONDA_ENV" python=$PYTHON_VERSION
fi

# Activate environment
# shellcheck disable=SC1091
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "$CONDA_ENV"

# ----------------------------
# 4. Install Python dependencies
# ----------------------------
echo "Schritt 4"
pip install -r ../10_open_code_interpreter/req2.txt


# TODO check tmp environemt variable

#TODO pin to gpu

# TODO set hf api key



