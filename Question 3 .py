##Question 3.a)
class TicketMachine():
    def __init__(self):
        self.__Amount = 0
        self.__State = "Idle"
    ##Question 3.b.i)
    def SetState(self,NewState):
        self.__State = NewState
        print(self.__State)
    ##Question 3.b.ii) 
    def ReturnCoins(self):
        print(self.__Amount)
        self.__Amount = 0
    ##Question 3.b.iii) 
    def PrintTicket(self):
        print("The total amount is:",self.__Amount)
        self.__Amount = 0
##Question 3.c)
    def ValidCoins(self, S):
        self.__Val = S
        if self.__Val== "10" or self.__Val == "20" or self.__Val == "50" or self.__Val == "100":
            return True
        else:
            return False
##Question 3.d)
    def CoinInserted(self, Value):
        self.__Amount = self.__Amount + int(Value) 
##Question 3.e)
    def StateChange(self):
        NewInput = input("Insert a coin (10,20,50,100) or type C for Cancel or A for Accept: ")
        if NewInput == "C":
            if self.__State == "Counting":
                self.__State = "Cancelled"
                TicketMachine.ReturnCoins(self)
            else:
                self.__State = "Idle"
        elif NewInput == "A":
            if self.__Amount == 0:
                print("No Coins Inserted")
                self.__State = "Idle"
            else:
                self.__State = "Accepted"
                TicketMachine.PrintTicket(self)
        else:
            TicketMachine.ValidCoins(self,NewInput)
            if TicketMachine.ValidCoins(self,NewInput) == True:
                TicketMachine.CoinInserted(self,NewInput)
                self.__State = "Counting"
            else:
                print("Invalid Input")

## Question 3.f)
ParkingMeter = TicketMachine()
## Question 3.g)
for i in range(0,8):
    ParkingMeter.StateChange() 
                
