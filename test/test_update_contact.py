from model.contact import Contact


def test_update_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(lastname="Updated")
    contact.id = old_contacts[0].id
    if app.contact.count() == 0:
        app.contact.create_new_contact(Contact(firstname="new contact", lastname="to update"))
        app.contact.update_first_contact(contact)
    else:
        app.contact.update_first_contact(contact)

    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
