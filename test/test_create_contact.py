# -*- coding: utf-8 -*-
import random
import string
import re

import pytest

from model.contact import Contact


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(maxlen):
    symbols = string.digits + ")" + "(" + "+" + "-" + " " * 3
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=random_string("firstname:", 10), middlename=random_string("middlename:", 10),
            lastname=random_string("lastname:", 10), nickname=random_string("nickname:", 10),
            company=random_string("company:", 10),
            address=random_string("address:", 10), bday="27", bmonth="August", byear="1986",
            homephone=random_phone(10),
            mobilephone=random_phone(10), workphone=random_phone(10), secondaryphone=random_phone(10),
            )

    for i in range(1)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
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
