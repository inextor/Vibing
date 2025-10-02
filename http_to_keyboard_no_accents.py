import http.server
import socketserver
import sys
import pyautogui
import time
import unicodedata
from urllib.parse import parse_qs

VERSION = "1.2.0" # Versión actual del script (sin acentos)

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

class WebUIKeyboardHandler(http.server.BaseHTTPRequestHandler):
    """
    Manejador HTTP con una interfaz web que permite elegir si se pulsa Enter.
    - GET: Sirve un formulario HTML con dos botones.
    - POST: Procesa los datos del formulario y los escribe con pyautogui.
    """

    def _get_html_form(self):
        """Lee y retorna el contenido del formulario HTML desde un archivo."""
        html_file_path = "index.html" # Asumiendo que index.html esta en el mismo directorio
        try:
            with open(html_file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: El archivo HTML '{html_file_path}' no fue encontrado.", file=sys.stderr)
            return "<h1>Error: Formulario HTML no encontrado.</h1>"
        except Exception as e:
            print(f"Error leyendo el archivo HTML: {e}", file=sys.stderr)
            return f"<h1>Error: {e}</h1>"

    def do_GET(self):
        """Sirve el formulario HTML."""
        try:
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(self._get_html_form().encode('utf-8'))
        except Exception as e:
            print(f"Error en GET: {e}", file=sys.stderr)

    def do_POST(self):
        """Procesa el formulario, escribe el texto y redirige."""
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            
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

            # Redirigir al usuario de vuelta al formulario
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()

        except Exception as e:
            print(f"Error en POST: {e}", file=sys.stderr)
            self.send_response(500)
            self.end_headers()

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
    httpd = http.server.HTTPServer(server_address, WebUIKeyboardHandler)
    
    print("--- Servidor con Interfaz Web (Sin Acentos) ---", file=sys.stderr)
    print(f"Version: {VERSION}", file=sys.stderr) # Imprimir la versión
    print(f"1. Abre tu navegador y ve a: http://localhost:{port}", file=sys.stderr)
    print("2. Haz clic en la ventana donde quieres escribir (editor, etc.).", file=sys.stderr)
    print("3. Usa el formulario web para enviar texto.", file=sys.stderr)
    print("Para detener, presiona Ctrl+C aqui.", file=sys.stderr)
    
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()