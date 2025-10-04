
# Vibing

<p align="center">
  <img src="https://raw.githubusercontent.com/Nexor-Soft/Vibing/main/vibing_banner.svg" alt="Vibing Banner">
</p>

<p align="center">
    <img src="https://img.shields.io/badge/python-3.10-blue.svg" alt="Python 3.10">
    <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="MIT License">
</p>

## ¿Qué es Vibing?

Vibing es una herramienta que te permite **programar usando tu voz**. Funciona como un puente entre tu voz y tu editor de código, permitiéndote dictar código, comandos o cualquier texto directamente en el lugar donde tengas el foco, ya sea tu IDE, un editor de texto o una terminal.

## ¿Cómo funciona?

La herramienta levanta un servidor web local con una interfaz sencilla. Desde esta interfaz, puedes enviar texto a tu escritorio. El texto se escribirá en cualquier ventana que tenga el foco en ese momento.

1.  **Inicia el servidor**: Ejecuta uno de los scripts `run_*.sh`.
2.  **Abre la interfaz web**: Ve a `http://localhost:8000` en tu navegador.
3.  **Selecciona la ventana de destino**: Haz clic en la ventana donde quieres escribir (por ejemplo, tu editor de código).
4.  **Envía el texto**: Escribe o pega el texto en la interfaz web y haz clic en "Enviar".

## Características

- **Independiente del editor**: Funciona con cualquier aplicación de escritorio.
- **Fácil de usar**: Interfaz web sencilla e intuitiva.
- **Personalizable**: Puedes editar los botones de texto predefinido para adaptarlos a tus necesidades.
- **Soporte para acentos**: Dos modos de funcionamiento para manejar los acentos.

## Instalación

```bash
chmod +x setup.sh
./setup.sh
```

## Uso

```bash
# Para la versión que reemplaza los acentos
./run_no_accents.sh

# Para la versión que usa xdotool para los acentos
./run_xdotool.sh
```

## Contribuir

Las contribuciones son bienvenidas. Si tienes alguna idea o sugerencia, no dudes en abrir un issue o un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
