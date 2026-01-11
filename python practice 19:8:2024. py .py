## Date: 19 August 2024
## Generate 10 random numbers which will all be in the range from
## 1 to 20 whole numbers. You have to ensure that each random number
## is unique. Store the random numbers in a new file called RandomFile.txt.
## Display the random numbers from the file. Use appropriate
## exception handling



##import random
##num = [0 for i in range(10)]
##f = open('randomfile.txt','w')
##for c in range (10):
##    index = 0
##    rnum = random.randint(1,20)
##    while index<c:
##        if num[index]==rnum:
##            rnum=random.randint(1,20)
##            index = 0
##        else:
##            index = index + 1
##    num[c]= rnum
##    f.write(str(rnum)+'\n')
##f.close()
##print (num)

##reading from the file
##try:
##    f1 = open('randomfile.txt', 'r')
##    line =






## A 1D array, rnum, which can hold 10 elements wil store random numbers
## in the range from 1 to 20. You have to ensure that each
## element hold unique random number. You also need to count
## the number of times can random number was required to generate
## to make it unique. You need to store the count for each unique number
## in another array. Display both the array values in the following format.
## 19 needed 4 count.



##
##import random
##num = [0 for i in range (10)]
##count = [0 for i in range(10)]
##for i in range (11):
##    index = 0
##    rc = 1
##    rand = random.randint(1,20)
##    while index < i:
##        if num[index]==rand:
##            rand == random.randint(1,20)
##            rc = rc + 1
##        else:
##            index = index + 1
##    num[i]= rand
##    count[i] = rc
##print (num, count)


##import random
##num = [0 for i in range(10)]
##count = [0 for i in range(10)]
####f = open('randomfile.txt','w')
##for c in range (10):
##    index = 0
##    rc = 1
##    rnum = random.randint(1,20)
##    while index<c:
##        if num[index]==rnum:
##            rnum=random.randint(1,20)
##            index = 0
##            rc = rc+1
##        else:
##            index = index + 1
##    num[c]= rnum
##    count[c]=rc
##    
####    f.write(str(rnum)+'\n')
####f.close()
##print (num, count








##recursive
## Write down the program code that will receive a number
## as a parameter and find the factorial of that number using
## iterative approach
##
##def IterativeFactorial(n):
##    result = 1
##    while n> 1:
##        result = result*n
##        n= n -1
##    return result
##
##
##n = int(input("enter a value"))
##print (IterativeFactorial(n))


##def RecursiveFactorial(n):
##    ##Base Case
##    if n==1:
##        return 1
##    else:
##        return n*RecursiveFactorial(n-1) ##recursive
##print (RecursiveFactorial(100)) 

##def RecursiveFactorial(n):
##    if n==1:
##        return 1
##    else:
##        result = n*RecursiveFactorial(n-1) ##Recursive call
##    return result
##print(RecursiveFactorial(10))
##

##def Display(n):
##    if n==1:
##        print (n)
##    else:
##        print(n)
##        Display(n-1)
##        print(n)
##Display(5) 




##find sum of n numbers
##def numbers(n):
##    total = 0
##    if n == 1:
##        return 1
##    else:
##        while n > 0: 
##            total = total + n
##            n = n - 1 
##        return total
##print (numbers(10))

##
##def iterativenumbers(n):
##    if n == 1:
##        return 1
##    else:
##        result = n + iterativenumbers(n-1)
##        return result
##
##
##print (iterativenumbers(10))



##
##
##def NaturalSum(n):
##    Sum=0
##    for i in range (1,n+1):
##        Sum=Sum+i
##    return Sum
##print(NaturalSum(10))
##
##
##def Naturalsumrecursive(n):
##    if n == 1:
##        return 1
##    else:
##        return n+Naturalsumrecursive(n-1)
##print (Naturalsumrecursive(5)) 




## Fibonacci Series


## try out recursive method as well



def fs(n):
    a = 0
    b = 1
    c=1
    while n>0:
        a=b
        b=c
        c=c+1
        n = n - 1
    return c
print (fs(5))
