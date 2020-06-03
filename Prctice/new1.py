num=int(input("Enter The Limits"))
for i in range(num):
    for j in range(num-i):
        print(" ",end='')
    for k in range(i+1):
        print("*",end='')
    print()
for i in range(num):
    for j in range(i+2):
        print(" ",end='')
    for k in range(num-i-1):
        print('*',end='')
    print()