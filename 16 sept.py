##A variable holds balance amount of 10000. Another variable holds daily

##limit of withdrawal of 5000. Maximum of 3 valid transactions can

##be allowed in a day and after every valid or any transaction that

##will be refused, the user must be asked

##whether to continue for more transaction. An input of Y will continue

##and N will stop the program. Use validation so that no other letters

##are given as input.

##If withdrawal reaches the day limit then no more trnasaction

##should be allowed.

##An input of amount will be taken which must be a multiple of 50

##and must be in whole number and cannot be 0 or a negative amount.

##You have to apply validation to ensure them. A withdrawal is refused

##if amount entered is greater than balance or greater than daily


##limit and will not be counted as a valid transaction.

##In each case a separate error message should be displayed.


##If amount withdrawn is 200 or less

##then a charge of 2% is imposed on the amount.


##If amount withdrwan is successful then display

##the new balance with a proper message. The daily limit should also

##be updated and displayed after every valid transaction



##balance = 10000
##daily_limit = 5000
##maximum_withdrawl_num = 3
##current_withdrawl_num = 0
##daily_withdrawl_amount = 0 
##decision = input("Do you want to transact any money, [y/n]")
##while current_withdrawl_num < 3 and decision == 'y':
##    withdrawl_amount = int(input("please enter the amount of money you want to withdrawl")
##    daily_withdrawl_amount += withdrawl_amount 
##    
##    if daily_withdrawl_amount < balance and daily_withdrawl_amount < daily_limit:
##        if withdrawl_amount%50 == 0 and withdrawl_amount == int(withdrawlamount) and withdrawl_amount > 0 :
##            if withdrawl_amount <= 200:
##                
##        









