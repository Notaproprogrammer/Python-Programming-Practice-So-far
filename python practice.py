#ABC
#Arithmetic operator
# + for addition
# - for subtraction
# / for decimal value
# // for integer value
# % for integer reminder
# * for multiplication
# ** for exponent

# selection:
# IF / CASE
# take input of a number and check if it is a positive or negetive  or neutral. Display
# with proper message

##
##num=int(input('Enter a number'))
##while num !=-99:
##    if num>0:
##        print("it is a positive number")
##    elif num<0:
##        print("it is a negetive number")
##    else:
##        print ("it is 0")
##print ("bye")


## number of seats will be taken as input which must be in the range
## from 1 to 10 inclusive and whole number. Apply both the validation
## type to accept the value


##
##
##
##
##seat = float(input("please enter the number of seats"))
##
##
##
##
##while seat<1 or seat >10 or seat != seat//1: ##seat%1!=0 ## seat!= int (seat) 
##    print ('invalid entry')
##    seat = float(input("please enter the number of seats")) 
##


##Using linear search algorithm solve the following problem
##Write down a subroutine which will take a whole number as a parameter
## It searches a global array and if the Value is found then returns the index
## if the value is not found then returns -1
## Call the subroutine and display a proper message based on the return value 
## based on the reutrn value
##if seat >= 1 and seat <= 10:
##    print ("alright")


global Values
Values=[10,11,8,5,25] 
def LinearSearch(searchvalue:int): #RETRUNS STRING
    global Values
    returnvalue=-1
    index=0
    while returnvalue==-1 and index<5:
        if searchvalue == Values[index]:
            returnvalue=index
        else:
            index=index+1
    return returnvalue 
#subroutine call
returnindex=LinearSearch(5)
if returnindex ==-1:
    print("Value is not present")
else:
    print("Value found at position",returnindex)
             
             




