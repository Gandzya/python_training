from model.contact import Contact


def test_update_contact(app):
    app.session.login("admin", "secret")
    app.contact.update_first_contact(Contact("Olga", "V", "Updated", "Gandzya", "Infopulse", "Poliova str 24d", "27",
                                           "August", "1986"))
    app.session.logout()
