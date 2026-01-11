IsValid=True
Str1=input('Enter the code as "999-aaa-AAA" format: ')
if len(Str1)!=10:
    IsValid=False
else:
    if Str1[2]!='-' and Str1[6]!='-':
        IsValid=False
    for i in range(0,2):
        char1=Str1[i]
        if char1<'0' or char1>'9':
            IsValid=False
    for i in range(3,6):
        char1=Str1[i]
        if char1<'a' or char1>'z':
            IsValid=Fa;se
    for i in range(7,len(Str1)):
        char1=Str1[i]
        if char1<'A' or char1>'Z':
            IsValid=False
If IsValid==True:
    print('This is a valid code')
else
    print('This is an invalid code')
