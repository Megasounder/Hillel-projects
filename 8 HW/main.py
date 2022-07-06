
class Human:
    def __init__(self, name, gender, age, country):
        self.name = name
        self.gender = gender
        self.age = age
        self.country = country

    def __str__(self):
        return f'Human(name: {self.name}, gender: {self.gender}, age: {self.age}, country: {self.country})'

    def __repr__(self):
        return f'Human("name": {self.name}, "gender": {self.gender}, "age": {self.age}, "country": {self.country})'

