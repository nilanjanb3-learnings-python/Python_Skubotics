import Function
def main():
    print("Enter Your choise")
    print("1. SignUp")
    print('2. LogIn')
    print()
    choise=input()
    if(choise=='1'):
        Function.signup()
        main()
    elif(choise=='2'):
        Function.login()
main()