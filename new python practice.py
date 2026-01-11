def lastlines(filename):
    count=0
    f=open(filename,'r')
    line=f.readline()
    while line!='':
        count=count+1
        line=f.readline()
    f.close()

    f=open(filename,'r')
    for x in range(1,count-3):
        f.readline()
    lineX=f.readline()
    print(lineX)
    lineY=f.readline()
    print(lineY)
    lineZ=f.readline()
    print(lineZ)
    f.close()

lastlines("lines.txt.rtf")
