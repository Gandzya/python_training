# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_new_contact(Contact("Olga", "V", "Karasiuk", "Gandzya", "Infopulse", "Poliova str 24d", "27",
                                   "August", "1986"))
    app.session.logout()
