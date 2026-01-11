####Question 1.a)
def Recursion(A,B):
    if A <= 100:
        return 1
    else:
        if A > B:
            return 5 + Recursion(A-1,B)
        else:
            return 10 + Recursion(A-10,B)
            
print(Recursion(104,102)) 
##Question 1.b)
def IterativeSolution():
    A = int(input("please enter a value for A"))
    B = int(input("Please enter a value for B"))
    count = 0
    count2 = 0
    if A < 100:
        return 1 
    while A > 100: 
        if A >= B:
            count = count + 1
            A = A-1
        else:
            count2 = Count2 + 1
            A = A - 10
        return (count*5) + 1
        return (count2*10) + 10
print (IterativeSolution())
##Question 1.c)
Recursion(104,102)
## Question 1.e)
def BubbleSort(NumberArray):
    Outer = len(NumberArray)-1
    swap = True
    while swap == True or Outer >= 0:
        Inner = 0
        swap = False
        while Inner < len(NumberArray)-1:
            if NumberArray[Inner]>NumberArray[Inner + 1]:
                Temp = NumberArray[Inner]
                NumberArray[Inner] = NumberArray[Inner + 1]
                NumberArray[Inner + 1] = Temp
                swap = True
            Inner = Inner + 1
        Outer = Outer - 1

## Question 1.f)
NumberArray = [0 for i in range (10)]
NumberArray[0]= 10
NumberArray[1]= 81
NumberArray[2]= 16
NumberArray[3]= 23
NumberArray[4] = 7
NumberArray[5] = 22
NumberArray[6] = 19
NumberArray[7] = 23
NumberArray[8] = 29
NumberArray[9] = 71
##BubbleSort(NumberArray)
##print(NumberArray)
##Question 1.g)
def BinarySearch(NumberArray,V2S):
    ##V2S is the value which we want to search)
    lowerbound = 0
    upperbound = len(NumberArray)-1
    found = False 
    while upperbound >= lowerbound and found == False:
        midvalue = int((lowerbound + upperbound)/2)
        if NumberArray[midvalue]==V2S:
            found = True
            print("Value is found at index:",midvalue)
        elif V2S > NumberArray[midvalue]:
            lowerbound = midvalue + 1
        else:
            upperbound = midvalue - 1
    if found == False:
        print("The value is not found")

BubbleSort(NumberArray)
BinarySearch(NumberArray,81) 


        
