from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create_new_group(self, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
        self.fill_group(group)
        wd.find_element_by_name("submit").click()
        self.group_cache = None

    def open_group_page(self):
        wd = self.app.wd
        #     if not (len(wd.find_elements_by_name("edit")) > 0 and wd.current_url.endswith("groups.php")):
        wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def update_first_group(self, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        self.fill_group(group)
        wd.find_element_by_name("update").click()
        self.group_cache = None

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

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)
