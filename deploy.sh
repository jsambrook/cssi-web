#!/usr/bin/env bash
#
# deploy.sh — Pull-and-build for common-sense.com
#
# Called every 15 minutes by cron via /home/john/bin/pull-cssi-web-repo.
# Pulls the repo, and if new commits are found, runs "npm run build".
# If the build fails, the previous dist/ is restored so the live site
# stays up. All output is logged to syslog (journalctl -t cssi-deploy).
#
set -euo pipefail

REPO_DIR="/git/cssi-web"
DIST_DIR="$REPO_DIR/dist"
BACKUP_DIR="$REPO_DIR/dist.bak"
LOG_TAG="cssi-deploy"

log() { logger -t "$LOG_TAG" "$*"; echo "$(date '+%Y-%m-%d %H:%M:%S') $*"; }

cd "$REPO_DIR"

export GIT_SSH_COMMAND='ssh -i /home/john/.ssh/id_ed25519_gh_np'

# Pull and check for changes
BEFORE=$(git rev-parse HEAD)
git pull --ff-only
AFTER=$(git rev-parse HEAD)

if [ "$BEFORE" = "$AFTER" ]; then
  log "No changes, skipping build."
  exit 0
fi

log "New commits: $BEFORE..$AFTER — rebuilding."

# Back up current dist
rm -rf "$BACKUP_DIR"
if [ -d "$DIST_DIR" ]; then
  cp -a "$DIST_DIR" "$BACKUP_DIR"
fi

# Build
if npm run build 2>&1 | logger -t "$LOG_TAG"; then
  log "Build succeeded."
  rm -rf "$BACKUP_DIR"
else
  log "Build FAILED — rolling back."
  rm -rf "$DIST_DIR"
  if [ -d "$BACKUP_DIR" ]; then
    mv "$BACKUP_DIR" "$DIST_DIR"
  fi
  exit 1
fi
