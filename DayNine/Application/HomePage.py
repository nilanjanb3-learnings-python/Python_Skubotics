def main():
    print("Enter Your choise")
    print("1. SignUp")
    print('2. LogIn')
    print()
    choise=input()
    if(choise=='1'):
        name=input('Enter Name\n')
        age=int(input('Enter Age\n'))
        password=input("Enter PassWord\n")
        phone=int(input("Enter Phone\n"))
        email=input('Enter Email Id\n')
        print("Given Details",'\n',name,'\n',age,'\n',password,'\n',phone,'\n',email)
    elif(choise=='2'):
        email_temp=input("Enter Email Id\n")
        password_temp=input('Enter Password\n')
main()
