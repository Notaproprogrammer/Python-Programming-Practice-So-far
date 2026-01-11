##f=open('practice.txt.py','r')
##fileArray=[''for i in range(10)]##A 1D array
##i=0
##count=0
##filedata=f.readline()
##while filedata!='':
##    fileArray[i]=filedata
##    count=count+1
##    i=i+1
##    filedata=f.readline()
##f.close()
##print('Number of lines read from the file: ',count)
##for i in range(len(fileArray)):
##    if fileArray[i]!='':
##        print(fileArray[i])


##
##f=open('practice.txt.py','r')
##f1=open('copy.txt','w')
##filedata=f.readline()
##while filedata!='':
##    f1.write(filedata)
##    filedata=f.readline()
##f.close()
##f1.close()


##copying selective data from one file to another file


f=open('practice.txt.py','r')
f1=open('copyname.txt','w')
filedata=f.readline()
while filedata!='':
    i=1
    Line=''
    ThisChar=filedata[i]
    while ThisChar!=',':
        Line=Line+ThisChar
        i=i+1
        ThisChar=filedata[i]
    f1.write(line+'\n')
    filedata=f.readline()
f.close()
f1.close()
                        
        
