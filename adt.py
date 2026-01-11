##Date :7.10.2024
global stack ##global array integer
global TopPointer ##global variable
global Continue ## glbal variable


Stack = [0 for i in range(5)] ## A 1D array of size 5, initialized as 0
TopPointer = -1 ## initiliazed as -1 to indicate empty stack
Continue = True ## initialized as True

def Push(Value):
    global Stack
    

while Continue:
    print ('-----stack operation-----')
    print('Options to select......')
    print ('1: Push\n2: POP\n3: PEEK\n4: Display\n5: EXIT')
    Choice = int(input('Enter your choice from 1 to 5: ')
    match Choice:
        case 1:
            val = int(input('Enter the value to insert: '))
            Push(Val)
        case 2:
            Pop()
        case 3:
            Peek() 
        case 3:
            Display()
        case 5:
            print('The program ends....')
            Exit()
        case _ :
            print('Wrong choice. Must be between 1 and 5 inclusive....') 
                
