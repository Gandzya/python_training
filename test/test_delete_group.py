from random import randrange

from model.group import Group


def test_delete_first_group(app):
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    if app.group.count() == 0:
        app.group.create_new_group(Group(name="New"))
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[index:index + 1] = []
    assert old_groups == new_groups
