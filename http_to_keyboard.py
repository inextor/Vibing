
import http.server
import socketserver
import sys
import pyautogui
from urllib.parse import parse_qs

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
                print(f"Escribiendo texto: {text_to_type[:100]}...", file=sys.stderr)
                pyautogui.write(text_to_type)

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

def run_server(port=8000):
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, WebUIKeyboardHandler)
    
    print("--- Servidor con Interfaz Web --- ", file=sys.stderr)
    print(f"1. Abre tu navegador y ve a: http://localhost:{port}", file=sys.stderr)
    print("2. Haz clic en la ventana donde quieres escribir (editor, etc.).", file=sys.stderr)
    print("3. Usa el formulario web para enviar texto.", file=sys.stderr)
    print("Para detener, presiona Ctrl+C aqui.", file=sys.stderr)
    
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
