# -*- coding: utf-8 -*-
import random
from model.group import Group


def test_add_group(app):
    app.session.login_as("admin", "secret")
    test_group = Group.random()
    app.group.create(test_group)
    app.session.logout()