##Sarah Viall

##Python Exercise 3: Recursive Binary Search

## Based on 160 chp 6 hw for logic

import time
import random

def binarySearch(passList, key, low, high):

    if (low>high):
        return -1

    middle=int ((low+high)/2)
    if(key<passList[middle]):
        high=middle-1
        return binarySearch(passList, key, low, high)
    elif(key>passList[middle]):
        low=middle+1
        return binarySearch(passList, key, low, high)
    else:
        return middle


ranList=range(1000000) #from numbers 0 to 999999

N=500 #Number of elements for list generation

ranList=[random.choice(ranList) for x in range(N)]
#Note:
#sortList = ranList.sort()
#  this doesn't work because .sort sorts the list in place
#  instead use the following two lines
sortList = ranList.copy()  #keeps original list intact
sortList.sort()

#print(sortList) #debug
low=0
high=N-1
print("Let's play Find the Key")
key=int (input("Enter Key Number to search for: "))
startTime=time.perf_counter()
result=binarySearch(sortList, key, low, high)
endTime=time.perf_counter()

if(result != -1):
    print(key, "found at location", result)
else:
    print(key, "not found.")

print("Start Time=", startTime)
print("End Time=  ", endTime)
print("Run Time=", float(endTime-startTime)*1000000, "uS")