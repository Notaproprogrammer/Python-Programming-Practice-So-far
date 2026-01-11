## DATE: 11 september
## A 1D array, Num has 10 numbers stored in it. The array is a global array
## Write down a subroutine which checks if number is odd or even.
## IF it is odd
## then stores the value in another array 1D array OddNum, and if it is even
## then stores the numbers in another arary, EvenNum.
## The arrays are then accessed and finds the highest odd number and
## lowest even numbers. IT also finds the total of all the odd numbers
## and even numbers separately and displays all the results.


global num
Num=[12,19,21,15,16,20,27,13,200,7]
def finder():
    global Num
    odd=[0 for i in range(10)]
    even=[0 for i in range(10)]
    for z in range (0,len(Num)):
        if Num[z]%2 == 0:
            even[z]=Num[z]
        else:
            odd[z]=Num[z]
    for j in range (0, len(odd)):
        for x in range(0,len(odd)):
            if odd[j]>odd[x]:
                biggestodd = odd[j]
    for y in range (0, len(even)):
        for t in range(0,len(odd)):
            if even[y]<even[t]:
                lowesteven = even[y]
    totalodd = 0
    totaleven=0
    for q in range(0,len(odd)):
        totalodd += odd[q]
    for s in range (0,len(even)):
        totaleven += even[s]
    print (totalodd)
    print (totaleven)
    print (odd)
    print (even)
    print (biggestodd)
    print (lowesteven)


finder()



        
                    
                
