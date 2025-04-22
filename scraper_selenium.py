from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os

# Directorio donde se guardarán los PDF
download_dir = os.path.abspath("descargas_pdf")

# Configurar opciones de Chrome
options = Options()
# options.add_argument("--headless")  # Si querés ver el navegador, comentá esta línea
options.add_argument("--disable-gpu")
# Opción para descargar archivos PDF automáticamente
options.add_experimental_option(
    "prefs",
    {
        "download.default_directory": download_dir,
        "plugins.always_open_pdf_externally": True,  # Forzar descarga de PDFs
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "profile.default_content_settings.popups": 0,
    },
)

# Iniciar el WebDriver
driver = webdriver.Chrome(options=options)
# Esperar que cargue el formulario
wait = WebDriverWait(driver, 10)
driver.get("https://www.csj.gov.py/ResolucionesWeb/Formularios/inicio.aspx")


# 1. Cargar FECHA DESDE
fecha_desde = wait.until(
    EC.presence_of_element_located((By.ID, "MainContent_datepickerDesde"))
)
fecha_desde.clear()
fecha_desde.send_keys("01-01-20")

# 2. Seleccionar DESPACHO ORIGEN
despacho_dropdown = Select(
    wait.until(EC.presence_of_element_located((By.ID, "MainContent_ddSalas")))
)
despacho_dropdown.select_by_value(
    "49"  # Cambia el valor según el despacho que quieras seleccionar
)

# 3. Seleccionar TIPO DE RESOLUCIÓN
tipo_res_dropdown = Select(
    wait.until(EC.presence_of_element_located((By.ID, "MainContent_ddTipoResolucion")))
)
tipo_res_dropdown.select_by_value(
    "2"
)  # Cambia el valor según el tipo de resolución que quieras seleccionar

# 4. Hacer clic en el botón Buscar
btn_buscar = wait.until(EC.element_to_be_clickable((By.ID, "MainContent_btnFiltro")))
btn_buscar.click()

# 5. Esperar los resultados (la tabla)
wait.until(EC.presence_of_element_located((By.ID, "divResultadoBusqueda")))

# 🧲 Buscar todos los links de PDF usando un patrón en el ID
pdf_links = driver.find_elements(
    By.XPATH, "//a[starts-with(@id, 'MainContent_listaResultadoTabla_lnkabrirPdf_')]"
)

print(f"🔍 Se encontraron {len(pdf_links)} links de PDF.")

cantidad_total_de_links = len(pdf_links)
# Verificar si hay más de 100 resultados
if cantidad_total_de_links > 100:
    print(
        "⚠️ Hay más de 100 resultados. Por favor, ajusta los filtros para reducir la cantidad de resultados."
    )
    driver.quit()

# 🧨 Descargar uno por uno
for i in range(0, cantidad_total_de_links):
    try:
        # Reobtené el elemento cada vez
        link = driver.find_element(
            By.ID, f"MainContent_listaResultadoTabla_lnkabrirPdf_{i}"
        )
        print(f"⬇️ Descargando PDF {i + 1}...")
        link.click()
        time.sleep(3)
    except Exception as e:
        print(f"❌ Error al descargar el PDF {i + 1}: {e}")

driver.quit()
print("✅ Proceso completo. PDFs descargados en:", download_dir)
# Fin del script
