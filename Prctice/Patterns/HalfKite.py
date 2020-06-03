lim=int(input("Give Limits\n"))
for i in range(lim):
    for j in range(i):
        print("*",end="")
    print()
for i in range(lim):
    for j in range(lim-i):
        print("*",end="")
    print()