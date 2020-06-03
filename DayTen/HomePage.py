import function
def main():
    print("Enter Your choise")
    print("1. SignUp")
    print('2. LogIn')
    print()
    choise=input()
    if(choise=='1'):
        function.signup()
    elif(choise=='2'):
        function.login()
main()