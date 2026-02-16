#!/usr/bin/env bash
set -euo pipefail

if ! command -v shellcheck >/dev/null 2>&1; then
  echo "shellcheck is not installed; skipping shell lint. Install it to enable shell lint checks." >&2
  exit 0
fi

shellcheck deploy.sh
