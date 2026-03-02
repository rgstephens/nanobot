---
name: lists
description: Manage personal named lists (todo, favorites, artists, sports teams, etc.)
---

# Lists

Manage personal named lists stored in the workspace. Lists are plain markdown files — one per list — so they're human-readable and persist across sessions.

## Storage

Lists live at `~/.nanobot/workspace/lists/<name>.md`. Each file contains one item per line in markdown list format.

## Script

All operations go through the script. Use the `exec` tool:

```bash
{baseDir}/scripts/lists.sh <command> <list-name> [args]
```

## Commands

```bash
# Show all items in a list
{baseDir}/scripts/lists.sh show todo
{baseDir}/scripts/lists.sh show "favorite artists"

# Add an item
{baseDir}/scripts/lists.sh add todo "Call dentist"
{baseDir}/scripts/lists.sh add "snooker players" "Ronnie O'Sullivan"

# Remove an item (case-insensitive match)
{baseDir}/scripts/lists.sh remove todo "Call dentist"
{baseDir}/scripts/lists.sh remove favorites "Drake"

# Search within a list
{baseDir}/scripts/lists.sh search "favorite artists" "rolling"

# List all lists with item counts
{baseDir}/scripts/lists.sh all

# Clear an entire list
{baseDir}/scripts/lists.sh clear "project ideas"
```

## Notes

- List names are case-insensitive; spaces are normalised to hyphens in the filename
- `remove` does a case-insensitive substring match — confirm with the user if ambiguous
- `add` silently skips exact duplicates
- Always use `show` before `remove` if the user's intent is unclear
