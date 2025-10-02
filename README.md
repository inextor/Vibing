# Servidor HTTP a Teclado

Este proyecto levanta un servidor web local con una interfaz sencilla para simular la escritura de texto en cualquier aplicación de tu escritorio.

## Requisitos

- Python 3
- `pip` y `venv` (generalmente incluidos con Python)

### Dependencias de Sistema (Solo para Linux)

En sistemas operativos basados en Debian/Ubuntu, `pyautogui` requiere algunas dependencias adicionales. Asegúrate de tenerlas instaladas ejecutando:

```bash
sudo apt-get install scrot python3-tk python3-dev
```

## Instalación y Configuración

Para facilitar la instalación, puedes usar el script de configuración.

1.  **Dar permisos de ejecución al script:**
    ```bash
    chmod +x setup.sh
    ```

2.  **Ejecutar el script:**
    ```bash
    ./setup.sh
    ```

El script se encargará de:
- Crear un entorno virtual de Python en una carpeta llamada `.venv`.
- Instalar las dependencias necesarias (listadas en `requirements.txt`) dentro de ese entorno.

## Uso

1.  **Activa el entorno virtual:**
    Cada vez que abras una nueva terminal para trabajar en el proyecto, debes activar el entorno:
    ```bash
    source .venv/bin/activate
    ```

2.  **Inicia el servidor:**
    ```bash
    python3 http_to_keyboard.py
    ```

3.  **Abre la interfaz web:**
    Abre tu navegador y ve a [http://localhost:8000](http://localhost:8000).

4.  **Utiliza la herramienta:**
    - Haz clic en la ventana de la aplicación donde quieres escribir (un editor de texto, un chat, etc.) para darle el foco.
    - Vuelve al navegador, escribe el texto en el recuadro y elige una de las dos acciones:
        - **Enviar**: Escribe el texto.
        - **Enviar y Agregar Enter**: Escribe el texto y luego pulsa la tecla Enter.

## Desactivar el Entorno

Cuando termines de usar el proyecto, puedes desactivar el entorno virtual simplemente escribiendo:

```bash
deactivate
```