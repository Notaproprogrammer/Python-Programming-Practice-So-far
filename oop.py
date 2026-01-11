##Date: 18/9/2024
## OOP (object oriented programming)
##class Human():
##    def __init__(self, PName, PAge,PHeight): ##init method is the constructor
##        ## for a class in Python
##        self.__Name = PName
##        self.__Age = PAge
##        self.__Height = PHeight
##    ##Methods
##    ##Methods are of two types where one is called getter method
##    ##another one is called setter method
##
##        ##Getter method
##    def Get_Name(self):
##        return self.__Name
##    def Get_Age(self):
##        return self.__Age
##    def Get_Height(self):
##        return self.__Height
##    ##setter method
##    def Set_Name(self,NewName):
##        self.__Name= NewName
##    def Set_Age(self,NewAge):
##        self.__Age=NewAge
##    def Set_Height(self,NewHeight):
##        if NewHeight>=1  and NewHeight <=2.0:
##            self.__Height=NewHeight
##        else:
##            print("Outside range, Height can not be set")
##    def Get_Summary(self):
##        return f"Name is {self.__Name} Age is {self.Get_Age()} and height is {self.__Height}"
##    
##
##Height=float(input('Enter Height:'))
##while Height<1.0 or Height >2.0:
##    print("Invalid input. Height must be between 1 and 2 inclusive")
##    Height =float(input('Enter height:')) 
##             
##
##
       
##H1=Human('abc',20,Height)
##print (H1.Get_Summary()) 
##H1.Set_Height(1.6)
##print (H1.Get_Summary())
##
####Creating an array of objects
##HumanArray=[Human("",0,0.0) for i in range (5)]

##
##9618/41/MJ/21
##class treasurechest():
##    def __init__(self, Pquestion, Panswer,Ppoints):
##        self.__question = Pquestion
##        self.__answer= Panswer
##        self.__points = Ppoints
##        
##        




##3b
arrayTreasure["" i in range (10)] 
def readData():
    filename = "treasurechest.rtf"
    try:
        file = open(filename,  'r')
        Question=file.readline().strip()
        while Question != "":
            Answer = file.readline().strip()
            Points = file.readline().strip()
            arrayTreasure.append(TreasureChest(Question, Answer, Points))
            Question =file.readline.strip()
        file.close()
    except IOError:
        print("Could not find the file")

    ## 3 c ii

def getPointds(self,attempt):
    if attempts ==1:
        return int(self.__points)
    elif attempts == 2:
        return int(self.__points)//2
    elif attemps == 3:
        return int(self.__points)//4
    





