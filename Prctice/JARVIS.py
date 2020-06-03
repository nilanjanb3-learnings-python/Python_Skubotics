'''Palindrome'''
num=int(input("Enter The Number"))
digit=0
temp=num
rev=0
while(temp!=0):
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
    if(num==rev):
        print("Palindrome")
        break
else:
    print("Not Palindrome")