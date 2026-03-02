#!/usr/bin/env bash
set -euo pipefail

LISTS_DIR="${HOME}/.nanobot/workspace/lists"
mkdir -p "$LISTS_DIR"

usage() {
  cat <<EOF
Usage: lists.sh <command> <list-name> [args]

Commands:
  show   <name>          Display all items in a list
  add    <name> <item>   Add an item (skips exact duplicates)
  remove <name> <query>  Remove items matching query (case-insensitive)
  search <name> <query>  Search items in a list
  all                    Show all lists with item counts
  clear  <name>          Delete all items in a list
EOF
}

# Normalise list name to a safe filename: lowercase, spaces -> hyphens
list_file() {
  local name
  name=$(echo "$1" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | tr -cd '[:alnum:]-')
  echo "$LISTS_DIR/${name}.md"
}

cmd_show() {
  local file
  file=$(list_file "$1")
  if [[ ! -f "$file" ]] || [[ ! -s "$file" ]]; then
    echo "List '$1' is empty."
    return 0
  fi
  echo "# $1"
  cat "$file"
}

cmd_all() {
  local found=0
  for f in "$LISTS_DIR"/*.md; do
    [[ -f "$f" ]] || continue
    found=1
    local name count
    name=$(basename "$f" .md)
    count=$(grep -c '^- ' "$f" 2>/dev/null || echo 0)
    printf "  %-24s %s items\n" "$name" "$count"
  done
  if [[ $found -eq 0 ]]; then
    echo "No lists yet."
  fi
}

cmd_add() {
  local file item
  file=$(list_file "$1")
  item="$2"

  if [[ -f "$file" ]] && grep -qxF "- $item" "$file" 2>/dev/null; then
    echo "'$item' is already in '$1'."
    return 0
  fi

  echo "- $item" >> "$file"
  echo "Added to '$1': $item"
}

cmd_remove() {
  local file query matches count
  file=$(list_file "$1")
  query="$2"

  if [[ ! -f "$file" ]]; then
    echo "List '$1' does not exist."
    return 1
  fi

  matches=$(grep -i "$query" "$file" 2>/dev/null || true)
  if [[ -z "$matches" ]]; then
    echo "No items matching '$query' found in '$1'."
    return 0
  fi

  count=$(echo "$matches" | wc -l | tr -d ' ')
  grep -iv "$query" "$file" > "${file}.tmp" && mv "${file}.tmp" "$file"
  echo "Removed $count item(s) from '$1':"
  echo "$matches"
}

cmd_search() {
  local file results
  file=$(list_file "$1")

  if [[ ! -f "$file" ]]; then
    echo "List '$1' does not exist."
    return 0
  fi

  results=$(grep -i "$2" "$file" 2>/dev/null || true)
  if [[ -z "$results" ]]; then
    echo "No items matching '$2' in '$1'."
  else
    echo "$results"
  fi
}

cmd_clear() {
  local file
  file=$(list_file "$1")
  if [[ ! -f "$file" ]]; then
    echo "List '$1' does not exist."
    return 0
  fi
  rm "$file"
  echo "Cleared list '$1'."
}

# Dispatch
case "${1:-}" in
  show)
    [[ -n "${2:-}" ]] || { usage; exit 1; }
    cmd_show "$2"
    ;;
  add)
    [[ -n "${2:-}" && -n "${3:-}" ]] || { usage; exit 1; }
    cmd_add "$2" "$3"
    ;;
  remove)
    [[ -n "${2:-}" && -n "${3:-}" ]] || { usage; exit 1; }
    cmd_remove "$2" "$3"
    ;;
  search)
    [[ -n "${2:-}" && -n "${3:-}" ]] || { usage; exit 1; }
    cmd_search "$2" "$3"
    ;;
  all)
    cmd_all
    ;;
  clear)
    [[ -n "${2:-}" ]] || { usage; exit 1; }
    cmd_clear "$2"
    ;;
  *)
    usage
    exit 1
    ;;
esac
