num=int(input("Enter A Number"))
digit=0
temp=num
rev=0
while(temp!=0):
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
    if(num==rev):
        print("Pallindrome")
    else:
        print('Not Pallindrome')