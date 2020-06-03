x=(input("Enter a 4 digit number"))
sum=0
for i in x:
    digit=int(i)
    if(digit%2!=0):
        sum+=digit
print(sum)