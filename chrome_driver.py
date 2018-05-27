import wait
import os
from selenium import webdriver

def execute(url):
    driver = webdriver.Chrome(os.environ["CHROME_PATH"])
    driver.get(url)
    search_box = driver.find_element_by_id('lst-ib')
    wait.animation('start', 10)
    search_box.send_keys('Welcome To Giggles\' Land')
    wait.animation('end', 10)
    driver.quit()
