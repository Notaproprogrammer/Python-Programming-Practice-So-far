##bubble sort  
##arr = [1,29,203,55,28,91,30]
##n = len(arr)-1
##sorted = True
##while sorted == True:
##    sorted = False 
##    for i in range (0,n):
##        if arr[i]>arr[i+1]:
##          temp = arr[i]
##          arr[i]= arr[i+1]
##          arr[i+1] = temp
##          sorted = True
##    n = n -1 
##print (arr)
##
##









##arr = [1, 29, 203, 55, 28, 91, 30]
##n = len(arr)
##sorted = False
##while not sorted:
##    sorted = True  # Reset to True at the start of each pass
##    for i in range(n - 1):  # Loop through the list
##        if arr[i] > arr[i + 1]:  # Swap if elements are in the wrong order
##            arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Pythonic swap
##            sorted = False  # A swap occurred, so the list is not sorted yet
##    n -= 1  # Reduce n after each full pass
##print(arr)

arr = [1234,123491234,2134191,341922314,512661435,431671435,612353147,113515]
##
##def sort():
##    n = len(arr)-1
##    sorted = False
##    while not sorted:
##        sorted = True
##        for i in range (0,n):
##            if arr[i]>arr[i + 1]:
##                temp = arr[i]
##                arr[i]=arr[i + 1]   
##                arr[i +1 ]=temp
##                sorted = False
##        n = n-1
##    print (arr)
##sort()
##

##arr.sort()
##print (arr)
for i in range (1, len(arr)):
    j = i-1 

