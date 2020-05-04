import getopt
import json
import os
import random
import string
import sys

import jsonpickle

from model.contact import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(maxlen):
    symbols = string.digits + ")" + "(" + "+" + "-" + " " * 3
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


n = 5
f = "data/contacts.json"

testdata = [
    Contact(firstname=random_string("firstname:", 10), middlename=random_string("middlename:", 10),
            lastname=random_string("lastname:", 10), nickname=random_string("nickname:", 10),
            company=random_string("company:", 10),
            address=random_string("address:", 10), bday="27", bmonth="August", byear="1986",
            homephone=random_phone(10),
            mobilephone=random_phone(10), workphone=random_phone(10), secondaryphone=random_phone(10),
            )

    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
