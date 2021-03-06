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
            if index is not None:
                self.app.wd.find_elements_by_name("selected[]")[index].click()

    def select_by_id(self, id):
            if id is not None:
                self.app.wd.find_element_by_id("%s" % id).click()

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

    def open_edit_page_by_id(self, id):
        wd = self.app.wd
        if not(wd.current_url.endswith("/edit.php")):
            wd.find_element_by_css_selector('a[href="edit.php?id=%s"]' % id).click()

    def return_to_homepage(self):
        self.app.wd.find_element_by_link_text("home page").click()

    def change_combobox_value_by_index(self, selector, value):
        wd = self.app.wd
        if value is not None:
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
        self.change_combobox_value_by_index("bday", contact.birthday_day)
        # u'изменение месяца рождения'
        self.change_combobox_value_by_index("bmonth", contact.birthday_month)
        self.change_field_value("byear", contact.birthday_year)
        # u'изменение дня юбилея'
        self.change_combobox_value_by_index("aday", contact.anniversary_day)
        # u'изменение месяца юбилея'
        self.change_combobox_value_by_index("amonth", contact.anniversary_month)
        self.change_field_value("ayear", contact.anniversary_year)
        self.change_field_value("address2", contact.adress_secondary)
        self.change_field_value("phone2", contact.phone_secondary)
        self.change_field_value("notes", contact.notes)

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.go_to_main_page()
            self.contact_cache = []
            for row in wd.find_elements_by_css_selector('tr[name=entry]'):
                cells = row.find_elements_by_css_selector('td')
                id = cells[0].find_element_by_css_selector('input').get_attribute('value')
                last_name = cells[1].text
                first_name = cells[2].text
                adress = cells[3].text
                all_mails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(first_name=first_name, last_name=last_name, id=id, adress=adress,
                                                  all_phones=all_phones, all_mails=all_mails))
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

    def edit_by_id(self, id, contact, bottom_button=True):
        self.open_edit_page_by_id(id=id)
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

    def delete_by_id(self, id):
        self.select_by_id(id=id)
        self.delete_button_click()
        self.go_to_main_page()
        self.contact_cache = None

    def delete_from_edit_page(self, id):
        self.open_edit_page_by_id(id)
        self.delete_from_editpage_button_click()
        self.go_to_main_page()
        self.contact_cache = None

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.go_to_main_page()
        self.open_edit_page(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        adress = wd.find_element_by_name("address").get_attribute("value")
        email_prime = wd.find_element_by_name("email").get_attribute("value")
        email_secondary = wd.find_element_by_name("email2").get_attribute("value")
        email_third = wd.find_element_by_name("email3").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        secondary_phone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(first_name=first_name, last_name=last_name, id=id, adress=adress,
                       email_prime=email_prime, email_secondary=email_secondary, email_third=email_third,
                       home_phone=home_phone,
                       work_phone=work_phone, mobile_phone=mobile_phone, phone_secondary=secondary_phone)

    def open_view_page_by_index(self, index):
        wd = self.app.wd
        self.go_to_main_page
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_from_view_page(self, index):
        import re
        wd = self.app.wd
        self.open_view_page_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search('H: (.*)', text).group(1)
        work_phone = re.search('W: (.*)', text).group(1)
        mobile_phone = re.search('M: (.*)', text).group(1)
        secondary_phone = re.search('P: (.*)', text).group(1)
        return Contact(home_phone=home_phone,work_phone=work_phone,
                       mobile_phone=mobile_phone, phone_secondary=secondary_phone)

    def create_contact_group_pair(self, orm, group_list):
        from model.group import Group
        import random
        contact_list = orm.get_contact_list()
        test_data = dict()
        if len(contact_list) > 0:
            self.app.group.create(Group.random())
            self.go_to_main_page()
            group_list = orm.get_group_list()
            test_data['group'] = sorted(group_list, key=Group.id_or_max)[-1]
            test_data['contact'] = random.choice(contact_list)
        elif len(group_list) > 0:
            self.app.contact.add(Contact.random())
            contact_list = orm.get_contact_list()
            test_data['group'] = random.choice(group_list)
            test_data['contact'] = sorted(contact_list, key=Contact.id_or_max)[-1]
        else:
            self.app.group.create(Group.random())
            self.go_to_main_page()
            self.app.contact.add(Contact.random())
            test_data['group'] = orm.get_group_list()[0]
            test_data['contact'] = orm.get_contact_list()[0]
        return test_data

    def get_contact_group_boundary(self, orm, in_group=False):
        import random
        group_list = orm.get_group_list()
        test_data = dict()
        contacts = list()
        group_number = 0
        if in_group:
            check = orm.get_contacts_in_group
        else:
            check = orm.get_contacts_not_in_group
        while len(contacts) == 0 and group_number <= len(group_list):
            contacts = check(group_list[group_number])
            if len(contacts) > 0:
                test_data['contact'] = random.choice(contacts)
                test_data['group'] = group_list[group_number]
                return test_data
            else:
                group_number += 1
        test_data = self.create_contact_group_pair(orm=orm, group_list=group_list)
        if in_group:
            self.add_contact_to_group(contact=test_data['contact'], group=test_data['group'])
        return test_data

    def change_combobox_value_by_text(self, selector, value):
        wd = self.app.wd
        combobox = wd.find_element_by_name(selector)
        Select(combobox).select_by_visible_text(value)

    def add_contact_in_group_button_click(self):
        wd = self.app.wd
        wd.find_element_by_name('add').click()

    def add_contact_to_group(self, contact, group):
        self.select_by_id(contact.id)
        selector = 'to_group'
        self.change_combobox_value_by_text(selector=selector, value=group.name)
        self.add_contact_in_group_button_click()
        self.go_to_main_page()

    def remove_contact_from_group(self, contact, group):
        self.select_by_id(contact.id)
        self.app.group.navigate_to_group_page(group_name=group.name)
        self.select_by_id(contact.id)
        self.app.group.remove_contact_button_click()
        self.go_to_main_page()