__author__ = 'Keiran'
# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    app.session.login_as("admin", "secret")
    test_group = Group.random()
    app.group.edit_first_group(test_group)
    app.session.logout()