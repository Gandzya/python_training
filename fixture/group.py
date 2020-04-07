class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create_new_group(self, group):
        wd = self.app.wd
        wd.find_element_by_name("new").click()
        self.fill_group(group)
        wd.find_element_by_name("submit").click()

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.select_first_group()
        wd.find_element_by_name("delete").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def update_first_group(self, group):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        self.fill_group(group)
        wd.find_element_by_name("update").click()

    def fill_group(self, group):
        wd = self.app.wd
        self.fill_field("group_name", group.name)
        self.fill_field("group_header", group.header)
        self.fill_field("group_footer", group.footer)

    def fill_field(self, locator, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(locator).click()
            wd.find_element_by_name(locator).clear()
            wd.find_element_by_name(locator).send_keys(text)
