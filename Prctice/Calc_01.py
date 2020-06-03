import math as m
class cal():
    def __init__(self, num1,num2):
        self.num1 = num1
        self.num2 = num2
    def log(self):
        return m.log(num1,10)

    def add(self):
        return num1+num2

    def mul(self):
        return num1*num2

    def div(self):
        return num1/num2

    def sub(self):
        return num1-num2


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
obj = cal(num1, num2)
choice = 5
while choice != 0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Log")
    choice = int(input("Select operation : "))
    if choice == 1:
        print("Result: ", obj.add())
    elif choice == 2:
        print("Result: ", obj.sub())
    elif choice == 3:
        print("Result: ", obj.mul())
    elif choice == 4:
        print("Result: ", round(obj.div(),3))
    elif choice==5:
        print(round(obj.log(),3))
    elif choice==0:
        print("Exiting...")
        break
    else:
        print("Invalid choice.")