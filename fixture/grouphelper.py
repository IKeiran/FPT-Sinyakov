class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def open_group_list_page(self):
        self.app.wd.find_element_by_link_text("groups").click()

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

    def fill_in(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def create(self, group):
        self.open_group_list_page()
        self.new_button_click()
        self.fill_in(group)
        self.submit_button_click()
        self.return_to_group_page()

    def delete_first(self):
        self.open_group_list_page()
        self.select_first_group()
        self.delete_button_click()
        self.return_to_group_page()

    def edit_first_group(self, test_group):
        self.open_group_list_page()
        self.select_first_group()
        self.edit_button_click()
        self.fill_in(test_group)
        self.update_button_click()
        self.return_to_group_page()