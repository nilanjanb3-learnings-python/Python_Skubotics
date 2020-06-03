import HomePage
def writeBlog():
    f = open ("Blog.txt", 'a')
    content=input("Enter Contents")
    content=content+'#'
    f.write(content)
    writer=input("Enter Writer name")
    writer=writer+'\n'
    f.write(writer)
    f.close()
    print('Post Updated')
    blogPage()

def readBlog():
    f = open ("Blog.txt", 'r')
    for x in f:
        l=x.split('#')
        print(l[0],',',l[1])
    f.close()
    print('-------END-------')
    blogPage()
def blogPage():
    print ("Enter Your choise")
    print ("1. Write Blog")
    print ('2. Read Blogs')
    print('3. Log Out')
    print ()
    choise = input ()
    if (choise == '1'):
        writeBlog()
    elif (choise == '2'):
        readBlog()
    elif(choise==3):
        Homepage.main()

