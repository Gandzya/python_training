from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, company=None, address=None,
                 bday=None, bmonth=None, byear=None, homephone=None, mobilephone=None, workphone=None,
                 secondaryphone=None, id=None, all_phones_from_home_page=None, allmails=None, email=None, email2=None,
                 email3=None):
        self.email3 = email3
        self.email2 = email2
        self.email = email
        self.allmails = allmails
        self.all_phones_from_home_page = all_phones_from_home_page
        self.secondaryphone = secondaryphone
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.homephone = homephone
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.address = address
        self.company = company
        self.nickname = nickname
        self.lastname = lastname
        self.middlename = middlename
        self.firstname = firstname
        self.id = id

    def __eq__(self, other):
        return self.firstname == other.firstname and self.lastname == other.lastname and self.allmails == other.allmails \
               and self.all_phones_from_home_page == other.all_phones_from_home_page and self.address == other.address and (
                       self.id == other.id or self.id is None or other.id is None)

    def __repr__(self):
        return "%s:%s %s %s %s %s" % (
            self.id, self.firstname, self.lastname, self.address, self.all_phones_from_home_page, self.allmails)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
