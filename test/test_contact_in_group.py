__author__ = 'Keiran'
import pytest

def test_add_contact_to_group(app, orm):
    with pytest.allure.step('Given a contact not in group'):
       test_data = app.contact.get_contact_group_boundary(orm=orm, in_group=False)
    with pytest.allure.step('When I add contact in the group'):
        app.contact.add_contact_to_group(contact=test_data['contact'], group=test_data['group'])
    with pytest.allure.step('Then group %s include added contact %s' % (test_data['group'],test_data['contact'])):
        assert test_data['contact'] in orm.get_contacts_in_group(test_data['group'])


def test_remove_contact_from_group(app, orm):
    with pytest.allure.step('Given a contact in group'):
        test_data = app.contact.get_contact_group_boundary(orm=orm, in_group=True)
    with pytest.allure.step('When I delete contact from the group'):
        app.contact.remove_contact_from_group(contact=test_data['contact'], group=test_data['group'])
    with pytest.allure.step('Then group %s does not include contact %s' % (test_data['group'],test_data['contact'])):
        assert test_data['contact'] not in orm.get_contacts_in_group(test_data['group'])
