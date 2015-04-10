from model.contact import Contact
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contact", "output file"])
except getopt.GetoptError as err:
    sys.exit(2)

n = 5
f = "data/contact.json"

for option, arg in opts:
    if option == '-n':
        n = int(arg)
    elif option == '-f':
        f = arg

test_data = [Contact(first_name='', mid_name='', last_name='',
                     adress='', email_prime='', home_phone = '')] + \
            [Contact.random() for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, 'w') as out_file:
    jsonpickle.set_encoder_options("json", indent=2)
    out_file.write(jsonpickle.encode(test_data))
