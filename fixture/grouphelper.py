from model.group import Group


class GroupHelper:

    group_cache = None

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
        self.select_group_by_index(0)

    def select_group_by_index(self, index):
        self.app.wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        self.app.wd.find_element_by_css_selector("input[value='%s']" % id).click()

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
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_list_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector('span.group'):
                text = element.text
                id = element.find_element_by_name('selected[]').get_attribute('value')
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

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
        self.group_cache = None

    def count(self):
        self.open_group_list_page()
        result = len(self.app.wd.find_elements_by_name('selected[]'))
        return result

    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        self.open_group_list_page()
        self.select_group_by_index(index)
        self.delete_button_click()
        self.return_to_group_page()
        self.group_cache = None

    def delete_by_id(self, id):
        self.open_group_list_page()
        self.select_group_by_id(id)
        self.delete_button_click()
        self.return_to_group_page()
        self.group_cache = None

    def edit_first_group(self, group):
        self.edit_by_index(0, group)

    def edit_by_id(self, group):
        self.open_group_list_page()
        self.select_group_by_id(group.id)
        self.edit_button_click()
        self.fill_group_form(group)
        self.update_button_click()
        self.return_to_group_page()
        self.group_cache = None

    def edit_by_index(self, index, group):
        self.open_group_list_page()
        self.select_group_by_index(index)
        self.edit_button_click()
        self.fill_group_form(group)
        self.update_button_click()
        self.return_to_group_page()
        self.group_cache = None

    def navigate_to_group_page(self, group_name):
        wd = self.app.wd
        wd.get(self.app.base_url+'?group=%s' % group_name)

    def remove_contact_button_click(self):
        wd = self.app.wd
        wd.find_element_by_name('remove').click()