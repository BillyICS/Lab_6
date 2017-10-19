class Student:
    def __init__(self, name, class_of='', major=''):
        self.name = name
        self.class_of = class_of
        self.major = major
        self.knowledge = 0

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name