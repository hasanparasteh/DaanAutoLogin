from os import environ, path
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from win10toast import ToastNotifier

from dotenv import load_dotenv
load_dotenv()


def is_session_not_reached(elm):
    if elm.get_attribute('data-target') == ".session_not_reach":
        return True
    else:
        False


def is_teacher_not_in_class(elm):
    if elm.get_attribute('data-target') == ".teacher-not-entered-classroom":
        return True
    else:
        False


toaster = ToastNotifier()

login_url = "http://iauctb.daan.ir/login-identification-form#login-identification-form"
username = environ.get("USER")
password = environ.get("PASS")
geckodriver = environ.get("GECKO")

driver = webdriver.Firefox(executable_path=geckodriver)
driver.get(login_url)

# Entering user password
inputs = driver.find_elements_by_css_selector(
    "form#signinform>div.form-group>input")
inputs[0].send_keys(username)
inputs[1].send_keys(password)
sleep(5)
driver.find_element_by_css_selector("button.btn-primary").click()

# Go Classes list
sleep(5)
driver.find_element_by_partial_link_text("جلسات من").click()

# Login into class
not_in_class = True
while not_in_class:
    try:
        class_login_btn = driver.find_elements_by_partial_link_text(
            "ورود دانشجو")

        for i in range(len(class_login_btn)):

            if is_teacher_not_in_class(class_login_btn[i]):
                toaster.show_toast("Teacher is not here...", "I have to retry logging in...")
                sleep(60)  # wait for 1 min

            if is_session_not_reached(class_login_btn[i]):
                toaster.show_toast("Too Soon....! I'll wait for 15 min :)")
                sleep(900)  # wait for 15 min

            if not is_session_not_reached(class_login_btn[i]) and not is_teacher_not_in_class(class_login_btn[i]):
                toaster.show_toast("I'm about to login!", "Don't make any sound..I'm going in :)")
                class_login_btn[i].click()
                not_in_class = False

    except NoSuchElementException:
        toaster.show_toast("No Active Classes",
                           "Horayyyy!! There is nothing to do...")
