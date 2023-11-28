#!/bin/bash

set -e

echo "Let's create a new release!"

python scripts/upgrade_version.py

TAG=$(python -c 'from PolyDeDupe.version import VERSION; print("v" + VERSION)')

read -p "Creating new release for $TAG. Do you want to continue? [Y/n] " prompt

if [[ $prompt == "y" || $prompt == "Y" || $prompt == "yes" || $prompt == "Yes" ]]; then
    python scripts/prepare_changelog.py
    git add -A
    git commit -m "Bump version to $TAG for release" || true && git push
    echo "Creating new git tag $TAG"
    git tag "$TAG" -m "$TAG"
    git push --tags
    python scripts/release_notes.py
else
    echo "Cancelled"
    exit 1
fi
