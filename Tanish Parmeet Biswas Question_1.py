## Question 1.a) 

class List():
    ## Data : INTEGER
    ## Pointer : INTEGER
    def __init__(self,pData,pPointer):
        self.Data = pData
        self.Pointer = pPointer

## Question 1.b.i) 
global LinkedList
LinkedList = [-1 for i in range (10)]

##Question 1.b.ii)
global StartPointer
StartPointer = 0

##Question 1.b.iii)

LinkedList[0] = List(5,2)
LinkedList[1] = List(15,9)
LinkedList[2] = List(56,3)
LinkedList[3] = List(25,8)
LinkedList[4] = List(45,5)
LinkedList[5] = List(7,7)
LinkedList[6] = List(20,-1)
LinkedList[7] = List(18,1)
LinkedList[8] = List(28,4)
LinkedList[9] = List(49,6)

## Question 1.c)

def DisplayValues():
    global StartPointer,LinkedList
    while StartPointer != -1:
        print(LinkedList[StartPointer].Data)
        StartPointer = LinkedList[StartPointer].Pointer


## Question 1.d)

def FindValue(SearchValue):
    global StartPointer,LinkedList
    Found = False
    lastpointer = 0
    while StartPointer != -1 and Found == False:
        if SearchValue == LinkedList[StartPointer].Data:
            if StartPointer == 0:
                return lastpointer
            else: 
                return LinkedList[lastpointer].Pointer
            Found = True
        else:
            lastpointer = StartPointer
            StartPointer = LinkedList[StartPointer].Pointer
    if Found == False:
        return -1
        print ("the value is not found")
    else:
        print ("the value is found") 
## Question 1.e)
def CountList():
    global StartPointer,LinkedList
    count = 0
    while StartPointer != -1:
        if LinkedList[StartPointer].Data != -1:
            count = count + 1
        StartPointer = LinkedList[StartPointer].Pointer
    return count
    print("The total number of nodes are: ",count)


## Question 1.f)
def DeleteNode():
    global StartPointer,LinkedList
    PreviousPointer = 0
    Deleted = False
    while Deleted == False:
        if LinkedList[StartPointer].Pointer != -1:
            PreviousPointer = StartPointer
            StartPonter = LinkedList[StartPointer].Pointer
            
        else:
            LinkedList[StartPointer].Data = -1
            LinkedList[PreviousPointer].Pointer = -1
            Deleted = True  

## Question 1.g.i)
DisplayValues()
CountList()
FindValue()
DeleteNode()
DeleteNode()
DisplayValues()
CountList()

