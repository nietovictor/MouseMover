import pyautogui
import random
import time

def mover_mouse_aleatorio(tiempo_min = 5, tiempo_max = 30):
    while True:
        # Espera un intervalo aleatorio entre 5 segundos y 30 segundos 
        intervalo = random.randint(tiempo_min, tiempo_max)
        print(f"Esperando {intervalo} segundos...")
        time.sleep(intervalo)
        
        # Obtiene la posición actual del mouse
        x, y = pyautogui.position()
        
        # Calcula un pequeño desplazamiento aleatorio
        dx = random.randint(-200, 200)
        dy = random.randint(-200, 200)
        
        # Mueve el mouse a la nueva posición
        pyautogui.moveTo(x + dx, y + dy, duration=0.2)

if __name__ == "__main__":
    mover_mouse_aleatorio()