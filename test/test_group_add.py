# -*- coding: utf-8 -*-

from model.group import Group


def test_group_add(app, db, check_ui, json_groups):
    test_group = json_groups
    old_groups = db.get_group_list()
    app.group.create(test_group)
    new_groups = db.get_group_list()
    old_groups.append(test_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(app.group.get_group_list(), key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)