##Date: 02 september
import random
def grid():
    g=[["" for i in range (5)]for x in range(5)]
    row=random.randint(0,4)
    col=random.randint(0,4)
    g[row][col]='X'
    turns= 0
    matched = False
    prow=0
    pcol=0
    tempcol=0
    temprow=0
    print (row,',',col)
    while turns<10 and matched == False:
        inp=input("enter move")
        error = False
        match inp:
            case 'd':
                temprow=prow+1
            case 'u':
                temprow=prow-1
            case 'l':
                tempcol = pcol - 1
            case 'r':
                tempcol = pcol + 1
           
        if temprow > 4 or temprow<0 or tempcol> 4 or tempcol<0:
            error = True
        else:
            error = False
        if error == False and g[temprow][tempcol] =='X':
            matched = True
        else:
            matched = False
            turns += 1
grid()
     ## xor gate = odd number of ones, three ones = 1, 1 ones = 1, 2 ones = 0.        
