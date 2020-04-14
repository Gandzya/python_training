from selenium.webdriver.support.select import Select

from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        #     if not (len(wd.find_elements_by_name("edit")) > 0 and wd.current_url.endswith("groups.php")):
        wd.find_element_by_link_text("home").click()

    def create_new_contact(self, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.contact_cache = None

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value=\"Delete\"]").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def update_first_contact(self, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("//img[@title=\"Edit\"]").click()
        self.fill_contact(contact)
        self.contact_cache = None

    def fill_contact(self, contact):
        wd = self.app.wd
        self.fill_field("firstname", contact.firstname)
        self.fill_field("middlename", contact.middlename)
        self.fill_field("lastname", contact.lastname)
        self.fill_field("nickname", contact.nickname)
        self.fill_field("company", contact.company)
        self.fill_field("address", contact.address)
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

    def open_contact_page(self):
        wd = self.app.wd

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            i = 2
            element_list = wd.find_elements_by_name("entry")
            for element in element_list:
                id = element.find_element_by_name("selected[]").get_attribute("value")
                lastname = element.find_element_by_xpath("//tr[" + str(i) + "]/td[2]").text
                firstname = element.find_element_by_xpath("//tr[" + str(i) + "]/td[3]").text
                i = i + 1
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id))
        return list(self.contact_cache)
