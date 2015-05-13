__author__ = 'Keiran'
# -*- coding: utf-8 -*-
from model.group import Group
import random
import pytest

def test_group_edit(app, db, check_ui):
    with pytest.allure.step('Given a group from group list'):
        if app.group.count() == 0:
            app.group.create(Group.random())
        old_groups = db.get_group_list()
        group = random.choice(old_groups)
    with pytest.allure.step('When I edit the group'):
        group.name = 'NewName'
        app.group.edit_by_id(group)
    with pytest.allure.step('Then new group list equal old group list with changed data'):
        new_groups = db.get_group_list()
        sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(app.group.get_group_list(), key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)