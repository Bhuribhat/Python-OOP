class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

# lambda function
sorted(student_objects, key=lambda student: student.age)   # sort by age
# >> [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

# The operator module functions allow multiple levels of sorting.
from operator import itemgetter, attrgetter

sorted(student_tuples, key=itemgetter(1, 2))               # sort by grade then age
# >> [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

sorted(student_objects, key=attrgetter('grade', 'age'))    # sort by grade then age
# >> [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]