from model.group import Group

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def open_group_list_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def select_first_group(self):
        self.app.wd.find_element_by_name("selected[]").click()

    def delete_button_click(self):
        self.app.wd.find_element_by_name("delete").click()

    def new_button_click(self):
        self.app.wd.find_element_by_name("new").click()

    def edit_button_click(self):
        self.app.wd.find_element_by_name("edit").click()

    def submit_button_click(self):
        self.app.wd.find_element_by_name("submit").click()

    def update_button_click(self):
        self.app.wd.find_element_by_name("update").click()

    def change_field_value(self, field_name, value):
        """
        :param field_name: element name
        :param value: sending keys, if value nor None
        :return:
        """
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(value)
            wd.find_element_by_name(field_name).click()

    def get_group_list(self):
        wd = self.app.wd
        self.open_group_list_page()
        groups = []
        for element in wd.find_elements_by_css_selector('span.group'):
            text = element.text
            id = element.find_element_by_name('selected[]').get_attribute('value')
            groups.append(Group(name=text, id=id))
        return groups

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def create(self, group):
        self.open_group_list_page()
        self.new_button_click()
        self.fill_group_form(group)
        self.submit_button_click()
        self.return_to_group_page()

    def count(self):
        self.open_group_list_page()
        result = len(self.app.wd.find_elements_by_name('selected[]'))
        return result

    def delete_first(self):
        self.open_group_list_page()
        self.select_first_group()
        self.delete_button_click()
        self.return_to_group_page()

    def edit_first_group(self, test_group):
        self.open_group_list_page()
        self.select_first_group()
        self.edit_button_click()
        self.fill_group_form(test_group)
        self.update_button_click()
        self.return_to_group_page()