# -*- coding: utf-8 -*-


def test_delete_group(app):
    app.session.login_as("admin", "secret")
    app.group.delete_first()
    app.session.logout()