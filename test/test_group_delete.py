# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_group_delete(app):
    if app.group.count() == 0:
        app.group.create(Group.random())
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups