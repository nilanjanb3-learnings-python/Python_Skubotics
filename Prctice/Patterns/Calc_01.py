class cal():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return a+b

    def mul(self):
        return a*b

    def div(self):
        return a/b

    def sub(self):
        return a-b


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
obj = cal(a, b)
choice = 1
while choice != 0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Select operation : "))
    if choice == 1:
        print("Result: ", obj.add())
    elif choice == 2:
        print("Result: ", obj.sub())
    elif choice == 3:
        print("Result: ", obj.mul())
    elif choice == 4:
        print("Result: ", round(obj.div(),5))
    elif choice ==0:
        print("Exiting...")
        break
    else:
        print("Invalid choice.")

print()