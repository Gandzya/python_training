from model.contact import Contact


def test_update_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(firstname="new contact", lastname="to update"))
        app.contact.update_first_contact(Contact(lastname="Updated"))
    else:
        app.contact.update_first_contact(Contact(lastname="Updated"))
