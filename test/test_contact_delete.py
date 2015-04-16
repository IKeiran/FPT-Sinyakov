# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_contact_delete(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.add(Contact.random())
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_by_id(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert (sorted(app.contact.get_contact_list(), key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max))