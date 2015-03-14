# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contact_delete_first(app):
    if app.contact.count() == 0:
        app.contact.add(Contact.random())
    app.contact.delete_first()