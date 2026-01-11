##Date: 2/10/2024 
## if it is not necessary to make the attribute private then do not do it 
class character:
    def __init__(self, PName, PXPosition, PYPosition):
        self.Name = PName
        self.PXposition = PXPosition
        self.PYposition=PYPosition
    def GetXposition(self):
        return self.PXposition
    def GetYposition(self):
        return self.PYposition




    def SetXposition(self,NewX):
        self.PXposition = self.PXposition + NewX
        if self.PXposition>10000:
            self.PXposition=10000
        elif self.PXposition<0:
            self.PXposition = 0
        self.PXposition = NewX
    def SetYpositin(self,NewY):
        self.PYposition = self.PYposition + NewY
        if self.PYposition>10000:
            self.PYposition=10000
        elif self.PYposition<0:
            self.PYposition = 0 


    def Move(self,Direction):
        if Direction == "up":
            self.SetYposition(10)
        elif Direction == "down":
            self.SetYposition(-10)
        elif Direction =="right":
            self.SetXposition(10)
        elif Direction =="left":
            self.SetXposition(-10)
Jack = Character(PXposition: 50, PYPosition: 50, PName = "Jack")
## You can overwrite a function in the parent class using super
