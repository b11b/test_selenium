from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome(executable_path="D:\\Kyrs Python\\testing automatization\\Chromdriver\\chromedriver.exe")

driver.get("https://chercher.tech/practice/dynamic-table")
driver.maximize_window()
time.sleep(2)

#section 1
x=0
y=0
s1_blueberry = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[1]/button[1]")
s1_blueberry.click()
check_window = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[2]/h1")
if check_window.text == "Blueberry":
    x += 1

else:
    y += 1


time.sleep(1)

s1_bannana = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[1]/button[2]")
s1_bannana.click()
if check_window.text == "Banana":
    x += 1

else:
    y += 1


time.sleep(1)

s1_strawberry = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[1]/button[3]")
s1_strawberry.click()
if check_window.text == "Strawberry":
        x += 1

else:
        y += 1
if x == 3:
    print("section 1 = pass")
else:
    print("section 1 = fail", "number fail", y)
time.sleep(1)


#section 2
x=0
s2_apple = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/button[1]")
s2_apple.click()


if check_window.text == "Apple":
    x += 1
else:
    print("Section 2 = fail")
time.sleep(1)

s2_orange = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/button[2]")
s2_orange.click()
if check_window.text == "Orange":
    x += 1
else:
    print("Section 2 = fail")
time.sleep(1)

s2_grape = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[2]/button[3]")
s2_grape.click()
if check_window.text == "Grape":
    x += 1
else:
    print("Section 2 = fail")
time.sleep(1)
if x == 3:
    print("section 2 = pass")
else:
    print("section 2 = fail")

#section 3

x=0
s3_pie = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[3]/button[1]")
s3_pie.click()
if check_window.text == "Pie":
    x += 1
else:
    print("Section 3 = fail")
time.sleep(1)

s3_Burger = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[3]/button[2]")
s3_Burger.click()
if check_window.text == "Burger":
    x += 1
else:
    print("Section 3 = fail")
time.sleep(1)

s3_juice = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[3]/button[3]")
s3_juice.click()
if check_window.text == "Juice":
    x += 1
else:
    print("Section 3 = fail")
time.sleep(1)
if x == 3:
    print("section 3 = pass")
else:
    print("section 3 = fail")


#Lowercase Section 3
x=0
ls3_banana = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[4]/button[1]")
ls3_banana.click()
if check_window.text == "banana":
    x += 1
else:
    print("Lowercase section 3 = fail")
time.sleep(1)

ls3_bananashake = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[4]/button[2]")
ls3_bananashake.click()
if check_window.text == ("Banana\nShake"):
    x += 1
else:
    print("Lowercase section 3 = fail")
time.sleep(1)

ls_bananajuice =driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[4]/button[3]")
ls_bananajuice.click()
if check_window.text == ('Banana "Juice'):
    x += 1
else:
    print("Lowercase section 3 = fail")
time.sleep(1)

ls_zs = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/div/div[1]/div[4]/input")
ls_zs.click()
if check_window.text == ('Zack Snyder'):
    x += 1
else:
    print("Lowercase section 3 = fail")
time.sleep(1)
if x == 4:
    print("Lowercase section 3 = pass")
else:
    print("Lowercase section 3 = fail")

#Dynamic Table Shuffles on refresh
#Выделить все чекбоксы
cbo1 = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/table/tbody/tr[2]/td[1]/input")
cbo2 = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/table/tbody/tr[3]/td[1]/input")
cbo3 = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/table/tbody/tr[4]/td[1]/input")
cbo4 = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/table/tbody/tr[5]/td[1]/input")
cbo1.click()
cbo2.click()
cbo3.click()
cbo4.click()
time.sleep(2)
cbo1.click()
cbo2.click()
cbo3.click()
cbo4.click()
time.sleep(2)


#Выбор только чекбокса selenium
cb1 = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/table/tbody/tr[2]/td[2]")
cb2 = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/table/tbody/tr[3]/td[2]")
cb3 = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/table/tbody/tr[4]/td[2]")
cb4 = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[1]/table/tbody/tr[5]/td[2]")
cbmas = cb1.text, cb2.text, cb3.text, cb4.text
j=0
while j <=3:
    if cbmas[j] == "selenium-webdriver.com":
        z = j
        break
    else:
        j+=1
cbomas = cbo1, cbo2, cbo3, cbo4
checkbox = cbomas[z]
checkbox.click()
time.sleep(2)
checkbox.click()

time.sleep(1)
driver.quit()
