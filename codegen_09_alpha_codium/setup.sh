#!/usr/bin/env bash
set -euo pipefail

# ----------------------------
# Config
# ----------------------------

echo "Building Docker Container"
pwd
docker build -f ./study_llm_codegeneration/codegen_09_alpha_codium/dockerfile --platform=linux/amd64 -t codegen_study-alpha_codium ./study_llm_codegeneration/codegen_09_alpha_codium/