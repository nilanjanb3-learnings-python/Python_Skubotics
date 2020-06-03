lim=int(input("Give Limits\n"))
for i in range(lim):
    for j in range(lim-i):
        print(' ',end="")
    for j in range(2*i+1):
        print('*',end='')
    print()

