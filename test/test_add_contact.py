# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_new_contact(Contact("Olga", "V", "Karasiuk", "Gandzya", "Infopulse", "Poliova str 24d", "27",
                                           "August", "1986"))
    app.session.logout()
