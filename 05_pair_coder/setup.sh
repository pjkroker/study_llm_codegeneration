#!/usr/bin/env bash
set -euo pipefail

# ----------------------------
# Config
# ----------------------------

echo "Building Docker Container"
docker build -f Dockerfile.Ubuntu --platform=linux/amd64 -t pair-coder-ubuntu .