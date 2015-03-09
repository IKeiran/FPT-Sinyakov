# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time

success = True
wd = WebDriver()
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("http://localhost/addressbook/")
    wd.find_element_by_name("pass").click()
    wd.find_element_by_name("pass").send_keys("\\undefined")
    wd.find_element_by_id("LoginForm").click()
    wd.find_element_by_css_selector("input[type=\"submit\"]").click()
    wd.find_element_by_link_text("add new").click()
    wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
    wd.find_element_by_link_text("home page").click()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
