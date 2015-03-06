# -*- coding: utf-8 -*-

from selenium.webdriver.firefox.webdriver import WebDriver

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_main_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def login_as(self, username, password):
        wd = self.wd
        self.open_main_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text('group page').click()

    def add_new_group(self, group):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def return_to_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def destroy(self):
        self.wd.quit()


    def send_keys_to_element_by_name(self, name, value):
        """
        :param wd: webdriver
        :param name: element name
        :param value: sending keys, if they present
        :return:
        """
        wd = self.wd
        wd.find_element_by_name(name).clear()
        wd.find_element_by_name(name).send_keys(value)
        if value is not None:
          wd.find_element_by_name(name).click()


    def add_contact(self, contact):
        wd = self.wd
        wd.get("http://localhost/addressbook/edit.php")
        self.send_keys_to_element_by_name("firstname", contact.first_name)
        self.send_keys_to_element_by_name("middlename", contact.mid_name)
        self.send_keys_to_element_by_name("lastname", contact.last_name)
        self.send_keys_to_element_by_name("nickname", contact.nick_name)
        self.send_keys_to_element_by_name("title", contact.title)
        self.send_keys_to_element_by_name("company", contact.company)
        self.send_keys_to_element_by_name("address", contact.adress)
        self.send_keys_to_element_by_name("home", contact.home_phone)
        self.send_keys_to_element_by_name("mobile", contact.mobile_phone)
        self.send_keys_to_element_by_name("work", contact.work_phone)
        self.send_keys_to_element_by_name("fax", contact.fax)
        self.send_keys_to_element_by_name("email", contact.email_prime)
        self.send_keys_to_element_by_name("email2", contact.email_secondary)
        self.send_keys_to_element_by_name("email3", contact.email_third)
        self.send_keys_to_element_by_name("homepage", contact.home_page)
        self.send_keys_to_element_by_name("firstname", contact.first_name)
        # u'изменение дня рождения'
        xpath_birthday_day = "//div[@id='content']/form/select[1]//option[" + contact.birthday_day + "]"
        wd.find_element_by_xpath(xpath_birthday_day).click()
        # u'изменение месяца рождения'
        xpath_birthday_month = "//div[@id='content']/form/select[2]//option[" + contact.birthday_month + "]"
        wd.find_element_by_xpath(xpath_birthday_month).click()
        self.send_keys_to_element_by_name("byear", contact.birthday_year)
        # u'изменение дня юбилея'
        xpath_anniversary_day = "//div[@id='content']/form/select[3]//option[" + contact.anniversary_day + "]"
        wd.find_element_by_xpath(xpath_anniversary_day).click()
        # u'изменение месяца юбилея'
        xpath_anniversary_month = "//div[@id='content']/form/select[4]//option[" + contact.anniversary_month + "]"
        wd.find_element_by_xpath(xpath_anniversary_month).click()
        self.send_keys_to_element_by_name("ayear", contact.anniversary_year)
        self.send_keys_to_element_by_name("address2", contact.adress_secondary)
        self.send_keys_to_element_by_name("phone2", contact.phone_secondary)
        self.send_keys_to_element_by_name("notes", contact.notes)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()