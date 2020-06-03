l=[2000,500,200,100,50,20,10,5,2,1]
amount=(input("Enter the amount"))
for i in l:
    rem = amount%i
    while rem > 0:
        notes=amount//i
    print (str (i) + " " + str (notes))


