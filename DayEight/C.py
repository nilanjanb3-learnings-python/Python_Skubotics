'''Init is self executable'''
class Cars:
    def __init__(self,Name,Colour):
        self.Name=Name
        self.Colour=Colour
    def CarInfo(self):
        print ("the name is ",self.Name,'and the color is ',self.Colour)
car1=Cars("Maruti","Black")
car2=Cars("BMW","RED")
car3=Cars()
car1.CarInfo()
car2.CarInfo()
