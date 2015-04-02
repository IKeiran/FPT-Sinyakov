__author__ = 'vs'


def test_phones_on_contact_view_page(app):
    app.go_to_main_page()
    contact_from_home_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.join_phones() == contact_from_edit_page.join_phones()