#!/usr/bin/env -S uv run --script
# /// script
# dependencies = ["spotipy>=2.24.0"]
# ///
"""spotify.py - Spotify integration for nanobot.

Commands:
  setup [--client-id ID --client-secret SECRET --redirect-uri URI]
                                            Configure credentials and authenticate
  auth                                      Re-authenticate
  followed                                  List all followed artists
  new-releases [--days N]                   Releases from followed artists (default: today)
"""

import json
import sys
from datetime import date, timedelta
from pathlib import Path

import spotipy
from spotipy.oauth2 import SpotifyOAuth

WORKSPACE = Path.home() / ".nanobot/workspace"
SPOTIFY_DIR = WORKSPACE / "spotify"
CONFIG_FILE = SPOTIFY_DIR / "config.json"
CACHE_FILE = SPOTIFY_DIR / ".cache"

SCOPES = "user-follow-read user-read-recently-played user-top-read"


def load_config() -> dict:
    if not CONFIG_FILE.exists():
        print("Spotify not configured. Run: spotify.py setup --client-id ID --client-secret SECRET --redirect-uri URI")
        sys.exit(1)
    return json.loads(CONFIG_FILE.read_text())


def make_auth(config: dict) -> SpotifyOAuth:
    return SpotifyOAuth(
        client_id=config["clientId"],
        client_secret=config["clientSecret"],
        redirect_uri=config["redirectUri"],
        scope=SCOPES,
        cache_path=str(CACHE_FILE),
        open_browser=False,
    )


def get_spotify() -> spotipy.Spotify:
    config = load_config()
    auth = make_auth(config)
    return spotipy.Spotify(auth_manager=auth)


def do_auth_flow(config: dict) -> None:
    """Run the paste-the-redirect-URL OAuth flow."""
    auth = make_auth(config)

    # Clear any stale cache first
    if CACHE_FILE.exists():
        CACHE_FILE.unlink()

    auth_url = auth.get_authorize_url()
    print("\nOpen this URL in your browser:")
    print(f"\n  {auth_url}\n")
    print(f"You'll be redirected to: {config['redirectUri']}?code=...")
    print("The page may show an error — that's fine. Copy the full URL from your address bar.\n")

    redirect_response = input("Paste the full redirect URL here: ").strip()
    code = auth.parse_response_code(redirect_response)
    auth.get_access_token(code, as_dict=False, check_cache=False)

    sp = spotipy.Spotify(auth_manager=auth)
    user = sp.current_user()
    print(f"\nAuthenticated as: {user['display_name']} ({user['id']})")
    print(f"Token cached at: {CACHE_FILE}")


def get_all_followed_artists(sp: spotipy.Spotify) -> list[dict]:
    """Fetch all followed artists, handling pagination."""
    artists = []
    after = None
    while True:
        result = sp.current_user_followed_artists(limit=50, after=after)
        items = result["artists"]["items"]
        artists.extend(items)
        after = result["artists"]["cursors"].get("after")
        if not after:
            break
    return artists


# --- commands ---

def cmd_setup(args: list[str]) -> None:
    """Store credentials and run OAuth flow."""
    SPOTIFY_DIR.mkdir(parents=True, exist_ok=True)

    client_id = ""
    client_secret = ""
    redirect_uri = ""

    i = 0
    while i < len(args):
        if args[i] == "--client-id" and i + 1 < len(args):
            client_id = args[i + 1]; i += 2
        elif args[i] == "--client-secret" and i + 1 < len(args):
            client_secret = args[i + 1]; i += 2
        elif args[i] == "--redirect-uri" and i + 1 < len(args):
            redirect_uri = args[i + 1]; i += 2
        else:
            i += 1

    if not client_id:
        client_id = input("Client ID: ").strip()
    if not client_secret:
        client_secret = input("Client Secret: ").strip()
    if not redirect_uri:
        redirect_uri = input("Redirect URI (must match your Spotify app settings): ").strip()

    config = {"clientId": client_id, "clientSecret": client_secret, "redirectUri": redirect_uri}
    CONFIG_FILE.write_text(json.dumps(config, indent=2))
    print(f"Config saved to {CONFIG_FILE}")

    do_auth_flow(config)


def cmd_auth(_args: list[str]) -> None:
    """Re-run the OAuth flow."""
    SPOTIFY_DIR.mkdir(parents=True, exist_ok=True)
    do_auth_flow(load_config())


def cmd_followed(_args: list[str]) -> None:
    """List all followed artists alphabetically."""
    sp = get_spotify()
    artists = get_all_followed_artists(sp)
    print(f"Following {len(artists)} artists:\n")
    for a in sorted(artists, key=lambda x: x["name"].lower()):
        print(f"  {a['name']}")


def cmd_new_releases(args: list[str]) -> None:
    """Show albums and singles released by followed artists within the last N days."""
    days = 1
    if "--days" in args:
        idx = args.index("--days")
        days = int(args[idx + 1])

    cutoff = date.today() - timedelta(days=days - 1)
    cutoff_str = cutoff.isoformat()

    sp = get_spotify()
    print(f"Fetching followed artists...", file=sys.stderr)
    artists = get_all_followed_artists(sp)
    print(f"Checking {len(artists)} artists for releases since {cutoff_str}...", file=sys.stderr)

    releases = []
    for artist in artists:
        result = sp.artist_albums(artist["id"], album_type="album,single", limit=5)
        for album in result["items"]:
            rel_date = album["release_date"]
            if len(rel_date) < 10:
                continue  # skip year-only or month-only dates
            if rel_date >= cutoff_str:
                releases.append({
                    "date": rel_date,
                    "artist": artist["name"],
                    "title": album["name"],
                    "type": album["album_type"],
                    "url": album["external_urls"]["spotify"],
                })

    if not releases:
        label = "today" if days == 1 else f"the last {days} days"
        print(f"No new releases from followed artists {label}.")
        return

    releases.sort(key=lambda x: (x["date"], x["artist"].lower()))
    label = "Today" if days == 1 else f"Last {days} days"
    print(f"\n{label}'s releases from followed artists ({len(releases)} found):\n")
    for r in releases:
        print(f"  [{r['type']}] {r['artist']} — {r['title']}")
        print(f"         Released: {r['date']}")
        print(f"         {r['url']}")
        print()


COMMANDS = {
    "setup": cmd_setup,
    "auth": cmd_auth,
    "followed": cmd_followed,
    "new-releases": cmd_new_releases,
}


def usage() -> None:
    print("Usage: spotify.py <command> [options]\n")
    print("Commands:")
    print("  setup --client-id ID --client-secret SECRET --redirect-uri URI")
    print("                         Configure credentials and authenticate")
    print("  auth                   Re-authenticate")
    print("  followed               List all followed artists")
    print("  new-releases           Show releases from followed artists today")
    print("  new-releases --days N  Show releases from the last N days")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd not in COMMANDS:
        usage()
        sys.exit(1 if cmd else 0)
    COMMANDS[cmd](sys.argv[2:])
