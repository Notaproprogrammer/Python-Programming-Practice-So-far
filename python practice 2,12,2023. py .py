def select(start , end):
    for i in range(start+1, end):
        thisString=str(i)
        Char1=int(thisString[-1:-2:-1])
        Char2=int(thisString[-2:-3:-1])
        total=Char1 + Char2
        if total ==6:
            print(thisString)

select(1400,3000)
            
    
    
