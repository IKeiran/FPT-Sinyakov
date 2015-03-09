# -*- coding: utf-8 -*-


def test_group_delete_first(app):
    app.session.login_as("admin", "secret")
    app.group.delete_first()
    app.session.logout()