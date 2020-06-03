def signup():
    try:
        f = open ("Signup.txt", 'a')
        name = input ('Enter Name\n')
        name=name+","
        f.write (name)
        age =(input ('Enter Age\n'))
        age = age+","
        f.write (age)
        password = input ("Enter PassWord\n")
        password=password+","
        f.write (password)
        phone = (input ("Enter Phone\n"))
        phone=phone+","
        f.write (phone)
        email = input ('Enter Email Id\n')
        f.write (email+"\n")
        f.close()
    except:
        print("File Not Supported")
def login(username,password):
    try:
        f = open ("Signup.txt", 'r')
        for x in f:
            l=x.split (',')
            if (l[2] == password and l[4]==username):
                print('Login Success')
                break
            else:
                print("Invalid Username Or Password")
                break
    except:
        print("Error 404")