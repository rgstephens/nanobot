---
name: version
description: Report the NanoBot base version, deployment version and the model from the config.json
---

# Version

Report version information for this NanoBot deployment.

## Script

```bash
{baseDir}/scripts/version.py
```

## Commands

```bash
# Show both the NanoBot base version and deployment version
{baseDir}/scripts/version.py
```

## Notes

- The deployment version is tracked in `VERSION` at the project root and baked into the Docker image
- The NanoBot base version comes from the installed `nanobot` Python package metadata
