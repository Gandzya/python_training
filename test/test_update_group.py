from model.group import Group


def test_update_group(app):
    app.session.login("admin", "secret")
    app.group.update_first_group(Group(name="Updated group", header="header", footer="footer"))
    app.session.logout()
