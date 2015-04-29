from fixture.orm import ORMFixtue
from model.group import Group


db = ORMFixtue(host="127.0.0.1", name='addressbook', user='root', password='')
# contacts = db.get_contacts_in_group(Group(id=1))
contact_list = list()
group_list = db.get_group_list()

for group in group_list:
    try:
        contacts = db.get_contacts_in_group(group)
        if len(contacts) > 0:
            print(contacts)
            #contact_list.update(contacts)
    except:
        print('error')
print(contact_list)
"""
print('')
try:

    for item in l:
        contacts = db.get_contacts_in_group(l)
        print(contacts)
    print (len(l))
except:
    pass
finally:
   pass
"""
#print(contacts)
