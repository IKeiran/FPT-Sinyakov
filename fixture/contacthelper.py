# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:

    contact_cache = None

    def __init__(self, app):
        self.app = app

    def count(self):
        self.go_to_main_page()
        result = len(self.app.wd.find_elements_by_name('selected[]'))
        return result

    def change_field_value(self, field_name, index):
        """
        :param field_name: element name
        :param index: sending keys, if value nor None
        :return:
        """
        wd = self.app.wd
        if index is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(index)
            wd.find_element_by_name(field_name).click()

    def select_first(self):
        self.select_by_index(0)

    def select_by_index(self, index):
        self.app.wd.find_elements_by_name("selected[]")[index].click()

    def delete_button_click(self):
        self.app.wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        self.app.wd.switch_to_alert().accept()

    def open_add_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/edit.php")):
            wd.find_element_by_link_text("add new").click()

    def go_to_main_page(self):
        wd = self.app.wd
        if not(len(wd.find_elements_by_name("add")) > 0 and len(wd.find_elements_by_name("to_group")) > 0):
            wd.find_element_by_link_text("home").click()

    def open_edit_page(self, index):
        wd = self.app.wd
        if not(wd.current_url.endswith("/edit.php")):
            wd.find_elements_by_css_selector('img[alt="Edit"]')[index].click()

    def return_to_homepage(self):
        self.app.wd.find_element_by_link_text("home page").click()

    def change_combobox_value(self, selector, value):
        wd = self.app.wd
        Select(wd.find_element_by_name(selector)).select_by_index(value)

    def fill_in(self, contact):
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.mid_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nick_name)
        self.change_field_value("company", contact.company)
        self.change_field_value("title", contact.title)
        self.change_field_value("address", contact.adress)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email_prime)
        self.change_field_value("email2", contact.email_secondary)
        self.change_field_value("email3", contact.email_third)
        self.change_field_value("homepage", contact.home_page)
        self.change_field_value("firstname", contact.first_name)
        # u'изменение дня рождения'
        self.change_combobox_value("bday", contact.birthday_day)
        # u'изменение месяца рождения'
        self.change_combobox_value("bmonth", contact.birthday_month)
        self.change_field_value("byear", contact.birthday_year)
        # u'изменение дня юбилея'
        self.change_combobox_value("aday", contact.anniversary_day)
        # u'изменение месяца юбилея'
        self.change_combobox_value("amonth", contact.anniversary_month)
        self.change_field_value("ayear", contact.anniversary_year)
        self.change_field_value("address2", contact.adress_secondary)
        self.change_field_value("phone2", contact.phone_secondary)
        self.change_field_value("notes", contact.notes)

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector('tr[name=entry]'):
                id = element.find_element_by_css_selector('input').get_attribute('value')
                last_name = element.find_elements_by_css_selector('td')[1].text
                first_name = element.find_elements_by_css_selector('td')[2].text
                self.contact_cache.append(Contact(first_name=first_name, last_name=last_name, id=id))
        return list(self.contact_cache)

    def submit_button_click(self, bottom_button):
        if bottom_button:
            self.app.wd.find_element_by_xpath("(//input[@type='submit'])[2]").click()
        else:
            self.app.wd.find_element_by_xpath("(//input[@type='submit'])[1]").click()

    def delete_from_editpage_button_click(self):
        self.app.wd.find_element_by_xpath("//form[@action='delete.php']/input[@type='submit']").click()

    def update_button_click(self, bottom_button):
        if bottom_button:
            self.app.wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        else:
            self.app.wd.find_element_by_xpath("(//input[@name='update'])[1]").click()

    def add(self, contact, bottom_button=True):
        self.open_add_page()
        self.fill_in(contact)
        self.submit_button_click(bottom_button)
        self.return_to_homepage()
        self.contact_cache = None

    def edit(self, index, contact, bottom_button=True):
        self.open_edit_page(index)
        self.fill_in(contact)
        self.update_button_click(bottom_button)
        self.return_to_homepage()
        self.contact_cache = None

    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        self.select_by_index(index)
        self.delete_button_click()
        self.go_to_main_page()
        self.contact_cache = None

    def delete_from_edit_page(self, index):
        self.open_edit_page(index)
        self.delete_from_editpage_button_click()
        self.go_to_main_page()
        self.contact_cache = None