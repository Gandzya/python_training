from random import randrange

from model.group import Group


def test_update_group(app):
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Updated group")
    group.id = old_groups[0].id
    if app.group.count() == 0:
        app.group.create_new_group(Group(name="New"))
    app.group.update_group_by_index(group, index)
    new_group = app.group.get_group_list()
    old_groups[index] = group
    assert len(old_groups) == len(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)
