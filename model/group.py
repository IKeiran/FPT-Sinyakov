__author__ = 'Keiran'


class Group:
    def __init__(self, name=None, header=None, footer=None):
        self.name = name
        self.header = header
        self.footer = footer

    @classmethod
    def random(cls):
        import random
        return cls(name="Group_name" + str(random.randint(0, 1000000)),
                   header="Group_header" + str(random.randint(0, 1000000)),
                   footer="Group_footer" + str(random.randint(0, 1000000)))