import Login
def main():
    print("Enter Your choise")
    print("1. SignUp")
    print('2. LogIn')
    print()
    choise=input()
    if(choise=='1'):
        Login.signup()
    elif(choise=='2'):
        username = input ("Enter Mail Id")
        password = input ("Enter Password")
        Login.login(username,password)
main()
