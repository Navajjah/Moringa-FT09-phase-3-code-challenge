class Magazine:
    def __init__(self, id, name, category=None):
        self._id = id
        self.name = name
        self.category = category or "General"
    
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if 2 <= len(value) <= 16:
            self._name = value
        else:
            print(f"Invalid new asssignment. '{value}' is not a valid string.") 
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if len(value) > 0:
            self.category = value
        else:
            print(f"Invalid new asssignment. '{value}' is not a valid string.")


    def __repr__(self):
        return f'<Magazine {self.name}>'
