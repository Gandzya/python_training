from model.group import Group


def test_update_group(app):
    app.group.update_first_group(Group(name="Updated group"))
