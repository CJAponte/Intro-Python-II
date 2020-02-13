class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __repr__(self):
        return f'{repr(self.name)} \n{repr(self.desc)}'