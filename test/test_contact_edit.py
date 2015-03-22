# -*- coding: utf-8 -*-

from model.contact import Contact
from random import randrange


def test_contact_edit_first(app):
    if app.contact.count() == 0:
        app.contact.add(Contact.random())
    contact = Contact.random()
    app.go_to_main_page()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    id = old_contacts[index].id
    app.contact.edit(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    old_contacts[index].id = id
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

"""
def test_contact_edit_first_bottom_submit(app):
    if app.contact.count() == 0:
        app.contact.add(Contact.random())
    contact = Contact.random()
    app.go_to_main_page()
    old_contacts = app.contact.get_contact_list()
    id = old_contacts[0].id
    app.contact.edit_with_bottom_submit(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    old_contacts[0].id = id
    pass
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
"""