# -*- coding: utf-8 -*-

from model.contact import Contact


def test_contact_add(app):
    contact = Contact.random()
    app.go_to_main_page()
    app.contact.add(contact)


def test_contact_add_with_bottom_submit_button(app):
    contact = Contact.random()
    app.go_to_main_page()
    app.contact.add_with_bottom_submit(contact)