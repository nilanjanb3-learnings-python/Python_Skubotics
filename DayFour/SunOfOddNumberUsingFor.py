x=(input("Enter a 4 digit number"))
sum=0
num=int(x)
for i in x:
    digit1=num%10
    if(digit1%2!=0):
        sum+=digit1
    num=num//10
print(sum)