#!/bin/bash
# Script para iniciar el servidor en modo "sin acentos"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)"
exec "$SCRIPT_DIR/run.sh" "no-accents"
