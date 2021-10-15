# Basic Class
class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print(f"Hi! I'm a dog. My name is {self.name}\nI'm {self.age} years old.")

    def talk(self):
        print("bark !!")

dome = Dog("dome", 20)     # create object
dome.speak()               # call class method

# Inheritance -> Cat is child class and Dog is parent class
class Cat(Dog):
    def __init__(self, name, age, color = "Red"):
        super().__init__(name,  age)
        self.color = color

    # override method
    def speak(self):       
        print(f"Hi! I'm a cat. My name is {self.name}\nI'm {self.age} years old.\nMy color is {self.color}.")

    def talk(self):
        print("meow !!")

tanwa = Cat("tanwa", 5, "Blue")
tanwa.talk()
cat = Cat("a", 1)
cat.speak()