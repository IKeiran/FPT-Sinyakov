from model.group import Group
import os.path
import json
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "output ашду"])
except getopt.GetoptError as err:
#    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a

test_data = [Group(name='', header='', footer='')] + \
            [Group.random() for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, 'w') as out_file:
    out_file.write(json.dumps(test_data, default=lambda x: x.__dict__, indent=2))

