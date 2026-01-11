class Card():
    def __init__(self,pNumber,pColour):
        self.__Number = pNumber
        self.__Colour = pColour
    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour
    
red1 = Card(1, "Red")
red2 = Card(2, "Red")
red3 = Card(3, "Red")
red4 = Card(4, "Red")
red5 = Card(5, "Red")
blue1 = Card(1,"Blue")
blue2 = Card(2,"Blue")
blue3 = Card(3,"Blue")
blue4 = Card(4,"Blue")
blue5 = Card(5,"Blue")
yellow1 = Card(1, "Yellow")
yellow2 = Card(2, "Yellow")
yellow3 = Card(3, "Yellow")
yellow4 = Card(4, "Yellow")
yellow5 = Card(5, "Yellow")

class Hand():
    def __init__(self, card1, card2, card3, card4, card5):
        self.__Cards = []
        self.__Cards.append(card1)
        self.__Cards.append(card2)
        self.__Cards.append(card3)
        self.__Cards.append(card4)
        self.__Cards.append(card5)
        self.__FirstCard = 0
        self.__NumberCards = 5
    def GetCard(self, index):
        return self.__Cards[index]
Player1 = Hand(red1,red2,red3,red4,yellow1)
Player2 = Hand(yellow2, yellow3,yellow4,yellow5,blue1)

def CalculateValue(player):
    score = 0
    for i in range (0,5):
        PlayerCard = player.GetCard(i)
        score = score + PlayerCard.GetNumber()
        colour = PlayerCard.GetColour()
        if colour == "Red":
            score = score + 5
        elif colour == "Blue":
            score = score + 10
        else:x
            score = score + 15
    return score

player1score = CalculateValue(Player1)
player2score = CalculateValue(Player2)
if player1score > player2score:
    print ("Player 1 wins")
elif player1score == player2score:
    print ("it is a draw")
else:
    print("Player 2 wins") 
