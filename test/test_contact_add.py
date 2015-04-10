# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest

b_button = [True, False]

@pytest.mark.parametrize('bottom_button', b_button, ids=[repr(x) for x in b_button])
def test_contact_add(app, bottom_button, json_contact):
    contact = json_contact
    app.go_to_main_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.add(contact, bottom_button = bottom_button)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)