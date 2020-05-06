# -*- coding: utf-8 -*-
import re


from model.contact import Contact


def test_add_contact(app, json_contact):
    contact = json_contact
    contact.all_phones_from_home_page = merge_phones_like_on_home_page(contact)
    old_contacts = app.contact.get_contact_list()
    app.contact.create_new_contact(contact)
    app.contact.open_home_page()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None,
                                                                              [contact.homephone,
                                                                               contact.mobilephone, contact.workphone,
                                                                               contact.secondaryphone]))))
