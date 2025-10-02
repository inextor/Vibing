import pyautogui
import time

print("Preparando para escribir 'test' con pyautogui.press() en un bucle...")
print("Por favor, haz clic en la ventana de destino en los próximos 3 segundos.")
time.sleep(3) # Dar tiempo al usuario para enfocar la ventana

text_to_write = 'test'
for char in text_to_write:
    pyautogui.press(char)
    time.sleep(0.1) # Pequeña pausa entre caracteres para mayor fiabilidad

print("Comando pyautogui.press() en bucle ejecutado.")
