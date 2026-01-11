##Question 1.a.i
class Node():
    def __init__(self, pLeftPointer, pData, pRightPointer):
        self.LeftPointer = pLeftPointer
        self.Data = pData
        self.RightPointer = pRightPointer
## Question 1.a.ii         
global FreePointer
global RootPointer
global Tree
Tree = [Node for i in range(10)]

## Question 1.b
def CreateTree():
    global FreePointer
    global RootPointer
    FreePointer = 0
    RootPointer = -1
    FreeList = Node.LeftPointer
    Node.RightPointer = -1
## Question 1.c 
def AddToTree(NewDataItem):
    if FreePointer == -1:
        print("Error, no free space left")
    else: 
        NewNodePointer = FreePointer
        Tree.Data[NewNodePointer]= NewDataItem
        FreePointer = Node.LeftPointer
        Tree.LeftPointer[NewNodePointer]=


##Question 2.a
Grid = [[""for i in range (10)]for j in range (30)]
class IslandClass():
    sand = "."
    def __init__(self, sand):
        for i in range(10):
            for j in range(30):
                Grid[i][j] = sand
##Question 2.b.i
    def GetSquare(rownum,columnnum):
        return Grid[rownum][columnnum]
##Question 2.b.ii
def DisplayGrid():
    print(Grid)
## Question 3.a
global QueueData
QueueData = [""for i in range (20)]
StartPointer = -1
EndPointer = 0
#Question 3.b
def Enqueue(DataItem):
    if EndPointer<20 and EndPointer>=0:
        if StartPointer == -1:
            StartPointer = 0
        else:
            QueueData[EndPointer]=DataItem
            EndPointer = EndPointer + 1
        print("Data is added successfully")
        return True 
    else:
        print("Data couldn't be added successfully")
        return False
    

## Question 3.c        
def ReadFile():
    FileName = input("Please Enter The Name Of The File")



##Question 3.e
def Remove():
    if QueueData[StartPointer]!="" and QueueData[StartPointer + 1]!="":   
        String = str(QueueData[StartPointer]&&" "&&QueueData[StartPointer+1])
        QueueData[StartPointer]=""
        QueueData[StartPointer+1]=""
        StartPointer = StartPointer + 2
        return String 
    else:
        return "No Items" 
    
    
    
    
    
    


