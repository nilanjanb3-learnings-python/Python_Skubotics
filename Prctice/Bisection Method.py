# Bisection Method
#function declairation
def fun(x):
    return x**2 - 4
a=float(input("Enter expecting lowest (a) Point"))
b=float(input("Enter expecting highest (b) Point"))
if fun(a)>0:
    print("Enter a value again")
if fun(b)<0:
    print("Enter b value again")
else:
    c = (a + b) / 2
    while fun(c)<=0.0:
        if fun(c)>0:
            b=c
            c = (a + b) / 2
        if fun(c)<0:
            a=c
            c = (a + b) / 2
        else:
            print("The result is" + str(c))
            break
