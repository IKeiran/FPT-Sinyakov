# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_contact_delete_from_edit_page(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.add(Contact.random())
    app.go_to_main_page()
    old_contacts = app.contact.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_from_edit_page(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert (sorted(app.contact.get_contact_list(), key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max))