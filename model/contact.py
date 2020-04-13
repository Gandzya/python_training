from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, company=None, address=None,
                 bday=None, bmonth=None, byear=None, id=None):
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
        return self.firstname == other.firstname and self.lastname == other.lastname and (
                self.id == other.id or self.id is None or other.id is None)

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.firstname, self.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
