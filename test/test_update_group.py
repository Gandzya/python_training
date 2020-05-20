import random

from model.group import Group


def test_update_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        db.create_new_group(Group(name="New"))
    old_groups = db.get_group_list()
    group_to_update = random.choice(old_groups)
    group = Group(name="Updated group")
    group.id = group_to_update.id
    app.group.update_group_by_id(group)
    new_group = db.get_group_list()
    old_groups.remove(group_to_update)
    old_groups.append(group)
    assert len(old_groups) == len(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_group, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
