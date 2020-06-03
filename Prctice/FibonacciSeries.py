terms=int(input("Enter The Number Of Terms"))
t1=0
t2=1
tn=0
for i in range(terms):
    print(t1)
    tn=t1+t2
    t1=t2
    t2=tn