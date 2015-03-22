# -*- coding: utf-8 -*-
from model.group import Group


def test_group_delete_first(app):
    if app.group.count() == 0:
        app.group.create(Group.random())
    old_groups = app.group.get_group_list()
    app.group.delete_first()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups