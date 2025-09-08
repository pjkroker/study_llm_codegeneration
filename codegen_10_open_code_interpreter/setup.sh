#!/usr/bin/env bash
set -euo pipefail

# ----------------------------
# Resolve the directory this script lives in (absolute)
# ----------------------------
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd -P)"
cd "$SCRIPT_DIR"

# ----------------------------
# Config
# ----------------------------
PROJECT_DIR="OpenCodeInterpreter"
CONDA_ENV="opencode"
PYTHON_VERSION="3.10"
MODEL_NAME="${1:-m-a-p/OpenCodeInterpreter-DS-6.7B}"

echo "set up script for OpenCodeGenerator"
# ----------------------------
echo "1. Clone repository"
# ----------------------------
if [ ! -d "$PROJECT_DIR" ]; then
  echo "no directoy $PROJECT_DIR found, cloning from github"
  git clone https://github.com/OpenCodeInterpreter/OpenCodeInterpreter.git
else
  echo "$PROJECT_DIR already exists"
fi

# ----------------------------
echo "2. Create conda environment"
# ----------------------------
if ! conda env list | grep -q "$CONDA_ENV"; then
  echo "no conda env $CONDA_ENV found, creating one"
  conda create -y -n "$CONDA_ENV" python=$PYTHON_VERSION
else
  echo "$CONDA_ENV already exists"
fi

# ----------------------------
echo "3. Activate conda environment $CONDA_ENV"
# ----------------------------
# shellcheck disable=SC1091
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "$CONDA_ENV"

# ----------------------------
echo "4. Install Python dependencies (modified to solve versions conflicts)"
# ----------------------------
pip install -r req2.txt

echo "end of set up script"


# TODO check tmp environemt variable

#TODO pin to gpu

# TODO set hf api key



