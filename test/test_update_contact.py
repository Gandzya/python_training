from random import randrange

from model.contact import Contact


def test_update_contact(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(lastname="Updated")
    contact.id = old_contacts[0].id
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(firstname="new contact", lastname="to update"))
    app.contact.update_contact_by_index(contact, index)

    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
