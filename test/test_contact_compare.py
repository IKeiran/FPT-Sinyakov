__author__ = 'Keiran'
from model.contact import Contact
import pytest


def test_contact_compare(app, orm):
    with pytest.allure.step('Given a sorted contact list from DB'):
        contacts_from_db = orm.get_contact_list()
        sorted_contacts_from_db = list(sorted(contacts_from_db, key=Contact.id_or_max))
    with pytest.allure.step('Given a sorted contact list from home page'):
        contacts_from_home_page = app.contact.get_contact_list()
        sorted_contacts_from_home_page = list(sorted(contacts_from_home_page, key=Contact.id_or_max))
    with pytest.allure.step('Then I compare this lists'):
        for index in range(len(sorted_contacts_from_db)):
            assert sorted_contacts_from_db[index] == sorted_contacts_from_home_page[index]
            assert sorted_contacts_from_db[index].join_mails() == sorted_contacts_from_home_page[index].all_mails
            assert sorted_contacts_from_db[index].join_phones() == sorted_contacts_from_home_page[index].all_phones
