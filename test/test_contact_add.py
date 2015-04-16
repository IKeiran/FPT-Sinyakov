# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest

b_button = [True, False]

@pytest.mark.parametrize('bottom_button', b_button, ids=[repr(x) for x in b_button])
def test_contact_add(app, db, check_ui, bottom_button, json_contact):
    contact = json_contact
    app.go_to_main_page()
    old_contacts = db.get_contact_list()
    app.contact.add(contact, bottom_button=bottom_button)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert (sorted(app.contact.get_contact_list(), key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max))