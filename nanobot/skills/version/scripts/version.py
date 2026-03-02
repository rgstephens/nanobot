#!/usr/bin/env -S uv run --script
# /// script
# dependencies = []
# ///
"""version.py - Report NanoBot base version and deployment version."""

import importlib.metadata
import sys
from pathlib import Path

# Deployment version baked into the image at /app/VERSION
VERSION_FILE = Path("/app/VERSION")


def main() -> None:
    try:
        base_version = importlib.metadata.version("nanobot-ai")
    except importlib.metadata.PackageNotFoundError:
        base_version = "unknown"

    if VERSION_FILE.exists():
        deploy_version = VERSION_FILE.read_text().strip()
    else:
        deploy_version = "unknown"

    print(f"NanoBot base version : {base_version}")
    print(f"Deployment version   : {deploy_version}")


if __name__ == "__main__":
    main()
