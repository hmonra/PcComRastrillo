# Librerias
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from datetime import datetime

# from selenium.common.exceptions import TimeoutException

# Opciones de navegación
options = webdriver.ChromeOptions()
options.page_load_strategy = 'normal'
options.add_argument('--start')
options.add_argument('--disable-extensions')
options.add_experimental_option("excludeSwitches", ['enable-automation'])
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-software-rasterizer")
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-features=VizDisplayCompositor')
options.add_argument('--allow-insecure-localhost')
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
# options.add_argument("--incognito")
options.add_argument('window-size=1920x1080')
options.add_argument('--disable-gpu')

options.add_argument("--force-device-scale-factor=1")
options.add_argument("--ignore-ssl-errors")
options.add_argument("--ignore-certificate-errors")
options.add_argument("enable-features=NetworkServiceInProcess")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("disable-features=NetworkService")

# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36")
options.add_argument(
    "user-agent=Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36")
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36")

chrome_prefs = {}
options.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}
chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}

driver = webdriver.Chrome(executable_path=r'RUTACHROMEDRIVER', # AQUI INDICA LA RUTA DE CHROMEDRIVER
                          options=options)

driver.execute_script("window.open('');")
driver.execute_script("window.open('');")
driver.execute_script("window.open('');")

# PRODUCTO QUE SE AÑADIRÁ AL CARRO PARA PODER CARGAR ENLACE SUMMARY
summary_item = 'https://www.pccomponentes.com/cart/addItem/803821'


# Para enviar mensaje de aviso por telegram
def telegram_bot_sendtext(bot_message):
    bot_token = 'BOTTOKEN' #AQUI INDICA EL TOKEN DE TU BOT
    bot_chatID = 'CHATID' #AQUI INDICA TU CHAT ID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    driver.get(send_text)


def comprar():
    # cod atriculo
    cod_articulo = driver.find_element(By.ID, 'codigo-articulo-pc')
    cod_articulo = cod_articulo.text

    print("Stock encontrado :D")
    print("Producto: ##  " + nombre + "  ##")
    print("Comenzando el proceso de compra...")

    # Añadiendo al carrito
    enlace_compra = "https://www.pccomponentes.com/cart/addItem/" + cod_articulo

    print("Accediendo al enlace de compra...")
    driver.get(enlace_compra)

    nombre_producto = WebDriverWait(driver, 30) \
        .until(EC.element_to_be_clickable((By.CLASS_NAME, 'enlace-disimulado')))
    nombre_producto = nombre_producto.text
    print(nombre_producto)

    print("Paso a pestaña summary...")
    driver.switch_to.window(driver.window_handles[1])
    # Botón pagar y finalizar
    print("Pulsando botón de pagar y finalizar...")
    WebDriverWait(driver, 60) \
        .until(EC.visibility_of and EC.element_to_be_clickable((By.CLASS_NAME, 'sc-iqHYmW.cfUOyE.sc-fBxREx.cNhRPb'))).click()
    print("Pulsado botón de pagar y finalizar...")
    time.sleep(20)
    telegram_bot_sendtext("✅ Compra realizada ✅:  " + nombre_producto)

    if driver.current_url == 'https://www.pccomponentes.com/cart/':
        print("Compra no realizada, algo ha fallado... :(")
    else:
        print("Compra finalizada :D")
    summary()
    navegacion()


def summary():
    print("Login para precargar página summary...")
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    login()
    time.sleep(2)
    print("Añado un producto para poder acceder al enlace summary...")
    driver.get(summary_item)
    time.sleep(1)
    print(summary_item)
    print("Cambio pestaña y accedo a enlace summary...")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://www.pccomponentes.com/cart/summary')
    time.sleep(2)
    # Botón entiendo y acepto las condiciones
    print("Cargada página summary...")
    print("Dejo pulsado botón de acepto las condiciones...")
    WebDriverWait(driver, 60) \
        .until(EC.visibility_of and EC.element_to_be_clickable((By.CLASS_NAME, 'sc-gVgoRu.uKwST'))).click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    print("Vacío el carrito...")
    WebDriverWait(driver, 60) \
        .until(EC.visibility_of and EC.element_to_be_clickable((By.ID, 'GTM-carrito-vaciarcarrito'))).click()
    time.sleep(1)
    driver.get('https://www.pccomponentes.com/')


def login():
    # Borrando cookies
    driver.switch_to.window(driver.window_handles[0])
    driver.delete_all_cookies()
    print("Borrando todas las cookies...")
    # Accediendo a web para login
    print("Accediendo a página para hacer login...")
    driver.get('https://www.pccomponentes.com/login')
    time.sleep(1)
    if driver.current_url == 'https://www.pccomponentes.com/login':
        # Se hace login
        print("Introduciendo credenciales...")
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#username'))).send_keys('EMAIL-CUENTA') # EMAIL LOGIN PCCOMPONENTES
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#password'))).send_keys('CONTRASEÑA-CUENTA') # CONTRASEÑA LOGIN PCCOMPONENTES
        time.sleep(1)
        WebDriverWait(driver, 5) \
            .until(EC.element_to_be_clickable((By.CLASS_NAME, 'sc-iqHYmW.kaLStl'))).click()
        print("Login en PCC OK...")
        time.sleep(1)
        cuadro_verificacion = WebDriverWait(driver, 5) \
            .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.ID, 'login-form')))
        cuadro_verificacion = cuadro_verificacion.text
        # print(cuadro_verificacion)
        if "El e-mail o la contraseña no son correctos." in cuadro_verificacion:
            print("Problema con verificación de login, reintentando...")
            login()
        else:
            print("Login confirmado...")

    else:
        print("Falso positivo, la cuenta sigue logueada...")


def navegacion():
    driver.switch_to.window(driver.window_handles[2])
    # Aquí se inicia la navegación
    driver.get('https://www.pccomponentes.com/outlet/')
    print("")
    print("## Accediendo a url... ##")
    # Cerrar menu audio/foto/video
    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#filterMenuLateral > div > div > div:nth-child(3)'))).click()
    print("")
    print("## Cerrar menu audio/foto/video... ##")
    time.sleep(1)
    # Cerrar menu cables
    WebDriverWait(driver, 5) \
        .until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#filterMenuLateral > div > div > div:nth-child(5)'))).click()
    print("")
    print("## Cerrar menu cables... ##")
    time.sleep(1)
    # Abrir menu componentes
    WebDriverWait(driver, 5) \
        .until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#filterMenuLateral > div > div > div:nth-child(7)'))).click()
    print("")
    print("## Abrir menu componentes... ##")
    time.sleep(1)
    # Pulsar botón ver más
    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#acc-fil-531 > div > a'))).click()
    print("")
    print("## Pulsar botón ver más... ##")
    time.sleep(1)
    # Selección tarjetas gráficas
    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#acc-fil-531-2 > ul > li:nth-child(7) > a'))).click()
    print("")
    print("## Selección tarjetas gráficas... ##")
    time.sleep(1)
    # Selección rastrillo
    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#acc-fil-0 > div > ul > li:nth-child(2)'))).click()
    print("")
    print("## Selección rastrillo... ##")
    # Selección ordenar por precio
    # WebDriverWait(driver, 5) \
    #  .until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#listOrder'))).click()
    # print("")
    # print("## Selección ordenar por precio ##")
    # time.sleep(1)
    # Selección mas baratos primero
    # WebDriverWait(driver, 5) \
      #  .until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#listOrder > option:nth-child(3)'))).click()
    # print("")
    # print("## Selección mas baratos primero ##")
    time.sleep(1)
    print("")
    print("## Extracción de enlaces... ##")
    print("")
    time.sleep(1)


print("Login para precargar página summary...")
driver.switch_to.window(driver.window_handles[0])
login()
time.sleep(1)
print("Añado un producto para poder acceder al enlace summary...")
driver.get(summary_item)
time.sleep(1)
print(summary_item)
print("Cambio pestaña y accedo a enlace summary...")
driver.switch_to.window(driver.window_handles[1])
driver.get('https://www.pccomponentes.com/cart/summary')
time.sleep(2)
# Botón entiendo y acepto las condiciones
print("Cargada página summary...")
print("Dejo pulsado botón de acepto las condiciones...")
WebDriverWait(driver, 60) \
    .until(EC.visibility_of and EC.element_to_be_clickable((By.CLASS_NAME, 'sc-gVgoRu.uKwST'))).click()
time.sleep(1)
driver.switch_to.window(driver.window_handles[0])
print("Vacío el carrito...")
WebDriverWait(driver, 60) \
    .until(EC.visibility_of and EC.element_to_be_clickable((By.ID, 'GTM-carrito-vaciarcarrito'))).click()
time.sleep(1)
driver.get('https://www.pccomponentes.com/')
navegacion()


while True:
    # Comprobación de login.
    driver.switch_to.window(driver.window_handles[0])
    driver.get('https://www.pccomponentes.com/')
    cuadro_login = WebDriverWait(driver, 15) \
        .until(EC.visibility_of_element_located and EC.element_to_be_clickable((By.CLASS_NAME, 'c-user-menu.js-user-menu')))
    cuadro_login = cuadro_login.text
    if "hmonrabal@" not in cuadro_login:
        print("Detectado cierre automático de sesión, volviendo a loguear...")
        # Accediendo a web para login
        login()
    else:
        print("--Sesión OK--")
    # Comprobación de página summary.
    driver.switch_to.window(driver.window_handles[1])
    if driver.current_url == 'https://www.pccomponentes.com/cart/summary':
        print("--Página summary OK--")
    else:
        print("--Perdida página summary, creando de nuevo--")
        summary()
    # Extracción de datos.
    driver.switch_to.window(driver.window_handles[2])
    current_time = datetime.now().time()
    time.sleep(1)
    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#acc-fil-0 > div > ul > li:nth-child(2)'))).click()
    time.sleep(1)
    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#acc-fil-0 > div > ul > li:nth-child(2)'))).click()
    time.sleep(1)
    elements = driver.find_elements(By.CLASS_NAME, 'GTM-productClick.enlace-superpuesto.cy-product-hover-link')
    try:
        for e in elements:
            nombre = (e.get_attribute("data-name"))
            enlace = (e.get_attribute("href"))
            precio = (e.get_attribute("data-price"))

            if '3070' in nombre:
                print("Producto encontrado...")
                print(nombre)
                print(enlace)
                print("Precio: ", precio, "€")
                try:
                    if "LHR" in nombre:
                        print("GPU con LHR, descartada...")
                    if "Rev" in nombre:
                        print("GPU con LHR, descartada...")
                    if precio < '630':
                        driver.switch_to.window(driver.window_handles[3])
                        driver.get(enlace)
                        cuadro_carrito = WebDriverWait(driver, 10) \
                            .until(EC.visibility_of and EC.element_to_be_clickable((By.ID, 'btnsWishAddBuy')))
                        cuadro_carrito = cuadro_carrito.text
                        if "Comprar" in cuadro_carrito:
                            comprar()
                        else:
                            driver.switch_to.window(driver.window_handles[2])
                            print("🔴 No hay stock :(")
                    else:
                        print("Precio demasiado elevado...")
                except TimeoutException:
                    print("")
                    print("Url Time out..")
                    print("URL: " + enlace)
                    driver.refresh()
                    continue

            if '5700' in nombre:
                print("Producto encontrado...")
                print(nombre)
                print(enlace)
                print("Precio: ", precio, "€")
                try:
                    if precio < '420':
                        driver.switch_to.window(driver.window_handles[3])
                        driver.get(enlace)
                        cuadro_carrito = WebDriverWait(driver, 10) \
                            .until(EC.visibility_of and EC.element_to_be_clickable((By.ID, 'btnsWishAddBuy')))
                        cuadro_carrito = cuadro_carrito.text
                        if "Comprar" in cuadro_carrito:
                            comprar()
                        else:
                            driver.switch_to.window(driver.window_handles[2])
                            print("🔴 No hay stock :(")
                    else:
                        print("Precio demasiado elevado...")
                except TimeoutException:
                    print("")
                    print("Url Time out..")
                    print("URL: " + enlace)
                    driver.refresh()
                    continue

            if '1660 Ti' in nombre:
                print("Producto encontrado...")
                print(nombre)
                print(enlace)
                print("Precio: ", precio, "€")
                try:
                    if precio < '235':
                        driver.switch_to.window(driver.window_handles[3])
                        driver.get(enlace)
                        cuadro_carrito = WebDriverWait(driver, 10) \
                            .until(EC.visibility_of and EC.element_to_be_clickable((By.ID, 'btnsWishAddBuy')))
                        cuadro_carrito = cuadro_carrito.text
                        if "Comprar" in cuadro_carrito:
                            comprar()
                        else:
                            driver.switch_to.window(driver.window_handles[2])
                            print("🔴 No hay stock :(")
                    else:
                        print("Precio demasiado elevado...")
                except TimeoutException:
                    print("")
                    print("Url Time out..")
                    print("URL: " + enlace)
                    driver.refresh()
                    continue

            if '3060 Ti' in nombre:
                print("Producto encontrado...")
                print(nombre)
                print(enlace)
                print("Precio: ", precio, "€")
                try:
                    if "LHR" in nombre:
                        print("GPU con LHR, descartada...")
                    if "Rev" in nombre:
                        print("GPU con LHR, descartada...")
                    if precio < '450':
                        driver.switch_to.window(driver.window_handles[3])
                        driver.get(enlace)
                        cuadro_carrito = WebDriverWait(driver, 10) \
                            .until(EC.visibility_of and EC.element_to_be_clickable((By.ID, 'btnsWishAddBuy')))
                        cuadro_carrito = cuadro_carrito.text
                        if "Comprar" in cuadro_carrito:
                            comprar()
                        else:
                            driver.switch_to.window(driver.window_handles[2])
                            print("🔴 No hay stock :(")
                    else:
                        print("Precio demasiado elevado...")
                except TimeoutException:
                    print("")
                    print("Url Time out..")
                    print("URL: " + enlace)
                    driver.refresh()
                    continue

            if '1660 SUPER' in nombre:
                print("Producto encontrado...")
                print(nombre)
                print(enlace)
                print("Precio: ", precio, "€")
                try:
                    if precio < '235':
                        driver.switch_to.window(driver.window_handles[3])
                        driver.get(enlace)
                        cuadro_carrito = WebDriverWait(driver, 10) \
                            .until(EC.visibility_of and EC.element_to_be_clickable((By.ID, 'btnsWishAddBuy')))
                        cuadro_carrito = cuadro_carrito.text
                        if "Comprar" in cuadro_carrito:
                            comprar()
                        else:
                            driver.switch_to.window(driver.window_handles[2])
                            print("🔴 No hay stock :(")
                    else:
                        print("Precio demasiado elevado...")
                except TimeoutException:
                    print("")
                    print("Url Time out..")
                    print("URL: " + enlace)
                    driver.refresh()
                    continue

            if '5600' in nombre:
                print("Producto encontrado...")
                print(nombre)
                print(enlace)
                print("Precio: ", precio, "€")
                try:
                    if precio < '280':
                        driver.switch_to.window(driver.window_handles[3])
                        driver.get(enlace)
                        cuadro_carrito = WebDriverWait(driver, 10) \
                            .until(EC.visibility_of and EC.element_to_be_clickable((By.ID, 'btnsWishAddBuy')))
                        cuadro_carrito = cuadro_carrito.text
                        if "Comprar" in cuadro_carrito:
                            comprar()
                        else:
                            driver.switch_to.window(driver.window_handles[2])
                            print("🔴 No hay stock :(")
                    else:
                        print("Precio demasiado elevado...")
                except TimeoutException:
                    print("")
                    print("Url Time out..")
                    print("URL: " + enlace)
                    driver.refresh()
                    continue

            else:
                driver.switch_to.window(driver.window_handles[2])
                print(nombre)
                print(enlace)
                print("Producto no coincide o sin stock...", current_time)
    except TimeoutException:
        print("")
        print("Url Time out..")
        navegacion()
        continue
