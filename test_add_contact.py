# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from classes.contact import Contact
from application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    contact = Contact.random()
    app.open_main_page()
    app.login_as("admin", "secret")
    app.add_contact(contact)
    app.logout()
