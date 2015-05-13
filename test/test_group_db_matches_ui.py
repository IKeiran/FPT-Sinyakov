__author__ = 'Keiran'
from model.group import Group
import pytest


def test_group_list(app, db):
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    with pytest.allure.step('Given a group list'):
        ui_group_list = app.group.get_group_list()
    with pytest.allure.step('When I clean group list from DB'):
        db_group_list = map(clean, db.get_group_list())
    with pytest.allure.step('Then UI group list is equal to the DB group list'):
        assert sorted(ui_group_list, key=Group.id_or_max) == sorted(db_group_list, key=Group.id_or_max)
