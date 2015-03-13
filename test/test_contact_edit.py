# -*- coding: utf-8 -*-

from model.contact import Contact


def test_contact_edit_first(app):
    contact = Contact.random()
    app.open_main_page()
    app.contact.edit(contact)


def test_contact_edit_first_bottom_submit(app):
    contact = Contact.random()
    app.open_main_page()
    app.contact.edit_with_bottom_submit(contact)