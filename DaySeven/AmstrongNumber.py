num=int(input("Enter A Number"))
l=len(str(num))
temp=num
ams=0
digit=0
while(temp!=0):
    digit=temp%10
    ams+=digit**l
    temp=temp//10
if(ams==num):
    print("Amstrong")
else:
    print("Not Amstrong")