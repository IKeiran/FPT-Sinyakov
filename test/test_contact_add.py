# -*- coding: utf-8 -*-

from model.contact import Contact


def test_contact_add(app):
    contact = Contact.random()
    app.open_main_page()
    app.session.login_as("admin", "secret")
    app.contact.add(contact)
    app.session.logout()


def test_contact_add_with_bottom_submit_button(app):
    contact = Contact.random()
    app.open_main_page()
    app.session.login_as("admin", "secret")
    app.contact.add_with_bottom_submit(contact)
    app.session.logout()