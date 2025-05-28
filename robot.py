import time
import random
import pyautogui
import webbrowser
import os

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
except ImportError:
    webdriver = None

try:
    import openpyxl
except ImportError:
    openpyxl = None

def actualizar_cursor():
    x, y = pyautogui.position()
    dx = random.randint(-50, 50)
    dy = random.randint(-50, 50)
    pyautogui.moveTo(x + dx, y + dy, duration=0.2)

def consultar_documentacion_web():
    urls = [
        "https://www.wikipedia.org/",
        "https://www.python.org/",
        "https://www.microsoft.com/"
    ]
    url = random.choice(urls)
    webbrowser.open(url)
    print(f"Consultando documentación: {url}")

def verificar_estado_web():
    if webdriver is None:
        print("Selenium no está instalado.")
        return
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.example.com")
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
    filepath = os.path.abspath(filename)
    app = xw.App(visible=True)
    wb = app.books.add()
    sht = wb.sheets[0]
    sht['A1'].value = "Reporte"
    sht['B1'].value = random.randint(1, 100)
    wb.save(filepath)
    print(f"Reporte Excel generado y abierto: {filename}")

def registrar_actividad():
    pyautogui.press('shift')
    print("Actividad registrada.")

tareas = [
    actualizar_cursor,
    consultar_documentacion_web,
    verificar_estado_web,
    generar_reporte_excel,
    registrar_actividad
]

if __name__ == "__main__":
    while True:
        tarea = random.choice(tareas)
        try:
            tarea()
        except Exception as e:
            print(f"Error en {tarea.__name__}: {e}")
        tiempo = random.randint(30, 120)
        print(f"Esperando {tiempo} segundos...\n")
        time.sleep(tiempo)