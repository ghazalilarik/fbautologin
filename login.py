from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = 'c:/Users/Hm/Downloads/chromedriver/chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get("https://www.facebook.com")

search = driver.find_element_by_id("email")
search.send_keys("youremail")

search = driver.find_element_by_id("pass")
search.send_keys("yourpassword")

search.send_keys(Keys.RETURN)