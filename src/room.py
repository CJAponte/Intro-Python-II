# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []
    
    def __str__(self):
        return f"{self.name}\n\n{self.desc}"
    
    def get_item(self, item):
        self.items.append(item)
    
    def drop_item(self, item):
        self.items.remove(item)
