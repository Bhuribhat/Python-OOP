# Parent Class
class User():
    #constructor
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    # method
    def show_detail(self):
        print("Personal's Details")
        print(f"Name\t : {self.name}\nAge\t : {self.age}\nGender\t : {self.gender}")

    def find_gender(self):
        if (self.gender.lower() == "male"):
            gen = "his"
        else:
            gen = "her"
        return gen

# Child Class
class Bank(User):
    # static variable
    userCount = 0

    # constructor
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0
        Bank.userCount += 1
    
    # method
    def deposit(self, amount):
        self.balance += amount
        gen = self.find_gender()
        print("-" * 49)
        print(f"{self.name} deposits ฿{amount} into {gen} bank account.")
        print("Account balance has been update : ฿", self.balance)
        print("-" * 49)

    def withdraw(self, amount):
        print("-" * 49)
        if (amount < self.balance):
            self.balance -= amount 
            gen = self.find_gender()
            print(f"{self.name} withdraws ฿ {amount} from {gen} bank account.")
            print("Account balance has been update : ฿", self.balance)
        else:
            print(f"{self.name} don't have enough money !")
        print("-" * 49)
    
    def view_balance(self):
        print("=" * 30)
        self.show_detail()
        print("Balance\t : ฿", self.balance)
        print("=" * 30)

# Static
class BankSystem():
    # static variable
    AllMember = list()

    def __init__(self, Person):
        BankSystem.AllMember.append(Person)

    @staticmethod
    def view_all():
        for member in BankSystem.AllMember:
            member.view_balance()

    @staticmethod
    def countMember():
        if (len(BankSystem.AllMember) == 0):
            print("There is nobody in system.")
        elif (len(BankSystem.AllMember) == 1):
            print("There is 1 person in system.")
        else:
            print("There are", len(BankSystem.AllMember), "people in system.")

        if (Bank.userCount - len(BankSystem.AllMember) == 0):
            print("There is nobody left.")
        elif (Bank.userCount - len(BankSystem.AllMember) == 1):
            print("There is 1 person who is not in system.")
        else:
            print("There are", Bank.userCount - len(BankSystem.AllMember), "people who are not in system.")

# Function
def Instruction():
    print("================== Instruction ==================")
    print("(1) View Instruction")
    print("(2) Deposit the amount into their bank account.")
    print("(3) Withdraw the amount from their bank account.")
    print("(4) View customer's balance.")
    print("(5) Add another customer")
    print("(6) Add customer to System")
    print("(7) End the program.")
    print("=" * 49)

def CustomerInformation():
    name = input("Enter person's name : ")
    age = int(input("Enter age : "))
    gender = input("Enter gender : ")
    return name, age, gender

def main():
    run = True
    Instruction()
    while run:
        name, age, gender = CustomerInformation()
        customer = Bank(name, age, gender)
        while True:
            command = input("Select your choice [1 - 7]: ")
            while ("1" > command or command > "7"):
                print("Invalid Input")
                command = input("Please select your new choice [1 - 7]: ")
            if (command == "1"):
                Instruction()
            elif (command == "2"):
                print("=" * 49)
                amount = int(input("Enter the amount of money: ฿ "))
                customer.deposit(amount)
            elif (command == "3"):
                print("=" * 49)
                amount = int(input("Enter the amount of money: ฿ "))
                customer.withdraw(amount)
            elif (command == "4"):
                customer.view_balance()
            elif (command == "5"):
                print("=" * 49)
                print("Add another customer")
                if (customer not in BankSystem.AllMember):
                    BankSystem(customer)
                else:
                    print("Customer already exists in system !")
                break
            elif (command == "6"):
                print("=" * 49)
                print("Add Customer to System.")
                if (customer not in BankSystem.AllMember):
                    BankSystem(customer)
                else:
                    print("Customer already exists in system !")
            elif (command == "7"):
                print("=" * 49)
                BankSystem.view_all()
                BankSystem.countMember()
                run = False
                break
    print("End program..")

if __name__ == "__main__":
    main()