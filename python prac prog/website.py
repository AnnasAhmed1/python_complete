from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# Step 1) Open Firefox 
browser = webdriver.Firefox()
# Step 2) Navigate to Facebook
browser.get("http://www.facebook.com")
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit   = browser.find_element_by_id("loginbutton")
username.send_keys("annastejani123@gmail.com")
password.send_keys("eat160902")
# Step 4) Click Login
submit.click()