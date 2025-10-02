#!/bin/bash
set -e # Exit on error

echo "--- Iniciando Servidor HTTP a Teclado ---"

# Directorio donde se encuentra el script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)"

# Limpiar caché de Python para asegurar que se cargue la última versión
echo "Limpiando caché de Python (__pycache__)..."
rm -rf "$SCRIPT_DIR/__pycache__"

# 1. Asegurarse de que el setup se ha ejecutado
# ... (existing setup.sh call) ...
SETUP_SCRIPT="$SCRIPT_DIR/setup.sh"

if [ ! -f "$SETUP_SCRIPT" ]; then
    echo "Error: No se pudo encontrar el script 'setup.sh'. Asegúrate de que esté en el mismo directorio."
    exit 1
fi

# Dar permisos de ejecución a setup.sh si no los tiene
if [ ! -x "$SETUP_SCRIPT" ]; then
    echo "Dando permisos de ejecución a 'setup.sh'..."
    chmod +x "$SETUP_SCRIPT"
fi

# Ejecutar el script de configuración
"$SETUP_SCRIPT"

# 2. Definir la ruta al ejecutable de Python del entorno virtual
VENV_PYTHON="$SCRIPT_DIR/.venv/bin/python3"

# 3. Comprobar si el ejecutable de Python existe
if [ ! -f "$VENV_PYTHON" ]; then
    echo "Error: No se pudo encontrar el ejecutable de Python en el entorno virtual."
    echo "Asegúrate de que el script 'setup.sh' se completó correctamente."
    exit 1
fi

# 4. Determinar qué script ejecutar basado en el argumento
SCRIPT_TO_RUN="http_to_keyboard_no_accents.py" # Por defecto

if [ "$1" == "xdotool" ]; then
    SCRIPT_TO_RUN="http_to_keyboard_xdotool.py"
    echo "Modo: Usando xdotool para acentos."
elif [ "$1" == "no-accents" ]; then
    SCRIPT_TO_RUN="http_to_keyboard_no_accents.py"
    echo "Modo: Reemplazando acentos (sin acentos)."
else
    echo "Modo: Por defecto, reemplazando acentos (sin acentos)."
    echo "Uso: ./run.sh [no-accents|xdotool]"
fi

echo ""
echo "-----------------------------------------------------"
echo "Iniciando el servidor con: $SCRIPT_TO_RUN"
"$VENV_PYTHON" "$SCRIPT_DIR/$SCRIPT_TO_RUN"
