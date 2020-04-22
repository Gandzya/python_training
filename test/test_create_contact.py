# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Olga", middlename="V", lastname="Karasiuk", nickname="Gandzya", company="Infopulse",
                      address="Poliova str 24d", bday="27", bmonth="August", byear="1986", homephone="123456",
                      mobilephone="654132", workphone="09878576", secondaryphone="(0)862615")
    app.contact.create_new_contact(contact)
    app.contact.open_home_page()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
