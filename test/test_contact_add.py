# -*- coding: utf-8 -*-

from model.contact import Contact


def test_contact_add(app):
    contact = Contact.random()
    app.go_to_main_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.add(contact)
    assert len(old_contacts)+1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_contact_add_with_upper_submit_button(app):
    contact = Contact.random()
    app.go_to_main_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.add(contact, bottom_button=False)
    assert len(old_contacts)+1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)