import pymysql

from model.contact import Contact
from model.group import Group


class DBFixture():
    def __init__(self, host, name, user, password):
        self.user = user
        self.password = password
        self.name = name
        self.host = host
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, firstname, lastname, middlename, nickname, company, address, bday, bmonth, byear, "
                "home, mobile, work, phone2, email, email2, email3 from addressbook "
                "where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, middlename, nickname, company, address, bday, bmonth, byear,
                 home, mobile, work, phone2, email, email2, email3) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, middlename=middlename,
                                    nickname=nickname, company=company,
                                    address=address, byear=byear, bday=bday, bmonth=bmonth, homephone=home,
                                    mobilephone=mobile,
                                    workphone=work, secondaryphone=phone2,
                                    email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
