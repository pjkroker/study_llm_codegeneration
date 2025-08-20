#!/usr/bin/env bash
set -euo pipefail

# ----------------------------
# Config
# ----------------------------

echo "Building Docker Container"
docker build -f dockerfile --platform=linux/amd64 -t ldb-ubuntu .