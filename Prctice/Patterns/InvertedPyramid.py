num=int(input("Enter\n"))
for i in range(0,num):
    for j in range(0,i):
        print(end=' ')
    for j in range(0,num-i):
        print('*',end=' ')
    print()