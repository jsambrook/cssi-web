#!/usr/bin/env bash
#
# deploy.sh — Pull-and-build for common-sense.com
#
# Called every 5 minutes by cron via /home/john/bin/pull-cssi-web-repo.
# Pulls the repo, and if new commits are found, runs "npm run build".
# If the build fails, the previous dist/ is restored so the live site
# stays up. All output is logged to syslog (journalctl -t cssi-deploy).
#
set -euo pipefail

REPO_DIR="/git/cssi-web"
DIST_DIR="$REPO_DIR/dist"
BACKUP_DIR="$REPO_DIR/dist.bak"
LOCK_FILE="$REPO_DIR/.deploy.lock"
LOG_TAG="cssi-deploy"

log() { logger -t "$LOG_TAG" "$*"; echo "$(date '+%Y-%m-%d %H:%M:%S') $*"; }

cd "$REPO_DIR"

exec 9>"$LOCK_FILE"
if ! flock -n 9; then
  log "Another deploy is already running; skipping this cycle."
  exit 0
fi

export GIT_SSH_COMMAND='ssh -i /home/john/.ssh/id_ed25519_gh_np'

# Ensure tracked-file mutations from previous runs do not block fast-forward updates.
if ! git diff --quiet || ! git diff --cached --quiet; then
  log "Working tree is dirty; resetting tracked files to HEAD."
  git reset --hard HEAD
fi

CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
BEFORE=$(git rev-parse HEAD)
git fetch origin "$CURRENT_BRANCH"
REMOTE_REF="origin/$CURRENT_BRANCH"
AFTER=$(git rev-parse "$REMOTE_REF")

if [ "$BEFORE" = "$AFTER" ]; then
  log "No changes, skipping build."
  exit 0
fi

log "New commits: $BEFORE..$AFTER — rebuilding."
git merge --ff-only "$REMOTE_REF"

# Refresh dependencies only when lockfiles changed or node_modules is missing.
if [ ! -d "$REPO_DIR/node_modules" ] || git diff --name-only "$BEFORE" "$AFTER" | grep -Eq '(^|/)(package.json|package-lock.json)$'; then
  log "Installing dependencies with npm ci."
  npm ci 2>&1 | logger -t "$LOG_TAG"
fi

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
