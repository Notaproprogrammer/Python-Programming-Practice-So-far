##class Node():
##    def __init__(self,PValue):
##        self.Value = PValue
##        self.Left = -1
##        self.Right = -1
##    def InsertValue(self,NewValue):
##        if NewValue<self.Value:
##            if self.Left == -1:
##                self.Left = Node(NewValue)
##            else:
##                self.Left.InsertValue(NewValue)
##        else:
##            if self.Right == -1:
##                self.Right = Node(NewValue)
##            else:
##                self.Right.InsertValue(NewValue)
##    def PreorderTraverse(self):
##        print(self.Value)
##        if self.Left != -1:
##            self.Left.PreorderTraverse()
##        if self.Right != -1:
##            self.Right.PreorderTraverse()
##    def PostorderTraverse(self):
##        if self.Left != -1:
##            self.Left.PostorderTraverse
##        if self.Right != -1:
##            self.Right.PostorderTraverse
##        print(self.Value)
##    def InorderTraverse(self,root):
##        if self.Left != -1:
##            self.Left.InorderTraverse(self.Left)
##        print(self.Value) 
##        if self.Right != -1:
##            self.Right.InorderTraverse(self.Right)
##    def FindAValue(self,SearchValue):
##        if SearchValue<self.Value:
##            if self.Left == -1:
##                return False
##            else:
##                return self.Left.FindAValue(SearchValue)
##        elif SearchValue>self.Value:
##            if self.Right == -1:
##                return False
##            else:
##                return self.Left.FindAValue(SearchValue)
##        else:
##            return True 
##            
## 
##
##
##       
##
##    
##
##
##
##Tree=Node(10) 
##Tree.InsertValue(5)
##Tree.InsertValue(4)
##Tree.InsertValue(12)
##Tree.InsertValue(11)
##Tree.InsertValue(3)
##Tree.InsertValue(22)
##Tree.InsertValue(19)
##Tree.InsertValue(6)
##Tree.InorderTraverse(10)
##print(Tree.Left.Right.Value)
##print(Tree.FindAValue(5))


##42/mj/24:
##class Node():
##    def __init__(self,pData):
##        self.__LeftPointer = -1
##        self.__RightPointer = -1
##        self.__Data = pData
##    def GetLeft(self):
##        return self.__LeftPointer
##    def GetRight(self):
##        return self.__RightPointer
##    def GetData(self):
##        return self.__Data
##    def SetLeft(self,NewLeft):
##        self.__LeftPointer = NewLeft
##    def SetRight(self,NewRight):
##        self.__RightPointer = NewRight
##
##
##class TreeCLass():
##    
##    def __init__(self):  
##        self.__Tree = [Node(-1) for i in range (20)]
##        self.__FirstNode = -1
##        self.__NumberNodes = -1
##    def InsertNode (self,NewNode):
##        if self.__NumberNodes = -1:
##            self.__Tree[0]=NewNode
##            self.__NumberNodes = self.__NumbderNodes + 1
##            self.__FirstNode = 0
##        else:
##            self.__Tree[self.__NumberNodes] = NewNode
##            NodePointerIndex = self.__FirstNode
##            Direction = ""
##            while(NodePointerIndex != -1):
##                PreviousPointerIndex = NodePointerIndex
##                if NewNOde.GetData() < self.__Tree[NodePointerIndex].GetData():
##                    NodePointerIndex = self.__Tree[NodePointerIndex.GetLeft()
##                    Direction = "Left"
##                else:
##                    NodePointerIndex = self.__Tree[NodePointerIndex].GetRight
##                    Direction = "Right" 
            


    ##traversing = Root left right (R-L-R) 
    
    ## value which has no left or right is called a leaf node. 
        
##9618/41/O/N/21

##3a
##in python, in 2d array column comes first then row during initialisation

##ArrayNodes = [[0 for i in range(3)]for j in range(20)]
##RootPointer = -1
##FreeNode = 0 
##def AddNode(ArrayNodes, RootPointer, FreeNode):
##    NodeData = int(input("Enter the Data"))
##    if FreeNode <= 19:
##        ArrayNodes[FreeNode][0]=-1
##        ArrayNodes[FreeNode][1]=NodeData
##        ArrayNodes[FreeNode][2] =-1
##        if RootPointer == -1:
##            RootPointer = 0
##        else:
##            Placed = False
##            CurrentNode = RootPointer
##            while Placed == False:
##                if NodeData < ArrayNodes[CurrentNode][1]:
##                    if ArrayNodes[CurrentNode][0] == -1:
##                        ArrayNodes[CurrentNode][0]= FreeNode
##                        Placed = True
##                    else:
##                         CurrentNode = ArrayNodes[CurrentNode][0]
##                else:
##                    if ArrayNodes[CurrentNode][2] == -1:
##                        ArrayNodes[CurrentNode][2] = FreeNode
##                        Placed = True
##                    else:
##                        CurrentNode = ArrayNodes[CurrentNode][2]
##        FreeNode = FreeNode + 1
##    else:
##        print("The tree is full")
##    return ArrayNodes, RootPointer, FreeNode
##         
##                        
##def PrintAll(ArrayNodes):
##    for i in range(0,FreeNode):
##        print(str(ArrayNodes[i][0]),     str(ArrayNodes[i][1]),    str(ArrayNodes[i][2]))                        
##
##
##for x in range(0,10):
##    ArrayNodes, RootPointer, FreeNode=AddNode(ArrayNodes, RootPointer, FreeNode)
##PrintAll(ArrayNodes)
##
##def InOrder(ArrayNodes,RootNode):
##    if ArrayNodes[RootNode][0] != -1:
##        InOrder(ArrayNodes, ArrayNodes[RootNode][0])
##    print (ArrayNodes[RootNode][1])
##    if ArrayNodes[RootNode][2] != -1:
##        InOrder(ArrayNodes,ArrayNodes[RootNode][2])
##        
##    
##        
##InOrder(ArrayNodes,0)        
