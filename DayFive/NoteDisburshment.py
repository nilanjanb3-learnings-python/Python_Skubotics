amt=int(input("Enter The Amount\n"))
l=[2000,500,200,100,50,20,10,5,2,1]
for i in l:
    num=amt//i
    amt=amt%i
    print(str(num)+" Notes Of "+str(i))
    print("No of{} notes={}".format(i,num))