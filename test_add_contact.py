# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest


def randomize_str(attr):
    import random
    return attr + str(random.randint(0,1000000))

class Contact:
    def __init__(self,first_name=None, mid_name=None, last_name=None, nick_name=None,
                    title=None, company=None, adress=None, home_phone=None, mobile_phone=None,
                    work_phone=None, fax=None, email_prime=None, email_secondary=None, email_third=None,
                    home_page=None, birthday_year=None, birthday_month=None, birthday_day=None, anniversary_year=None,
                    anniversary_day=None, anniversary_month=None, adress_secondary=None,
                    phone_secondary=None, notes=None):
        self.first_name = first_name
        self.mid_name = mid_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.title = title
        self.company = company
        self.adress = adress
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email_prime = email_prime
        self.email_secondary = email_secondary
        self.email_third = email_third
        self.home_page = home_page
        self.birthday_year = birthday_year
        self.birthday_month = birthday_month
        self.birthday_day = birthday_day
        self.anniversary_year = anniversary_year
        self.anniversary_day = anniversary_day
        self.anniversary_month = anniversary_month
        self.adress_secondary = adress_secondary
        self.phone_secondary = phone_secondary
        self.notes = notes

    @classmethod
    def random(cls):
        import random
        """
        :return: Сontact
        """
        return cls(first_name = randomize_str('first_name'),
        mid_name = randomize_str('mid_name'),
        last_name = randomize_str('last_name'),
        nick_name = randomize_str('nick_name'),
        title = randomize_str('title'),
        company = randomize_str('company'),
        adress = randomize_str('adress'),
        home_phone = randomize_str('home_phone'),
        mobile_phone = randomize_str('mobile_phone'),
        work_phone = randomize_str('work_phone'),
        fax = randomize_str('fax'),
        email_prime = randomize_str('email_prime'),
        email_secondary = randomize_str('email_secondary'),
        email_third = randomize_str('email_third'),
        home_page = randomize_str('home_page'),
        birthday_year = str(random.randint(1950,2015)),
        birthday_month = str(random.randint(0,12)),
        birthday_day = str(random.randint(0,31)),
        anniversary_year = str(random.randint(1950,2015)),
        anniversary_month = str(random.randint(0,12)),
        anniversary_day =str(random.randint(0,31)),
        adress_secondary = randomize_str('adress_secondary'),
        phone_secondary = randomize_str('phone_secondary'),
        notes = randomize_str('notes'))

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

    def add_contact(self, wd, contact):
        wd.get("http://localhost/addressbook/edit.php")
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.mid_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nick_name)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.adress)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email_prime)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email_secondary)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email_third)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.home_page)
        # u'изменение дня рождения'
        xpath_birthday_day = "//div[@id='content']/form/select[1]//option["+ contact.birthday_day+"]"
        wd.find_element_by_xpath(xpath_birthday_day).click()
        # u'изменение месяца рождения'
        xpath_birthday_month = "//div[@id='content']/form/select[2]//option["+ contact.birthday_month+"]"
        wd.find_element_by_xpath(xpath_birthday_month).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()

        # u'изменение дня юбилея'
        xpath_anniversary_day = "//div[@id='content']/form/select[3]//option[" + contact.anniversary_day+"]"
        wd.find_element_by_xpath(xpath_anniversary_day).click()
        # u'изменение месяца юбилея'
        xpath_anniversary_month = "//div[@id='content']/form/select[4]//option[" + contact.anniversary_month+"]"
        wd.find_element_by_xpath(xpath_anniversary_month).click()
        wd.find_element_by_name("byear").send_keys(contact.birthday_year)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.anniversary_year)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.adress_secondary)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone_secondary)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
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
