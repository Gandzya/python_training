# -*- coding: utf-8 -*-
import random
from time import sleep

from model.group import Group


def test_delete_contact_from_group(app, json_contact, orm, check_ui):
    if len(orm.get_group_list()) == 0 or len(orm.get_contact_list()) == 0:
        new_group = Group(name="group for contact")
        app.group.create_new_group(new_group)
        new_contact = json_contact
        app.contact.create_new_contact_with_group(new_contact, new_group)

    groups = orm.get_group_list()

    groups_with_contacts = []

    for grp in groups:
        if len(orm.get_contacts_in_group(grp)) > 0:
            groups_with_contacts.append(grp)

    group_to_delete = random.choice(groups_with_contacts)
    contact_to_delete = random.choice(orm.get_contacts_in_group(group_to_delete))
    app.contact.delete_from_group(group_to_delete, contact_to_delete)
    sleep(10)
    assert contact_to_delete not in orm.get_contacts_in_group(group_to_delete)
