x=int(input("Enter a 4 digit number"))
sum=0
while x>0:
    digit1=x%10
    if(digit1%2!=0):
        sum+=digit1
    x=x//10
print(sum)