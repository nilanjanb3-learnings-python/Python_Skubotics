'''Pass=Student is inheriting from Person
If Student han unique method then don't use pass'''
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(self.fname,self.lname)
x=Person('Nilanjan','Bhattacharjee')
x.printname()
y=Person("Rittick","Bhttacharjee")
y.printname()
class Student(Person):
    def __init__(self,fname,lname,clg):
        self.clgname=clg
    def printnameclg(self):
        print(self.fname,self.lname,self.clgname)
obj=Student()

