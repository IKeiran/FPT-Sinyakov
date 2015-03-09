# -*- coding: utf-8 -*-


def test_contact_delete_from_edit_page(app):
    app.session.login_as("admin", "secret")
    app.contact.delete_from_edit_page()
    app.session.logout()