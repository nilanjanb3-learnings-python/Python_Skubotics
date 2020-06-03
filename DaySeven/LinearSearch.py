l=[10,20,30,40,50,60,70,80,90]
def search (l,num):
    for i in l:
        if(i==num):
            print("Found")
            break
    else:
        print("Not Found")
num=int(input("Enter A Number To Be Search"))
search(l,num)