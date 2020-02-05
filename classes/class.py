class Person:
    def __init__(self,first_name):
        self.first_name=first_name
    def print_info(self):
        print(f'name:{self.first_name}')


p=Person('Andrew')
p.print_info()
