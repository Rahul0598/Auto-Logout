from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://quora.com")

form = driver.find_element_by_class_name("regular_login")

uname = form.find_element_by_name('email')
uname.send_keys('devajjir@gmail.com')

pword = form.find_element_by_name('password')
pword.send_keys('123456')
pword.send_keys(Keys.RETURN)

time.sleep(10)

dropDown = driver.find_element_by_class_name("MoreNavItem")
dropDown.click();
time.sleep(5)
l1 = dropDown.find_element_by_class_name("LegalNavLinks")
logout = l1.find_element_by_class_name("logout")
logout.click()

time.sleep(3)

uname.set_attribute
