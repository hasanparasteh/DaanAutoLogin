from os import environ, path
from time import sleep

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from win10toast import ToastNotifier

load_dotenv()

toaster = ToastNotifier()
login_url = "http://iauctb.daan.ir/login-identification-form#login-identification-form"
username = environ.get("USER")
password = environ.get("PASS")

driver = webdriver.Firefox(
    executable_path=r"C:\Users\hasan\.webdriver\geckodriver.exe")
driver.get(login_url)

# Entering user password
inputs = driver.find_elements_by_css_selector(
    "form#signinform>div.form-group>input")
inputs[0].send_keys(username)
inputs[1].send_keys(password)
sleep(2)
driver.find_element_by_css_selector("button.btn-primary").click()

# Go Classes
sleep(2)
driver.find_element_by_partial_link_text("جلسات من").click()

# Find Exact Active Class
try:
    class_login_btn = driver.find_elements_by_partial_link_text("ورود دانشجو")

    if len(class_login_btn) != 0:
        for i in range(len(class_login_btn)):
            if not class_login_btn[i].get_attribute('data-target') == ".session_not_reach":
                toaster.show_toast(
                    "I'm in class", "Please don't make any sound...Teacher is talking")
                class_login_btn[i].click()
except NoSuchElementException:
    toaster.show_toast("No Active Classes",
                       "Horayyyy!! There is nothing to do...")
