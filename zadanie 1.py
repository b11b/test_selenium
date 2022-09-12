from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="D:\\Kyrs Python\\testing automatization\\Chromdriver\\chromedriver.exe")
driver.get("https://chercher.tech/practice/dropdowns")
driver.maximize_window()
time.sleep(2)


#Перебор списка product

dropdown_product = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[2]/div[1]/select" )
dd_product_options = Select(dropdown_product)

x = 0
while x <= 4:
          dd_product_options.select_by_index(x)
          time.sleep(1)
          x += 1
          print(dd_product_options.first_selected_option.text)


#Перебор списка animals
dropdown_animals = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[2]/div[2]/select")
dd_animals_option  = Select(dropdown_animals)

x = 0
while x <= 3:
         dd_animals_option.select_by_index(x)
         time.sleep(1)
         x += 1
         print(dd_animals_option.first_selected_option.text)

time.sleep(2)

#Проверка списка в drop made using
dropdown_made_using = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[2]/div[5]/div[1]/button")
dropdown_made_using.click()
time.sleep(1)
dropdown_made_using_ul = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[2]/div[5]/div[1]/ul")
items = dropdown_made_using_ul.find_elements(By.TAG_NAME, "li")
for item in items:
    text = item.text
    print(text)
time.sleep(1)

#Выбор значений в Food Items
food_items = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/p/select")
f_i = Select(food_items)
x=0
while x < 4:
      f_i.select_by_index(x)
      time.sleep(1)
      print(f_i.first_selected_option.text)
      f_i.deselect_by_index(x)
      x += 1
      time.sleep(1)
x=0
while x <= 3:
      f_i.select_by_index(x)
      x += 1

time.sleep(2)

driver.quit()

