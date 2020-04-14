# -*- coding: utf-8 -*-
from datetime import time
from sys import maxsize

from model.group import Group


def test_create_group(app):
    old_group = app.group.get_group_list()
    group = Group(name="new group", header="header", footer="footer")
    app.group.create_new_group(group)
    assert len(old_group) + 1 == app.group.count()
    new_group = app.group.get_group_list()
    old_group.append(group)
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)

    def test_create_empty_group(app):
        app.group.create_new_group(Group(name="", header="", footer=""))
