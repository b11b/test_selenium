
#Данное задание не получилось выполнить, буду дальше искать причину.

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

driver.get("https://chercher.tech/practice/drag-drop.html")
#driver.get("https://qavbox.github.io/demo/dragndrop/")
driver.maximize_window()
time.sleep(3)

action_chains = ActionChains(driver)

source = driver.find_element(By.XPATH, "/html/body/div[1]")
dest = driver.find_element(By.ID, "destination")
action_chains.move_to_element(dest).perform()


time.sleep(1)
driver.quit()