from pony.orm import *
from datetime import datetime
from model.contact import Contact
from model.group import Group
from pymysql.converters import decoders


class ORMFixtue:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixtue.ORMContact, table='address_in_groups', column='id', reverse='groups', lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        first_name = Optional(str, column='firstname')
        last_name = Optional(str, column='lastname')
        address = Optional(str, column='address')

        home_phone = Optional(str, column='home')
        mobile_phone = Optional(str, column='mobile')
        work_phone = Optional(str, column='work')
        email_prime = Optional(str, column='email')
        email_secondary = Optional(str, column='email2')
        email_third = Optional(str, column='email3')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixtue.ORMGroup, table='address_in_groups', column='group_id', reverse='contacts', lazy = True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders)
        self.db.generate_mapping()

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixtue.ORMGroup))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            result = Contact(id=str(contact.id),
                           first_name=contact.first_name, last_name=contact.last_name, adress=contact.address,
                           home_phone=contact.home_phone, mobile_phone=contact.mobile_phone, work_phone=contact.work_phone,
                           email_prime=contact.email_prime, email_secondary=contact.email_secondary, email_third=contact.email_third)
            return result
        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixtue.ORMContact if c.deprecated is None))

    @db_session
    def get_orm_group(self, group):
        return list(select(g for g in ORMFixtue.ORMGroup if g.id == group.id))[0]

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = self.get_orm_group(group)
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = self.get_orm_group(group)
        return self.convert_contacts_to_model(
            select(c for c in ORMFixtue.ORMContact if c.deprecated is None and orm_group not in c.groups))

    # @db_session
    # def get_contact_group_boundry(self):
    #     return list(select(d for d in ORMFixtue.ORMBoundary))
