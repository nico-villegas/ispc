# Test Case 2
#"[PIL QA 2022] [SPRINT 3] La contraseña esta enmascarada cuando se escribe en el campo 'Contraseña' "  

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

# Cierra el popup

webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
time.sleep(5)

# Ingresa a la página de login

login = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div[2]/div/div/div[1]/a[2]")
login.click()
time.sleep(20)

# Cierra el popup

login = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div/section/div[1]/button")
login.click()

# Rellena el campo "E-mail"

usuario = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/form/div[1]/label/div/input")
usuario.send_keys("nicovillegas650@gmail.com")
usuario.send_keys(Keys.TAB)
time.sleep(5)

# Rellena el campo "Contraseña"

contrasenia = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/form/div[2]/div/label/div/input")
contrasenia.send_keys("Nico1234")
time.sleep(5)

# Test
text_esperado = "password"
type = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/form/div[2]/div/label/div/input").get_attribute("type")
assert type == text_esperado, "No se muestra mensaje de validacion"
print("_________________ \n")
print("Pass \n")
print("_________________")

driver.close()