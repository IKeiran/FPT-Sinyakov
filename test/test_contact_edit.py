# -*- coding: utf-8 -*-

from model.contact import Contact
from random import randrange
import pytest



bot_button = [True, False]

@pytest.mark.parametrize('bottom_button', bot_button, ids=[repr(x) for x in bot_button])
def test_contact_edit_with_upper_submit(app, bottom_button):
    if app.contact.count() == 0:
        app.contact.add(Contact.random())
    contact = Contact.random()
    app.go_to_main_page()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    id = old_contacts[index].id
    app.contact.edit(index, contact, bottom_button)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    old_contacts[index].id = id
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
