__author__ = 'Keiran'
# -*- coding: utf-8 -*-
from model.group import Group


def test_group_edit_first(app):
    if app.group.count() == 0:
        app.group.create(Group.random())
    test_group = Group.random()
    app.group.edit_first_group(test_group)