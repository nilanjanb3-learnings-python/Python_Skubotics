k=1
lim=int(input("Give Limits\n"))
for i in range(lim):
    for j in range(i+1):
        print(k,end="")
        k+=1
    print()