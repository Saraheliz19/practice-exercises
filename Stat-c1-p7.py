#Sarah Viall   Prj 7

def mean(anyList):
    sum=0
    for i in anyList:
        sum+=i
    return sum/len(anyList)

def median(anyList):
    tmpList=list(anyList)
    tmpList.sort()
    L=len(tmpList)
    if (L%2==1):
        return tmpList[int(L/2)]
    else:
        print(tmpList)
        print(tmpList[int(L/2)-1])
        print(tmpList[int((L/2))])
        print(tmpList[int(L/2)-1:(int(L/2)+1)])
        return mean(tmpList[int(L/2)-1:int(L/2)+1])

def mode(anyList):
    tmpList=list(anyList)
    tmpList.sort()
    currentCount=0
    currentValue=tmpList[0]
    bigCount=1
    bigValue=tmpList[0]
    
    for v in tmpList:
        if v!=currentValue:
            if(currentCount>=bigCount):
                bigCount=currentCount  
                bigMode=currentValue
            currentCount=1
            currentValue=v
        else:
            currentCount+=1
        if(currentCount>=bigCount):
            bigCount=currentCount  
            bigMode=currentValue
            
    return bigMode












numList=[5,8,12,4]
longList=[4,5,8,5,2,3,4,2,1,1,5,8,9,6,6,3,2,1,2,4,7,5,2,5,2,9,9,9,9,9,9,9,9,9,9,9]

print(mean(numList))
print(median(numList))
print(mode(longList))