#!/usr/bin/env bash
set -euo pipefail

# ----------------------------
# Config
# ----------------------------

echo "Building Docker Container"
pwd
#--no-cache 
#--build-arg CACHEBUST=$(date +%s)
docker build --build-arg CACHEBUST=$(date +%s)  -f ./study_llm_codegeneration/codegen_09_alpha_codium/dockerfile2 --platform=linux/amd64 -t codegen_study-alpha_codium ./study_llm_codegeneration/codegen_09_alpha_codium/