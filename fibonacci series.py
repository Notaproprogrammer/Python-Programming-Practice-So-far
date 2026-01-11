#### without recursion
##def fibo(n):
##    a = 0
##    b = 1
##    if n == 1 or n == 0:
##        return n
##    else:
##        while n>1:
##            c = a + b
##            a = b
##            b = c
##            n = n-1
##    return c
##print (fibo(10))
##
##
##def numberpattern(v1,v2,end):
##    while end>v1:
##        print (v1)
##        temp = v2
##        v2 = v1
##        v1 = v1 + temp
##    print (v1)
##numberpattern(1,1,12)
##def linearsearch(index,sv):
##    global a
##    if index==len(a):
##        return "not found" 
##    elif a[index] == sv:
##        return "it's found" 
##    else:
##        return linearsearch(index+sv)
##
##global a
##a = [15,16,6,8,2,10]
##print(linearsearch(0,15))
global b
b = [1,5,7,11,19,20]

##def recursivebinary(lowerbound, upperbound, sv):
##    mid = (upperbound + lowerbound)/2
##    if b[mid] = sv:
##        return 1
##    else:
##        if sv> mid:
##            return (mid+1, upperbound, sv)
##        else:
##            upperbound = mid
##            return(lowerbound, mid
##

##def fibo(n):
##    global counter
##    counter = counter + 1
##    if n==0 or n==1:
##        return n
##    else:
##        return fibo(n-1) + fibo (n-2)
#### main program
##global counter
##counter = 0
##print (fibo(5))
##print ('the number of times the function was called:', counter) 
##



##A subroutine is required to receive a number as a parameter and counts
##how many numbers are above that number, below that number
##and equal to that number in a text file and returns those count.
##The subroutine generates 10 random numbers which will all be in the
##range from 1 to 20 whole numbers. You have to ensure that each
##random number is unique.
##You need to store the number of times needed for each number to be
##unique in a 1D array.
##Each random number should be trasferred to a new file, RandomFile.txt. 
##The subroutine should display the randomly generated unique values
##with number of times repeated for each.
##The program then reads the file and returns the count

##Call the subroutine and based on the return values display
##proper messages

##import random 
##
##def count(n:int):
##    a = [0 for i in range(10)]
##    for i in range (0,10):
##        index = 0
##        random = random.randint(1,20)
##        while index<i:
##            if a[index] == random:
##                random = random.randint(1,20)
##                index = 0
##            else:
##                index= index+1
##        a[i]= random


##Date: 02 september
import random
def grid():
    g[[""for i in range (5)]for i in range(5)]
    col=random.randint(0,4)
    row=random.randint(0,4)
print (col,',',row)

             
    
    
    
