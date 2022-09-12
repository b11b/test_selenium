from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver import ActionChains


driver = webdriver.Chrome(executable_path="D:\\Kyrs Python\\testing automatization\\Chromdriver\\chromedriver.exe")
driver.get("https://chercher.tech/practice/hidden-division-popup")
driver.implicitly_wait(5)




#open popup
popbtn = driver.find_element(By.XPATH, "/html/body/a")
popbtn.click()
time.sleep(2)

#добавление файла
fileadd = driver.find_element(By.XPATH, "/html/body/div/div/ul[2]/li/input")
fileadd.send_keys("D:/Kyrs Python/testing automatization/docTOadd.txt")


#alert
alert = driver.find_element(By.XPATH, "/html/body/div/div/ul[1]/li[2]/button").click()
time.sleep(2)
print("Текс модального окна:", driver.switch_to.alert.text)
driver.switch_to.alert.accept()

#добавление имени
name = driver.find_element(By.XPATH, "/html/body/div/div/input")
name.send_keys("Hello world")
time.sleep(2)
closebtn = driver.find_element(By.XPATH, "/html/body/div/div/ul[1]/li[1]/button").click()








time.sleep(3)
driver.quit()