__author__ = 'Keiran'
from model.group import Group


def test_group_list(app, db):
    ui_group_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_group_list = map(clean, db.get_group_list())
    assert sorted(ui_group_list, key=Group.id_or_max) == sorted(db_group_list, key=Group.id_or_max)
