# -*- coding: utf-8 -*-


def test_contact_delete_first(app):
    app.open_main_page()
    app.session.login_as("admin", "secret")
    app.contact.delete_first()
    app.session.logout()