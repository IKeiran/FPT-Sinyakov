__author__ = 'Keiran'
# -*- coding: utf-8 -*-
from model.group import Group


def test_group_name_header_first(app):
    if app.group.count() == 0:
        app.group.create(Group.random())
    old_groups = app.group.get_group_list()
    group = Group(name='NewName')
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
