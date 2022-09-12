from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="D:\\Kyrs Python\\testing automatization\\Chromdriver\\chromedriver.exe")
driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")
driver.maximize_window()
time.sleep(2)

clickbtn = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[2]/button[1]").click()
wait = WebDriverWait(driver, 6).until(EC.alert_is_present())
print("Текс модального окна:", driver.switch_to.alert.text)
time.sleep(2)
driver.switch_to.alert.accept()

clickbtn2 = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[2]/button[2]").click()
time.sleep(10)
textcheck = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[2]/h2")
if textcheck.text == "Selenium Webdriver":
    print(textcheck.text)
else:
    print("Faild")


clickbtn3 = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[2]/button[3]").click()
time.sleep(10)
clbs = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[2]/button[4]")
print(clbs.text)
clbs.click()
time.sleep(10)


clickbtn4 = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[2]/button[5]" ).click()
time.sleep(10)
cbs3 = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[2]/button[6]").click()
time.sleep(2)


clickbtn5 = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[2]/button[7]").click()
time.sleep(10)


time.sleep(3)
driver.quit()