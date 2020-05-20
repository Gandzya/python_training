from selenium.webdriver.support.select import Select

from model.contact import Contact
import re


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

    def delete_first_contact(self, index):
        self.delete_contact_by_index(index)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value=\"Delete\"]").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_id(id).click()
        wd.find_element_by_xpath("//input[@value=\"Delete\"]").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def update_first_contact(self, contact, index):
        self.update_contact_by_index(contact, index)

    def update_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.open_contact_by_index(index)
        self.fill_contact(contact)
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.contact_cache = None

    def update_contact_by_id(self, contact):
        wd = self.app.wd
        self.open_contact_by_id(contact.id)
        self.fill_contact(contact)
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.contact_cache = None

    def open_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()

    def open_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("//input[@id=%s]//ancestor::tr//img[@title='Edit']" % id).click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@title='Details']")[index].click()
        # row = wd.find_elements_by_name("entry")[index]
        # cell = row.find_elements_by_tag_name("td")[7]
        # cell.find_element_by_tag_name("a").click()

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
        self.fill_field("byear", contact.byear)
        self.fill_field("home", contact.homephone)
        self.fill_field("mobile", contact.mobilephone)
        self.fill_field("work", contact.workphone)
        self.fill_field("phone2", contact.secondaryphone)

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
        self.open_home_page()
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            element_list = wd.find_elements_by_name("entry")
            for element in element_list:
                cells = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                lastname = cells[1].text  # element.find_element_by_xpath("//tr[" + str(i) + "]/td[2]").text
                firstname = cells[2].text  # element.find_element_by_xpath("//tr[" + str(i) + "]/td[3]").text
                address = cells[3].text
                allphones = cells[5].text
                allmails = cells[4].text
                if allmails == '':
                    allmails = None
                self.contact_cache.append(
                    Contact(lastname=lastname, firstname=firstname, id=id, all_phones_from_home_page=allphones,
                            allmails=allmails, address=address))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone, email=email, email2=email2, email3=email3,
                       address=address, id=id)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search(" W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone)
