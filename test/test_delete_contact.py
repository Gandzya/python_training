from model.contact import Contact


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(firstname="new contact", lastname="to delete"))
        app.contact.delete_first_contact()
    else:
        app.contact.delete_first_contact()
