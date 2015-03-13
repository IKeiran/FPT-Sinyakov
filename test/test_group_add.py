# -*- coding: utf-8 -*-
from model.group import Group


def test_group_add(app):
    test_group = Group.random()
    app.group.create(test_group)