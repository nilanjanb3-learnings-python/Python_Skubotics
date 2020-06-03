m=[10,20,30,40,50,60,70,80,90,100,110]
def search (m,num):
    l=0
    u=len(m)
    while(l<=u):
        mid=(l+u)//2
        if m[mid]==num:
            print("Found")
            break
        else:
            if(m[mid]<num):
                l=mid
            if(m[mid]>num):
                u=mid
            if(num<m[0] or num>m[-1]):
                print("Not Found")
                break
num=int(input("Enter A Number To Be Searched"))
search(m,num)
