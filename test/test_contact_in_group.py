__author__ = 'Keiran'


def test_add_contact_to_group(app, orm):
    test_data = app.contact.get_contact_group_boundary(orm=orm, in_group=False)
    app.contact.add_contact_to_group(contact=test_data['contact'], group=test_data['group'])
    assert test_data['contact'] in orm.get_contacts_in_group(test_data['group'])


def test_remove_contact_from_group(app, orm):
    test_data = app.contact.get_contact_group_boundary(orm=orm, in_group=True)
    app.contact.remove_contact_from_group(contact=test_data['contact'], group=test_data['group'])
    assert test_data['contact'] not in orm.get_contacts_in_group(test_data['group'])

    # app.contact.add_contact_to_group(contact=test_data['contact'], group=test_data['group'])