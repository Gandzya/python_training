import random
from time import sleep

from model.contact import Contact


def test_delete_contact(app, db, check_ui):
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    if len(old_contacts) == 0:
        app.contact.create_new_contact(Contact(firstname="new contact", lastname="to delete"))
    app.contact.delete_contact_by_id(contact.id)
    sleep(2)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts

    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
