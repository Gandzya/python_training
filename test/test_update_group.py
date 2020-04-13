from model.group import Group


def test_update_group(app):
    old_group = app.group.get_group_list()
    group = Group(name="Updated group")
    group.id = old_group[0].id
    if app.group.count() == 0:
        app.group.create_new_group(Group(name="New"))
        app.group.update_first_group(group)
    else:
        app.group.update_first_group(group)
    new_group = app.group.get_group_list()
    old_group[0] = group
    assert len(old_group) == len(new_group)
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)
