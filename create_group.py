# -*- coding: utf-8 -*-

from selenium.common.exceptions import NoAlertPresentException

import pytest
from application import Application
from group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_group(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_group_page()
    app.create_new_group(Group(name="new group", header="header", footer="footer"))
    app.logout()


def test_create_empty_group(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_group_page()
    app.create_new_group(Group(name="", header="", footer=""))
    app.logout()
