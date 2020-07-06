from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = 'c:/Users/Hm/Downloads/chromedriver/chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get("https://www.facebook.com")

element = driver.find_element_by_id("email")
element.send_keys("youremail")

element = driver.find_element_by_id("pass")
element.send_keys("yourpassword")

element.send_keys(Keys.RETURN)

#Be Sure to Subscribe My Youtube Channel #GhazaliLarik
