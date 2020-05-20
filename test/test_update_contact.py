import random
from random import randrange

from model.contact import Contact


def test_update_contact(app, db, check_ui):
    old_contacts = db.get_contact_list()
    contact_to_update = random.choice(old_contacts)
    contact = Contact(lastname="Updated", firstname="updated", address="updated")
    contact.id = contact_to_update.id
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(Contact(firstname="new contact", lastname="to update"))
    app.contact.update_contact_by_id(contact)

    new_contacts = db.get_contact_list()
    old_contacts.remove(contact_to_update)
    old_contacts.append(contact)
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)

