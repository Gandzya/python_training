# -*- coding: utf-8 -*-
import pytest

from application import Application
from contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact("Olga", "V", "Karasiuk", "Gandzya", "Infopulse", "Poliova str 24d", "27",
                                   "August", "1986"))
