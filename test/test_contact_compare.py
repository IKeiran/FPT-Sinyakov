__author__ = 'Keiran'
from model.contact import Contact


def test_contact_compare(app, db):
    contacts_from_db = db.get_contact_list()
    contacts_from_home_page = app.contact.get_contact_list()
    assert sorted(contacts_from_home_page, key=Contact.id_or_max) == sorted(contacts_from_db, key=Contact.id_or_max)

    assert contacts_from_home_page.all_mails == contacts_from_db.join_mails()
    assert contacts_from_home_page.all_phones == contacts_from_db.join_phones()