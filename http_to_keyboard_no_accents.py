import http.server
import socketserver
import sys
import pyautogui
import time
import unicodedata
from urllib.parse import parse_qs
import os

VERSION = "1.3.0" # Versión actual del script (sin acentos)

def strip_accents(text):
    # Mapeo manual para reemplazar acentos y ñ/Ñ
    accents_map = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'ñ': 'n', 'Ñ': 'N',
    }
    for accented_char, non_accented_char in accents_map.items():
        text = text.replace(accented_char, non_accented_char)
    return text

# --- Configuracion de PyAutoGUI ---
pyautogui.PAUSE = 0.01
pyautogui.FAILSAFE = True

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="www", **kwargs)

    def do_POST(self):
        """Procesa el formulario, escribe el texto y redirige."""
        try:
            # Responder inmediatamente para que el cliente no espere
            self.send_response(200)
            self.send_header('Content-Length', '0')
            self.end_headers()

            # Leer el cuerpo de la solicitud
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            
            # Crear un proceso hijo para manejar la escritura
            pid = os.fork()

            if pid == 0:  # Proceso hijo
                try:
                    parsed_data = parse_qs(body)
                    text_to_type = parsed_data.get('text_to_type', [''])[0]
                    action = parsed_data.get('action', ['send'])[0]

                    if text_to_type:
                        self._type_text(text_to_type)

                        if action == 'send_with_enter':
                            pyautogui.press('enter')
                            print("Escritura completada (con Enter).", file=sys.stderr)
                        else:
                            print("Escritura completada (sin Enter).", file=sys.stderr)
                    else:
                        print("Peticion POST recibida sin texto para escribir.", file=sys.stderr)
                
                except Exception as e:
                    print(f"Error en el proceso hijo: {e}", file=sys.stderr)
                
                finally:
                    os._exit(0)  # Salir del proceso hijo

        except Exception as e:
            print(f"Error en POST: {e}", file=sys.stderr)
            # No se puede enviar respuesta si los encabezados ya se enviaron
            pass

    def _type_text(self, text):
        """Funcion central para simular la escritura, reemplazando acentos y usando pyautogui.press() para cada caracter."""
        if not text:
            print("Nada que escribir.", file=sys.stderr)
            return
        
        # Eliminar acentos del texto
        text_to_write = strip_accents(text)
        
        print(f"Texto a escribir (sin acentos): '{text_to_write}'", file=sys.stderr)
        print(f"Escribiendo texto: {text_to_write[:100]}... (usando pyautogui.press() para cada caracter)", file=sys.stderr)
        
        for char in text_to_write:
            pyautogui.press(char)
            time.sleep(0.02) # Pequeña pausa entre caracteres para mayor fiabilidad
        
        print("Escritura completada.", file=sys.stderr)

def run_server(port=8000):
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, CustomHandler)
    
    print("--- Servidor con Interfaz Web (Sin Acentos) ---", file=sys.stderr)
    print(f"Version: {VERSION}", file=sys.stderr) # Imprimir la versión
    print(f"Sirviendo archivos desde el directorio 'www'", file=sys.stderr)
    print(f"1. Abre tu navegador y ve a: http://localhost:{port}", file=sys.stderr)
    print("2. Haz clic en la ventana donde quieres escribir (editor, etc.).", file=sys.stderr)
    print("3. Usa el formulario web para enviar texto.", file=sys.stderr)
    print("Para detener, presiona Ctrl+C aqui.", file=sys.stderr)
    
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
