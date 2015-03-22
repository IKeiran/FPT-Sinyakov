# -*- coding: utf-8 -*-
from model.group import Group


def test_group_add(app):
    test_group = Group.random()
    old_groups = app.group.get_group_list()
    app.group.create(test_group)
    assert len(old_groups)+1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(test_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)