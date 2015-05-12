__author__ = 'Keiran'
from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixtue

def test_contact_add_in_group(orm):
    contacts = orm.get_contacts_in_group(Group(id=90))
    pass
    print(contacts)

    """
    group_list = orm.get_group_list()
    contact_in_group = set()
    contacts = list()
    for group in group_list:
        try:
            contacts = orm.get_contacts_in_group(group)
            contact_in_group.add(contacts)
        except:
            pass

    contact_list = orm.get_contact_list()
    print(contact_list)
    print(group_list)
        """