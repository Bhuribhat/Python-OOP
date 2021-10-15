# Dunder Method
class Person:
    def __init__(self, name):
        self.name = name
    
    # string representation of an object
    def __repr__(self):
        return f"Person({self.name})"

    # multiply
    def __mul__(self, x):
        if type(x) is not int:
            raise Exception("Invalid argument, must be int")

        self.name = self.name * x
    
    # call using ()
    def __call__(self, y):
        print("Called this function", y)

    # length
    def __len__(self):
        return len(self.name)

# Person(Pooh)
Pooh = Person("Pooh")
print(Pooh)

# Person(PoohPoohPoohPooh)
Pooh * 4
print(Pooh)

# Called this function 4
Pooh(4)

# 16 (because Person(PoohPoohPoohPooh))
print(len(Pooh))