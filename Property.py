class Employee:
    # constructor
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # @property -> we can remove () when we call that function
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    # getter
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # setter
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # deleter
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

# Initialize
emp_1 = Employee('John', 'Smith')
emp_1.fullname = "Corey Schafer"

# Usage
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname