class Person:
    def __init__(self, name):
        self.name = name


class MDPerson(Person):
    def __init__(self, name):
        self.name = 'Doctor' + name


class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ',Esquire'


person = Person('Fudd')
doctor = MDPerson('Fudd')
lawer = JDPerson('Fudd')

print(doctor.name)
print(person.name)
print(lawer.name)
