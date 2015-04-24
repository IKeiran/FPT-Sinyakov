__author__ = 'Keiran'
from model.contact import Contact


def test_contact_compare(app,orm):
    contacts_from_db = orm.get_contact_list()
    sorted_contacts_from_db = list(sorted(contacts_from_db, key=Contact.id_or_max))
    contacts_from_home_page = app.contact.get_contact_list()
    sorted_contacts_from_home_page = list(sorted(contacts_from_home_page, key=Contact.id_or_max))
    #assert sorted_contacts_from_db == sorted_contacts_from_home_page
    #assert sorted(contacts_from_home_page, key=Contact.id_or_max) == sorted(contacts_from_db, key=Contact.id_or_max)
    for index in range(len(sorted_contacts_from_db)):
        assert sorted_contacts_from_db[index] == sorted_contacts_from_home_page[index]
        assert sorted_contacts_from_db[index].join_mails() == sorted_contacts_from_home_page[index].all_mails
        assert sorted_contacts_from_db[index].join_phones() == sorted_contacts_from_home_page[index].all_phones

    # contacts_from_home_page = app.contact.get_contact_list()
    # assert sorted(contacts_from_home_page, key=Contact.id_or_max) == sorted(contacts_from_db, key=Contact.id_or_max)
    # assert contacts_from_home_page.all_mails == contacts_from_db.join_mails()
    # assert contacts_from_home_page.all_phones == contacts_from_db.join_phones()