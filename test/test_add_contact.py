# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    contact = Contact.random()
    app.open_main_page()
    app.session.login_as("admin", "secret")
    app.contact.add_contact(contact)
    app.session.logout()
