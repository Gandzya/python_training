# -*- coding: utf-8 -*-
from datetime import time

from model.group import Group


def test_create_group(app):
    app.group.open_group_page()
    app.group.create_new_group(Group(name="new group", header="header", footer="footer"))


def test_create_empty_group(app):
    app.group.open_group_page()
    app.group.create_new_group(Group(name="", header="", footer=""))
