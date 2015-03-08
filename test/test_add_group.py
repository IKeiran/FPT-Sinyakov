# -*- coding: utf-8 -*-
import random
from model.group import Group


def test_add_group(app):
    app.session.login_as("admin", "secret")
    test_group = Group("Friends" + str(random.randint(0, 1000000)), "My friends", "for current time")
    app.group.create(test_group)
    app.session.logout()