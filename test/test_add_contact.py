# -*- coding: utf-8 -*-
import pytest

from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    contact = Contact.random()
    app.open_main_page()
    app.session.login_as("admin", "secret")
    app.contact.add_contact(contact)
    app.session.logout()
