import pyautogui
import random
import time

def mover_mouse_aleatorio( margen=50):
    screen_width, screen_height = pyautogui.size()
    centro_x, centro_y = screen_width // 2, screen_height // 2

    
    
    
    x, y = pyautogui.position()
    
    # Si el mouse está demasiado cerca de los bordes, lo lleva al centro
    if (x < margen or x > screen_width - margen or
        y < margen or y > screen_height - margen):
        print("Demasiado cerca del borde, moviendo al centro.")
        pyautogui.moveTo(centro_x, centro_y, duration=0.2)

    dx = random.randint(-200, 200)
    dy = random.randint(-200, 200)
    nuevo_x = x + dx
    nuevo_y = y + dy

    print("Moviendo el raton...")
    # Asegura que la nueva posición no esté demasiado cerca de los bordes
    if (nuevo_x < margen or nuevo_x > screen_width - margen or
        nuevo_y < margen or nuevo_y > screen_height - margen):
        print("Movimiento evitaría el margen, moviendo al centro.")
        pyautogui.moveTo(centro_x, centro_y, duration=0.2)
    else:
        pyautogui.moveTo(nuevo_x, nuevo_y, duration=0.2)
        

if __name__ == "__main__":
    while True:
        tiempo_min = 5
        tiempo_max = 30
        intervalo = random.randint(tiempo_min, tiempo_max)
        print(f"Esperando {intervalo} segundos...")
        time.sleep(intervalo)

        mover_mouse_aleatorio()