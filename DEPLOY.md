# NanoBot Deployment Guide

## Overview

NanoBot has two layers of content that deploy differently:

| Layer | What it contains | How it deploys |
|---|---|---|
| **Docker image** | Application code, built-in skills, scripts | `docker build` → `docker push` → server pulls |
| **Docker volume** | Config, credentials, memory, list data | Lives on the server; persists across deploys |

Understanding this split is essential when adding new skills or changing configuration.

---

## What Goes Where

### Baked into the image (`nanobot/` source tree)

- Core application code
- Built-in skills: `nanobot/skills/*/SKILL.md` and `nanobot/skills/*/scripts/*.sh`
- Workspace templates (copied to volume on first `nanobot onboard`)

**Rule of thumb**: if it's code or agent instructions, it goes in the repo.

### Lives in the volume (`~/.nanobot/` on the server)

- `config.json` — API keys, model settings, channel tokens
- `workspace/memory/MEMORY.md` — long-term facts the agent accumulates
- `workspace/memory/HISTORY.md` — conversation log
- `workspace/USER.md`, `SOUL.md`, `AGENTS.md` — persona customisation
- `workspace/lists/*.md` — personal list data (todo, favorites, etc.)

**Rule of thumb**: if it's user data or secrets, it lives in the volume.

---

## Workflow

### Adding or updating a skill

Skills live in the source tree so they travel with the image:

```
dev machine:
  1. Edit nanobot/skills/<skill-name>/SKILL.md
  2. Edit nanobot/skills/<skill-name>/scripts/*.sh
  3. git commit && git push

build:
  make docker-release

server:
  docker compose pull && docker compose up -d
```

No manual file copying to the server required.

### Changing config (API keys, model, channels)

Edit `~/Docker/nanobot/.nanobot/config.json` directly on the server (or via `scp`). No image rebuild needed — the volume is mounted at runtime.

### First-time server setup

```bash
# 1. Create project directory
mkdir -p ~/Docker/nanobot

# 2. Copy compose file
scp docker-compose.yml server:~/Docker/nanobot/

# 3. Copy local config (already configured with API keys)
scp ~/.nanobot/config.json server:~/Docker/nanobot/.nanobot/config.json

# 4. Start gateway
nano ~/.nanobot/config.json

# 5. Start gateway
docker compose up -d nanobot-gateway
```

---

## Docker Compose

The `docker-compose.yml` mounts `~/.nanobot` from the host into the container at `/root/.nanobot`:

```yaml
volumes:
  - ~/.nanobot:/root/.nanobot
```

This means:
- Skill scripts baked into the image are at e.g. `/usr/local/lib/python3.12/site-packages/nanobot/skills/lists/scripts/lists.sh`
- List data written by those scripts goes to `/root/.nanobot/workspace/lists/` (the volume)
- Config and memory persist across image updates

---

## Build & Push

```bash
# Login to private registry
make docker-login

# Build multi-arch (amd64 + arm64) and push
make docker-release
```

See `Makefile` for details.

---

## Skills Reference

### Lists skill (`nanobot/skills/lists/`)

Manages personal named lists (todo, favorites, snooker players, etc.).

- **Script**: `nanobot/skills/lists/scripts/lists.sh` — baked into image
- **Data**: `~/.nanobot/workspace/lists/*.md` — in the volume, persists across deploys

Available commands (invoked by the agent via the `exec` tool):

```bash
lists.sh show   <name>          # display list
lists.sh add    <name> <item>   # add item
lists.sh remove <name> <query>  # remove matching items
lists.sh search <name> <query>  # search items
lists.sh all                    # show all lists
lists.sh clear  <name>          # delete list
```

List files are plain markdown — you can view or edit them directly on the server at `~/.nanobot/workspace/lists/`.

---

### Google gog skill

Auth with google on Mac and **save creds to file**

```sh
# On Dev Mac
GOG_KEYRING_BACKEND=file GOG_KEYRING_PASSWORD=xxx gog auth add nworksgreg@gmail.com --services docs,drive,gmail,sheets
scp ~/Library/Application\ Support/gogcli/keyring/* 10.2.2.6:/tmp/gogcli-keyring/
# On prod server
sudo cp /tmp/gogcli-keyring/* ~/Docker/nanobot/.gogcli/keyring/
docker compose restart
docker exec nanobot-gateway gog auth list
```

### Spotify skill (`nanobot/skills/spotify/`)

Queries the Spotify API for followed artists and new releases.

- **Script**: `nanobot/skills/spotify/scripts/spotify.py` — baked into image (runs via `uv run --script`, deps auto-installed)
- **Credentials**: `~/.nanobot/workspace/spotify/config.json` — in the volume
- **Token cache**: `~/.nanobot/workspace/spotify/.cache` — in the volume, persists across deploys

#### First-time setup (run locally, not in Docker)

OAuth requires a browser. Do this once on your dev machine before deploying:

```bash
# 1. Create a Spotify Developer App at https://developer.spotify.com/dashboard
#    Add redirect URI: http://127.0.0.1:8888/callback

# 2. Run setup (opens browser for OAuth)
cd ~/Dev/llm/nanobot
source .venv/bin/activate
uv run --script nanobot/skills/spotify/scripts/spotify.py setup \
  --client-id YOUR_CLIENT_ID \
  --client-secret YOUR_CLIENT_SECRET
```

The credentials and token are written to `~/.nanobot/workspace/spotify/` which is already in the Docker volume mount. No extra copying needed.

#### Available commands (invoked by the agent via the `exec` tool)

```bash
spotify.py followed               # list all followed artists
spotify.py new-releases           # releases from followed artists today
spotify.py new-releases --days 7  # releases in the last 7 days
spotify.py auth                   # re-authenticate if token expires
```

#### Re-authentication after token expiry

Spotify refresh tokens don't expire unless revoked, so this should rarely be needed. If it is, run `spotify.py auth` locally (browser required), which updates the cached token in the volume.
