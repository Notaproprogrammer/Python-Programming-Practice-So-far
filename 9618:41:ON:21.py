def Unknown(x,y):
    if x<y:
        print(x+y)
        return Unknown(x+1,y)*2 
    elif x == y:
        return 1
    else:
        print(x+y)
        return Unknown(x-1,y)%2 
        
        

Unknown(10,15)
Unknown(10,10)
Unknown(15,10)


