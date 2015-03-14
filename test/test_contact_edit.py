# -*- coding: utf-8 -*-

from model.contact import Contact


def test_contact_edit_first(app):
    if app.contact.count() == 0:
        app.contact.add(Contact.random())
    contact = Contact.random()
    app.go_to_main_page()
    app.contact.edit(contact)


def test_contact_edit_first_bottom_submit(app):
    if app.contact.count() == 0:
        app.contact.add(Contact.random())
    contact = Contact.random()
    app.go_to_main_page()
    app.contact.edit_with_bottom_submit(contact)