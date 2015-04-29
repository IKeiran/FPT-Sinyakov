__author__ = 'Keiran'
from model.contact import Contact


def test_contact_compare(app,orm):
    contacts_from_db = orm.get_contact_list()
    sorted_contacts_from_db = list(sorted(contacts_from_db, key=Contact.id_or_max))
    contacts_from_home_page = app.contact.get_contact_list()
    sorted_contacts_from_home_page = list(sorted(contacts_from_home_page, key=Contact.id_or_max))
    for index in range(len(sorted_contacts_from_db)):
        assert sorted_contacts_from_db[index] == sorted_contacts_from_home_page[index]
        assert sorted_contacts_from_db[index].join_mails() == sorted_contacts_from_home_page[index].all_mails
        assert sorted_contacts_from_db[index].join_phones() == sorted_contacts_from_home_page[index].all_phones
