#Test case 1
# "[PIL QA 2022] [SPRINT 3] Verificar que se muestre el mensaje de validación en caso de que el usuario deje los campos 'E-mail' y 'Contraseña' en blanco"

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#Ingresa a la page

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://shop.samsung.com/ar/")
time.sleep(5)

#Cierra el popup 
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
time.sleep(5)

#Entra en la pagina de login
login = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div[2]/div/div/div[1]/a[2]")
login.click()
time.sleep(20)

#Cierra el popup
login_popup = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div/section/div[1]/button")
login_popup.click()

#Hace clic en el boton "Entrar"
entrar = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/form/div[4]/div/button")
entrar.click()
time.sleep(10)

# Test
text_esperado = "Entre con un e-mail válido"
text_web = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/form/div[2]").text
assert text_esperado == text_web, "No se muestra mensaje de validacion"
print("_________________ \n")
print("Pass \n")
print("_________________")

driver.close()