from os import path, environ
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from dotenv import load_dotenv
load_dotenv()

login_url = "http://iauctb.daan.ir/login-identification-form#login-identification-form"
username = environ.get("USER")
password = environ.get("PASS")

driver = webdriver.Firefox(
    executable_path=r"C:\Users\hasan\.webdriver\geckodriver.exe")
driver.get(login_url)

# Entering user password
inputs = driver.find_elements_by_css_selector("form#signinform>div.form-group>input")
inputs[0].send_keys(username)
inputs[1].send_keys(password)
sleep(2)
driver.find_element_by_css_selector("button.btn-primary").click()

# Go Classes
sleep(2)
driver.find_element_by_partial_link_text("جلسات من").click()

# Find Exact Active Class
