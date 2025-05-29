import time
import random
import pyautogui
import webbrowser
import os
import keyboard
from selenium.webdriver.edge.service import Service
from mouseMover import mover_mouse_aleatorio	

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
except ImportError:
    webdriver = None

try:
    import openpyxl
except ImportError:
    openpyxl = None


def verificar_estado_web():
    urls = [
        "https://www.wikipedia.org/",
        "https://www.python.org/",
        "https://www.microsoft.com/"
    ]
    url = random.choice(urls)
    if webdriver is None:
        print("Selenium no está instalado.")
        return
    service = Service()
    driver = webdriver.Edge(service=service)
    driver.get(url)
    print("Verificando estado web con Selenium.")
    time.sleep(3)
    driver.quit()

def generar_reporte_excel():
    try:
        import xlwings as xw
    except ImportError:
        print("xlwings no está instalado.")
        return

    filename = f"reporte_{random.randint(1000,9999)}.xlsx"
    filepath = os.path.join(os.getcwd(), filename)
    app = xw.App(visible=True)
    wb = app.books.add()
    sht = wb.sheets[0]
    sht['A1'].value = "Reporte"
    sht['B1'].value = random.randint(1, 100)
    wb.save(filepath)
    print(f"Reporte Excel generado y abierto: {filename}")
    app.quit()
    time.sleep(5)
    os.remove(filepath)

def registrar_actividad():
    print("Pulsando teclas")
    keyboard.press_and_release('down')
    time.sleep(1)
    keyboard.press_and_release('down')
    time.sleep(1)
    keyboard.press_and_release('down')
    time.sleep(1)
    keyboard.press_and_release('right')
    time.sleep(1)
    keyboard.press_and_release('up')
    

tareas = [
    mover_mouse_aleatorio,
    verificar_estado_web,
    registrar_actividad,
    generar_reporte_excel
]

if __name__ == "__main__":
    while True:
        tarea = random.choice(tareas)
        try:
            tarea()
        except Exception as e:
            print(f"Error en {tarea.__name__}: {e}")
        tiempo = random.randint(5, 10)
        print(f"Esperando {tiempo} segundos...\n")
        time.sleep(tiempo)