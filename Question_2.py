## Question 2.a) 
class Coffer:
    ## Question : STRING
    ## Answer : STRING
    ## Points : INTEGER
    ## MaximumAttempts : INTEGER
    def __init__(self,pQuestion,pAnswer,pPoints,pMaximumAttempts):
        self.__Question = pQuestion
        self.__Answer = pAnswer
        self.__Points = pPoints
        self.__MaximumAttempts = pMaximumAttempts
    ## Question 2.b)
    def GetQuestion(self):
        return self.__Question
    def GetAttempts(self):
        return self.__MaximumAttempts
    ## Question 2.c.i)
    def GetPoints(self,UserAttempts):
        if UserAttempts <= self.__MaximumAttempts:
            return int(self.__Points/UserAttempts)
        else:
            return 0

    ## Question 2.c.ii) 
    def CheckAnswer(self,UserAnswer):
        if UserAnswer == self.__Answer:
            return True
        else:
            return False
## Question 2.d)
def ReadData():
    ArrayCoffer = []
