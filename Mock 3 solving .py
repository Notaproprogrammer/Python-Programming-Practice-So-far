## Record Type will not have any private attributes
## mock 3 correction
## 1 c
def AddToTree(NewDataItem):
    global FreePointer, RootPointer, Tree
    if FreePointer ==-1:
        print('Error, no free space left')
    else:
        NewNodePointer=FreePointer
        Tree[NewNodePointer].Data=NewDataItem
        FreePointer = Tree[FreePointer].LeftPointer
        Tree[NewNodePointer].LeftPointer =-1

        if RootPointer == -1:
            RootPointer = NewNodePointer
        else:
            Placed = False
            Direction = ""
            CurrentNode = RootPointer
            while Placed == False:
                if NewDataItem < Tree[CurrentNode].Data:
                    if Tree[CurrentNode].LeftPointer == -1:
                        Tree[CurrentNode].LeftPointer = FreePointer - 1
                        Placed = True
                        Direction = "Left"
                    else:
                        CurrentNode = Tree[CurrentNode].LeftPointer
                    else:
                        if Tree[CurrentNode].RightPointer == -1:
                            Tree[CurrentNode].RightPointer = FreePointer
                            Placed = True
                            Direction = "Right"
                        else:
                            CurrentNode = Tree[CurrentNode].RightPointer
##in order traversing is always ascending order
##  1 d

## 1 e
def Traverse(Pointer):
    global Tree, FreePointer, RootPointer
    if Pointer != 1:
        TraverseTree(Tree[Pointer].LeftPointer)
        print(Tree[Pointer].Data)
        TraverseTree(Tree[Pointer].RightPointer)

def TraverseTree(Pointer):
    global Tree, FreePointer, RootPointer
    if Tree[Pointer].LeftPointer !=-1:
        TraverseTree(Tree[Pointer].LeftPointer)
    print(Tree[Pointer].Data)
    if Tree[Pointer].RightPointer != -1:
        TraverseTree(Tree[Pointer].RightPointer)


CreateTree()
AddToTree("Dublin")
AddToTree("")
AddToTree("")
AddToTree("")
AddToTree("")
AddToTree("")
AddToTree("Copenhagen")
AddToTree("Athens")
AddToTree("Dhaka")
OutputNodes()
TraverseTree(0)
## 2b ii
def DisplayGrid(obj):
    for i in range 



## Record Type will not have any private attributes
## Variable with all capital letters is a constant
## 2 a
class IslandClass:
    def __init__(self):
        SAND = '.' 
        self.__Grid = [[SAND for j in range(30)] for i in range(10)]

def StartDig(obj):
    
