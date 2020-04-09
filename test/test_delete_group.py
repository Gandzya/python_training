from model.group import Group


def test_delete_first_group(app):
    app.group.open_group_page()
    if app.group.count() == 0:
        app.group.create_new_group(Group(name="New"))
        app.group.open_group_page()
        app.group.delete_first_group()
    else:
        app.group.delete_first_group()
