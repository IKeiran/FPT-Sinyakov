# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest

b_button = [True, False]

@pytest.mark.parametrize('bottom_button', b_button, ids=[repr(x) for x in b_button])
def test_contact_add(app, db, check_ui, bottom_button, json_contact):
    app.go_to_main_page()
    with pytest.allure.step('Given a contact'):
        contact = json_contact
    with pytest.allure.step('Given a contact list'):
        old_contacts = db.get_contact_list()
    with pytest.allure.step('When I add contact to the contact list'):
        app.contact.add(contact, bottom_button=bottom_button)
    with pytest.allure.step('Then the new contact list is equal to the old list with the added contact'):
        new_contacts = db.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert (sorted(app.contact.get_contact_list(), key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max))