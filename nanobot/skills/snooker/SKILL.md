---
name: snooker
description: Look up snooker rankings, results, player profiles, live matches and head-to-head records via api.snooker.org.
---

# Snooker

Query live snooker data — rankings, results, player profiles, and more.

## Script

```bash
{baseDir}/scripts/snooker.py <command> [options]
```

## Commands

```bash
# Current world rankings (top 20)
{baseDir}/scripts/snooker.py rankings

# Rankings for a specific season
{baseDir}/scripts/snooker.py rankings --season 2024

# Player profile (search by name)
{baseDir}/scripts/snooker.py player "O'Sullivan"
{baseDir}/scripts/snooker.py player "Ronnie"

# Recent results
{baseDir}/scripts/snooker.py results
{baseDir}/scripts/snooker.py results --days 3

# Live matches in progress
{baseDir}/scripts/snooker.py live

# Matches scheduled for tomorrow (default) or a specific date
{baseDir}/scripts/snooker.py upcoming
{baseDir}/scripts/snooker.py upcoming --date 2026-03-15

# Tournaments active tomorrow (default) or a specific date
{baseDir}/scripts/snooker.py tournaments
{baseDir}/scripts/snooker.py tournaments --date 2026-03-15

# Full schedule (tournaments + matches) for tomorrow or a specific date
{baseDir}/scripts/snooker.py schedule
{baseDir}/scripts/snooker.py schedule --date 2026-03-15

# Head-to-head record (split name pairs by position)
{baseDir}/scripts/snooker.py h2h Ronnie O'Sullivan Mark Selby
```

## Setup (first time only)

Requires an approved `X-Requested-By` API key from api.snooker.org.
Contact webmaster@snooker.org to request access, then run:

```bash
{baseDir}/scripts/snooker.py setup --api-key YOUR_KEY
```

Config is stored at `~/.nanobot/workspace/snooker/config.json` (in the Docker volume).

## Notes

- All data is from the main professional tour (tour ID 1)
- Rankings show top 20 by prize money for the current season
- `player` returns up to 3 matching results if the name is ambiguous
- `h2h` searches by last name or full name — be specific if names are ambiguous
