#Test case 1
# "[PIL QA 2022] [SPRINT 3] Verificar que se muestre el mensaje de validación en caso de que el usuario deje los campos 'E-mail' y 'Contraseña' en blanco"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#Ingresa a la page

driver = webdriver.Edge(executable_path=r"edgedriver_win64\msedgedriver.exe")
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
login = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div/section/div[1]/button")
login.click()

#Hace clic en el boton "Entrar"
entrar = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/form/div[4]/div/button")
entrar.click()
time.sleep(10)

driver.close()