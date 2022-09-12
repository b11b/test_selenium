from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="D:\\Kyrs Python\\testing automatization\\Chromdriver\\chromedriver.exe")

driver.get("https://chercher.tech/practice/frames-example-selenium-webdriver")
driver.maximize_window()
time.sleep(2)

#заполнение топик
driver.switch_to.frame(driver.find_element(By.ID, "frame1"))
topic = driver.find_element(By.XPATH, "/html/body/input").send_keys("123")

#чекбокс
driver.switch_to.frame(driver.find_element(By.ID, "frame3"))
checkbox = driver.find_element(By.XPATH, "/html/body/input").click()

#возвращение на главный фрейм
driver.switch_to.default_content()

#Список перебор
driver.switch_to.frame(driver.find_element(By.ID, "frame2"))
drop_animals = driver.find_element(By.XPATH, "/html/body/select")
select_d_animals = Select(drop_animals)
select_d_animals.select_by_index(3)
time.sleep(2)
select_d_animals.select_by_index(2)
time.sleep(2)
select_d_animals.select_by_index(1)
time.sleep(2)
select_d_animals.select_by_index(0)
time.sleep(2)
select_d_animals.select_by_index(1)










time.sleep(3)
driver.quit()
