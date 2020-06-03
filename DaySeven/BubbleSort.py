l = []
num = int (input ("How Many Numbers You Wanna Add"))
for i in range (num):
    numbers = int (input ("Enter Number "+str(i+1)+'\n'))
    l.append (numbers)
print("List Is = ",l)
n = len (l)
for i in range (n):
    for j in range (0,(n-1-i)):
        if l[j] > l[j + 1]:
            (l[j],l[j+1]) = (l[j+1],l[j])
print ("Sorted List Is:")
print (l)