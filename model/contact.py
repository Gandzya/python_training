class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, company=None, address=None,
                 bday=None, bmonth=None, byear=None):
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.address = address
        self.company = company
        self.nickname = nickname
        self.lastname = lastname
        self.middlename = middlename
        self.firstname = firstname
