import Blog
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
def login():
    try:
        f=open("Signup.txt",'r')
        username = input ("Enter Mail Id")
        password = input ("Enter Password")
        for x in f:
            if(x.find(username)>=0):
                l=x.split(',')
                if(l[2]==password):
                    print("Login Success")
                    Blog.blogPage()
                    break
                else:
                    print("Invalid Password")
                    break
        else:
            print("Invalid Username")
    except:
        print("Error 404")