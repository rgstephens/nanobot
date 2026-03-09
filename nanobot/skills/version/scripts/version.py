#!/usr/bin/env python3
"""version.py - Report NanoBot base version and deployment version."""

import sys
import tomllib
from pathlib import Path

APP_DIR = Path("/app")


def main() -> None:
    # Base version from pyproject.toml baked into the image
    pyproject = APP_DIR / "pyproject.toml"
    if pyproject.exists():
        with pyproject.open("rb") as f:
            base_version = tomllib.load(f).get("project", {}).get("version", "unknown")
    else:
        base_version = "unknown"

    # Deployment version from VERSION file baked into the image
    version_file = APP_DIR / "VERSION"
    deploy_version = version_file.read_text().strip() if version_file.exists() else "unknown"

    print(f"NanoBot base version : {base_version}")
    print(f"Deployment version   : {deploy_version}")


if __name__ == "__main__":
    main()
