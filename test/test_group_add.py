# -*- coding: utf-8 -*-

from model.group import Group
import pytest


def test_group_add(app, db, check_ui, json_groups):
    with pytest.allure.step('Given a group list'):
        old_groups = db.get_group_list()
    test_group = json_groups
    with pytest.allure.step('When I add a group %s to the list' % test_group):
        app.group.create(test_group)
    new_groups = db.get_group_list()
    with pytest.allure.step('Then the new group list is equal to the old list with the added group'):
        old_groups.append(test_group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(app.group.get_group_list(), key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)