## Linear Search
##global Arr
##Arr = [1,19,190,921,224,31,0,31,33] 
##
##def LinearSearch(Search):
##    global Arr
##    Found = False 
##    for i in range(0,len(Arr)):
##        if Arr[i] == Search:
##            print("The value is found at index:",i)
##            Found = True 
##            return 1
##    return 0
##    print("The value is not found") 
##    
##LinearSearch(19) 
##
##
##
## Bubble Sort
##
##global EmpID, EmpInfo
##
##EmpID = [102,109,104,101, 103]
##EmpInfo = [                      # 2D: Name, Dept, Salary
##    ["John", "IT", 55000],
##    ["Amy", "HR", 92000],
##    ["Zane", "Finance", 87000],
##    ["Mike", "IT", 64000],
##    ["Emma", "HR", 73000]
##]
##
##def BubbleSort():
##    global EmpID, EmpInfo
##    Sorted = False
##    Max = len(EmpInfo) - 1
##    
##    while Sorted == False:
##        Sorted = True
##        for i in range(0,Max):
##            if EmpInfo[i][2] < EmpInfo[i+1][2]:
##                sorted = False
##                temp = EmpInfo[i][2]
##                EmpInfo[i][2] = EmpInfo[i+1][2]
##                EmpInfo[i+1][2] = temp
##
##                temp2 = EmpInfo[i][1]
##                EmpInfo[i][1] = EmpInfo[i+1][1]
##                EmpInfo[i+1][1] = temp2
##
##                temp3 = EmpInfo[i][0]
##                EmpInfo[i][0] = EmpInfo[i+1][0]
##                EmpInfo[i+1][0] = temp3
##
##                temp4 = EmpID[i]
##                EmpID[i] = EmpID[i+1]
##                EmpID[i+1] = temp4
##
##
##        Max = Max - 1
##
##BubbleSort()
##print (EmpID)
##print (EmpInfo) 
##    
##    


## Insertion Sort

##global EmpID, EmpInfo
##EmpID = [104, 101, 109, 103, 102]
##EmpInfo = [
##    ["Zane", "Finance", 87000],
##    ["Mike", "IT", 64000],
##    ["Amy", "HR", 92000],
##    ["Emma", "HR", 73000],
##    ["John", "IT", 55000]
##]
##
##
##def InsertionSort():
##    global EmpID, EmpInfo
##    for i in range (1, len(EmpID)):
##        key = EmpID[i]
##        key1 = EmpInfo[i][0]
##        key2 = EmpInfo[i][1]
##        key3 = EmpInfo[i][2] 
##        j = i-1
##        while j>=0 and EmpID[j] > key:
##            EmpID[j+1] = EmpID[j]
##          
##            EmpInfo[j+1][0] = EmpInfo[j][0]
##
##            EmpInfo[j+1][1] = EmpInfo[j][1]
##
##            EmpInfo[j+1][2] = EmpInfo[j][2]
##
##            j = j-1
##        EmpID[j+1]=key
##        EmpInfo[j+1][0]=key1
##        EmpInfo[j+1][1]=key2
##        EmpInfo[j+1][2]=key3
##
##InsertionSort()
##print(EmpID, EmpInfo) 


##BinarySearch
##
##
##global Marks, Names
##
##Marks = [98, 95, 93, 90, 85]
##Names = ["Sam", "Jade", "Chris", "Zara", "Ben"]
##
##
##def BinarySearch(SearchValue):
##    Found = False
##    UpperValue = len(Marks)-1
##    LowerValue = 0 
##    while Found == False and UpperValue >= LowerValue:
##        MidValue = int((UpperValue + LowerValue)/2)
##        if Marks[MidValue] == SearchValue:
##            print("Student is Found and the name of the student is: ", Names[MidValue])
##            Found = True 
##        elif Marks[MidValue] > SearchValue:
##            LowerValue = MidValue + 1
##        else:
##            UpperValue = MidValue - 1
##
##    if Found == False:
##        print("The Student is not found or present")
##BinarySearch(98) 
##

##InsertionSort2

##
##global StudentID, StudentInfo
##
##StudentID = [105, 101, 106, 102, 104]
##StudentInfo = [
##    ["Ayesha", "Physics", 88],
##    ["Brian", "Math", 95],
##    ["Chloe", "Biology", 78],
##    ["David", "Chemistry", 92],
##    ["Eli", "CS", 85]
##]
##def InsertionSort():
##    for i in range(1,len(StudentInfo)):
##        key = StudentInfo[i][2]
##        key1 = StudentInfo[i][0]
##        key2 = StudentInfo[i][1]
##        key3 = StudentID[i]
##        j = i - 1
##        while j >=0 and StudentInfo[j][2] < key:
##            StudentInfo[j+1][0] = StudentInfo[j][0]
##            StudentInfo[j+1][1] = StudentInfo[j][1]
##            StudentInfo[j+1][2] = StudentInfo[j][2]
##            StudentID[j+1]= StudentID[j]
##            j = j - 1
##        StudentInfo[j+1][0] = key1
##        StudentInfo[j+1][1] = key2
##        StudentInfo[j+1][2] = key
##        StudentID[j+1]= key3
##
##
##InsertionSort()
##print(StudentID, StudentInfo) 

#### Recursion
##def factorial(n):
##    if n == 1:                      # Base case
##        return 1
##    else:
##        return n * factorial(n-1) 
##
#### using recursion to find factorial of 4, starting with factorial(4) 
## 4 * factorial(3)
##  → 3 * factorial(2)
##      → 2 * factorial(1)
##          → returns 1
##→ 2 * 1 = 2 → 3 * 2 = 6 → 4 * 6 = 24









## Reverse String
##def Reverse(Str):
##    if len(Str) <= 1:
##        return Str
##    else:
##        return Reverse(Str[1:]) + Str[0]
##ReverseString = Reverse("hello")
##print(ReverseString) 

## How many times a character comes in a string
##def Count(Str, SV):
##    if Str == "":
##        return 0
##    elif Str[0]==SV:
##        return 1 + Count(Str[1:], SV)
##    else:
##        return 0 + Count(Str[1:],SV)
##CountVal = Count("Hello", "l")
##print (CountVal) 

##def Power(x,n):
##    if x == 1 or n==0:
##        return 1
##    elif n > 0:
##        return x * Power(x, n-1)
##    else:
##        return 1/Power(x,-n) 
##PowerVal = Power(10,-1)
##print(PowerVal) 

## Binary Search using recursion:

##arr = [5, 9, 14, 23, 35, 46]
##
##def BinarySearch(ARR, low, high, SV):
##    if low > high:
##        return -1
##    mid = (low + high)//2
##    if ARR[mid] == SV:
##        return mid
##    elif ARR[mid]<SV:
##        return BinarySearch(ARR,mid+1, high, SV)
##    else:
##        return BinarySearch(ARR,low, mid-1, SV)
##Index = BinarySearch(arr,0,len(arr)-1, 35)
##print(Index)


##
##arr = [100, 85, 70, 55, 40, 25]
##def BinarySearch(Arr, low, high, SV):
##    if low>high:
##        return -1
##    mid = (low+high)//2
##    if Arr[mid] == SV:
##        return mid
##    elif Arr[mid]>SV:
##        return BinarySearch(Arr, low, mid-1, SV)
##    else:
##        return BinarySearch(Arr, mid+1, high, SV)
##Index = BinarySearch(arr, 0, len(arr)-1, 70)
##print(Index) 
##
##| Traversal     | Order of Visit      |
##| ------------- | ------------------- |
##| **Inorder**   | Left → Root → Right |
##| **Preorder**  | Root → Left → Right |
##| **Postorder** | Left → Right → Root |

