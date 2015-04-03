# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest


# test_data = [Contact(first_name='', mid_name='', last_name='')]\
           # + \
test_data = [Contact.random() for i in range(5)]

b_button = [True, False]

@pytest.mark.parametrize('contact', test_data, ids=[repr(x) for x in test_data])
def test_contact_add(app, contact):
    app.go_to_main_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.add(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


"""
@pytest.mark.parametrize('bottom_button', b_button, ids=[repr(x) for x in b_button])
def test_contact_add_with_upper_submit_button(app, bottom_button):
    contact = Contact.random()
    app.go_to_main_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.add(contact, bottom_button = bottom_button)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
"""