

##Linear Search
##arr = [1,3,4,5]
##search=int(input("please enter the number you are looking for: "))
##found = False
##n = 0
##while not found and n<len(arr):
##    if arr[n]==search:
##        print("value is found")
##        found = True
##    elif n == len(arr) - 1 and arr[n] != search:
##        print ("value is not found in the array")
##
##    n = n + 1 



## effecient bubble sort

##arr = [125,213,985,123,5123,592,1,234]
##
##sort = False
##
##n = len(arr)
##
##while not sort:
##    sort = True
##    for i in range (0,n-1):
##        if arr[i] > arr[i+1]:
##            sort = False 
##            temp = arr[i]
##            arr[i]=arr[i+1]
##            arr[i+1] = temp
##    n=n-1 
##
##print(arr) 

## insertion sort


##
##arr = [125,234,902,126,369,467,90093,1234,54673,303021,6546]
##n = len(arr)
##for i in range(1,n):
##    val = arr[i] 
##    j = i-1
##    while j>=0 and val<arr[j]:
##        arr[i] = arr[j] 
##        arr[j] = val
##        j = j - 1
##
##print (arr)
##

##arr = [125, 234, 902, 126, 369, 467, 90093, 1234, 54673, 303021, 6546]
##n = len(arr)
##for i in range(1, n):
##    val = arr[i]
##    j = i - 1
##    # Shift elements to the right until the correct position is found
##    while j >= 0 and val < arr[j]:
##        arr[j + 1] = arr[j]
##        j = j - 1
##    # Insert the value in its correct position
##    arr[j + 1] = val
##
##print(arr)





##for i in range (1, len(arr)):
##   value = arr[i]
##   j = i-1
##   while j>=0 and value < arr[j]:
##       arr[j+1]=arr[j]
##       j = j-1
##   arr[j+1]= value
##
##
##
##
##print (arr) 
##


















##
##
##arr = [123, 1234,1231,23451,242145,12551,24231,455321,355643,1242,1,2340912324,2412,223,12]
##
##n = len(arr)
##for i in range (1, n):
##    value = arr[i]
##    j = i-1
##    while j >=0 and value<arr[j]:
##        arr[j+1]=arr[j]
##        j = j - 1
##    arr[j+1] = value
##
##
##print (arr)






##9618/mj22/41

##Question2_J2022.
##ans 2a)
##Health=string
##Colour=integer
##defenceitem=string
##
##class Balloon:
##    def __init__(self, pColour, pDefenceItem):
##        self.__Health = 100
##        self.__Colour = pColour
##        self.__DefenceItem = pDefenceItem
##
##
##    def GetDefenceItem(self):
##        return self.__DefenceItem
##
##    def ChangeHealth(self,changehealth):
##        self.__Health = self.__Health + changehealth
##
##    def CheckHealth(self):
##        if self.__Health<=0:
##            return True
##        else:
##            return False
##defenceitem = input("Enter  defence Item: ")
##colourballoon=input("Enter the colour of the balloon: ")
##Balloon1 = Balloon(colourballoon,defenceitem)
##
##def Defend(myballoon):
##    strength=int(input("enter the strength of the opponent: "))
##    myballoon.ChangeHealth(-strength)
##    print("you defended with: ", str(myballoon.GetDefenceItem()))
##    if myballoon.CheckHealth() == True:
##        print ("No health is remaining")
##    else:
##        print("There is still some health left")
##    return myballoon
##
##
##
##Balloon1 = Defend(Balloon1) 

    
##9618/41/O/N/22
##Question2_N22
## number : integer
## colour : string 
class Card:
    def __init__(self,pNumber, pColour):
        self.__Number = pNumber
        self.__Colour = pColour

    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour
red1 = Card(1,"red")
red2 = Card(2,"red")
red3 = Card(3,"red")
red4 = Card(4,"red")
red5 = Card(5,"red")
blue1 = Card(1,"blue")
blue2 = Card(2,"blue")
blue3 = Card(3,"blue")
blue4 = Card(4,"blue")
blue5 = Card(5,"blue")
yellow1 = Card(1,"yellow")
yellow2 = Card(2,"yellow")
yellow3 = Card(3,"yellow")
yellow4 = Card(4,"yellow")
yellow5 = Card(5,"yellow")

class Hand:
    def __init__(self,Card1,Card2,Card3,Card4,Card5):
        self.__FirstCard = 0
        self.__NUmberCards = 5
        self.__Cards = []
        self.__Cards.append(Card1)
        self.__Cards.append(Card2)
        self.__Cards.append(Card3)
        self.__Cards.append(Card4)
        self.__Cards.append(Card5)
    def GetCard(self, index):
        return self.__Cards[index]
Player1 = Hand(red1,red2,red3,red4,yellow1)
Player2 = Hand(yellow2,yellow3,yellow3,yellow5,blue1) 


def CalculateValue(player):
    score = 0
    for i in range(0,5):
        cardgot= player.GetCard(i)
        score = score + cardgot.GetNumber()
        colour = cardgot.GetColour()
        if colour == "red":
            score = score + 5
        elif colour == "blue":
            score = score + 10
        elif colour == "yellow":
            score = score + 15
    return score
player1score = CalculateValue(Player1)
player2score = CalculateValue(Player2)
if player1score > player2score:
    print ("Player 1 wins")
elif player2score > player1score:
    print ("Player 2 wins")
else:
    print ("It is a draw")

print (player1score)
print (player2score) 


