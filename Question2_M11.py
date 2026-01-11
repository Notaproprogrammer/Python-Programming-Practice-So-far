## Question 2.a.i)

## DECLARE NameList : ARRAY[1:8]OF STRING
NameList = ["" for i in range (8)]

NameList[0] = "Zehan"
NameList[1] = "Zavian"
NameList[2] = "Maizah"
NameList[3] = "Javaira"
NameList[4] = "Haziq"
NameList[5] = "Eshal"
NameList[6] = "Azlan"
NameList[7] = "Aleena"

##Question 2.a.ii)

def Find(Name,Start,Finish):
    isFound = False
    while Start <= Finish and isFound == False: 
        MidVal = int((Start + Finish)/2)
        if NameList[MidVal] == Name:
            print ("The Name is Found")
            return MidVal
            isFound = True
            break
        elif Name < NameList[MidVal]:
            Start = MidVal + 1
            Find(Name, Start, Finish)
        else:
            Finish = MidVal - 1 
            Find(Name,Start, Finish)
        if isFound==False:
            return -1
    

Find("Eshal",0,7)
            
            
