global storeddata
storeddata = [-1 for i in range (10)]
def hash(datatoadd):
    location = (datatoadd % 10) # generating location
    return location
def AddItem(datatoadd):
    global storeddata
    location = hash(datatoadd)
    if storeddata[location] == -1:
        storeddata[location] = datatoadd
        return True
    else:
        Found = False
        counter = 0
        while Found == False and counter < 10:
            location += 1
            if location > 9:
                location = 0
            if storeddata[location] == -1:
                storeddata[location] = datatoadd
                Found = True
                return True
            else:
                counter +=1
        if counter == True:
            print('Array Full: Space not found to add Data')
            return False



n = int(input("enter the number of values you want to input then input the values: "))
max = n + 1        
for i in range (1,max):
    num = int(input("enter number= " ))
    AddItem(num)
print (storeddata)

def search(datasearch):
    global storeddata
    location = hash(datasearch)
    if storeddata[location] == datasearch:
        return location
    else:
        counter = 0
        while counter < 10:
            location = location +1
            if location > 9: ##Wrap around 
                location = 0
            if storeddata[location] == -1:
                return -1
            elif storeddata[location] == datasearch:
                return location
            else:
                counter = counter + 1
        if counter == 10: ##when all the array elements are checked
            ## no need to search more
            print ("data not found in arary")
            return -1
address = search(3)
print(address) 







