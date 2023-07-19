import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element("css selector", "#articlecount a")
# Because it was id we used # sign

# article_count.click()

all_portals=driver.find_element("link text","Wikipedia")

search = driver.find_element(by="name",value="search")


search.send_keys("Python")

search.send_keys(Keys.ENTER)





time.sleep(60)

# driver.quit()