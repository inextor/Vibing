import pyautogui
import time

print("Preparando para escribir 'test'...")
print("Por favor, haz clic en la ventana de destino en los próximos 3 segundos.")
time.sleep(3) # Dar tiempo al usuario para enfocar la ventana

pyautogui.write('test')
print("Comando pyautogui.write('test') ejecutado.")
