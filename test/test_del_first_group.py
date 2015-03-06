# -*- coding: utf-8 -*-


def test_add_group(app):
    app.session.login_as("admin", "secret")
    app.group.delete_first()
    app.session.logout()