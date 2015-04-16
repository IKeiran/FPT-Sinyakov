__author__ = 'vs'
from fixture.db import DBFixture


db_fixture = DBFixture(host="localhost", name="addressbook",
                       user="root", password="")
print(db_fixture.get_group_list())


print (db_fixture.get_contact_list())