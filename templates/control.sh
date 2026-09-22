#!/bin/sh
set -eu
script_dir=$(CDPATH= cd -- "$(dirname "$0")" && pwd)
case "${1:-}" in status|mark-paused|--help|-h) ;; *) printf "%s\n" "Only status and mark-paused are supported; no worker control." >&2; exit 64;; esac
exec python3 "$script_dir/local-tools.py" "$@"
