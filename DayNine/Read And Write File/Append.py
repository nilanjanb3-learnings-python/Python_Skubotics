f=open("Demo.txt",'a')
f.write("\n First Code")
f.close()
f=open("Demo.txt",'r')
for x in f:
    print(x)
f.close()