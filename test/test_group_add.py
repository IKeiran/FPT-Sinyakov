# -*- coding: utf-8 -*-

from model.group import Group


def test_group_add(app, json_groups):
    test_group = json_groups
    old_groups = app.group.get_group_list()
    app.group.create(test_group)
    assert len(old_groups)+1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(test_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)