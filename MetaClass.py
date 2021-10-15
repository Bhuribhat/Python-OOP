"""
class create an object, but it is an object itself 
because class was passed to metaclass and return object back
"""
def hello():
    class Hi:
        print("hihi")
    return Hi

def add_attribute(self):
    self.z = 9

class Test:
    pass

class Foo:
    def show(self):
        print("yo")

hello()                  # hihi
print(type(Test()))      # <class '__main__.Test'>
print(type(Test))        # <class 'type'>

""" 
functionn type create CLASS using these different arguments
Type("name", (bases), {attr}) 
name : internal representation of a class
base : anything that we inherited from -> Super Class / Parent Class
attr : any attributes 
"""
Test1 = type("Test", (), {})
Test2 = type("Test", (Foo,), {"x":5, "add_attribute":add_attribute})

t = Test2()
t.wy = "hello"
t.add_attribute()

print(t.x)               # 5
print(t.wy)              # hello
t.show()                 # yo
print(t.z)               # 9

# create our own metaclass
class Meta(type):
    def __new__(self, class_name, bases, attrs):
        newAttr = {}     # dict
        # change all attrs to capital
        for name, value in attrs.items():
            if name.startswith("__"):
                newAttr[name] = value
            else:
                newAttr[name.upper()] = value

        return type(class_name, bases, newAttr)

class Dog(metaclass = Meta):
    x = 5
    y = 8

    def speak(self):
        print("bark !!")

d = Dog()
print(d.X)                # 5
d.SPEAK()                 # bark !!