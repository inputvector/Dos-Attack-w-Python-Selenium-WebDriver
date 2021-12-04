import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import datetime
import sys

PATH= "/usr/local/bin/chromedriver"
ser = Service(PATH)
op = webdriver.ChromeOptions()
op.add_argument("--headless") #prevents browser opens every time
driver = webdriver.Chrome(service=ser, options=op)
driver.get("http://54.183.211.190/") 
driver.set_window_size(1133, 1025)
driver.find_element(By.ID, "song").click()
driver.find_element(By.ID, "ccn").click()
driver.find_element(By.ID, "ccn").send_keys("1234567")
driver.find_element(By.NAME, "submitb").click()
res_file = open("/Users/bekir/Documents/DosResult.txt","a")
res_file.writelines(str(datetime.datetime.now())+"========================================= \n")
res_file.writelines(driver.page_source + "\n")
