#!/bin/bash
set -e

echo "--- Configurando el entorno virtual para el Servidor HTTP a Teclado ---"

# Verificar que python3 este instalado
if ! command -v python3 &> /dev/null
then
    echo "Error: python3 no está instalado. Por favor, instálalo para continuar."
    exit 1
fi

# Crear el entorno virtual si no existe
if [ ! -d ".venv" ]; then
    echo "Creando entorno virtual en la carpeta '.venv'..."
    python3 -m venv .venv
else
    echo "El entorno virtual '.venv' ya existe."
fi

# Instalar dependencias desde requirements.txt usando el pip del venv
echo "Instalando dependencias desde requirements.txt..."
.venv/bin/pip install -r requirements.txt

echo ""
echo "--- ¡Configuración completada! ---"
echo ""
echo "Recordatorio de dependencias de sistema (solo para Linux/Debian/Ubuntu):"
echo "Si aún no lo has hecho, asegúrate de tener instalados los siguientes paquetes:"
echo "sudo apt-get install scrot python3-tk python3-dev"
echo ""
echo "Para iniciar el servidor, primero activa el entorno con:"
echo "source .venv/bin/activate"
echo ""
echo "Y luego ejecuta el script:"
echo "python3 http_to_keyboard.py"
