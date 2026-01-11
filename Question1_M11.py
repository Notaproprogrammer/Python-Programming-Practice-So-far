## Question_1.a) 

class Node:
    ## DECLARE Name : STRING
    ## DECLARE Pointer : INTEGER
    def __init__(self,pName, pPointer):
        self.Name = pName
        self.Pointer = pPointer

## Question 1.b) 

global Queue, HeadPointer, TailPointer, FreePointer 

## DECLARE Queue : ARRAY[1:10] OF TYPE Node
## DECLARE HeadPointer : INTEGER
## DECLARE TailPointer : INTEGER
## DECLARE FreePointer : INTEGER 

Queue = [-1 for i in range (10)] 

Queue[0] = Node("",1)
Queue[1] = Node("",2)
Queue[2] = Node("",3)
Queue[3] = Node("",4)
Queue[4] = Node("",5)
Queue[5] = Node("",6)
Queue[6] = Node("",7)
Queue[7] = Node("",8)
Queue[8] = Node("",9)
Queue[9] = Node("",-1) 




## Question 1.c)

def CreateQueue():
    global HeadPointer, TailPointer, FreePointer

    HeadPointer = -1
    TailPointer = -1
    FreePointer = 0


## Question 1.d)
def AddName(NewName):
    global HeadPointer, TailPointer, FreePointer
    if FreePointer == -1:
        print ("Error, There are no Free Nodes Available!")
    else:
        CurrentPointer = FreePointer
        Queue[CurrentPointer].Name = NewName
        FreePointer = Queue[CurrentPointer].Pointer
    if HeadPointer == -1:
        HeadPointer = HeadPointer + 1

    Queue[CurrentPointer].Pointer = -1 
    TailPointer = TailPointer + 1 
    


## Question 1.e)
def RemoveName():
    global HeadPointer, TailPointer, FreePointer
    if HeadPointer > TailPointer:
        print ("The Queue is Empty")
    else:
        print (Queue[HeadPointer].Name,"has been removed")
        CurrentPointer = HeadPointer
        HeadPointer = HeadPointer + 1
    if HeadPointer == TailPointer:
        TailPointer = -1

    FreeList = Queue[CurrentPointer]
    FreePointer = TailPointer + 1


## Question 1.f.i)
CreateQueue()
AddName("Ayann")
AddName("Kashif")
AddName("Talib")
if HeadPointer == TailPointer:
    print(Queue[HeadPointer].Name)
else:
    for i in range (0,TailPointer + 1):
        if Queue[i].Name != "":
            print(Queue[i].Name)
RemoveName()

    
