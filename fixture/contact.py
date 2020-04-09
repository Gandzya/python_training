from selenium.webdriver.support.select import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create_new_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value=\"Delete\"]").click()
        wd.switch_to_alert().accept()

    def update_first_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@title=\"Edit\"]").click()
        self.fill_contact(contact)

    def fill_contact(self, contact):
        wd = self.app.wd
        self.fill_field("firstname", contact.firstname)
        self.fill_field("middlename", contact.middlename)
        self.fill_field("lastname", contact.middlename)
        self.fill_field("nickname", contact.middlename)
        self.fill_field("company", contact.middlename)
        self.fill_field("address", contact.middlename)
        self.fill_date("bday", contact.bday)
        self.fill_date("bmonth", contact.bmonth)
        self.fill_field("byear", contact.middlename)

    def fill_date(self, locator, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(locator).click()
            Select(wd.find_element_by_name(locator)).select_by_visible_text(text)

    def fill_field(self, locator, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(locator).click()
            wd.find_element_by_name(locator).clear()
            wd.find_element_by_name(locator).send_keys(text)

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))
