from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="D:\\Kyrs Python\\testing automatization\\Chromdriver\\chromedriver.exe")
driver.get("https://chercher.tech/practice/popups")
main_window = driver.current_window_handle
driver.maximize_window()
time.sleep(2)

pop1 = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[2]/input[1]").click()
time.sleep(1)
print("Текс модального окна:", driver.switch_to.alert.text)
driver.switch_to.alert.accept()


pop2 = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[2]/input[2]").click()
time.sleep(1)
print("Текс модального окна:", driver.switch_to.alert.text)
driver.switch_to.alert.accept()

#К СОЖАЛЕНИЮ С ДАННЫМ ОКНОМ НЕ У МЕНЯ НЕ ПОЛУЧИЛОСЬ ПОВЗАИМОЙДЕСТОВАТЬ, БУДУ РАЗБИРАТЬСЯ ДАЛЬШЕ.

#pop3 = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[2]/input[3]").click()
#time.sleep(1)
#prompt = Alert(driver)
#print("Текс модального окна:", driver.switch_to.alert.text)
#prompt.send_keys("123")
#time.sleep(3)
#prompt.accept()


#Добавление файла
fileadd = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[2]/input[5]")
fileadd.send_keys("D:/Kyrs Python/testing automatization/docTOadd.txt")
time.sleep(2)
file_dl = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[2]/input[4]").click()


#Проверка ссылок в sub_menu
#1
sub_menu = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[3]/div/button")
achains = ActionChains(driver)
achains.move_to_element(sub_menu).perform()
time.sleep(3)
cct = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[3]/div/div/a[1]").click()
url1 = driver.current_url
if url1 == "https://chercher.tech/":
    print("CherCherTech pass")
else:
    print("Failed CherCher")
time.sleep(1)
driver.back()

#2
sub_menu = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[3]/div/button")
achains = ActionChains(driver)
achains.move_to_element(sub_menu).perform()
time.sleep(3)
cct = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[3]/div/div/a[2]").click()
url2 = driver.current_url
if url2 == "https://www.google.com/":
    print("Google pass")
else:
    print("Failed Google")
time.sleep(1)
driver.back()

#3
#Переход корректный, но значения параметров в конце меняется, поэтому проверка fail.
sub_menu = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[3]/div/button")
achains = ActionChains(driver)
achains.move_to_element(sub_menu).perform()
time.sleep(3)
cct = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[3]/div/div/a[3]").click()
url3 = driver.current_url
if url3 == "https://www.bing.com/?toWww=1&redig=76BEA423D1024FFFB91E01CC17A7DF43":
    print("Bing pass")
else:
    print("Failed Bing")
time.sleep(1)
driver.back()


#Кнопка дабл клик
double_click_me = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[3]/input")
achains.double_click(double_click_me).perform()
time.sleep(2)
print("Текс модального окна:", driver.switch_to.alert.text)
time.sleep(1)
driver.switch_to.alert.accept()
time.sleep(3)

#Кнопка новое окно гугл
new_wind_google = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/a[1]/input").click()
driver.switch_to.window(driver.window_handles[1])
url4 = driver.current_url
if url4 == "https://www.google.com/":
    print("Google pass")
else:
    print("Failed Google")
time.sleep(1)
driver.close()
driver.switch_to.window(main_window)

#multi окна
multi_wind = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/a[2]/input").click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
url5 = driver.current_url
if url5 == "https://www.yahoo.com/":
    print("Yhoo pass")
else:
    print("Failed Yhoo")
time.sleep(2)
driver.switch_to.window(driver.window_handles[2])
url6 = driver.current_url
if url6 == "https://www.bing.com/":
    print("Bing pass")
else:
    print("Failed Bing")
time.sleep(2)
driver.switch_to.window(driver.window_handles[3])
url7 = driver.current_url
if url7 == "https://www.google.com/":
    print("Google pass")
else:
    print("Failed Google")
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[2])
driver.close()
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(main_window)

#инпут поля dolor
dolor_input1 = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[4]/input[1]")
dolor_input1.send_keys("123")
dolor_input2 = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[4]/input[2]")
dolor_input2.send_keys("321")
dolor_input3 = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[4]/input[3]")
dolor_input3.send_keys("54623")

#дроп даун и перебор значений
dolor_select = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[4]/select")
dolor_select_1 = Select(dolor_select)

x = 0
while x <= 3:
         dolor_select_1.select_by_index(x)
         time.sleep(1)
         x += 1
         print(dolor_select_1.first_selected_option.text)

#Чек боксы
checkbox = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/p[3]/input[1]").click()
time.sleep(1)

radio_btn = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/p[3]/input[2]").click()





time.sleep(3)
driver.quit()




time.sleep(3)
driver.quit()
