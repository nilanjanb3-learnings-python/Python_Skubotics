num=int(input("Enter Limits\n"))
for i in range(num):
    for j in range(num-i-1):
        print(' ',end='')
    for j in range(i+1):
        print('*',end=' ')
    print()
for i in range(num):
    for j in range(i+1):
        print(' ',end='')
    for j in range(num-i-1):
        print('*',end=' ')
    print()