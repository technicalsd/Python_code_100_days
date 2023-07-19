from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)


driver.get("https://londonappbrewery.com/sendy/subscription?f=m7"
           "Xj2bDOCQnlJ27yezLEAtJi1mhUIxOaJcJGZYMLLX6wx5MZd0b2FunBI8dOomNt&_ga=2.37450080.1317678701.1679193598-1391208777.1679193598")

time.sleep(10)

name = driver.find_element("name","name")


name.send_keys("Saurabh Deulkar")

email = driver.find_element("name","email")

email.send_keys("arundeulkar71@gmail.com")

gdpr = driver.find_element("name","gdpr")

gdpr.click()


link = driver.find_element('link text',"Subscribe to list")

link.click()

time.sleep(60)