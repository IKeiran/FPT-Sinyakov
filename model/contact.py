__author__ = 'Keiran'
# -*- coding: utf-8 -*-
from sys import maxsize


def randomize_str(attr, max_len=5, include_spaces = True):
    import random, string
    symbols = string.ascii_letters + string.digits
    if include_spaces:
        symbols += " " * 10
    return attr + "".join(random.choice(symbols) for i in range(max_len)).rstrip().lstrip()

class Contact:
    def __init__(self, first_name=None, mid_name=None, last_name=None, nick_name=None,
                 title=None, company=None, adress=None, home_phone=None, mobile_phone=None,
                 work_phone=None, fax=None, email_prime=None, email_secondary=None, email_third=None,
                 home_page=None, birthday_year=None, birthday_month=None, birthday_day=None, anniversary_year=None,
                 anniversary_day=None, anniversary_month=None, adress_secondary=None,
                 phone_secondary=None, notes=None, id=None, all_phones=None, all_mails=None):
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
        self.all_phones = all_phones
        self.all_mails = all_mails

    def __clear__(self, s):
        import re
        return re.sub("[() -]", "", s)

    def __join_all__(self, params):
        return '\n'.join(filter(lambda x: x != "",
                    map(lambda x: self.__clear__(x),
                        filter(lambda x: x is not None, params))))

    def join_phones(self):
        self.all_phones = self.__join_all__([self.home_phone, self.mobile_phone, self.work_phone, self.phone_secondary])
        return self.all_phones

    def join_mails(self):
        self.all_mails = self.__join_all__([self.email_prime, self.email_secondary, self.email_third])
        return self.all_mails

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
                   email_prime=randomize_str('email_prime', include_spaces=False),
                   email_secondary=randomize_str('email_secondary', include_spaces=False),
                   email_third=randomize_str('email_third', include_spaces=False),
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
            and (self.first_name == other.first_name) and (self.last_name == other.last_name) \
                and (self.adress == other.adress) #(self.all_phones == other.all_phones)
      #          and (self.all_mails == other.all_mails)