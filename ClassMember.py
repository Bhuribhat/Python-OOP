""" Class or static variable can be referred through a class,
    but not directly through an instance. """

class example:
    staticVariable = 9               # Access through class

print(example.staticVariable)        # gives 9

# Access through an instance
instance = example()
print(instance.staticVariable)       # gives 9

# Change within an instance
instance.staticVariable = 12
print(instance.staticVariable)       # gives 12
print(example.staticVariable)        # gives 9

""" Class or static variable are quite distinct from and
    does not conflict with other member variable with the same name. """

class Fruits(object):
    # class / static variable
    count = 0
    
    # member variable -> can have the same name
    def __init__(self, name, count):
        self.name = name
        self.count = count
        Fruits.count += count

def main():
    apples = Fruits("apples", 3);
    pears = Fruits("pears", 4);
    print(apples.count)
    print(pears.count)
    print(Fruits.count)
    print(apples.__class__.count)    # This is Fruit.count
    print(type(pears).count)         # So is this

if __name__ == '__main__':
    main()