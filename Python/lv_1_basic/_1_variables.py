import json
class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

person = Person("Ken",5,'M')
person2 = person
person2.sex = 'F'
print(json.dumps(person.sex))
print(json.dumps(person2.sex))