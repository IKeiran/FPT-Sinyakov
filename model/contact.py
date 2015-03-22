__author__ = 'Keiran'
# -*- coding: utf-8 -*-
from sys import maxsize


def randomize_str(attr):
    import random
    return attr + str(random.randint(0, 1000000))


class Contact:
    def __init__(self, first_name=None, mid_name=None, last_name=None, nick_name=None,
                 title=None, company=None, adress=None, home_phone=None, mobile_phone=None,
                 work_phone=None, fax=None, email_prime=None, email_secondary=None, email_third=None,
                 home_page=None, birthday_year=None, birthday_month=None, birthday_day=None, anniversary_year=None,
                 anniversary_day=None, anniversary_month=None, adress_secondary=None,
                 phone_secondary=None, notes=None, id=None):
        self.first_name = first_name
        self.mid_name = mid_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.title = title
        self.company = company
        self.adress = adress
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email_prime = email_prime
        self.email_secondary = email_secondary
        self.email_third = email_third
        self.home_page = home_page
        self.birthday_year = birthday_year
        self.birthday_month = birthday_month
        self.birthday_day = birthday_day
        self.anniversary_year = anniversary_year
        self.anniversary_day = anniversary_day
        self.anniversary_month = anniversary_month
        self.adress_secondary = adress_secondary
        self.phone_secondary = phone_secondary
        self.notes = notes
        self.id = id

    @classmethod
    def random(cls):
        import random
        return cls(first_name=randomize_str('first_name'),
                   mid_name=randomize_str('mid_name'),
                   last_name=randomize_str('last_name'),
                   nick_name=randomize_str('nick_name'),
                   title=randomize_str('title'),
                   company=randomize_str('company'),
                   adress=randomize_str('adress'),
                   home_phone=randomize_str('home_phone'),
                   mobile_phone=randomize_str('mobile_phone'),
                   work_phone=randomize_str('work_phone'),
                   fax=randomize_str('fax'),
                   email_prime=randomize_str('email_prime'),
                   email_secondary=randomize_str('email_secondary'),
                   email_third=randomize_str('email_third'),
                   home_page=randomize_str('home_page'),
                   birthday_year=str(random.randint(1950, 2015)),
                   birthday_month=str(random.randint(0, 12)),
                   birthday_day=str(random.randint(0, 31)),
                   anniversary_year=str(random.randint(1950, 2015)),
                   anniversary_month=str(random.randint(0, 12)),
                   anniversary_day=str(random.randint(0, 31)),
                   adress_secondary=randomize_str('adress_secondary'),
                   phone_secondary=randomize_str('phone_secondary'),
                   notes=randomize_str('notes'))

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __repr__(self):
        return 'First name: %s; Last name: %s; id = %s' % (self.first_name, self.last_name, self.id)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
        and (self.first_name == other.first_name) and (self.last_name == other.last_name)