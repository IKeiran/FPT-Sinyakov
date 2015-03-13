__author__ = 'Keiran'
# -*- coding: utf-8 -*-
from model.group import Group


def test_group_edit_first(app):
    test_group = Group.random()
    app.group.edit_first_group(test_group)