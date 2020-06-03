lim=int(input("Give Limits"))
for i in range(lim):
    for j in range(lim-i):
        print("*",end="")
    print()