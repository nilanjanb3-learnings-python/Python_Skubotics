x=int(input("Enter a 4 digit number"))
digit1=x//1000
stage1=x%1000
digit2=stage1//100
stage2=stage1%100
digit3=stage2//10
digit4=stage2%10
if(digit1%2==0):
	digit1=0
else:
	digit1=digit1
if(digit2%2==0):
	digit2=0
else:
	digit2=digit2
if(digit3%2==0):
	digit3=0
else:
	digit3=digit3
if(digit4%2==0):
	digit4=0
else:
	digit4=digit4
sum=(digit1+digit2+digit3+digit4)
print("The result of sum of odd digits in the number is\n"+str(sum))