password=input("Enter The PassWord")
flag=0
sflag=0
if (6<len(password) and len(password)<20):
    for i in password:
        if(i.isdigit()):
            flag+=1
        elif(i=='@' or i=='#' or i=='$'):
            sflag+=1
if(flag>0 and sflag>0):
    print("Correct PassWord")
else:
    print("In Correct Password")