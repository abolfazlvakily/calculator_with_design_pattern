from interface import implements
from web.oop import interface


class Sum(implements(interface.Calculate)):
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def execute(self):
        return self.first_number + self.second_number


class Subtraction(implements(interface.Calculate)):
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def execute(self):
        result = self.first_number - self.second_number
        return result
