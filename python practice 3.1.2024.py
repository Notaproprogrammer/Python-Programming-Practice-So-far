global sample, result

sample = [ [12,11,9,20,23],
           [13,12,19,50,3],
           [1,11,19,120,123],
           [120,110,90,200,123],
           [112,101,9,200,203],
           [5,115,95,205,235]s
         ] 


result=[-1 for i in range(5)]
print (result)

def Mix():
    global sample, result


    for i in range(5):
        count = 0
        total = 0
        for j in range(6):
            if sample[j][i]>10:
                count = count +1
                total = total+sample[j][i]
        result[i]= int(total/count)
        print(result[i])
Mix()
                
