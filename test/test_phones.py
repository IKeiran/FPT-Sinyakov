import pytest

def test_phones_on_contact_view_page(app):
    app.go_to_main_page()
    with pytest.allure.step('Given a group list from view page'):
        contact_from_home_page = app.contact.get_contact_from_view_page(0)
    with pytest.allure.step('Given a group list from edit page'):
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    with pytest.allure.step('Then I compare this lists'):
        assert contact_from_home_page.join_phones() == contact_from_edit_page.join_phones()