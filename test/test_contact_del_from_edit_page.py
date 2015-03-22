# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contact_delete_from_edit_page(app):
    if app.contact.count() == 0:
        app.contact.add(Contact.random())
    app.go_to_main_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_from_edit_page()
    assert len(old_contacts)-1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts