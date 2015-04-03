__author__ = 'Keiran'
from random import randrange


def test_contact_compare(app):
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page == contact_from_edit_page
    assert contact_from_home_page.all_mails == contact_from_edit_page.join_mails()
    assert contact_from_home_page.all_phones == contact_from_edit_page.join_phones()