## two 1d array,name and mark has information of 5 students, Both the arrays are global array write down the program for the subroutine which will receive a mark is found.
##If the mark is not found then return not found. Complete the program with effecient linear search.


##global  Name, Mark
##
##Name = ['x', 'p', 'a', 'd', 'c']
##Mark = [75, 65, 88, 55]
##def linearsearch(mark:int):
##    global Name, Mark
##    Foundat = -1
##    index = 0
##    while Foundat == -1 and index<5:
##        if mark == Mark[index]:
##            Foundat= index
##
##        else:
##            index = index + 1
##    return returnState
##
##ret = linearsearch(65)
##
##print("name: " + ret) 
##





## A 2D array, Itemnumber stores item code in whole numbers
## The array is made up of 5 rows and 3 columns.
## A user gives input of an item code and the program
## searches and if it is found then displays the locaiton and if not
## found then displays a message not found
## write an efficient linear search algorithm

##global marks
##marks= [[10,20,30], [15, 25, 35], [50,60,70],
##     [1,2,3],
##     [4,0,20]]
##def search(mark:int):
##    global marks
##    found = False
##    index = 0
##    while found == False and index <5:
##        col = 0
##        while col <3 and found == False:
##            if mark == marks[index][col]:
##                print("its found")
##                found = True
##            else:
##                col = col + 1
##        index = index + 1
##
##search(10.5)
##                


## You can only use binary search when the values in the array or list is already
## sorted either in ascending order or descending order. The value we are searching for
## is always found in the mid(Middle) or centre position. 



##Mark=[35,38,39,45,75]
##low = 0
##high = 4
##found = False
##value = int(input("Enter a value to search: "))
##
##while high>=low and found == False:
##
##    mid=(low+high)//2
##
##    if value==Mark[mid]:
##        print("the value is found at position ", mid)
##        found = True
##    elif value>Mark[mid]:
##        low = mid + 1
##    else:
##        high = mid - 1
##if found == False:
##    print("the value is not found")
##
        




























## 8th july 2024:


## Binary search algorithm
## A 1D array, Name has names of 5 students. Another 1D array,
## Marks has marks of 5 students. The values are stored
## using corresponding index. The marks arrat
## is alreadt sorted in descending order. Both the arrays
## are global arrays.
## Write a program for the subroutine, BinarySearch,
## Which receives a mark and searches the mark in the array mark in Marks array.
## If the mark is found then it returns
## name of the student. IF not found then it returns not found
## Apply binary search algorithm from the program
## Call the subroutine and display a proper message based on
## the return value.



##
##global Names, Marks
##
##Names = ['b', 'p', 'c', 'g', 'd']
##Marks = [98, 95, 93, 90, 85]
##
##val = int(input("please enter a value to start with: " )) 
##def BinarySearch(sv:int):
##    global Names, Marks
##    low = 0
##    high = 4
##    index = 0
##    foundname='not found'
##    while high >= low and foundname == "not found":
##        mid = int((high + low)/2)
##        if Marks[mid]== sv:
##            foundname = Names[mid]
##        elif Marks[mid]< sv:
##            high = mid - 1
##        else:
##            low = mid + 1
##    return foundname
##
#### Calling the subroutine
##
##returnvalue = BinarySearch(val)
##if returnvalue == "not found":
##    print ("the mark is not found")
##else:
##    print ("the mark is obtained by", returnvalue)





## Bubble sort algorithm
## A 1D array, Name has names of  5 students stored in it.
## Two other 1D, Age and Height has values stored for the students
## Apply efficient Bubble sort based on Age for all the
## arrays in the descending order of age. Display the output ion
## the following:
## Name is p, age is 19, height is 1.2

##
##Name = ['x' , 'a', 'g' , 'p' , 'b']
##Age = [15, 18, 16, 19, 17]
##Height = [1.1, 1.5, 1.4, 1.2, 1.3]
##
##
##
##index = 0
##sort1ce = False
##max = 4
##while sort1ce == False:
##    sort1ce = True
##    for i in range(0, max):
##        for index in range (4):
##            if Age[index] < Age[index+1]:
##                sort1ce = False
##                temp1 = Age[index]
##                Age[index] = Age[index+1]
##                Age[index + 1] = temp1
##                temp2 = Name[index]
##                Name[index] = Name[index + 1]
##                Name[index + 1] = temp2
##                temp3 = Height[index]
##                Height[index] = Height[index + 1 ]
##                Height[index + 1] = temp3
##            
##    max =  max - 1
##
####print
##for i in range (5):
##    print ('name is', Name[i], "Age is", Age[i], "Height is", Height[i]) 
##        
##
##            



## ineffecient one:

##
##Name = ['x' , 'a', 'g' , 'p' , 'b']
##Age = [15, 18, 16, 19, 17]
##Height = [1.1, 1.5, 1.4, 1.2, 1.3]
##
##
##max = 4
##for i in range (max): 
##    for index in range (4):
##        if Age[index] < Age[index+1]:
##            sort1ce = False
##            temp1 = Age[index]
##            Age[index] = Age[index+1]
##            Age[index + 1] = temp1
##            temp2 = Name[index]
##            Name[index] = Name[index + 1]
##            Name[index + 1] = temp2
##            temp3 = Height[index]
##            Height[index] = Height[index + 1 ]
##            Height[index + 1] = temp3
##            
##
####print
##for i in range (5):
##    print ('name is', Name[i], "Age is", Age[i], "Height is", Height[i]) 
##        
##
##                
##
##        
##              
##                
##            














## Bubble sort on a 2D array based on the second column in Ascending order
## do it in effecient way



##AL = [
##            [1,70,30,40],
##            [2,15,20,30],
##            [3,55,99,21] ]
##swapped = True
##
##max = 2 ## Here boundary value will be less than 1 of the number of values in the column(or row)
##
##while swapped == True:
##    swapped = False
##    for i in range (0,max):
##        if AL[i][1]>AL[i+1][1]:
##            temp1=AL[i][1]
##            AL[i][1]=AL[i+1][1]
##            AL[i+1][1]=temp1
##
##            temp0=AL[i][0]
##            AL[i][0]=AL[i+1][0]
##            AL[i+1][0]=temp0
##
##            
##            temp2=AL[i][2]
##            AL[i][2]=AL[i+1][2]
##            AL[i+1][2]=temp2
##            
##            temp3=AL[i][3]
##            AL[i][3]=AL[i+1][3]
##            AL[i+1][3]=temp3
##    max=max-1
##
##for i in range(3):
##    print (AL[i][0],AL[i][1],AL[i][2],AL[i][3])
##
##






























##
## 10th july 2024
## Bubble sort, between a 1D array and a 2D array
## A 1D array, IDnum stores id numbers of 5 employees. A 2D array, Info,
## Stores the names, departments and salaries of the employees
## in consecutive columns. The two arrays data are stored using
##corresponding index.
## Based on the names of the 2D array, arrange both arrays in
## asceding order using effective Bubble sort algorithm


##IDnum=[5,30,42,2,6]
##Info = [ ['Smith', 'HR', '100000'],
##         ['Johnson', 'IT','120000'],
##         ['Peters', 'HR', '110000'],
##         ['Allen', 'HR', '99000'],
##         ['Sam', 'IT', '75000'] ]
##
##
##
##swapped = False
##max =4
##
##while swapped == False:
##    swapped = True
##    for i in range (0,max):
##        if Info[i][0]>Info[i+1][0]:
##            swapped = False
##            temp1 = Info[i][0]
##            Info[i][0] = Info[i+1][0]
##            Info[i+1][0]= temp1
##        
##            temp2=IDnum[i]
##            IDnum[i]=IDnum[i+1]
##            IDnum[i+1]=temp2
##
##            temp3=Info[i][1]
##            Info[i][1]=Info[i+1][1]
##            Info[i+1][1]=temp3
##
##            temp4=Info[i][2]
##            Info[i][2]=Info[i+1][2]
##            Info[i+1][2]=temp4
      ##max=max-1         
##            
##
##
##
##
##
##
##
##for j in range(5):
##    print ("The name is:",Info[j][0],",The Id number:",IDnum[j],",The department is:",Info[j][1],",The salary is:",Info[j][2])
##
##





##INSERTION SORT:

## Insertion sort on 1D array in ascending order

##Data = [12,11,25,75, 52, 56, 57, 59, 91, 85]
##for pointer in range(1,10): ## Loop used for picking one element ata a time
#### starting from second position
##    valueToInsert=Data[pointer]##extracting one value
##    Hole = pointer-1##storing the position
##    while (Hole>=0) and Data[Hole]>valueToInsert:
##        Data[Hole+1]=Data[Hole]
##        Hole=Hole-1
##    Data[Hole+1]=valueToInsert ##placing the value in its correct position
##for i in range (10):
##    print (Data[i], end=' ') 
##            
##
##




##another method without pointer - 1 :changes that will be made in hole>=0 and where is data[hole]


##Data = [12,11,25,75, 52, 56, 57, 59, 91, 85]
##for pointer in range(1,10): ## Loop used for picking one element ata a time
#### starting from second position
##    valueToInsert=Data[pointer]##extracting one value
##    Hole = pointer##storing the position
##    while (Hole>=1) and Data[Hole-1]>valueToInsert:
##        Data[Hole]=Data[Hole-1]
##        Hole=Hole-1
##    Data[Hole]=valueToInsert ##placing the value in its correct position
##for i in range (10):
##    print (Data[i], end=' ') 
##            









## 15th July :





## inseertion sort using 2D array based on third column in descending order


a = [
      [25,4,3],
      [10,1,6],
      [9,3,9],
      [20,2,5],
      [15,7,7] ] 


for p in range (1,5):
    valins = a[1][p]
    hole = p - 1

    while (hole>=0) and a[1][hole]<valins:
        a[1][hole+1] = a[1][hole]
    
    a[hole] = valins
for i in range (5):
    print (a[1][i], end =' ')
    
        
    
        
    

