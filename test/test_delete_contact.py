from random import randrange

from model.contact import Contact


def test_delete_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="new contact", lastname="to delete")
    index = randrange(len(old_contacts))
    if app.contact.count() == 0:
        app.contact.create_new_contact(contact)
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts
