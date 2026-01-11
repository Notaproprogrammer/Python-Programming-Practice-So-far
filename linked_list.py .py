class node():
    def __init__(self,pData):
        seld.Data = pData
        self.Next =-1



class Linkedlist():
    def __init__(self):
        self.Head =-1 ##start value of head is -1
    def TraverseList(self):
        if self.Head ==-1:
            print("The Linked List is empty")
        else:
            Current = self.Head ##Head value will change. So a temporary variable has been used
            while Curren!= -1:
                print (Current.Data,end = '----->')
                Current = Current.Next
    def LengthOfTheList(self):
        TotalNode = 0
        if self.Head == -1:
            print("Linked list is empty")
            return TotalNode
        Current = self.Head
        while Current != -1:
            TotalNode+= 1
            Current = Current.Next
        return TotalNode
    def SearchAValue(self, PSearchValue):
        Found = False
        Count = 1
        if self.Head == -1:
            print("Linked List is empty..")
        else:
            Current= self.Head
            while Current != -1 and not Found:
                if Current.Data==PSearchValue:
                    print("the node is present at node number",Count)
                    Found = True
                else:
                    Current=Current.Next
                    Count = Count + 1
            if Found == False:
                print("The node value is not present in the list")
    def InsertAtBeginning(self,PData):
        NewNode = Node(PData)
        NewNode.Next = self.Head
        self.Head = NewNode
        print("The node got added")
    def InsertAtEnd(self,PData):
        NewNode = Node(PData)
        if self.Head == -1:
            self.Head = NewNode
            print("The node got added")
        else:
            Current = self.Head
            while Current.Next != -1:
                Current=Current.Next
            Current.Next = NewNode
            print("The node got added")
    def AddAfterASpecificValue(self, PsearchVal, PData):
        if self.Head == -1:
            print ("Linked List is empty. Insertion cannot be performed")
        else:
            Current = self.Head
            Found = False
            while Current != -1 and not Found:
                if Current.Data ==PsearchVal:
                    NewNode= Node(PData)
                    NewNode.Next = Current.Next
                    Current.Next = NewNode
                    print("The node got added")
                    Found = True
                else:
                    Current=Current.Next
            if Found == False:
                print("The node value is not present in the list so new node cannot be inserted")
    def AddBeforeASpecificValue(self, PSearchVal,PData):
        Found = False
        if self.Head == -1:
            print ("Linked list is empty. Insertion cannot be performed based on a value")
        else:
            if self.Head.Data == PSearchVal:
                NewNode = Node(PData)
                NewNdoe.Next = self.Head
                self.Head = NewNode
                Found = True
                print ("The node got added")
            else:
                Previous = self.Head
                Current = self.Head.Next
                while Current != -1 and not Found:
                    if Current.Data == PSearchVal:
                        NewNode = Node(PData)
                        Previous.Next = NewNode
                        NewNode.Next = Current
                        Found = True
                    else:
                        Previous = Previous.Next
                        Current = Current.Next
        if Found == False:
            print("Node value is not present in the list so new node cannot be inserted") 
                    
    def DeleteAtBeginning(self):
        if self.Head== -1:
            print ("Linked List is empty. Deletion cannot be performed")
        else:
            if self.Head.Next == -1:
                self.Head = -1
                print ("The node got deleted")
            else:
                Current = self.Head
                self.Head = Current.Next
                Current.Next =-1
                print ("The node got deleted")
    def DeleteAtEnd(self):
        if self.Head == -1:
            print("Linked list is empty.Deletion cannot be performed")
        else:
            if self.Head.Next == -1:
                self.Head =-1
                print ("The node got deleted")
            else:
                Previous=self.Head
                Current = self.Head.Next
                while Current.Next != -1:
                    Current = Current.Next
                    Previous = Previous.Next
                Previous.Next =-1
                print("The Node got deleted")
            
            
            
                
