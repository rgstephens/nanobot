---
name: spotify
description: Check new releases from followed artists and browse your Spotify library.
---

# Spotify

Query the user's Spotify account — followed artists, new releases, and more.

## Script

```bash
{baseDir}/scripts/spotify.py <command> [options]
```

## Commands

```bash
# List all followed artists
{baseDir}/scripts/spotify.py followed

# New releases from followed artists today
{baseDir}/scripts/spotify.py new-releases

# New releases in the last N days
{baseDir}/scripts/spotify.py new-releases --days 7
```

## Setup (first time only — must run locally, not in Docker)

1. Create a Spotify Developer App at https://developer.spotify.com/dashboard
2. Note the redirect URI configured in your Spotify app settings
3. Run:

```bash
{baseDir}/scripts/spotify.py setup \
  --client-id YOUR_ID \
  --client-secret YOUR_SECRET \
  --redirect-uri YOUR_REDIRECT_URI
```

The script prints an auth URL. Open it in your browser, authorise the app, then copy the
full redirect URL from your address bar (the page may show an error — that's fine) and
paste it back into the terminal. The token is cached at `~/.nanobot/workspace/spotify/.cache`
and refreshes automatically — setup only needs to happen once.

## Notes

- `new-releases` checks every followed artist via the Spotify API; progress is logged to stderr
- The OAuth token is stored in the volume (`~/.nanobot/workspace/spotify/`) and persists across Docker restarts
- If the token expires and auto-refresh fails, run `spotify.py auth` locally to re-authenticate
- Requires a free Spotify account; Spotify Premium is not needed for read-only queries
