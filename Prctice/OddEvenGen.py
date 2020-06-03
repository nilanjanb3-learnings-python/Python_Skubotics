choice=int(input("1.Even\n2.Odd\n"))
num=int(input("Enter The Limits\n"))
for i in range(1,num+1):
    if(choice==1 and i%2==0):
        print(i)
    if(choice==2 and i%2!=0):
        print(i)
else:
    print()