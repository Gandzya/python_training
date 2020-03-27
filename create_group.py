# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

from group import Group


def logout(wd):
    wd.find_element_by_link_text("Logout").click()


class CreateGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def create_new_group(self, wd, group):
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("header_name").click()
        wd.find_element_by_name("header_name").clear()
        wd.find_element_by_name("header_name").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()

    def open_group_page(self, wd):
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def test_create_group(self):
        wd = self.wd;
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_group_page(wd)
        self.create_new_group(wd, Group(name="new group", header="header", footer="footer"))
        logout(wd)

    def test_create_empty_group(self):
        wd = self.wd;

        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_group_page(wd)
        self.create_new_group(wd, Group(name="", header="", footer=""))
        logout(wd)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
