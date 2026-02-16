#!/usr/bin/env bash
set -euo pipefail

if ! command -v shellcheck >/dev/null 2>&1; then
  echo "shellcheck is not installed. Install it to run shell linting." >&2
  exit 127
fi

shellcheck deploy.sh
