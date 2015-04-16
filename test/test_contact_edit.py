# -*- coding: utf-8 -*-

from model.contact import Contact
from random import randrange
import pytest


bot_button = [True, False]

@pytest.mark.parametrize('bottom_button', bot_button, ids=[repr(x) for x in bot_button])
def test_contact_edit(app, db, check_ui, bottom_button):
    if app.contact.count() == 0:
        app.contact.add(Contact.random())
    contact = Contact.random()
    app.go_to_main_page()
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    id = old_contacts[index].id
    app.contact.edit_by_id(id, contact, bottom_button)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    old_contacts[index].id = id
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert (sorted(app.contact.get_contact_list(), key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max))