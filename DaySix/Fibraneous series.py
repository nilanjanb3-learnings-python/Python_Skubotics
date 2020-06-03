num=int(input("Enter the limits"))
first=0
second=1
for i in range(num):
    print(first)
    temp=first
    first=second
    second=temp+first
    print(second)