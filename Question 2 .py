## Question 2.a.i)
global SName,SAverage
SName = ["" for i in range (10)]
SAverage = [0 for j in range(10)]
## Question 2.a.ii)
def ProcessMarks(): 

## Question 2.b):
def InsertionSort():
    global SName, SAverage
    for i in range (1,10):
        keyavg = SAverage[i]
        keyname = SName[i]
        j = j-1
        while j >= 0 and key>SAverage[j]:
            SAverage[j+1]= SAverage[j]
            SName[j+1] = SName[j]
            j = j - 1
        j = j + 1
        SAverage[j] = keyavg
        SName[j] = keyname
## Question 2.c)
def DisplayValues():
    print("Student Name", "Average Mark")
    print(SName,Saverage) 
## Question 2.e)
ProcessMarks()
InsertionSort()
DisplayValues()
WriteToFile()
              
