# -*- coding: utf-8 -*-
import random
from time import sleep

from model.group import Group


def test_add_random_group_to_new_contact(app, json_contact, orm, check_ui):
    if len(orm.get_group_list()) == 0 and len(orm.get_contact_list() == 0):
        new_group = Group(name="group for contact")
        app.group.create_new_group(new_group)
        new_contact = json_contact
        app.contact.create_new_contact_with_group(new_contact, new_group)

    groups = orm.get_group_list()
    contacts = orm.get_contact_list()

    contact_to_add = random.choice(contacts)
    group_to_add = random.choice(groups)

    app.contact.add_to_group(contact_to_add, group_to_add)
    assert contact_to_add in orm.get_contacts_in_group(group_to_add)
