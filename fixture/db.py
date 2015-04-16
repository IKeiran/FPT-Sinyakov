__author__ = 'Keiran'
import mysql.connector
from model.group import Group
from model.contact import Contact

class DBFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        cursor = self.connection.cursor()
        group_list = []
        try:
            cursor.execute('select group_id, group_name, group_header, group_footer from group_list')
            for row in cursor:
                (id, name, header, footer) = row
                group_list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return group_list

    def get_contact_list(self):
        cursor = self.connection.cursor()
        contact_list = []
        try:
            cursor.execute("select id, firstname, lastname, address from addressbook WHERE deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, first_name, last_name, adress) = row
                contact_list.append(Contact(id=str(id), first_name=first_name, last_name=last_name, adress=adress))
        finally:
            cursor.close()
        return contact_list

    def destroy(self):
        self.connection.close()