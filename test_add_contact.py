# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from classes.contact import Contact
import unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_main_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login_as(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def send_keys_to_element_by_name(self, wd, name, value):
        """
        :param wd: webdriver
        :param name: element name
        :param value: sending keys, if they present
        :return:
        """
        if value is not None:
            wd.find_element_by_name(name).click()
            wd.find_element_by_name(name).clear()
            wd.find_element_by_name(name).send_keys(value)

    def add_contact(self, wd, contact):
        wd.get("http://localhost/addressbook/edit.php")
        self.send_keys_to_element_by_name(wd, "firstname", contact.first_name)
        self.send_keys_to_element_by_name(wd, "middlename", contact.mid_name)
        self.send_keys_to_element_by_name(wd, "lastname", contact.last_name)
        self.send_keys_to_element_by_name(wd, "nickname", contact.nick_name)
        self.send_keys_to_element_by_name(wd, "title", contact.title)
        self.send_keys_to_element_by_name(wd, "company", contact.company)
        self.send_keys_to_element_by_name(wd, "address", contact.adress)
        self.send_keys_to_element_by_name(wd, "home", contact.home_phone)
        self.send_keys_to_element_by_name(wd, "mobile", contact.mobile_phone)
        self.send_keys_to_element_by_name(wd, "work", contact.work_phone)
        self.send_keys_to_element_by_name(wd, "fax", contact.fax)
        self.send_keys_to_element_by_name(wd, "email", contact.email_prime)
        self.send_keys_to_element_by_name(wd, "email2", contact.email_secondary)
        self.send_keys_to_element_by_name(wd, "email3", contact.email_third)
        self.send_keys_to_element_by_name(wd, "homepage", contact.home_page)
        self.send_keys_to_element_by_name(wd, "firstname", contact.first_name)
        # u'изменение дня рождения'
        xpath_birthday_day = "//div[@id='content']/form/select[1]//option[" + contact.birthday_day + "]"
        wd.find_element_by_xpath(xpath_birthday_day).click()
        # u'изменение месяца рождения'
        xpath_birthday_month = "//div[@id='content']/form/select[2]//option[" + contact.birthday_month + "]"
        wd.find_element_by_xpath(xpath_birthday_month).click()
        self.send_keys_to_element_by_name(wd, "byear", contact.birthday_year)
        # u'изменение дня юбилея'
        xpath_anniversary_day = "//div[@id='content']/form/select[3]//option[" + contact.anniversary_day + "]"
        wd.find_element_by_xpath(xpath_anniversary_day).click()
        # u'изменение месяца юбилея'
        xpath_anniversary_month = "//div[@id='content']/form/select[4]//option[" + contact.anniversary_month + "]"
        wd.find_element_by_xpath(xpath_anniversary_month).click()
        self.send_keys_to_element_by_name(wd, "ayear", contact.anniversary_year)
        self.send_keys_to_element_by_name(wd, "address2", contact.adress_secondary)
        self.send_keys_to_element_by_name(wd, "phone2", contact.phone_secondary)
        self.send_keys_to_element_by_name(wd, "notes", contact.notes)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_test_add_contact(self):
        contact = Contact.random()
        success = True
        wd = self.wd
        self.open_main_page(wd)
        self.login_as(wd, "admin", "secret")
        self.add_contact(wd, contact)
        self.logout(wd)
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
