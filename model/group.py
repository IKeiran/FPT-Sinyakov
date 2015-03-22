__author__ = 'Keiran'
from sys import maxsize


class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    @classmethod
    def random(cls):
        import random
        return cls(name="Group_name" + str(random.randint(0, 1000000)),
                   header="Group_header" + str(random.randint(0, 1000000)),
                   footer="Group_footer" + str(random.randint(0, 1000000)))

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize