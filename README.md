# Servidor HTTP a Teclado

Este proyecto levanta un servidor web local con una interfaz sencilla para simular la escritura de texto en cualquier aplicación de tu escritorio.

## Requisitos

- Python 3
- `pip` y `venv` (generalmente incluidos con Python)

### Dependencias de Sistema (Solo para Linux)

`pyautogui` requiere algunas dependencias adicionales. Asegúrate de tenerlas instaladas ejecutando:

```bash
sudo apt-get install scrot python3-tk python3-dev
```

Si vas a usar la versión con `xdotool`, también necesitas instalarlo:

```bash
sudo apt-get install xdotool
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

Ahora puedes iniciar el servidor usando los scripts ejecutables directos. El script `run.sh` (llamado por estos) **limpiará automáticamente la caché de Python** antes de iniciar el servidor para asegurar que siempre se ejecute la última versión.

1.  **Asegúrate de que los scripts `run_no_accents.sh` y `run_xdotool.sh` tengan permisos de ejecución:**
    ```bash
    chmod +x run_no_accents.sh run_xdotool.sh
    ```

2.  **Para iniciar la versión que reemplaza los acentos:**
    ```bash
    ./run_no_accents.sh
    ```

3.  **Para iniciar la versión que usa `xdotool` para los acentos:**
    ```bash
    ./run_xdotool.sh
    ```
    *(Asegúrate de tener `xdotool` instalado para esta opción: `sudo apt-get install xdotool`)*

### Pasos Comunes (después de iniciar el servidor)

1.  **Abre la interfaz web:**
    Abre tu navegador y ve a [http://localhost:8000](http://localhost:8000).

2.  **Utiliza la herramienta:**
    - Haz clic en la ventana de la aplicación donde quieres escribir (un editor de texto, un chat, etc.) para darle el foco.
    - Vuelve al navegador, escribe el texto en el recuadro y elige una de las dos acciones:
        - **Enviar**: Escribe el texto.
        - **Enviar y Agregar Enter**: Escribe el texto y luego pulsa la tecla Enter.

## Desactivar el Entorno

Cuando termines de usar el proyecto, puedes desactivar el entorno virtual simplemente escribiendo:

```bash
deactivate
```