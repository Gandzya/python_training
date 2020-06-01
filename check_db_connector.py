import pymysql.cursors

from fixture.orm import ORMFixture
from model.group import Group

connection = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')

try:
    l = connection.get_contacts_in_group(Group(id="72"))
    for item in l:
        print (item)

finally:
    pass