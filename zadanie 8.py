from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="D:\\Kyrs Python\\testing automatization\\Chromdriver\\chromedriver.exe")
driver.get("https://chercher.tech/practice/implicit-wait-example")
driver.maximize_window()

waiter = webdriver.support.wait.WebDriverWait(driver, 15)
waiter.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div/div/div/div[1]/div[1]/div[2]/input[1]")))
cb1=driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[2]/input[1]").click()
waiter.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[2]/input[2]")))
cb2=driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[2]/input[2]").click()
waiter.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[2]/input[3]")))
cb3=driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[2]/input[3]").click()
waiter.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[2]/input[4]")))
cb4=driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[2]/input[4]").click()
waiter.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[2]/input[5]")))
cb5=driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[2]/input[5]").click()
waiter.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[2]/input[6]")))
cb5=driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[2]/input[6]").click()

time.sleep(3)
driver.quit()
