# -*- coding: utf-8 -*-
from model.group import Group


def test_group_delete_first(app):
    if app.group.count() == 0:
        app.group.create(Group.random())
    app.group.delete_first()