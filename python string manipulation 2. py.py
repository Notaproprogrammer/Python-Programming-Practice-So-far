str2=""
str1=input('Enter a string to process: ')
char1=input('Enter a character to find from the string: ')
char2=input('Enter a character to replace in the string: ')
for i in range(len(str1)):
    char3=str1[i]
    if char1==char3:
        str2 = str2 + char2
    else:
        str2 = str2 + char3
print('Processed string after replacement is '+ str2) 
