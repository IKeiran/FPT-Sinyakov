__author__ = 'Keiran'
from sys import maxsize


def randomize_str(attr, max_len=5):
    import random, string
    symbols = string.ascii_letters + string.digits + " " * 10
    return attr + "".join(random.choice(symbols) for i in range(max_len)).rstrip()


class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    @classmethod
    def random(cls):
        return cls(name=randomize_str("Group_name"),
                   header=randomize_str("Group_header"),
                   footer=randomize_str("Group_footer"))

    def __repr__(self):
        return "%s:%s;%s;%s" % (self.id, self.name, self.header, self.footer)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize