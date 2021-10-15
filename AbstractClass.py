# Abstract Base Class
from abc import ABC, abstractmethod

# Inheritance from ABC
class Member(ABC):
    def __init__(self, m_id, fname, lname):
        self.m_id = m_id
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return "ID: {} {} {}".format(self.m_id, self.fname, self.lname)
    
    # cannot write method in super class
    @abstractmethod
    def discount(self):
        pass

    def full_name(self):
        return "{} {}".format(self.fname, self.lname)

# Inheritance from Member
class Gold(Member):
    # override method
    def discount(self):
        return .10

class Silver(Member):
    # override method
    def discount(self):
        return .05

if __name__ == "__main__":
    g = Gold(fname = "Peter", lname = "Parker", m_id = "49")
    print(g)
    print(g.discount())
    print(g.full_name())

    s = Silver(fname = "Sam", lname = "Sung", m_id = "69")
    print(s)
    print(s.discount())
    print(s.full_name)