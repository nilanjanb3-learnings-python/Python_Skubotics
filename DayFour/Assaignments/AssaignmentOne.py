s={0,1,2,3,4,5,6,7,8,9}
password=(input("Enter The Password\n Must contain at least one digit\nMust contain at least one of the following special characters @, #, $ \nLength should be between 6 to 20 characters."))
n=set(password)
print(n)
p=s.intersection(n)
m=list(p)
print(p)
if(len(password)<6):
    print("Length should be greater than 6")
if(len(password)>20):
    print("Password should be less than 20")
if(len(m)==0):
    print("Ok")

else:
    print("Must be a digit in Password")
