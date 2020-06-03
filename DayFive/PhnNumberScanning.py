l=input("Enter A Number In Below Format\nXXX-XXX-XXXX where 'X' is a digit\n")
m=l[0:3]
n=l[4:7]
p=l[8:12]
if(l[3] and l[7]=='-'):
    print("Writting Manner is Correct")
else:
    print("Write Numbers In Correct Manner")
if(m.isdigit() and n.isdigit() and p.isdigit()):
    print("All The Inputs Are Correct")
else:
    print("Input Digits Only")
