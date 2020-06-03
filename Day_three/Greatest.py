)
if(x>y and y>=z) :
    print("x greatesr")
    if(y>z):
        print("z lowest")
    else:
        print('y&z are lowest')
elif(y>x and x>=z) :
    print("y greatest")
    if(x>z):
        print("Z lowest")
    else:
    print("x&z are lowest")
elif(x==y and y==z):
    print("Equal")
else :
    print("Z greatest")