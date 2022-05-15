import random

class Student:
    # Static Variable
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw"]

    # Constructor
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Student: ").strip()
        house = input("House: ").strip()
        return cls(name, house)

    # Getter Method
    @property
    def name(self):
        return self._name

    @property
    def house(self):
        return self._house

    # Setter Method
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw"]:
            raise ValueError("Invalid House")
        self._house = house

    # Method
    @classmethod
    def cast_spell(cls, name):
        print(f"{name} is casting spell from {random.choice(cls.houses)}")
        print("Expecto Patronum!!")

if __name__ == '__main__':
    student = Student.get()

    # cause error "Invalid House"
    try: student.house = "Number 4, Private Drive"
    except Exception as error:
        print(error)
    print(student)

    # will not cause error and change stydent's house
    student._house = "Number 4, Private Drive"
    print(student)

    # class method
    student.cast_spell("Harry")